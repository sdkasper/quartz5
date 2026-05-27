---
name: lean-obsidian-weekly
description: Generate a weekly Lean Obsidian Weekly newsletter by researching across Obsidian communities and drafting curated content
---

# Lean Obsidian Weekly

Generate a weekly Obsidian community newsletter — research, curate, and draft in one command.

## What It Does

Automatically:
1. Determines the next issue number
2. Researches Obsidian Community Hub, Reddit, forum, Twitter/BlueSky, and GitHub for the past 7 days
3. Curates the best plugins, themes, and community discussions
4. Drafts the full newsletter with your voice
5. Asks you what LeanProductivity content to promote this week
6. Saves the draft to `09 Blog/Substack/Lean Obsidian Weekly NNN.md` (zero-padded issue number)
7. Offers to push the draft to Substack for review

## How to Use

### Generate a New Issue

```
/lean-obsidian-weekly
```

The skill will:
- Research all platforms automatically
- Present curated content for each section
- Ask you to provide any LeanProductivity content links to include
- Create a ready-to-review draft in your vault
- Offer to publish as a Substack draft

### Review & Publish Workflow

1. Check the generated file in `09 Blog/Substack/`
2. Edit any sections as needed (adjust editorial commentary, reorder items, etc.)
3. Let Claude know when you're ready to push to Substack (`substack_publisher.py --draft`)
4. Review in Substack editor, then publish live

## Newsletter Sections

Each issue includes:

| Section | What | Target |
|---------|------|--------|
| **Plugin Radar** | Two subsections: "Rising Stars" (3 new plugins by score/downloads) + "Most Downloaded This Week" (top 3 by 7-day downloads) | ~150 words |
| **Community Buzz** | 3-5 top discussions from Reddit, forum, Twitter/BlueSky with brief takes | ~150 words |
| **Quick Tips** | 1-2 power-user tricks surfaced from the community | ~80 words |
| **From LeanProductivity** | Your recent YouTube videos, blog posts, or LOT updates | ~60 words |

Total per issue: ~500 words (lean and focused vs. verbose).

**Note:** Newsletter filenames use zero-padded numbers without special characters (e.g., `Lean Obsidian Weekly 001`, `002`, etc.) for Obsidian wiki link compatibility.

## Plugin Radar — Data Requirements

To populate the two subsections, the skill needs to source:
- **Rising Stars:** Access to Community Hub's plugin directory with release dates, ratings/scores, and download counts (absolute)
- **Most Downloaded This Week:** Download analytics for 7-day window (may require API access or manual research from Community Hub trending)

If download data is unavailable, fall back to: "most discussed in community this week" or "trending on Community Hub" as proxy signals for popularity.

## Research Sources (Priority Order)

1. **Obsidian Community Hub** (`community.obsidian.md`) — Official directory of plugins/themes
2. **Reddit** (`r/ObsidianMD`) — Active community discussions, setups, workflows
3. **Obsidian Forum** (`forum.obsidian.md`) — Technical discussions, plugin help, feature requests
4. **Twitter/BlueSky** — Real-time community reactions, announcements
5. **GitHub Releases** — Plugin and theme release announcements

## Frontmatter Auto-Set

The generated file includes:
- `substackStatus: pending` — so `substack_publisher.py` picks it up automatically
- `created` & `updated` — current date/time
- `tags: blog/newsletter, obsidian/community`
- `type: newsletter`
- `issue: NNN` — auto-incremented
- `week: YYYY-Www` — ISO week format

## Integration with Publisher

Once you approve the draft:

```bash
python ~/.claude/scripts/substack_publisher.py --draft
```

This will:
- Create a Substack draft of your newsletter
- Update the file with `substackId` and `substackUrl`
- Let you review in the Substack editor before going live

## Tips

- Run this on a **Tuesday morning** to capture the week's discussions before they drop off feeds
- Keep editorial takes concise — let the links speak
- Promote your own content naturally in "From LeanProductivity" (one or two items, not a hard sell)
- Pin or share the Substack draft with your audience for feedback before publishing live
