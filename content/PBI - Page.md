---
aliases:
  - Page
author:
  - Sascha D. Kasper
description: Set default page layout, background, size, and outspace pane for all report pages in your Power BI theme JSON.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - general
created: 2023-09-11T16:21
updated: 2025-12-11T09:11
---

# Page
Use the `"page"` element to define the default layout of all pages in your report. You cannot only control how they look like by defining
- background
	- visibility
	- color
	- transparency
	- image (if not a color)
- size
	- type
	- height
	- width
	- vertical alignment
- [[Outspace Pane]]

but also
- whether they can be used as tooltip
- whether you want to allow Q&A on them

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "page": {
                "*": {
                    "settings": [{
                        "allowUseAsTooltip": false,
                        "allowQnA": false
                    }],
                    "background": [{
                        "show" : "true",
                        "color": { "solid": { "color": "#000000" } },
                        "transparency": 0,
                        "image": { "name": "", "url": "", "scaling": "Normal" }
                    }],
                    "outspace": [{
                        "color": { "solid": { "color": "#1B2631" } },
                        "transparency": 0
                    }],
                    "displayArea": [{
                        "type": "16:9",
                        "height": 720,
                        "width": 1280,
                        "verticalAlignment": "Middle"
                    }]
                }
            }
        }
    }
}
```

## Settings
>[!attention] Make sure to have no visual selected.

![[Page Settings.webp]]

# Related


