---
aliases:
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Obsidian-Tweaks-&-Tips---Episode-III
description: Four Obsidian tweaks covering styled table of contents, finding missing and empty notes with Dataview, and faster startup with Plugin Groups.
cover:
date: 2023-12-29
updated: 2026-03-09T14:25:25+02:00
draft: false
categories:
  - obsidian
cssclasses:
tags:
  - obsidian
  - tweaks
created: 2023-12-29T00:00
---

# In a Nutshell

> [!important|float-r] Useful / Download  
> - [TOC CSS snippet](https://wiki.sascha-kasper.com/obsidian/tweaks/css-toc-formatting/)  
> - [List missing notes](https://wiki.sascha-kasper.com/obsidian/tweaks/dv-list-missing-notes/)  
> - [List empty notes](https://wiki.sascha-kasper.com/obsidian/tweaks/dv-list-empty-notes/)  
> * Series:
> [[Obsidian Tweaks & Tips - Episode I|Ep. I]]  
> [[Obsidian Tweaks & Tips - Episode II|Ep. II]]  
> [[Obsidian Tweaks & Tips - Episode IV|Ep. IV]]  
> [[Obsidian Tweaks & Tips - Episode V|Ep. V]]

This is the third part of the ongoing series about Obsidian tweaks and tips. I keep collecting those from all over the internet and demonstrate them in the video below.

# Make the table of contents match your note

I found this one on Reddit, posted by user [stassinari](https://www.reddit.com/user/stassinari/). It modifies the appearance of the note outline in the side pane to match the heading formats of your note. This makes it easier to read and -- especially for longer notes -- navigate.

Outline before

Outline after

For this, you need a CSS snippet. You can [copy the code from here](https://wiki.sascha-kasper.com/obsidian/tweaks/css-toc-formatting/). The video above explains how to use it.

# Find missing files

## List links to non-existing notes

Copy the code from the link below and insert it into your note. Remember to add three backticks before and after the code to mark it as a code block.

For this, you need a dataview query.

You can [copy the code from here](https://wiki.sascha-kasper.com/obsidian/tweaks/dv-list-missing-notes/).

# Find empty files

## List notes without content

This is another dataview query that you can easily adapt to your own needs. The version you can find at the link below will search your complete vault and return a list of empty notes.

You can [copy the code from here](https://wiki.sascha-kasper.com/obsidian/tweaks/dv-list-empty-notes/).

# Load Obsidian faster

## Reduce Obsidian startup time

Technically, this is not a tweak. Look for the "Plugin Groups" plugin. It allows you to delay the loading of plugins, letting you start working in Obsidian faster without having to fully disable plugins.

# More in This Series

- [[Obsidian Tweaks & Tips - Episode I|Episode I]] -- Templater callout script, auto-hide properties
- [[Obsidian Tweaks & Tips - Episode II|Episode II]] -- Active tab color, hotkey sync, hide specific properties
- Episode III -- Styled TOC, find missing/empty notes, Plugin Groups
- [[Obsidian Tweaks & Tips - Episode IV|Episode IV]] -- Bad YAML finder, stacked tabs, dropdown fields, bullet threading
- [[Obsidian Tweaks & Tips - Episode V|Episode V]] -- Columns, floating callouts, table styles, tasks dashboard, help tooltip
