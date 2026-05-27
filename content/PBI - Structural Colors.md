---
aliases:
  - Structural Colors
author:
  - Sascha D. Kasper
description: Define axis gridlines, highlights, and background colors for all visuals using Power BI structural color properties.
cover:
date: 2023-09-13
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - general
created: 2023-09-13T09:30
updated: 2025-10-03T08:30
---

# Structural Colors

These colors define how axis gridlines, highlights, and backgrounds for visuals look like. For a detailed description, which elements fall into which category, [check this link](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#set-structural-colors).

- `"foreground"` (also known as `"firstLevelElements"`)
- `"foregroundNeutralSecondary"` (aka `"secondLevelElements"`)
- `"backgroundLight"` (aka `"thirdLevelElements"`) - general background colors
- `"foregroundNeutralTertiary"` (aka `"fourthLevelElements"`)
- `"background"`
- `"backgroundNeutral"` (aka `"secondaryBackground"`)
- `"tableAccent"` - the color to be used as [[Table Accent]] color in table and matrix visuals

>[!info] All fore- and backgrounds are covered in [[Foreground, Background]].

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "foreground": "#FFFFFF",
    "foregroundNeutralSecondary": "#B3B3B3",
    "foregroundNeutralTertiary": "#B3B3B3",
    "background": "#1B2631",
    "backgroundNeutral": "#808080",
    "backgroundLight": "#25D0F7",
    "tableAccent": "#25D0F7",
}
```

# Related



[Structural Colors in Power BI Desktop | Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#set-structural-colors)
