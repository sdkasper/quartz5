---
aliases:
  - obsidian-course/dv-list-empty-notes
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/DV---list-empty-notes
description: Find all empty (zero-byte) notes in your Obsidian vault with this quick Dataview query.
cover:
date: 2023-12-27
draft: false
categories:
  - obsidian
  - dataview
cssclasses:
tags:
  - obsidian
  - dataview
created: 2023-12-27T13:15
updated: 2026-01-09T11:58
---


# Setup
Paste the code below into your note. Remember to add three backticks before and after the code to mark it as a codeblock.

This will search your complete vault. You can use filters if you want to limit the search to a specific folder or property.
# Code
```text
dataview
TABLE WITHOUT ID
	file.link AS "Empty Notes", file.path AS "File Path"
WHERE file.size = 0
SORT "File Path" ASC, "Empty Notes" ASC
```
# Result
So, in summary, this query creates a table of all empty notes, showing the file link and file path for each note. The table is sorted first by file path and then by file link, both in ascending order. An empty note is defined as a note that has a size of 0.

- `TABLE WITHOUT ID`: starts the creation of a table without an ID column.
- `file.link AS "Empty Notes", file.path AS "File Path"`: This line defines the columns of the table. The table will have two columns: “Empty Notes” and “File Path”. **The “Empty Notes” column will contain the links to the files**, and the **“File Path” column will contain the full paths of the files**.
- `WHERE file.size = 0`: filters the files to include only those that have a size of 0. **In other words, it includes only empty files**.
- `SORT "File Path" ASC, "Empty Notes" ASC`: **sorts** the results **first by the “File Path”** column in ascending order, and **then by the “Empty Notes”** column in ascending order.
## Example output
![[DV - list empty notes output.webp|Dataview table showing one empty note with its file path]]
