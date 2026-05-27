---
aliases:
  - Property - Visual Header Tooltip
author:
  - Sascha D. Kasper
description: Style the help-icon tooltip in the visual header with font, background, and transparency settings in theme JSON.
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

# Visual Header Tooltip
The '"visualheaderTooltip"' property can be defined for all visuals. It includes settings for the tooltip that can be displayed when a user hovers over the "help" icon in a visual's header.

You can define the tooltip's
- background
- font color, size, family, and style
- transparency

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "visualHeaderTooltip": [{
					"themedBackground": { "solid": { "color": "#1B2631" } },
                    "titleFontColor": { "solid": { "color": "#DBDBDB" } },
                    "fontSize": 9,
                    "fontFamily": "Segoe UI",
                    "bold": false,
                    "italic": false,
                    "underline": false,
                    "background": { "solid": { "color": "#1B2631" } },
                    "transparency": 5
                }]
            }
        }
    }
}
```

## Effect
![[Visual Header Tooltip.webp]]

## Settings
>[!hint] Note that the `"Help tooltip"` needs to be enabled in the visual's formatting pane.

![[Visual Header Tooltip Settings.webp]]

Back to [[Visual Styles]]
