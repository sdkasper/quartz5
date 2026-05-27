---
aliases:
  - obsidian/tweaks/dvjs-missing-notes-with-incoming-link-count
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/DVJS---missing-notes-with-incoming-link-count
description: Find uncreated notes in your vault and see how many times each one is linked, so you know which to create first.
cover:
date: 2024-06-03
draft: false
categories:
  - obsidian
  - dataview
cssclasses:
tags:
  - obsidian
  - dataview
created: 2024-06-03T09:27
updated: 2026-01-09T11:58
---

# Setup
This is a DataviewJS query to find files that do not exist and count how often you link to each of these files.
# Code
Don't forget to start and end the code block with three backticks.

```text
dataviewjs
dv.paragraph("## Uncreated Notes with Mentions Count");

let links = dv.app.metadataCache.unresolvedLinks;
let data = [];

for (let file in links) {
    for (let unresolved in links[file]) {
        data.push({ 
            note: unresolved, 
            mentions: links[file][unresolved] 
        });
    }
}

let groupedData = data.reduce((acc, curr) => {
    let found = acc.find(item => item.note === curr.note);
    if (found) {
        found.mentions += curr.mentions;
    } else {
        acc.push(curr);
    }
    return acc;
}, []);

groupedData.sort((a, b) => b.mentions - a.mentions);

dv.table(["Uncreated Note", "Mentions"], groupedData.map(item => [item.note, item.mentions]));
```
# Result

![[DVJS - missing notes with incoming link count-20240603092945119.webp|Table of 111 uncreated notes sorted by mention count, top entry linked 18 times]]
