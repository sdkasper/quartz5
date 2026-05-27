---
aliases:
author:
  - Sascha D. Kasper
source:
description: Auto-pull the first embedded image from any note and use it as a cover in Bases Cards View.
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
- No extra properties needed
- Create a formula property called `fFirstImage`
- In Cards View, select `fFirstImage` as the image property

# Code
```
if(file.embeds[0].containsAny("jpg","gif","webp","jpeg","avif","png"), file.embeds[0])
```

# Source
- [[Obsidian Bases Made Simple - Advanced Tips]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M)
