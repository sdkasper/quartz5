---
aliases:
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Obsidian-Bases-Made-Simple---Getting-Started
description: "Learn the fundamentals of Obsidian Bases: enable the plugin, understand views, and build your first progress bar with formulas."
cover: Obsidian Bases Made Simple - Getting Started.webp
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
updated: 2026-03-15T16:34:57+02:00
---
# In a Nutshell

> [!important|float-r] Useful
> * Tutorial: [YouTube](https://youtu.be/34NAe62IH-M)
> * Docs: [Bases Documentation](https://help.obsidian.md/bases)
> * Download: [Obsidian Templates & Vaults](https://kspr.me/store)
> * Wiki: [Snippets & Examples](https://kspr.me/wiki)
> * Support: [Discord](https://kspr.me/discord)

Obsidian Bases is a built-in core plugin that turns your frontmatter properties into interactive views — tables, cards, lists, and maps. No code, no config files, no third-party plugins. Enable it and go.

This is Part 1 of a 3-part series covering Bases from the ground up. Here you will learn the core concepts, understand how the four view types work, and build your first progress bar using formulas. [[Obsidian Bases Made Simple - Visual Use Cases|Part 2]] covers visual use cases like recipe cards and travel maps. [[Obsidian Bases Made Simple - Advanced Tips|Part 3]] dives into ratings, dynamic MoCs, and quick tips.

# What Bases Can Do
Bases reads your notes' frontmatter properties and lets you view, filter, sort, and calculate across them. It is great for tracking information, planning projects, managing content, organizing collections, and building dashboards. For everyday workflows, it is much faster than writing Dataview queries.

Here is what you get out of the box:

- **Table View** — structured rows and columns, the best starting point
- **Cards View** — visual, image-driven browsing for recipes, books, or collections
- **List View** — compact inline properties without the visual weight of a table
- **Map View** — interactive maps for notes with location data
- **Formulas** — calculated columns that reference properties and other formulas
- **No configuration** — enable the plugin and start building

There is one key constraint to keep in mind: Bases only reads frontmatter properties. Inline fields, inline tags inside note content, or Dataview annotations are invisible to it. Everything Bases works with must live in the YAML block at the top of your notes.

This makes consistency critical. Three simple rules save you a lot of trouble later:

1. **Clear names** — stick to simple, predictable property names like `status`, `type`, `date`, `rating`. Avoid spaces and inconsistent capitalization.
2. **Compatible types** — if a property is a number in one note, it should be a number in all notes. Mixing types breaks filters and formulas.
3. **Consistent use** — every note in a collection should use the same set of properties. Missing properties show up as blank cells.

# Getting Started

Enabling Bases takes about five seconds. Go to Obsidian **Settings**, then **Core Plugins**, and activate **Bases**. There are no options to configure.

Once enabled, there are two ways to create a Base:

- **Standalone `.base` file** — a dedicated file that acts as a database view. Create one via the file menu or by naming a new file with the `.base` extension.
- **Code block inside a note** — embed a Base directly in any markdown note using a `bases` code block.

Both look the same and use the same syntax. The difference is context.

When a Base lives inside a note, that note becomes its reference point. In the syntax, this is called `this`. All queries and filters run relative to that note. When a Base lives in its own `.base` file, the currently active note defines the context instead.

If that sounds abstract right now, it will make perfect sense once you see the progress bar examples below.

# The Four View Types

Views are what turn a Base from raw data into something useful. The same data can look completely different depending on the view you choose.

## Table

The Table View shows one row per note and one column per property. This is the best starting point when building a new Base, checking data quality, or working with structured information like projects, tasks, or lists. You can sort by any column, group rows, and edit values directly in the table.

## List

The List View is more compact. Instead of columns, it shows selected properties inline, separated by commas. This works well when you want a clean overview without the visual weight of a full table.

## Cards

The Cards View is ideal for visual content. It shines when your notes include images, covers, or thumbnails — think recipes, books, collections, or mood boards. Cards make browsing and inspiration-driven workflows much more natural.

## Map

The Map View is for notes that include location data. Bases uses coordinates from a `location` property to place items on an interactive map. This view is perfect for travel planning, location-based research, or anything where geography matters.

All four views use the same underlying data. You can switch between them at any time without changing your notes. Choosing the right view is often the difference between a Base that feels awkward and one that feels effortless.

# Building a Progress Bar

One of the most common things people want to track is progress. How far along am I? How much is left? Bases can calculate and visualize this with formulas — no scripts, no Dataview, no plugins.

## Two-Value Progress Bar

This approach compares a current value to a target value. Your notes need two numeric frontmatter properties:

- `estimatedEffort` — the target (hours, pages, points, or any unit)
- `currentEffort` — where you are right now

Both values must use the same unit. Otherwise, the percentage makes no sense.

To set this up, create a new Base (or a new view in an existing one), filter it to the relevant notes, and add `estimatedEffort` and `currentEffort` as columns. At this point, the Base already works — you can see the raw numbers.

To add a percentage, create a formula column called `percentage`. The logic divides `currentEffort` by `estimatedEffort`, multiplies by 100, and rounds to one decimal:

```
(currentEffort / estimatedEffort * 100).round(1)
```

Now add a second formula called `progressBar`. This uses the `repeat` function to draw a green square for each 10% of progress and a gray square for the remainder:

```
("🟩".repeat(((formula.percentage / 100) * 10).round(0)) + "⬛".repeat(((100 - formula.percentage) / 100 * 10).floor()))
```

The result is a visual bar that updates instantly when you change values in the table. You can sort by the progress bar column to see which items are closest to completion.

## Single-Value Progress Bar

If your notes already have a single `progress` property (a number from 0 to 100), you can skip the division step and go straight to visualization. This approach uses three formulas.

**`progressPct`** normalizes the value to a 0–1 range:

```
progress / 100
```

**`progressTxt`** creates a human-readable percentage string:

```
if(formula.progressPct > 0, (formula.progressPct * 100).round(), "0") + " %"
```

**`progressBar`** draws a ten-step bar using filled and empty blocks:

```
if(formula.progressPct * 10 > 0, "▰".repeat(number(formula.progressPct * 10))) + if((formula.progressPct * 10).floor() < 10, "▱▱▱▱▱▱▱▱▱▱".slice(0, 10 - (formula.progressPct * 10).floor()), "").toString()
```

The `floor` function ensures the bar never shows as completely full unless the value is actually 100%. Any changes to the `progress` property update the percentage and bar instantly.

This method is perfect when you already track progress as a single number — habits, learning goals, reading progress, or manual project tracking.

# What's Next

This was the foundation: what Bases is, how to enable it, the four view types, and your first formulas. In [[Obsidian Bases Made Simple - Visual Use Cases|Part 2]], you will build visual use cases — recipe cards with images, travel maps with interactive markers, date calculations, and a birthday tracker. [[Obsidian Bases Made Simple - Advanced Tips|Part 3]] covers advanced techniques like visual star ratings, using the first image as a card cover, dynamic Maps of Content, and a quick tips roundup with FAQ.
