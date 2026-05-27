---
aliases:
  - Property - Divider
author:
  - Sascha D. Kasper
description: Style the divider line between title and content on all Power BI visuals with color, width, and padding options.
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

# Divider
The '"divider"' property can be defined for all visuals. It includes settings for
- visibility
- color
- style
- width
- use of padding

The '"ignorePadding"' attribute defines whether the divider line will respect the values for left and right padding:

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "divider": [{
                    "show": true,
                    "color": { "solid": { "color": "#1C1C1C" } },
                    "style": "dotted",
                    "width": 1,
                    "ignorePadding": true
                }]
            }
        }
    }
}
```

## Effect
![[Divider.webp]]

## Settings
### Divider
![[Divider Settings.webp]]

### Padding
![[Padding Settings.webp]]

Back to [[Visual Styles]]
