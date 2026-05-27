# Newsletter Orchestration Scripts

Direct invocation of the Lean Obsidian Weekly newsletter pipeline.

## run_newsletter.py

Orchestrates the complete newsletter pipeline: CLI data collection, caching, generation, and git operations.

### Quick Start

```bash
cd D:\GitProjects\lean-obsidian-weekly

# Preview mode (uses cached data, no git ops)
python D:\Lean\ Notes\09\ Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py --mode preview

# Full pipeline (fetch all CLIs, generate, commit, push)
python D:\Lean\ Notes\09\ Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py --mode full

# Full pipeline with custom date range
python D:\Lean\ Notes\09\ Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py --mode full --start-date 2026-05-01 --end-date 2026-05-07

# Full pipeline but skip git operations
python D:\Lean\ Notes\09\ Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py --mode full --skip-commit
```

### Arguments

| Argument | Values | Default | Notes |
|----------|--------|---------|-------|
| `--mode` | `full`, `preview` | `preview` | Full runs all CLIs + commit/push; preview uses cached data only |
| `--start-date` | YYYY-MM-DD | 7 days ago | Optional custom start date |
| `--end-date` | YYYY-MM-DD | today | Optional custom end date |
| `--skip-commit` | flag | false | Skip git commit and push if true |
| `--output` | filename | `Lean Obsidian Weekly NNN.md` | Custom output filename (saved to `D:\Lean Notes\09 Blog\Substack\`) |

### Modes

#### Preview Mode (`--mode preview`)

- Uses existing `cache/latest_research.json`
- Generates newsletter from cached data
- Shows preview in terminal
- No git operations
- **Fastest:** ~2-3 seconds

**Use when:**
- Testing content changes before full run
- Regenerating newsletter from same data
- Network issues prevent fresh CLI fetches

```bash
python run_newsletter.py --mode preview
```

#### Full Mode (`--mode full`)

- Runs all 5 CLI commands (plugins, forum, reddit, youtube, bluesky)
- Validates data freshness
- Merges results into `cache/latest_research.json`
- Generates newsletter
- Shows preview in terminal
- Commits cache and pushes to origin/master (unless `--skip-commit`)
- **Duration:** ~30 seconds (including network latency)

**Use when:**
- First-time newsletter generation
- Refreshing data after a week (Tuesday scheduled run)
- Custom date ranges for backfilling past weeks

```bash
python run_newsletter.py --mode full
```

### Environment

Before running full pipeline, ensure:

1. **Working directory:** `D:\GitProjects\lean-obsidian-weekly`
2. **YOUTUBE_API_KEY** (optional, but videos won't appear if missing)
   ```bash
   export YOUTUBE_API_KEY="AIzaSyAX6oXwIFKwAMZ9oyBZ4uZc7m-d3jruzuU"
   ```
3. **Git working tree is clean:**
   ```bash
   git status  # Should show "nothing to commit"
   ```
4. **Output directory exists:**
   ```bash
   mkdir -p "D:\Lean Notes\09 Blog\Substack"
   ```

### Output

The script prints:

1. **Progress log** — each CLI call, merge, generation step with timestamps
2. **Newsletter preview** — full generated markdown for review
3. **Summary** — errors, skipped sources, next steps

### Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| "Git working tree not clean" | Uncommitted changes exist | `git stash` before running |
| "YOUTUBE_API_KEY not set" | Env var missing | Set it; videos will be skipped but pipeline continues |
| "Output file not found" | Newsletter generation failed | Check `cache/latest_research.json` structure; review error log |
| "Cache file not found" (preview mode) | No cache exists | Run with `--mode full` first to generate cache |
| CLI timeout (30s) | Network issue or CLI hanging | Retry; if persistent, check forum/Reddit API status |

### Next Steps After Successful Run

1. **Review the newsletter preview** — verify all sections populated
2. **Spot-check 2-3 links** — ensure URLs are valid
3. **Check output file exists:**
   ```bash
   ls -lh "D:\Lean Notes\09 Blog\Substack\Lean Obsidian Weekly*.md"
   ```
4. **If full pipeline:**
   - Cache is already committed and pushed
   - Use `/substack-publish` to post the draft to Substack
5. **If preview mode:**
   - Use `/substack-publish` to post the draft to Substack
   - Re-run with `--mode full` if you need to commit fresh data

### Troubleshooting

**Script can't find Python:**
```bash
# From PowerShell, ensure Python is in PATH:
python --version
```

**CLI commands fail with "not found":**
- Verify working directory is `D:\GitProjects\lean-obsidian-weekly`
- Check `bin/` contains the CLI executables

**Newsletter shows "Untitled" posts:**
- Indicates malformed CLI output (missing `title` field)
- Check individual CLI output manually:
  ```bash
  cd D:\GitProjects\lean-obsidian-weekly
  python bin/obsidian-community-pp-cli plugins new --days 7 --min-rating 90
  ```

**Empty sections (no Newcomers, no Forum Topics, etc.):**
- CLI returned empty data (common for weekends or slow weeks)
- Check with cached data from previous week
- Try widening date range: `--start-date 2026-04-30`

### Skill Integration

This script is invoked by the `/lean-obsidian-weekly` skill. The skill provides:
- Mode selection prompts
- Date range validation
- Preview review before commit
- Substack publishing guidance

**Invoke the skill instead of the script for:**
- Interactive mode selection
- Help with troubleshooting
- Guided walkthrough of preview

**Use the script directly for:**
- Automation in CI/CD pipelines
- Repeatable scheduled runs
- Custom scripting workflows
