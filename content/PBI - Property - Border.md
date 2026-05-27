---
aliases:
  - Property - Border
author:
  - Sascha D. Kasper
description: Set border color, visibility, and radius for all Power BI visuals using the shared border property in theme JSON.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visual-styles
created: 2023-09-11T16:31
updated: 2025-12-11T09:11
---

# Border

The '"border"' property can be defined for all visuals. It includes settings for a visual's border
- color
- visibility
- radius

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "border": [{
                    "color": { "solid": { "color": "#46607E" } },
                    "show": true,
                    "radius": 5
                }]
            }
        }
    }
}
```

## Effect
![[Border.webp]]

## Settings
![[Border Settings.webp]]
