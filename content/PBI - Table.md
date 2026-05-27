---
aliases:
  - Table
author:
  - Sascha D. Kasper
description: Style the table visual in Power BI theme JSON with grid, column headers, values, and subtotal settings.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visuals
created: 2023-09-11T16:26
updated: 2025-12-11T09:11
---

# Table
>[!hint]- A note about shared properties
>Depending on the chart type, some properties listed in [[Visual Styles]], can be customized for this chart type, too. While the respective code is in the JSON file, it is disabled and the chart will inherit the shared properties from the `"visualStyles"` section.
>This is done by adding a `_` to the property name.
>E.g.:
>Under `"visualStyles/*/*"`, there is a property called `"title"`.
>The same property can be customized for this chart. To inherit the settings from the `"visualStyles"` section, I renamed the property for in the chart section to `"title_"`. If you want to customize the `"title"` settings for this chart type, just rename it to `"title"` in the chart section of the JSON file.

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
		"tableEx": {
			"*": {
				"stylePreset": [{ "name": "Minimal" }],
				"grid": [{
					"gridVertical": false,
					"gridVerticalColor": { "solid": { "color": "#B3B3B3" } },
					"gridVerticalWeight": 1,
					"gridHorizontal": true,
					"gridHorizontalColor": { "solid": { "color": "#B3B3B3" } },
					"gridHorizontalWeight": 1,
					"rowPadding": 2,
					"outlineColor": { "solid": { "color": "#25D0F7" } },
					"outlineWeight": 2,
					"textSize": 10,
					"imageHeight": 100
				}],
				"columnHeaders": [{
					"fontColor": { "solid": { "color": "#DBDBDB" } },
					"backColor": { "solid": { "color": "#1B2631" } },
					"outline": "Frame",
					"autoSizeColumnWidth": false,
					"fontFamily": "Segoe UI",
					"fontSize": 10,
					"alignment": "Center",
					"wordWrap": true
				}],
				"values": [{
					"fontColor": { "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 0, "Percent": 0 } } } }  },
					"fontColorPrimary": { "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 0, "Percent": 0 } } } } },
					"backColorPrimary": { "solid": { "color": "#1B2631"}},
					"fontColorSecondary": { "solid": { "color": "#FFFFFF"}},
					"backColorSecondary": { "solid": { "color": "#1B2631"}},
					"outline": "Frame",
					"urlIcon": true,
					"wordWrap": true,
					"fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
					"fontSize": 10
				}],
				"total": [{
					"totals": true,
					"fontColor": { "solid": { "color": "#DBDBDB" } },
					"backColor": { "solid": { "color": "#1B2631" } },
					"outline": "Frame",
					"fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
					"fontSize": 10
				}]
			}
		}
    }
}
```

## Effect
![[Table.webp]]

## Settings
>[!attention] With the chart selected

![[Table Settings.webp]]

Back to [[Included Visuals]]

# Related
[[Matrix]]
