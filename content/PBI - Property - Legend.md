---
aliases:
  - Property - Legend
author:
  - Sascha D. Kasper
description: Configure legend visibility, position, title, and font styling for all Power BI visuals in theme JSON.
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

# Legend

The '"legend"' property can be defined for all visuals. It includes settings for the legend's
- visibility
- position
- title display
- font color, size, and style

## Syntax
```JSON
{
	"name": "LeanProductivity"
    "visualStyles": {
        "*": {
            "*": {
	            "legend": [{
	                    "show": true,
	                    "position": "Top",
	                    "showTitle": false,
	                    "labelColor": { "solid": { "color": "#B3B3B3"   } },
	                    "fontFamily": "Segoe UI",
	                    "fontSize": 10,
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
![[Legend.webp]]

## Settings
![[Legend Settings.webp]]

Back to [[Visual Styles]]
