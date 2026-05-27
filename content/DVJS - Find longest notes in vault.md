---
aliases:
  - obsidian/tweaks/dvjs-find-longest-notes-in-vault
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/DVJS---Find-longest-notes-in-vault
description: Discover your longest notes by word count with this DataviewJS query using the Better Word Count plugin.
cover:
date: 2024-11-18
draft: false
categories:
  - obsidian
  - dataview
cssclasses:
tags:
  - obsidian
  - dataview
created: 2024-11-18T11:32
updated: 2026-01-25T13:14
---

# Summary
Finds the specified number of notes in your vault, sorted by their length.
# Setup
Requires these community plugins:
- [Dataview](obsidian://show-plugin?id=dataview)
- [Better Word Count](obsidian://show-plugin?id=better-word-count)
# Code
```text
dataviewjs
const bwc = app.plugins.plugins["better-word-count"].api; // Access the Better Word Count plugin's API
const luxon = dv.luxon;

// Get all pages in the vault, ensure they are markdown, exclude "excalidraw.md"
const pages = await dv.pages('""').where(page => page.file.ext === "md" && page.file.path.endsWith("excalidraw.md") == false);

// Array to store the final rows for the table
const tableRows = [];

// Use Promise.all to wait for all word counts
await Promise.all(pages.map(async (page) => {
    const wordCount = await bwc.getWordCountPagePath(page.file.path); // Get word count for the page using Better Word Count plugin
    page.wordCount = wordCount; // Add the word count as a property to the page object
}));

// Create a new array that is sorted
const sortedPages = [...pages].sort((pageA, pageB) => pageB.wordCount - pageA.wordCount);

// Iterate through the sorted pages and add rows to the tableRows array
const numberOfNotesToShow = 10; // Number of largest notes to display
for (let i = 0; i < numberOfNotesToShow && i < sortedPages.length; i++) {
    const page = sortedPages[i];
    const wordCount = page.wordCount;
    const relativeModified = luxon.DateTime.fromISO(page.file.mtime).toRelative();

    tableRows.push([
        page.file.link,
        wordCount,
        relativeModified,
    ]);
}

// Print the table with the top notes based on word count
dv.table(["Name", "Word Count", "Last modified"], tableRows);
```
# Result
Returns a table like this:
![[DVJS - Find longest notes in vault-20241118113617778.webp|Top 10 longest notes ranked by word count, highest at 12,211 words]]
