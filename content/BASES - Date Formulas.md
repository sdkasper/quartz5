---
aliases:
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/BASES---Date-Formulas
description: Copy-paste date formulas for Obsidian Bases -- filter notes by today, this week, this month, and more.
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
updated: 2026-05-14T14:46:06
substackStatus: published
substackId: 191738548
substackUrl: https://skasper.substack.com/p/obsidian-bases-date-formulas
---

# Setup
- These are formula properties added to a Base
- They are based on a frontmatter property called `created` (if you prefer, you can substitute this with the system's "created time" property)
- Filename-based formulas assume `YYYY-MM-DD` naming

# Code
## Today's Date
```
today().toString()
```
## Custom Date Format
```
today().format("YYYY-MM")
```
## Date from Filename
```
date(file.name.slice(0,10))
```
## Notes Created Today
```
today().format("YYYY-MM-DD") == note["created"]
```
## Notes Created Yesterday
```
(today() - "1 d").format("YYYY-MM-DD") == note["created"]
```
## Notes Created Same Day as Current Note
```
this.created.format("YYYY-MM-DD") == note["created"]
```
## Notes Created This Week
```
today().format("Yw") == date(note["created"]).format("Yw")
```
## Notes Created Last Week
```
(today() - "1 w").format("Yw") == date(note["created"]).format("Yw")
```
## Notes Created This Month
```
today().format("YYYY-MM") == note["created"].format("YYYY-MM")
```
## Notes Created Last Month
```
(today()- "1 M").format("YYYY-MM") == note["created"].format("YYYY-MM")
```
## Notes Created This Year
```
today().format("YYYY") == note["created"].format("YYYY")
```
## Notes Created Last Year
```
(today()- "1 y").format("YYYY") == note["created"].format("YYYY")
```

# Source
- [[Obsidian Bases Made Simple - Visual Use Cases]]
- See also: [[BASES - This Day In History]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M?t=1228&si=1OtSWRmoBxDA11u5)
