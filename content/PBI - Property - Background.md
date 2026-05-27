---
aliases:
  - Property - Background
author:
  - Sascha D. Kasper
description: Control background visibility, color, and transparency for all Power BI visuals via the shared background property.
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

# Background

The '"background"' property can be defined for all visuals. It includes settings for background
- visibility
- color
- transparency

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "background": [{
                    "show": true,
                    "color": { "solid": { "color": "#1B2631" } },
                    "transparency": 0
                }]
            }
        }
    }
}
```

## Effect
These settings controls the red area in the image.
![[Visual Background.webp]]

## Settings
![[Visual Background Settings.webp]]

Back to [[Visual Styles]]
