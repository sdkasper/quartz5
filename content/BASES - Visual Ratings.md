---
aliases:
author:
  - Sascha D. Kasper
source:
description: Turn numeric ratings into star visuals in Obsidian Bases with emoji or Lucide icon formulas.
cover: zAttachments/BASES - Visual Ratings.webp
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
updated: 2026-03-15T21:14:07+02:00
---

# Setup
- Notes need a numeric `myRating` property (e.g. 1-10)
- Two approaches: emoji-based or Lucide icon-based
- Find icon names at [lucide.dev](https://lucide.dev/)
# Code
## Snippet 1 - Emoji-Based (`fVisualRating1`)
```
if([myRating] >= 9, "⭐⭐⭐⭐⭐ " + [myRating],
 if([myRating] >= 7, "⭐⭐⭐⭐⚫ " + [myRating],
 if([myRating] >= 5, "⭐⭐⭐⚫⚫ " + [myRating],
 if([myRating] >= 3, "⭐⭐⚫⚫⚫ " + [myRating],
 if([myRating] >= 1, "⭐⚫⚫⚫⚫ " + [myRating],
 "⚫⚫⚫⚫⚫ " + [myRating]
 )))))
```
## Snippet 2 - Icon-Based (`fVisualRating2`)
```
if(myRating.isEmpty() || myRating < 1 || myRating > 10, "11111".split("").map(icon("star-off")), "11111".split("").slice(0, number(myRating/2).floor()).map(icon("star")) + if(number(myRating/2) - number(myRating/2).floor() >= 0.5, [icon("star-half")], []))
```

# Source
- [[Obsidian Bases Made Simple - Advanced Tips]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M)
