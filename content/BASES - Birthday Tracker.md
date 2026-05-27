---
aliases:
author:
  - Sascha D. Kasper
source:
description: Track birthdays and countdowns in Obsidian Bases with formulas for remaining days and current age.
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
- Notes need a `birthday` property (date type)
- Filter by tag `person` where `birthday` is not empty
- Works for deadlines, anniversaries, contract renewals

# Code
## Snippet 1 - `fRemainingDays`
```
((number(
  date(today().format("YYYY") + "-" + birthday.format("MM-DD")) +
  if(date(today().format("YYYY") + "-" + birthday.format("MM-DD")) < today(), "1y", "0y")
) - number(today())) / 86400000).round()
```
## Snippet 2 - `fAge`
```
if(birthday.format("MM-DD") <= today().format("MM-DD"),
today() - birthday, today() - (birthday + duration("1 year")))
```

# Source
- [[Obsidian Bases Made Simple - Visual Use Cases]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M)
