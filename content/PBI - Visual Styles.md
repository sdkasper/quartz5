---
aliases:
  - Visual Styles
author:
  - Sascha D. Kasper
description: Use the visualStyles section to control styling for every visual, page, and filter pane in your Power BI theme.
cover:
date: 2023-09-13
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visual-styles
created: 2023-09-13T09:42
updated: 2025-10-03T08:30
---

# Visual Styles

The `"visualStyles"` section is a crucial component that allows you to define and customize the visual styles for various elements and aspects of your reports and dashboards. This section provides detailed control over the aesthetics and presentation of visuals.

By leveraging the `"visualStyles"` section, you can fine-tune the styling of each visual element within your reports. This includes settings for

- all the visuals (shared and individual properties) 
- the report's page and background
- the filter pane

This is also the area where you can define formatting across multiple visuals. There are several properties that many visuals share, and defining them once for all of them saves time and increases the visual consistency of your reports.

### Shared Properties across Visuals


## Syntax
```JSON
{
	"name": "LeanProductivity",
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


