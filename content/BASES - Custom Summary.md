---
aliases:
author:
  - Sascha D. Kasper
source:
description: Fix Obsidian Bases column averages by excluding blank values with a custom summary formula.
cover: zAttachments/Obsidian Bases Made Simple - Advanced Tips.webp
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
updated: 2026-03-09T00:00
---

# Setup
- Right-click a column header and choose "Summarize"
- Click "Add summary" to use a custom formula
- The default average includes blanks; this formula excludes them

# Code
```
(values.sum() / values.filter(value.toString().trim() != "null").length).round(1)
```

# Source
- [[Obsidian Bases Made Simple - Advanced Tips]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M)
