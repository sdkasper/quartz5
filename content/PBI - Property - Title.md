---
aliases:
  - Property - Title
author:
  - Sascha D. Kasper
description: Style the title for all Power BI visuals with font, background, alignment, and heading tag settings in theme JSON.
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

# Title
The '"title"' property can be defined for all visuals. It includes settings for
- visibility
- html heading tag to use online
- text wrapping
- font color, size, family, and style
- background

## Syntax
```JSON
{
   "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "title": [{
                    "show": true,
                    "heading": "Heading3",
                    "titleWrap": true,
                    "fontColor": { "solid": { "color": { "#DBDBDB" } } },
                    "background": { "solid": { "color": "#29394B" } },
                    "fontSize": 9,
                    "fontFamily": "Segoe UI Semibold",
                    "alignment" : "left",
                    "bold": false,
                    "italic": false,
                    "underline": false
                }]
            }
        }
    }
}
```

## Effect
![[Title.webp]]

## Settings
![[Title Settings.webp]]

Back to [[Visual Styles]]
