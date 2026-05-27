# CLI Commands Reference

All commands run from `D:\GitProjects\lean-obsidian-weekly`.

## Plugin Radar

### Trending Plugins (Most Downloaded This Week)
```bash
python bin/obsidian-community-pp-cli plugins trending --limit 3
```
- Fetches top 3 plugins by weekly download delta
- Output: JSON, one per line
- Expected fields: id, name, author, description, url, health, total_downloads, weekly_delta

### New Plugins (Newcomers)
```bash
python bin/obsidian-community-pp-cli plugins new --days 7 --min-rating 90
```
- Fetches plugins created in past N days with health >= 90%
- Output: JSON, one per line
- Expected fields: id, name, author, description, url, health, total_downloads, created_at

### Updated Plugins (Latest Updates)
```bash
python bin/obsidian-community-pp-cli plugins updated --days 7 --min-rating 90
```
- Fetches plugins with latest release in past N days, health >= 90%
- Output: JSON, one per line
- Expected fields: id, name, author, description, url, health, total_downloads, latest_release_at

## Community Buzz

### Forum Topics
```bash
python bin/obsidian-forum-pp-cli topics --latest --days 7 --sort views --limit 5
```
- Fetches topics active in past N days, sorted by views/replies/activity
- Output: JSON array (not one-per-line), pretty-printed
- Expected fields: id, title, url, views, reply_count, tags, snippet, created_at, bumped_at

### Reddit Posts
```bash
python bin/scrape-creators-pp-cli reddit --subreddit ObsidianMD --sort top --time week --limit 5
```
- Fetches top posts from r/ObsidianMD sorted by engagement
- Output: JSON, one per line
- Expected fields: title, url, score, comments, author

### YouTube Videos
```bash
export YOUTUBE_API_KEY="AIzaSyAX6oXwIFKwAMZ9oyBZ4uZc7m-d3jruzuU"
python bin/scrape-creators-pp-cli youtube --query obsidian --latest 5
```
- Searches YouTube for "obsidian" videos, filters out non-app content (crystals, games, etc.)
- Requires YOUTUBE_API_KEY env var — silently skips if missing
- Output: JSON, one per line
- Expected fields: title, url, published_at
- ⚠️ Off-topic videos occasionally slip through keyword filtering; verify in preview

### Bluesky Posts
```bash
python bin/scrape-creators-pp-cli bluesky --query "obsidian.md" --days 7 --limit 5
```
- Fetches posts mentioning "obsidian.md" from past N days, sorted by engagement
- Output: JSON, one per line
- Expected fields: text (post body), url, likes, reposts, author

## Data Merging

Combine all CLI outputs into `cache/latest_research.json`:

```json
{
  "week": "2026-W20",
  "generated_at": "2026-05-14T12:00:00Z",
  "newcomers": [...],              // from plugins new
  "latest_updates": [...],         // from plugins updated
  "most_downloaded": [...],        // from plugins trending
  "forum_topics": [...],           // from forum topics
  "community_buzz": [...],         // from reddit + youtube + bluesky combined
  "quick_tips": [...]              // hardcoded defaults
  "featured_post": {               // from blog.sascha-kasper.com
    "title": "...",
    "url": "...",
    "description": "..."
  }
}
```

## Newsletter Generation

```bash
python scripts/newsletter_generator.py --input cache/latest_research.json --output "D:\Lean Notes\09 Blog\Substack\Lean Obsidian Weekly 003.md" --dry-run
```

Options:
- `--input FILE` — JSON cache file (required)
- `--output FILE` — Save to file (optional, saves to vault)
- `--dry-run` — Preview only, no Substack posting
- `--issue NUM` — Issue number (default: current week)

Output: Markdown newsletter with 6 sections
- Plugin Radar (Newcomers, Updates, Most Downloaded)
- Community Buzz (Forum + Social)
- Quick Tips
- From LeanProductivity (blog post or video)
- Footer with links

## Date Ranges

For custom date ranges, manually modify cache before generating:

```bash
# Modify cache/latest_research.json with data from custom date range
# Then generate with same command above
```

Limitations:
- Forum: ~30 days of history
- Plugins: new releases tracked indefinitely, but trending only shows 7-day delta
- Reddit/Bluesky: ~30 days of history
- YouTube: no date filtering in API, only latest N videos

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Zero videos returned | YOUTUBE_API_KEY missing or invalid | Set env var: `export YOUTUBE_API_KEY="..."` |
| Forum shows old topics | API returns by activity, not creation date | Use `--days` filter; check bumped_at not created_at |
| Bluesky shows non-Obsidian posts | Query too broad or off-topic posts popular | Verify manually; consider narrowing query |
| Plugins section empty | Rating filter too high (>90%) | Lower `--min-rating` or check plugin ecosystem |
| git commit fails | Uncommitted changes in repo | Run `git stash` first, then retry |
