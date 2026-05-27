---
aliases:
  - Card
author:
  - Sascha D. Kasper
description: Style the original Power BI card visual with theme JSON for value labels, category labels, and word wrap.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visuals
created: 2023-09-11T16:27
updated: 2025-12-11T09:11
---

# Card
>[!hint]- A note about shared properties
>Depending on the chart type, some properties listed in [[Visual Styles]], can be customized for this chart type, too. While the respective code is in the JSON file, it is disabled and the chart will inherit the shared properties from the `"visualStyles"` section.
>This is done by adding a `_` to the property name.
>E.g.:
>Under `"visualStyles/*/*"`, there is a property called `"title"`.
>The same property can be customized for this chart. To inherit the settings from the `"visualStyles"` section, I renamed the property for in the chart section to `"title_"`. If you want to customize the `"title"` settings for this chart type, just rename it to `"title"` in the chart section of the JSON file.

This is the "original" card visual. For the new one, check [[Card Visual]].

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
		"card": {
			"*": {
				"labels": [{ "color": { "solid": { "color": "#FFFFFF" } },
				"labelDisplayUnits": 0,
				"labelPrecision": 0,
				"fontSize": 25,
				"fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
				"bold": false,
				"italic": false,
				"underline": false,
				"preserveWhitespace": true
				}],
				"categoryLabels": [{
					"show": true,
					"color": { "solid": { "color": "#B3B3B3" } },
					"fontSize": 10,
					"fontFamily": "Segoe UI"
				}],
				"wordWrap": [{
					"show": true
				}],
				"background_": [{
					"show": true,
					"color": { "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 14, "Percent": 0 } } } }  },
					"transparency": 0
				}],
				"title_": [{
					"show": true,
				    "fontColor": { "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 12, "Percent": 0 } } } }  },
				    "background": { "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 3, "Percent": -0.5 } } } }  },
				    "alignment": "left",
				    "fontSize": 11,
				    "fontFamily": "Segoe UI Semibold"
				}],
				"border_": [{
				    "show": true,
				    "color": { "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 14, "Percent": 0 } } } }  }
				}]
			}
		}
    }
}
```

## Effect
![[Card.webp]]

## Settings
>[!attention] With the chart selected

![[Card Settings.webp]]

Back to [[Included Visuals]]

# Related
[[Card]]
[[Multi Row Card]]
