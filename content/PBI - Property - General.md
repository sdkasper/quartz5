---
aliases:
  - Property - General
author:
  - Sascha D. Kasper
description: Set layer order, responsiveness, outline color, and orientation for all Power BI visuals via the general property.
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

# General

The '"general"' property can be defined for all visuals. It includes settings for
- layer order
- responsiveness
- outline color and weight
- orientation.

## Syntax
```JSON
{
	"name": "LeanProducitivity",
	"visualStyles": {
        "*": {
            "*": {
                "general": [{
					"keepLayerOrder": true,
					"responsive": true,
                    "outlineColor": {   "solid": { "color": "#1B2631" } },
                    "outlineWeight": 2,
                    "orientation": 0
                }]
			}
		}
	}
}
```

## Settings
![[General Visual Settings.webp]]
![[General Visual Border Settings.webp]]

Back to [[Visual Styles]]
