---
aliases:
  - Property - Sub Title
author:
  - Sascha D. Kasper
description: Style the subtitle for all Power BI visuals with font, alignment, wrapping, and heading tag settings in theme JSON.
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

# Sub Title
The '"subTitle"' property can be defined for all visuals. It includes settings for
- visibility
- html heading tag to use online
- text wrapping
- font color, size, family, and style
- alignment

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "subTitle": [{
                    "show": true,
                    "heading": "Heading4",
                    "fontFamily": "Segoe UI",
                    "fontSize": 9,
                    "bold": false,
                    "italic": false,
                    "underline": false,
                    "fontColor": { "solid": { "color": "#DBDBDB" } },
                    "alignment": "left",
                    "titleWrap": true
                }]
            }
        }
    }
}
```

## Effect
![[Sub Title.webp]]

## Settings
![[Sub Title Settings.webp]]

Back to [[Visual Styles]]
