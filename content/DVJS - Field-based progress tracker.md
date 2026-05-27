---
aliases:
  - obsidian/tweaks/dvjs-field-based-progress-tracker
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/DVJS---Field-based-progress-tracker
description: Track habit completion with a DataviewJS snippet that counts boolean frontmatter fields and shows your progress percentage.
cover:
date: 2024-06-05
draft: false
categories:
  - obsidian
  - dataview
cssclasses:
tags:
  - obsidian
  - dataview
created: 2024-06-05T07:18
updated: 2026-01-09T11:58
---

# Summary
This query will
- check a note's frontmatter for fields (properties) starting with a certain string - in the example with "habit"
- count how many such fields are there
- check how many of them are set to "true"
- calculate the percentage of "true" fields versus total fields
# Setup
This is a DataviewJS query to find files that have "bad" - i.e. corrupt - frontmatter.
# Code
Don't forget to start and end the code block with three backticks.

```dataviewjs
// Get the current page's metadata
const page = dv.current();

// Check if the page and its frontmatter exist
if (page && page.file && page.file.frontmatter) {
    // Access the frontmatter of the current page
    const frontmatter = page.file.frontmatter;

    // Filter the frontmatter to only include keys that start with "habit"
    const habits = Object.entries(frontmatter).filter(([key, value]) => key.startsWith("habit"));

    // Count the total number of "habit" fields
    const totalHabits = habits.length;

    // Count how many of those "habit" fields are set to true
    const trueHabits = habits.filter(([key, value]) => value === true).length;

    // Calculate the completion percentage of true "habit" fields
    const completionPercentage = totalHabits > 0 ? (trueHabits / totalHabits) * 100 : 0;

    // Display the total number of "habit" fields
    dv.paragraph(`Total habit fields: ${totalHabits}`);

    // Display the number of "habit" fields that are true
    dv.paragraph(`True habit fields: ${trueHabits}`);

    // Display the completion percentage of true "habit" fields
    dv.paragraph(`Completion percentage: ${completionPercentage.toFixed(2)}%`);
} else {
    // Display a message if no frontmatter is found in the current note
    dv.paragraph("No frontmatter found in the current note.");
}
```
# Result

![[DVJS - Field-based progress tracker.webp|Note with ten habit checkboxes, two checked, showing 20% completion]]
