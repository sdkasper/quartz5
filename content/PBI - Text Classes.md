---
aliases:
  - Text Classes
author:
  - Sascha D. Kasper
description: Define reusable text styles for labels, callouts, titles, and headers in your Power BI theme JSON.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - general
created: 2023-09-11T11:45
updated: 2025-12-11T09:11
---

# Text Classes

The `"textClasses"` property is used to define custom text formatting that can be applied to different text elements within your reports and dashboards. This property allows you to create and customize specific text styles, such as font size, font weight, or text color, for various purposes.

By utilizing the `"textClasses"` property, you can enhance the visual appeal and readability of your Power BI assets and ensure that text elements are styled appropriately to convey information effectively to your audience.

## Syntax

```JSON
{
	"name": "LeanProductivity"
    "textClasses": {
        "label": {
	        "color": "#DBDBDB",
	        "fontFace": "Segoe UI",
	        "fontSize": 9
		},
        "callout": {
	        "color": "#FFFFFF",
	        "fontFace": "Segoe UI",
	        "fontSize": 45
		},
        "title": {
	        "color": "#FFFFFF",
	        "fontFace": "Segoe UI",
	        "fontSize": 11
		},
        "header": {
	        "color": "#DBDBDB",
	        "fontFace": "Segoe UI",
	        "fontSize": 10
		},
    },
}
```

## Settings
![[Text Classes Settings.webp]]

# Related


