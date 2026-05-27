---
aliases:
  - obsidian/tweaks/dvjs-log-review-and-analysis
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/DVJS---Log-Review-and-analysis
description: "Pull tagged log entries like #win from your daily notes into a summary table using DataviewJS."
cover:
date: 2025-02-18
draft: false
categories:
  - obsidian
  - dataview
cssclasses:
tags:
  - obsidian
  - dataview
created: 2025-02-18T09:36
updated: 2026-01-25T13:13
---


This query is part of the logging versus journaling video tutorial over here: https://youtu.be/GK7TLrILmjE.
# Code
Don't forget to start and end the code block with three backticks.

```text
dataviewjs
dv.table(["Date", "Win"],  // Define table headers
	await Promise.all(dv.pages('"06 BJ/10 Daily/2025"')  // Get all notes from the specified folder
	  .filter(p => p.file.path.endsWith(".md"))  // Ensure only Markdown files are considered
	  .map(async p => {
		  let content = await dv.io.load(p.file.path);  // Load the full note content
		  
		  // Find all occurrences of "#win" followed by text (captures text after "#win")
		  let matches = content.match(/#win\s+(.*)/g);

		  // Extract and clean text: remove "#win", trim spaces, and join multiple matches with line breaks
		  let winText = matches ? matches.map(m => m.replace("#win", "").trim()).join("<br>") : "";

		  // Return a row for the table only if "#win" is found
		  return matches ? [p.file.link, winText] : null;
	  }))
	  .then(rows => rows.filter(row => row)) // Remove null values (notes without "#win")
);
```

# Result
This query creates a table based on log entries in your daily notes with two columns.
The first column shows the note's name and links to it.
The second column displays the text from the daily note after the tag `#win`
## Screenshot
![[DVJS - Log Review and analysis.webp|Dataview table pulling tagged win entries from daily notes with dates]]
