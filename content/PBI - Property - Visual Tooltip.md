---
aliases:
  - Property - Visual Tooltip
author:
  - Sascha D. Kasper
description: Customize data tooltips for all Power BI visuals with title color, value color, background, and font settings.
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

# Visual Tooltip
The '"visualTooltip"' property can be defined for all visuals. Not to be confused with the [[Property - Visual Header Tooltip]], it includes settings for the tooltip's
- title font color
- value font color
- background
- font family and size

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "visualTooltip": [{
                    "titleFontColor": { "solid": { "color": "#DBDBDB" } },
                    "themedValueFontColor": { "solid": { "color": "#FFFFFF" } },
                    "themedBackground": { "solid": { "color": "#1B2631" } },
                    "valueFontColor": { "solid": {  "color": "#FFFFFF" } },
                    "actionFontColor": { "solid": { "color": "#25D0F7" } },
                    "background": { "solid": { "color": "#1C1C1C"   } },
                    "fontFamily":"wf_standard-font, helvetica, arial, sans-serif",
                    "fontSize": 9
                }]
            }
        }
    }
}
```

## Effect
This red box is what you control with these settings.
![[Visual Tooltip.webp]]

## Settings
![[Visual Tooltip Settings.webp]]

Back to [[Visual Styles]]
