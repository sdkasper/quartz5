---
aliases:
  - Data Colors
author:
  - Sascha D. Kasper
description: Define your report's primary color palette with the dataColors array in the Power BI theme JSON.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - general
created: 2023-09-11T11:45
updated: 2025-12-11T09:11
---

# Data Colors

The `"dataColors"` array in the Theme JSON file defines the primary color palette for your reports. You can customize these colors to match your organization's branding. Each color code in the array corresponds to a specific purpose, such as data series colors or background colors.

The first eight colors will be visible in Power BI's color picker. You can define more than those, though, and they will be used in visuals for coloring your data.

## Syntax

```JSON
{
    "name": "LeanProductivity",
    "dataColors": [
        "#25D0F7",
        "#007BFF",
        "#FFED68",
        "#77C66B",
        "#A991D4",
        "#FC3634",
        "#CC7859",
        "#FFD700",
        "#3498DB",
        "#46607E",
        "#DBDBDB",
    ],
}
```

## Settings
![[Theme Colors Settings.webp]]

# Related


