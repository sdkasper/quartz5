---
aliases:
  - obsidian-course/dv-list-missing-notes
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/DV---list-missing-notes
description: List all broken wikilinks in your vault with a simple Dataview query so you can spot and fix missing notes fast.
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
created: 2023-12-27T12:21
updated: 2026-01-09T11:58
---


# Setup
Paste the code below into your note. Remember to add three backticks before and after the code to mark it as a codeblock.

Adjust the values for file names and file paths you want to exclude by replacing `Template` and `90 Organize` with whatever works for your vault. If you need only one of these filter options, you can delete the other one. Of course, you can also add additional ones following the pattern in the example.
# Code
```text
dataview
TABLE WITHOUT ID
	out AS "Target", file.link as "Source"
FLATTEN file.outlinks as out
WHERE !(out.file)
	AND !contains(meta(out).path, "/")
	AND !contains(file.link,"Template")
	AND !contains(file.path, "90 Organize/")
SORT out ASC
```
# Result
This query creates a table of broken links (links that do not point to an existing file) that do not point to a different folder or to a file with “Template” in its name or to a file in the “90 Organize” folder. The table has two columns: “Target” (the broken link) and “Source” (the file that contains the link).

- `TABLE WITHOUT ID`: starts the creation of a table without an ID column.
- `out AS "Target", file.link as "Source"`: defines the columns of the table. **The table will have two columns: “Target” and “Source”**. The “Target” column will contain the values of `out` (which are the outgoing links from a file), and the “Source” column will contain the links to the files themselves.
- `FLATTEN file.outlinks as out`: flattens the `outlinks` property of each file (which is an array of links) into a single list of links, and assigns it to the variable `out`.
- `WHERE !(out.file)`: filters the list of links to include only those that do not point to an existing file. **In other words, it includes only broken links.**
- `AND !contains(meta(out).path, "/")`: further filters the list of links to exclude those whose path contains a “/”. **This effectively excludes links that point to a different folder**.
- `AND !contains(file.link,"Template")`: further filters the list of links to exclude those whose file link contains the word “Template”. **This can be useful to exclude template files from the results**.
- `AND !contains(file.path, "90 Organize/")`: further filters the list of links to exclude those whose file path contains “90 Organize/”. **This can be useful to exclude files in a specific folder (in this case, “90 Organize”) from the results**.
- `SORT out ASC`: sorts the results in ascending order by the Target column.
## Example output
![[DV - list missing notes output.webp|Dataview table listing 62 broken wikilinks with their source notes]]
