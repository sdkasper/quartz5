---
aliases:
  - obsidian/tweaks/bases-absolute-progress-bars
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/BASES---Absolute-Progress-Bars
description: Build visual progress bars in Obsidian Bases using two numeric properties and block-character formulas.
cover: zAttachments/BASES - Absolute Progress Bars.webp
date: 2026-01-15
draft: false
categories:
  - obsidian
  - bases
cssclasses:
tags:
  - obsidian
  - bases
created: 2025-12-15T17:34
updated: 2026-05-14T14:46
substackStatus: draft
substackId: 190951069
substackUrl: https://skasper.substack.com/publish/post/190951069
---

# Setup
- You need two numeric properties (e.g. `estimatedEffort` and `currentEffort`) in your notes
- In you base, click on **Properties**, **Add Formula**, and give it a name (e.g. `fProgressPct`)
	- Copy/paste the first code snippet from below
- Create another property (e.g., `fProgressTxt`)
	- Copy/paste the second code snippet from below
- Create another property (e.g., `fProgressBar`)
	- Copy/paste the third code snippet from below
- You can replace the icons in the formula with whatever you prefer

# Result
You get a view like this:
![[zAttachments/BASES - Absolute Progress Bars.webp|Bases table with seven notes showing progress percentage and block-character progress bars]]

# Code
## Snippet 1 - `fProgressPct`
```
progress / 100
```
## Snippet 2 - `fProgressTxt`
```
if(formula.fProgressPct> 0, (formula.fProgressPct * 100).round(), "0") + " %"
```
## Snippet 3 - `fProgressBar`
```
if(formula.fProgressPct * 10 > 0, "▰".repeat (number(formula.fProgressPct * 10))) + if((formula.fProgressPct * 10).floor() < 10, "▱▱▱▱▱▱▱▱▱▱".slice( 0, 10 - (formula.fProgressPct * 10).floor()), "").toString()
```

# Source
- [[Obsidian Bases Made Simple - Getting Started]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M)
