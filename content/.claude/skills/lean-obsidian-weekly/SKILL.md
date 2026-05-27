---
name: lean-obsidian-weekly
description: Manually trigger the Lean Obsidian Weekly newsletter pipeline. Fetches 7-day content from Obsidian ecosystem sources (plugins, forum, Reddit, Bluesky, YouTube), merges into cache, generates markdown newsletter, and commits to git. Use when you need to regenerate the newsletter outside the scheduled Tuesday run, or with custom date ranges. Supports full pipeline (all CLIs + generate + commit) or preview-only mode.
keywords: newsletter, obsidian, automation, content aggregation, community, plugin discovery
---

# Lean Obsidian Weekly Pipeline

Generate the Lean Obsidian Weekly newsletter on-demand with custom date ranges and data sources.

## Before Running, Ask Yourself

- **Which data is fresh?** Do I need all CLIs or can I use cached data? Full pipeline takes ~30s, preview-only takes ~2s.
- **What's my target date range?** Default is last 7 days from today. Custom ranges let you backfill past weeks.
- **Preview or publish?** Always preview first if content will be committed and pushed.
- **Do I need Substack posting?** This skill generates locally. Use `/substack-publish` separately if needed.

## NEVER Do

- **NEVER run the full pipeline more than once per day** — CLI rate limits (especially YouTube API, forum pagination) can trigger throttling (silently returning empty or stale data). If you need to regenerate within 24 hours, use preview-only mode instead: `--mode preview`. Running full pipeline twice within hours will break the second run with incomplete sections.

- **NEVER skip the preview step before committing** — This is mandatory, not optional. Preview catches silent failures: missing data, API outages, broken plugins sections. User permission to "skip preview" does NOT override this rule. Always run with `--dry-run` first to inspect output. Only commit if you visually verify ALL 6 sections (Newcomers, Updates, Downloaded, Forum, Social, Tips, LeanProductivity) contain data.

- **NEVER commit without verifying the output file exists** — File write failures in `D:\Lean Notes\09 Blog\Substack\` silently succeed in git status. Always check the target directory physically: `ls -la "D:\Lean Notes\09 Blog\Substack\"` and verify the newsletter file is actually there with non-zero size before committing.

- **NEVER use custom dates older than 30 days** — Forum API, plugin registry, Reddit, and Bluesky only retain ~30 days of history. Requests older than 30 days WILL return empty sections (this is a hard API constraint, not a data pattern). Reject backfill requests older than 30 days. If user insists, explain: "APIs don't have historical data older than ~30 days. Generated newsletter will have empty sections."

- **NEVER assume YouTube results are app-related** — The CLI filters by keyword but off-topic videos slip through (crystals, games, Minecraft servers). Always preview the "From LeanProductivity" section and reject any videos that aren't about Obsidian app/plugins.

- **NEVER forget to set YOUTUBE_API_KEY for full pipeline** — YouTube CLI silently skips if the env var is missing. Before running full pipeline, VERIFY the key is set: `echo $YOUTUBE_API_KEY` (must print a non-empty string). If empty, full pipeline will silently omit all YouTube videos.

- **NEVER run git operations if you have uncommitted changes** — The skill runs `git add` and `git commit` on the cache. Other uncommitted changes could get partially committed or conflict. Before full pipeline, check `git status` must show "clean" (no uncommitted changes). If you see uncommitted files, run `git stash` first. Do NOT rationalize that changes are "unrelated" - stash is safety.

## Core Workflow

### Step 1: Choose Mode

**Full Pipeline** (recommended first-run or refreshing all data)
```
- Run all 3 CLI scrapers (plugins, forum, social)
- Validate data freshness
- Merge into cache/latest_research.json
- Generate newsletter
- Preview in terminal
- Commit cache + push
```

**Preview-Only** (testing, exploring changes)
```
- Use existing cache/latest_research.json
- Generate newsletter
- Show preview
- No git operations
```

### Step 2: Set Date Range (Optional)

Default: last 7 days from today.

Custom example: articles from May 1-7, 2026
```
start-date: 2026-05-01
end-date: 2026-05-07
```

### Step 3: Validate Environment (MANDATORY BEFORE FULL PIPELINE)

Run these checks. If any fail, do NOT proceed to Step 4.

**Check 1: Git working tree is clean**
```bash
cd D:\GitProjects\lean-obsidian-weekly
git status
```
Expected output: `On branch master` + `nothing to commit, working tree clean`
If you see uncommitted files: `git stash` first, then proceed.

**Check 2: YOUTUBE_API_KEY is set**
```bash
echo $YOUTUBE_API_KEY
```
Expected output: Non-empty string starting with `AIza...`
If empty: Set `export YOUTUBE_API_KEY="..."` and verify again.
(If you don't have the key, preview-only mode will work but YouTube section will be empty.)

**Check 3: Target directory exists and is writable**
```bash
ls -la "D:\Lean Notes\09 Blog\Substack\"
```
Expected output: Directory listing with existing newsletter files
If error or missing: Create directory or check permissions before proceeding.

**Only after all 3 checks pass:** Proceed to Step 4.

### Step 4: Run Pipeline

**Full pipeline with today's date:**
```bash
cd D:\GitProjects\lean-obsidian-weekly
export YOUTUBE_API_KEY="..." # if not already set
python bin/obsidian-community-pp-cli plugins trending --limit 3
python bin/obsidian-community-pp-cli plugins new --days 7 --min-rating 90
python bin/obsidian-community-pp-cli plugins updated --days 7 --min-rating 90
python bin/obsidian-forum-pp-cli topics --latest --days 7 --sort views --limit 5
python bin/scrape-creators-pp-cli reddit --subreddit ObsidianMD --sort top --time week --limit 5
python bin/scrape-creators-pp-cli youtube --query obsidian --latest 5
python bin/scrape-creators-pp-cli bluesky --query "obsidian.md" --days 7 --limit 5
python scripts/newsletter_generator.py --input cache/latest_research.json --output "D:\Lean Notes\09 Blog\Substack\Lean Obsidian Weekly 003.md" --dry-run
```

**Preview-only (cached data):**
```bash
cd D:\GitProjects\lean-obsidian-weekly
python scripts/newsletter_generator.py --input cache/latest_research.json --dry-run
```

### Step 5: Inspect Output (MANDATORY - DO NOT SKIP)

Preview is your safety net. Silent API failures (outages, throttling) produce no errors - only empty sections in the generated file. Inspect before committing.

**Always run preview first:**
```bash
python scripts/run_newsletter.py --mode full --skip-commit
```
This generates the file WITHOUT committing it. Inspect the output file at: `D:\Lean Notes\09 Blog\Substack\Lean Obsidian Weekly [NUM].md`

**Verify these criteria (HARD STOPS - if any fail, do NOT commit):**
- [ ] **Date range correct** — Filename and title show correct week/dates
- [ ] **All 6 sections populated with data** — Newcomers, Updates, Most Downloaded, Forum, Social, Tips, LeanProductivity (if any section is empty, you have an API failure)
- [ ] **No "Untitled" posts** — Would indicate missing titles in source data
- [ ] **Links are valid URLs** — Spot-check 2-3 links (click one to verify it works)
- [ ] **YouTube section has real Obsidian videos** — Not off-topic (games, crystals, unrelated)

**FORMATTING VALIDATION (MANDATORY - run grep checks before committing):**

Run these checks on the output file. Any match = formatting error, do NOT commit:

```bash
# Must return 0 matches (no bold links):
grep -P '\*\*\[' "D:\Lean Notes\09 Blog\Substack\Lean Obsidian Weekly NNN.md"

# Must return 0 matches (no bold descriptions):
grep -P '^\*\*[^[]' "D:\Lean Notes\09 Blog\Substack\Lean Obsidian Weekly NNN.md"

# Must return 0 matches (no h1 title in content body):
grep -P '^# Lean Obsidian Weekly' "D:\Lean Notes\09 Blog\Substack\Lean Obsidian Weekly NNN.md"

# Must return 0 matches (no description text before frontmatter ends):
grep -P '^Your weekly digest' "D:\Lean Notes\09 Blog\Substack\Lean Obsidian Weekly NNN.md"
```

**Correct format rules (from Weekly 001 reference):**
- Content starts with `# Plugin Radar` - no h1 newsletter title in body
- Plugin links: `[Name](url)` - NEVER `**[Name](url)**`
- Metadata line immediately after link (no blank line): `Score: XX | By author | Date | downloads`
- Descriptions as blockquotes: `> text` - NEVER plain text, NEVER bold
- Newcomers: no downloads field in metadata (just Score, author, Created date)
- Most Downloaded: numbered plain links `1. [Name](url)` - never bold
- Footer: `*Lean Obsidian Weekly is published every Friday. Only plugins with a score >= 90 are considered.*`

**If ANY section is empty or malformed:** Do NOT commit. Investigate:
- Was full pipeline run today already? (Rate limiting?) Use preview-only mode instead.
- Is YOUTUBE_API_KEY set? Run `echo $YOUTUBE_API_KEY` to verify.
- Are APIs online? Check forum/Reddit in browser to confirm data exists.

**Only after all criteria pass:** Proceed to Step 6 to commit.

### Step 6: Commit & Push (Full Pipeline Only)

```bash
git add cache/latest_research.json
git commit -m "chore: newsletter research W$(date +%V)"
git push origin master
```

## Reference Loading

MANDATORY: CLI command reference (commands, parameters, expected output)

```
See: references/cli-commands.md
```

Do NOT Load: generic git/Python documentation

## Self-Verification (MANDATORY GATES)

**Before running anything:**
- [ ] `git status` is clean (no uncommitted changes)? If not: `git stash` now.
- [ ] `echo $YOUTUBE_API_KEY` returns non-empty value? If not: set it first.
- [ ] Target dir exists: `ls -la "D:\Lean Notes\09 Blog\Substack\"` works?

**Before committing (Full Pipeline only):**
- [ ] Preview shows all 6 sections have data? (empty sections = API failure, investigate before committing)
- [ ] Newcomers section has real plugins (not off-topic)?
- [ ] Updates section has real plugins?
- [ ] Most Downloaded section has real plugins?
- [ ] Forum section has real topics (not empty)?
- [ ] Social section has real posts (Reddit/Bluesky/YouTube)?
- [ ] YouTube videos are Obsidian-related (not games/crystals)?
- [ ] Output file exists in `D:\Lean Notes\09 Blog\Substack\` with non-zero size?

**If any check fails:**
STOP. Do NOT commit. Diagnose the failure first (see "Troubleshooting" in referenced cli-commands.md).

**If all checks pass:**
- [ ] Run: `git add cache/latest_research.json && git commit -m "chore: newsletter research W$(date +%V)"`
- [ ] Run: `git push origin master`

## Common Mistakes & How to Avoid Them

### "I need to regenerate the newsletter twice in one day"

**Wrong:** Running full pipeline twice in a few hours.
```bash
python scripts/run_newsletter.py --mode full  # Run 1
python scripts/run_newsletter.py --mode full  # Run 2 (within 24h) = BROKEN
```

**Why it breaks:** YouTube API, forum pagination, Reddit API all have rate limits. Second run gets throttled, returns empty or stale data. You won't see an error - just empty sections in the preview.

**Right:** Use preview-only for second run.
```bash
python scripts/run_newsletter.py --mode full   # Run 1 (refreshes all APIs)
# ... (later, same day):
python scripts/run_newsletter.py --mode preview  # Run 2 (uses cached data, no API hits)
```

### "Can you generate the newsletter for January 2026?"

**Wrong:** Passing old dates to `--start-date` / `--end-date`.
```bash
python scripts/run_newsletter.py --mode full --start-date 2026-01-01 --end-date 2026-01-31
# Result: Empty sections (APIs don't have data that old)
```

**Why it breaks:** Forum API, plugin registry, Reddit, Bluesky only keep ~30 days of history. This is a hard API constraint, not a preference. Older data = no results, silently.

**Right:** Reject requests older than 30 days.
- If user asks: "APIs only retain ~30 days of history. The generated newsletter for January would have empty sections. I can only generate newsletters from the past ~30 days."
- If you must generate old data: Explain the limitation upfront. Preview will show empty sections. Do NOT commit broken data.

### "Just skip the preview, I trust you"

**Wrong:** Committing without preview.
```bash
python scripts/run_newsletter.py --mode full
# (No preview step, straight to commit)
```

**Why it breaks:** Silent API failures produce no errors. Forum outage? Plugin API throttled? You won't know until you see empty sections in preview. User permission doesn't matter - preview is mandatory for data safety.

**Right:** ALWAYS preview before committing.
```bash
python scripts/run_newsletter.py --mode full --skip-commit  # Preview
# (Inspect file, verify all sections populated)
python scripts/run_newsletter.py --mode full  # Commit only after preview passes
```

### "I have other git work in progress - should I stash first?"

**Wrong:** Running full pipeline with uncommitted changes.
```bash
git status  # Shows uncommitted files
python scripts/run_newsletter.py --mode full  # Runs anyway
# (Possible: git commit fails, or cache merges incorrectly)
```

**Why it breaks:** Full pipeline runs `git add` and `git commit` on the cache. If you have uncommitted changes, the commit could fail or behave unpredictably. Don't rationalize that your files are "unrelated" - they're not, until you stash them.

**Right:** Stash first, always.
```bash
git stash  # Save all uncommitted changes
python scripts/run_newsletter.py --mode full
git stash pop  # Restore changes after newsletter is done
```

## Related Skills

- `/substack-publish` — Post draft to Substack after generating locally
- `/commit` — Custom git commit with hooks
- `/ideas` — Archive newsletter ideas from community buzz
