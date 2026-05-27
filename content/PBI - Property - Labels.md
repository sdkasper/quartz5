---
aliases:
  - Property - Labels
author:
  - Sascha D. Kasper
description: Control data label fonts, colors, positions, density, and background for all Power BI visuals in theme JSON.
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

# Property - Labels
The '"labels"' property can be defined for all visuals. It includes settings for
- label visibility
- font color, size, family, style
- background display, color, transparency
- display units
- label precision
- label position
- label overflow
- label density

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "labels": [{
                    "show": true,
                    "color": { "solid": { "color": { "#FFFF" } } },
                    "fontSize": 10,
                    "fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
                    "enableBackground": false,
                    "backgroundColor": { "solid": { "color": "#000000" } },
                    "backgroundTransparency": 90,
                    "labelDisplayUnits": 0,
                    "labelPrecision": 1,
                    "bold": false,
                    "italic": false,
                    "underline": false,
                    "labelPosition": "Auto",
                    "labelOverflow": false,
                    "labelDensity": 50
                }]
            }
        }
    }
}
```

## Effect
![[Data Labels.webp]]

## Settings
![[Data Labels - Settings.webp]]

Back to [[Visual Styles]]
