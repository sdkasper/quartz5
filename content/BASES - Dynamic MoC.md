---
aliases:
author:
  - Sascha D. Kasper
source:
description: Create a single reusable Base that auto-lists notes in whatever folder you embed it in.
cover: zAttachments/BASES - Dynamic MoC.webp
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
updated: 2026-03-15T21:08:29+02:00
---
# Setup
- Create a new Base, filter to markdown files, and switch to advanced filter
- Embed the Base in folder notes or drag it to the side panel
- Uses `this` context so the same Base adapts to any folder

# Code
```
file.inFolder(this.file.folder)
```

# Source
- [[Obsidian Bases Made Simple - Advanced Tips]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M)
