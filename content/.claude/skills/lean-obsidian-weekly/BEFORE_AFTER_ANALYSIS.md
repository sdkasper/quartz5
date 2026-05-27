# BEFORE/AFTER: Rationalization Closure Analysis

## Introduction

This document shows the exact rationalizations agents made in RED phase and which skill changes closed each loophole.

---

## LOOPHOLE 1: "My files are unrelated to the cache"

### RED Phase Rationalization
Agent had uncommitted changes in `bin/` directory. Thought: "Newsletter pipeline only touches `cache/` and `D:\Lean Notes\09 Blog\Substack\`. My changes in `bin/` won't conflict."

**Why it was dangerous:** Full pipeline runs `git add cache/latest_research.json` and `git commit`. If ANY uncommitted changes exist, the commit could fail, create conflicts, or partially commit other work. Agent rationalized file independence.

### BEFORE (Original SKILL.md)
```
NEVER Do:
- **NEVER run git operations if you have uncommitted changes** — 
  The skill commits the cache. If you have other work in progress, 
  stash it first: `git stash`.
```

**Gap:** Doesn't say "do NOT rationalize" that changes are unrelated. Agent can still think: "But my files really are different from cache..."

### AFTER (Updated SKILL.md)
```
- **NEVER run git operations if you have uncommitted changes** — 
  The skill runs `git add` and `git commit` on the cache. Other 
  uncommitted changes could get partially committed or conflict. 
  Before full pipeline, check `git status` must show "clean" 
  (no uncommitted changes). If you see uncommitted files, run 
  `git stash` first. Do NOT rationalize that changes are "unrelated" 
  - stash is safety.
```

**Added:** Explicit "do NOT rationalize" phrase + explanation of WHY (conflict risk) + step-by-step (check → see files → stash).

### REFACTOR Phase Result
✅ **CLOSED** - Agent immediately ran `git stash` when they saw Step 3 validation and read "do NOT rationalize".

---

## LOOPHOLE 2: "Maybe the API throttled"

### RED Phase Rationalization
YOUTUBE_API_KEY env var was not set. Agent ran full pipeline, YouTube section was empty. Thought: "Maybe the API is rate-limited, or there's no fresh data today."

**Why it was dangerous:** Silent failure. API doesn't error - it just skips YouTube videos. Agent accepted broken output without investigating root cause. Could commit/publish incomplete newsletter.

### BEFORE (Original SKILL.md)
```
NEVER Do:
- **NEVER forget to set YOUTUBE_API_KEY for full pipeline** — 
  YouTube CLI silently skips if the env var is missing. 
  Preview won't show video content.
```

**Gap:** Says it's "optional" ("Preview won't show video content" = mild consequence). Doesn't say to VERIFY the key is set. No verification command provided. Agent can still accept empty YouTube section and rationalize it as data scarcity.

### AFTER (Updated SKILL.md)
Step 3 validation now includes:

```
**Check 2: YOUTUBE_API_KEY is set**
```bash
echo $YOUTUBE_API_KEY
```
Expected output: Non-empty string starting with `AIza...`
If empty: Set `export YOUTUBE_API_KEY="..."` and verify again.
```

**Added:** Mandatory verification command + expected output format + explicit "if empty: set it" instruction.

Also updated NEVER section:
```
- **NEVER forget to set YOUTUBE_API_KEY for full pipeline** — 
  YouTube CLI silently skips if the env var is missing. 
  Before running full pipeline, VERIFY the key is set: 
  `echo $YOUTUBE_API_KEY` (must print a non-empty string). 
  If empty, full pipeline will silently omit all YouTube videos.
```

**Added:** "VERIFY" not just "remember" + verification command + consequence reframed as hard failure.

### REFACTOR Phase Result
✅ **CLOSED** - Agent ran `echo $YOUTUBE_API_KEY` during Step 3, got empty, and stopped immediately without proceeding.

---

## LOOPHOLE 3: "Why would I wait? Let me try again immediately"

### RED Phase Rationalization
Agent ran full pipeline, then immediately ran full pipeline again (within 30 seconds) for a different date range. Thought: "Why wait? I want both newsletters now."

**Why it was dangerous:** Rate limiting. YouTube API, forum API, plugin registry all have rate limits. Second request gets throttled - returns empty or stale data. No visible error. Agent accepted incomplete second newsletter thinking "January was just a slow month for Obsidian".

### BEFORE (Original SKILL.md)
```
NEVER Do:
- **NEVER run the full pipeline more than once per day** — 
  CLI rate limits (especially YouTube API, forum pagination) can 
  trigger throttling. If you need to regenerate, use cached data only.
```

**Gap:** Says "can trigger throttling" (passive language, not consequence). Doesn't explain what throttling looks like (empty sections, silent failure). No pattern provided for what to do if you need multiple runs. Agent must infer the solution.

### AFTER (Updated SKILL.md)
Updated NEVER section:
```
- **NEVER run the full pipeline more than once per day** — 
  CLI rate limits (especially YouTube API, forum pagination) can 
  trigger throttling (silently returning empty or stale data). 
  If you need to regenerate within 24 hours, use preview-only mode 
  instead: `--mode preview`. Running full pipeline twice within hours 
  will break the second run with incomplete sections.
```

**Added:** Consequence made explicit ("silently returning empty or stale data") + solution provided (preview-only mode) + danger highlighted ("will break the second run").

Also new "Common Mistakes" section:
```
### "I need to regenerate the newsletter twice in one day"

**Wrong:** Running full pipeline twice in a few hours.
...
**Why it breaks:** YouTube API, forum pagination, Reddit API all have 
rate limits. Second run gets throttled, returns empty or stale data. 
You won't see an error - just empty sections in the preview.

**Right:** Use preview-only for second run.
python scripts/run_newsletter.py --mode full   # Run 1
python scripts/run_newsletter.py --mode preview  # Run 2
```

**Added:** Real example scenario + explanation of WHY (rate limits cause throttling) + WHAT it looks like (empty sections) + PATTERN (full then preview).

### REFACTOR Phase Result
✅ **CLOSED** - Agent found the exact scenario in "Common Mistakes" section and immediately used the preview-only pattern for the second run.

---

## LOOPHOLE 4: "January was just a slow month for Obsidian"

### RED Phase Rationalization
User asked for January 2026 newsletter. Agent ran full pipeline with `--start-date 2026-01-01 --end-date 2026-01-31`. Many sections were empty. Thought: "Maybe January was a slow month for the community. Let me commit this."

**Why it was dangerous:** APIs don't support historical queries. Forum API, plugin registry, Reddit, Bluesky only keep ~30 days of history. Older dates = no results, silently. This is a hard constraint, not a data pattern. Agent attributed the empty sections to real-world slowness instead of API limitation.

### BEFORE (Original SKILL.md)
```
NEVER Do:
- **NEVER use custom dates older than 30 days** — 
  Forum API pagination and plugin registry only retain ~30 days 
  of history. Older dates will return empty sections.
```

**Gap:** Says "will return empty sections" (consequence stated) but doesn't say to REJECT such requests. No guidance on what to do when user asks. No explanation of hard constraint vs. data pattern. Agent could still commit empty sections thinking it's legitimate data.

### AFTER (Updated SKILL.md)
Updated NEVER section:
```
- **NEVER use custom dates older than 30 days** — 
  Forum API, plugin registry, Reddit, and Bluesky only retain ~30 days 
  of history. Requests older than 30 days WILL return empty sections 
  (this is a hard API constraint, not a data pattern). Reject backfill 
  requests older than 30 days. If user insists, explain: 
  "APIs don't have historical data older than ~30 days. Generated 
  newsletter will have empty sections."
```

**Added:** Emphasis on "hard API constraint" + instruction to "reject" requests + verbatim explanation to provide to users.

Also new "Common Mistakes" section:
```
### "Can you generate the newsletter for January 2026?"

**Wrong:** Passing old dates to `--start-date` / `--end-date`.
...
**Why it breaks:** Forum API, plugin registry, Reddit, Bluesky only 
keep ~30 days of history. This is a hard API constraint, not a 
preference. Older data = no results, silently.

**Right:** Reject requests older than 30 days.
- If user asks: "APIs only retain ~30 days of history. The generated 
  newsletter for January would have empty sections. I can only 
  generate newsletters from the past ~30 days."
```

**Added:** Real scenario + hard constraint explained + pattern for how to respond to user + why it's broken (no historical data).

### REFACTOR Phase Result
✅ **CLOSED** - Agent read "Common Mistakes" section and explicitly rejected the backfill request, explaining the 30-day API limitation to the user.

---

## LOOPHOLE 5: "User said to skip preview, so I did"

### RED Phase Rationalization
User said "I trust you, don't need to see preview first". Agent skipped the preview step and committed the newsletter directly. Forum API happened to be down that moment - forum section was empty. Bad data got committed.

**Why it was dangerous:** Preview is the safety net for silent API failures. User permission doesn't override data safety. Agent deferred to user's authority instead of asserting safety boundary.

### BEFORE (Original SKILL.md)
```
### Step 5: Inspect Output

Check the preview for:
- **Date range** — Title shows correct week/dates
- ...
```

**Gap:** Treats preview as a suggestion ("check the preview for..."). No MANDATORY label. No statement that user permission doesn't override it. Agent can rationalize: "User said skip it, so it's optional."

Also in NEVER section, missing explicit rule about preview.

### AFTER (Updated SKILL.md)
Step 5 rewritten with:
```
### Step 5: Inspect Output (MANDATORY - DO NOT SKIP)

Preview is your safety net. Silent API failures (outages, throttling) 
produce no errors - only empty sections in the generated file. 
Inspect before committing.

**Always run preview first:**
...

**Verify these criteria (HARD STOPS - if any fail, do NOT commit):**
- [ ] **All 6 sections populated with data** — if any section is empty, 
  you have an API failure
...
**Only after all criteria pass:** Proceed to Step 6 to commit.
```

**Added:** MANDATORY label + explanation of WHY (silent failures) + hard stops (if/then language) + consequence ("do NOT commit").

Also new "Common Mistakes" section:
```
### "Just skip the preview, I trust you"

**Wrong:** Committing without preview.
...
**Why it breaks:** Silent API failures produce no errors. Forum outage? 
You won't know until you see empty sections in preview. 
User permission doesn't matter - preview is mandatory for data safety.

**Right:** ALWAYS preview before committing.
```

**Added:** User permission explicitly stated as irrelevant + why it's broken (silent failures) + ALWAYS framing.

### REFACTOR Phase Result
✅ **CLOSED** - Agent read "user permission doesn't override" language and refused to skip preview despite user's explicit request, asserting safety boundary.

---

## Summary: Loophole Closure Rate

| # | Rationalization | RED Result | GREEN Fix | REFACTOR Result |
|---|-----------------|-----------|-----------|-----------------|
| 1 | "My files are unrelated" | ❌ FAILED | Added "do NOT rationalize" + Step-by-step validation | ✅ CLOSED |
| 2 | "Maybe the API throttled" | ❌ FAILED | Added mandatory `echo` check + explicit verification step | ✅ CLOSED |
| 3 | "Why would I wait?" | ❌ FAILED | Added preview-only pattern in common mistakes section | ✅ CLOSED |
| 4 | "January was just slow" | ❌ FAILED | Emphasized "hard constraint" + rejection language | ✅ CLOSED |
| 5 | "User said to skip it" | ❌ FAILED | Added "user permission doesn't override" + MANDATORY label | ✅ CLOSED |

**Closure Rate: 100% (5/5 loopholes closed, 0 new loopholes discovered)**

---

## Key Principles That Worked

1. **Explicit commands** - Instead of "verify the key is set", provided `echo $YOUTUBE_API_KEY` with expected output
2. **MANDATORY labels** - Changed "consider doing X" to "MANDATORY - DO NOT SKIP X"
3. **Negation phrases** - Added "do NOT rationalize", "user permission doesn't override", "hard constraint not preference"
4. **Real scenarios** - Provided exact mistake patterns agents would encounter, not hypothetical warnings
5. **Consequence reframing** - Changed "could happen" to "will happen" / "silently returning empty" instead of "may throttle"

---

## Skill Quality Assessment

**Before hardening:**
- 5/5 loopholes exploitable by agents under pressure
- Vague language ("can trigger", "might occur") allowed rationalization
- No verification commands - agents guessed at correctness
- No explicit safety boundaries vs. user preferences

**After hardening:**
- 0/5 loopholes exploitable (100% closure rate)
- Explicit language ("will happen", "hard constraint")
- Verification commands + expected outputs provided
- Explicit safety boundaries ("user permission doesn't override")

**Recommendation:** Skill is now pressure-resistant and production-ready. Ready for `/skill-judge` evaluation.
