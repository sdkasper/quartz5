---
aliases:
  - obsidian/tweaks/bases-relative-progress-bars
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/BASES---Relative-Progress-Bars
description: Build emoji progress bars in Obsidian Bases that show completion relative to estimated effort.
cover:
date: 2026-01-15
draft: false
categories:
  - obsidian
  - bases
cssclasses:
tags:
  - obsidian
  - bases
created: 2025-12-15T17:32
updated: 2026-01-15T18:07
---

# Setup
- You need two numeric properties (e.g. `estimatedEffort` and `currentEffort`) in your notes
- In your base, click on **Properties**, **Add Formula**, and give it a name (e.g. `fPercentage`)
	- Copy/paste the first code snippet from below
- Create another property (e.g., `fProgressBar`)
	- Copy/paste the second code snippet from below
- You can replace the emojis in the formula with whatever you prefer

# Result
You get a view like this:

![[BASES - Relative Progress Bars.webp|Bases table with emoji progress bars showing current versus estimated effort per note]]
# Code
## Snippet 1 - `fPercentage`
```
(currentEffort / estimatedEffort * 100).round(1)
```
## Snippet 2 - `fProgressBar`
```
("🟩".repeat(((formula.fPercentage / 100) * 10).round(0)) + "⬛".repeat(((100 - formula.fPercentage) / 100 * 10).floor()))
```

# Source
- [[Obsidian Bases Made Simple - Getting Started]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M)
