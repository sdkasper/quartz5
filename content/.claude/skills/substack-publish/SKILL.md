---
name: substack-publish
description: Publish Obsidian blog posts from `09 Blog` to Substack. Runs the substack_publisher.py script with interactive guidance — previews candidates, publishes drafts, promotes to live, updates existing posts. Use when the user wants to cross-post blog content to Substack.
---

# Substack Publisher

Orchestrates the `substack_publisher.py` vault script for cross-publishing blog posts to Substack.

## Prerequisites

Before first use, verify:
1. Substack publication exists (created at substack.com)
2. Cookie configured in `~/.claude/secrets/substack_cookies.env`
3. `python-substack` installed (`pip install python-substack`)

If any prerequisite is missing, guide the user through setup.

## Workflow

### Step 1 — Preview candidates

Always start with a dry-run to show what would be published.

```bash
python ~/.claude/scripts/substack_publisher.py --dry-run --report
```

Present the results to the user. If no candidates found, explain that posts need `substackStatus: pending` in frontmatter.

### Step 2 — User selects action

Based on the dry-run results, ask the user:
- **Publish as drafts** — creates Substack drafts for review (`--draft`)
- **Publish live** — publishes directly (`--publish`)
- **Single file** — process one specific post (`--file "Post Name.md"`)
- **Update existing** — re-sync already published posts (`--update`)

### Step 3 — Execute

Run the chosen command:

```bash
# Drafts (default, recommended for first use)
python ~/.claude/scripts/substack_publisher.py --draft --report

# Live publish
python ~/.claude/scripts/substack_publisher.py --publish --report

# Single file
python ~/.claude/scripts/substack_publisher.py --draft --file "Post Name.md" --report

# Update existing
python ~/.claude/scripts/substack_publisher.py --update --report
```

### Step 4 — Verify

After publishing, confirm:
- Frontmatter updated with `substackId` and `substackUrl`
- Report generated in `.claude/reports/`
- Suggest the user check the post on Substack for formatting

## Marking Posts for Publishing

To queue a post, add to its frontmatter:

```yaml
substackStatus: pending
```

Valid values: `pending` (queued), `draft` (on Substack as draft), `published` (live), `skip` (excluded).

Posts without `substackStatus` are ignored. Posts with `draft: true` are always skipped.

## File Locations

- **Cross-posted blog posts** live in `09 Blog/` (the script scans `*.md` there)
- **Substack-only posts** (newsletter rewrites, adapted content) live in `09 Blog/Substack/`
- The script scans both locations for candidates

When creating Substack-specific content (e.g., via `/repurpose` for Substack), always save to `09 Blog/Substack/`. This keeps newsletter-only content out of the Quartz blog pipeline.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No candidates found" | Add `substackStatus: pending` to target posts |
| Auth error / 403 | Refresh cookie in `~/.claude/secrets/substack_cookies.env` |
| "No primary publication" | Create a Substack publication first at substack.com |
| Image upload fails | Install Pillow: `pip install Pillow` |
| webp not supported | Script auto-converts to PNG if Pillow is installed |
