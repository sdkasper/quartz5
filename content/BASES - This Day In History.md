---
aliases:
  - obsidian/tweaks/bases-this-day-in-history
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/BASES---This-Day-In-History
description: Surface notes created on this day in previous years with an embeddable Obsidian Base query.
cover:
date: 2025-10-09
draft: false
categories:
  - obsidian
  - bases
cssclasses:
tags:
  - obsidian
  - bases
created: 2023-12-25T11:32
updated: 2026-01-15T18:08
---


# Setup
- Create a new "Base" - either directly in Obsidian or in the editor of your choice. Let's call it `This Day in History.base`.
- Open the new file in your text editor. 
- Copy the code below and paste it into the editor.
- Save the file.
- Adapt the code in the text editor or open the file in Obsidian and adjust the filter settings there to match your environment.
- Embed the Base in your daily notes.

> [!important] Important
> This is based on the assumption that your daily notes are named in the format `YYYY-MM-DD`. If they are not, you need to adapt the query accordingly.

# Result
You will get a list of notes created on this day over the years. If you place it inside a callout, it looks like this:

![[BASES - This Day In History.webp|Callout listing daily notes created on October 9 in previous years|600]]


> [!info] 
> The code will only give you a list of files. In the image above, I embedded the Base in a callout.


# Code
```text
filters:
  and:
    - file.basename != this.file.basename
properties:
  file.name:
    displayName: Name
views:
  - type: list
    name: Table
    filters:
      and:
        - file.name.contains(date(this.file.name).format("MM-DD").toString())
    sort:
      - property: file.name
        direction: DESC
```

# Source
- [[Obsidian Bases Made Simple - Visual Use Cases]]
- See it in action: [YouTube](https://youtu.be/34NAe62IH-M)
