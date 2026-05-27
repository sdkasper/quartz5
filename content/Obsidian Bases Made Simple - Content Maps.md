---
aliases:
author:
  - Sascha D. Kasper
source:
description: Build dynamic content maps in Obsidian using Bases — folder-based, tag-based, and property-driven — that auto-update and scale to thousands of notes.
cover: zAttachments/Obsidian Bases Made Simple - Content Maps.webp
date: 2026-03-09
draft: false
categories:
  - obsidian
  - bases
cssclasses:
tags:
  - obsidian
  - bases
created: 2026-03-09T00:00
updated: 2026-03-15T16:31:55+02:00
---
# In a Nutshell

> [!important|float-r] Useful
> * This video: [YouTube](https://youtu.be/o74ChaKxp8g)  
> * Bases tutorial: [YouTube](https://youtu.be/34NAe62IH-M)  
> * Playlist: [Obsidian Series](https://www.youtube.com/watch?v=b2_b1KrheJ4&list=PLpKDvBsvZY3ZM4t36RvtcCXnEYhknVCFU&pp=sAgC)  
> * Download: [Decision Matrix Template](https://shop.sascha-kasper.com/b/tplmcdm)  
> * Wiki: [Snippets & Examples](https://kspr.me/wiki)  
> * [Discord](https://kspr.me/discord)

Content maps sound great in theory — a single note that shows everything related to a topic, folder, or project. In practice, they break. Static maps need constant manual updates. Dataview queries introduce a learning curve and slow down as vaults grow. Waypoint is fast but limited to folders with zero customization.

The problem is not content maps themselves. It is the approach behind them. **Bases** solves this by building content maps from data — your frontmatter properties, tags, and folder structure — instead of manual links. The result is a content map that updates itself, stays fast at scale, and adapts to different contexts without duplication.

This post covers three approaches: folder-based, tag-based, and property-driven content maps. It also includes a head-to-head comparison of Bases, Dataview, and Waypoint. If you are new to Bases, start with [[Obsidian Bases Made Simple - Getting Started|Part 1: Getting Started]].
# Why Content Maps Fail

Static content maps work when you have a handful of notes. You add links by hand, maybe build a small dashboard, and everything feels organized. But as your vault grows, these maps quietly turn into maintenance work. You update links. You fix references. You work around folder structures. At some point, the system meant to save time starts creating work.

Plugins can help, but each comes with trade-offs:

**Dataview** is powerful. It queries your vault dynamically and supports almost any structure. But it has a steeper learning curve than Bases, and performance degrades noticeably as note counts increase.

**Waypoint** is fast and simple. It generates folder listings automatically. But it is limited to folders only — no tags, no properties, no customization beyond file names.

Content maps do not fail because they are a bad idea. They fail because the underlying approach is either hard to maintain, does not scale, or both. What you really want is something dynamic, easy, and fast — no matter how big your vault gets.

# Three Ways to Build Content Maps

All three approaches below use a single Base file. You define it once and add views for different purposes. No duplication, no separate query files scattered across your vault.

## Folder-Based Content Maps

The simplest starting point: show all notes in a specific folder.

Create a new Base file and call it something like `Dynamic MoC`. By default, it lists every note in the vault. Click **Filter** and set an "all views" filter to markdown files only — good practice to exclude non-note files.

Then add a "this view" filter: `file path starts with [Your Folder]`. Rename the view to something descriptive like "Folder A — All". You now have a dynamic list of every note in that folder.

From here, click **Properties** and select the frontmatter fields you want to see. They show up as columns, you can rearrange them, and — unlike Dataview — you can edit values directly in the table. The content map becomes a tool to interact with your notes, not just a read-only list.

**Sorting and grouping** are equally straightforward. Click a column header to sort. Use the Sort button to add grouping by any property — for example, group notes by `status`.

### Dynamic "This Folder" View

Instead of hardcoding a folder path, you can make the content map adapt to whichever folder the active note lives in. Create a new view, switch to **advanced filter**, and enter this snippet:

```
file.inFolder(this.file.folder)
```

This tells Bases to return all notes in the same folder as the currently active file. If you drag the Base file into the side panel with this view selected, the list updates every time you open a note in a different folder. Instant context switching, zero configuration.

### Dataview Comparison

For reference, here is what the equivalent Dataview queries look like.

A simple folder listing:

```
dataview
TABLE WITHOUT ID
	file.link
WHERE contains(file.path,"Folder A")
```

With properties:

```
dataview
TABLE WITHOUT ID
	file.link, tags, status, checked AS "checked?", progress
WHERE contains(file.path,"Folder A")
```

Grouped by status:

```
dataview
TABLE WITHOUT ID
	status,
	rows.file.link AS "Notes"
WHERE contains(file.path, "Folder A")
GROUP BY status
SORT status ASC
```

And the dynamic "this folder" equivalent:

```
dataview
TABLE WITHOUT ID
	file.link, tags, status, checked AS "checked?", progress
WHERE file.folder = this.file.folder
```

The Bases version achieves the same result with clicks instead of code — and lets you edit values directly.

## Tag-Based Content Maps

Folder-based maps assume every note belongs in one place. Tags remove that restriction. A tag-based content map finds notes by context, not location — regardless of where they are stored.

In the same Base file, duplicate an existing view and change the filter to `file tags contains [your tag]`. With no folder filter, this returns matching notes from across the entire vault.

Because it is still a Bases view, you get the same features: editable properties, sorting, grouping, and multiple view types.

### Cards View with Cover Images

If your notes contain images — recipes, book notes, travel logs — you can turn the tag-based map into a visual gallery. Switch the view layout to **Cards**, then add a formula property called `fFirstImage`:

```
if(file.embeds[0].containsAny("jpg","gif","webp","jpeg","avif","png"), file.embeds[0])
```

Right-click the view name and select `fFirstImage` as the **Image property**. The first embedded image in each note becomes the card cover automatically. For more visual use cases, see [[Obsidian Bases Made Simple - Visual Use Cases|Part 2: Visual Use Cases]].

You can also combine tag filters with folder filters for more targeted results.

## Property-Driven Content Maps

Tags describe what something is. Properties describe how it behaves — its status, progress, priority, or workflow state.

Duplicate a view and filter by any frontmatter property. For example, `status contains In Progress` returns every in-progress note across your vault. This is not a static overview — it is a live work-in-progress dashboard you can update directly.

The real power comes from combining properties and context. Sort by `progress`, then group by `tags` to see activities per project. This works with any property: status, priority, area, client, date, or custom workflow states.

If you want to visualize progress numbers as bars or ratings as stars inside a Bases view, those techniques are covered in [[Obsidian Bases Made Simple - Advanced Tips|Part 3: Advanced Tips]] and the [Bases tutorial video](https://youtu.be/34NAe62IH-M).

# Bases vs Dataview vs Waypoint

> [!file|float-r] Decision Matrix
> Download: [Free Template](https://shop.sascha-kasper.com/b/tplmcdm)

Three criteria matter when choosing a content map approach: **ease of use**, **flexibility**, and **longevity**.

**Ease of use** covers how fast you can get started, whether you can reuse what you build, and how easy it is to maintain. Bases uses a visual interface — click to filter, sort, and group. Dataview requires learning its query language. Waypoint needs almost no setup but offers nothing to configure.

**Flexibility** includes customization and scalability. Bases supports multiple view types, editable properties, formulas, and grouping. Dataview matches on customization but slows down at scale. Waypoint lists file names only.

**Longevity** considers how likely each solution is to be supported long-term. Bases is built into Obsidian by the core team. Dataview and Waypoint are community plugins — powerful, but dependent on volunteer maintenance.

Using a multi-criteria decision matrix to weigh these factors, Bases scores highest across all three dimensions.

## Real-Time Performance

At 10 notes, all three approaches load instantly. The differences show up at scale:

- **1,000 notes:** Bases loads fast. Dataview shows a noticeable delay. Waypoint loads fast but displays only file names — no properties, no sorting, no grouping.
- **4,000+ notes:** The gap widens further. Bases maintains speed. Dataview becomes visibly slower with complex queries.

As long as your vault is small and stable, any approach works. As it grows, the trade-offs in performance and flexibility become real. Bases reduces work over time instead of increasing it.

# FAQ

*Do I need coding knowledge to use Bases?*

No. The visual interface handles filtering, sorting, grouping, and view switching without any code. Advanced filters use a simple formula syntax, but even the most complex snippet in this post — `file.inFolder(this.file.folder)` — reads like plain English.

*Can Bases replace Dataview completely?*

For most content map use cases, yes. Bases covers filtering, grouping, sorting, multiple views, and direct editing. Where Dataview still has an edge is in complex inline queries and deeply nested logic. You can use both side by side — they read the same frontmatter and do not interfere with each other.

*How many views can one Base file have?*

There is no practical limit. One Base file can hold dozens of views — each with different filters, sorting, grouping, and layouts. This is the key idea: one Base becomes the backbone, views are just different lenses.

*Does Bases work with large vaults?*

Yes. In a vault with roughly 4,000 notes, Bases shows no noticeable performance penalty. It is designed to stay fast regardless of vault size.

*Where can I find the formulas and snippets?*

All formulas from this series and many more are available on the [wiki](https://kspr.me/wiki). If you have questions, the [Discord](https://kspr.me/discord) is the best place to ask.

# What's Next

This post extends the Bases series with a focus on content maps. If you missed the earlier parts: [[Obsidian Bases Made Simple - Getting Started|Part 1]] covers the fundamentals, [[Obsidian Bases Made Simple - Visual Use Cases|Part 2]] walks through visual use cases, and [[Obsidian Bases Made Simple - Advanced Tips|Part 3]] covers advanced tips including ratings and dynamic MoCs.

All formulas are documented on the [wiki](https://kspr.me/wiki). For questions and ideas, join the [Discord](https://kspr.me/discord).
