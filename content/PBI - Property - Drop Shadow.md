---
aliases:
  - Property - Drop Shadow
author:
  - Sascha D. Kasper
description: Add drop shadows to all Power BI visuals with theme JSON settings for color, blur, angle, spread, and position.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visual-styles
created: 2023-09-11T16:32
updated: 2025-12-11T09:11
---

# Drop Shadow
The '"dropShadow"' property can be defined for all visuals and defines a visual's drop shadow properties. It includes settings for
- visibility
- color
- position
- preset
- spread
- blur
- angle
- distance
- transparency

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "dropShadow": [{
                    "show": false,
                    "color": { "solid": { "color": "#252423" } },
                    "position": "Outer",
                    "preset": "BottomRight",
                    "shadowSpread": 3,
                    "shadowBlur": 10,
                    "angle": 45,
                    "shadowDistance": 10,
                    "transparency": 70
                }]
            }
        }
    }
}
```

## Effect
>[!hint] Note the red shadow.

![[Drop Shadow.webp]]

## Settings
![[Drop Shadow Settings.webp]]



Back to [[Visual Styles]]
