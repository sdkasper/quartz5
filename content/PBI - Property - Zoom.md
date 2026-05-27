---
aliases:
  - Property - Zoom
author:
  - Sascha D. Kasper
description: Toggle the zoom slider on category and value axes for Power BI visuals using the shared zoom property.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visual-styles
created: 2023-09-11T16:33
updated: 2025-12-11T09:11
---

# Zoom

The '"zoom"' property can be defined for all visuals. Note that not all visuals support a zoom slider. It includes settings for
- overall visibility
- axis-specific visibility
- label visibility
- tooltip visibility

## Syntax
 ```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "zoom": [{
                    "show": false,
                    "showOnCategoryAxis": true,
                    "showOnValueAxis": true,
                    "showLabels": false,
                    "showTooltip": false
                }]
            }
        }
    }
}
```

## Effect
![[Zoom.webp]]

## Settings
![[Zoom Settings.webp]]

Back to [[Visual Styles]]
