---
aliases:
author:
  - Sascha D. Kasper
source:
description: Build editable Dataview tables in Obsidian using DataviewJS and Metadata Menu so you can update fields without opening each note.
cover:
date: 2023-12-25
draft: false
categories:
  - obsidian
  - dataview
cssclasses:
tags:
  - obsidian
  - dataview
created: 2023-12-25T15:36
updated: 2025-10-03T08:30
---


# Setup
This is a DataviewJS query, utilizing the Metadata Menu Plugin and Templater to create a table with results that can be edited directly, i.e., without having to open the respective note.
# Code
Don't forget to start and end the code block with three backticks.

```text
dataviewjs
const {fieldModifier: f} =
	  this.app.plugins.plugins["metadata-menu"].api;

dv.table(['Date', '🚶', '🏋️‍♀️', '🍴', '😴', '🧑‍🤝‍🧑', 'PU', 'CR', '🗒️'],
dv.pages('')
	.where(p => p.file.path.includes('06 📖 BJ/10 Daily'))
	// .where(p => p.tags && p.tags.includes('BJ/Daily'))
	// .filter(p => !p.file.path.includes('90 Organize'))
	// .filter(p => !p.file.path.includes('99 🧪 The Lab'))
	.filter(p => p.Week && p.Week == '2023-W52')
	.sort(p => p.file.name)
	.map(p => [
		p.file.link,
		f(dv, p, "Walk"),
		f(dv, p, "Workout"),
		f(dv, p, "Challenge1"),
		f(dv, p, "Sleep"),
		f(dv, p, "REL"),
		f(dv, p, "Challenge2"),
		f(dv, p, "Challenge3"),
		f(dv, p, "Note")
	])
)
```
# Result
![Animated demo of editing habit fields directly in a Dataview table without opening each note](https://i.imgur.com/mDkcI4G.gif)
