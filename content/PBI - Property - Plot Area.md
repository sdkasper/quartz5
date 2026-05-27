---
aliases:
  - Property - Plot Area
author:
  - Sascha D. Kasper
description: Set a background image and transparency for the plot area across all Power BI visuals in theme JSON.
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

# Plot Area
The '"plotArea"' property can be defined for all visuals and lets you define an image background. It includes settings for
- image name, path, scaling
- transparency

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "plotArea": [{
                    "image": { "name": "", "url": "", "scaling": "Normal" },
                    "transparency": 0
                }]
            }
        }
    }
}
```

## Effect
Note the image behind the data bars.
![[Plot Area Background Image.webp]]

## Settings
![[Plot Area Settings.webp]]

Back to [[Visual Styles]]
