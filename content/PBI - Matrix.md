---
aliases:
  - Matrix
author:
  - Sascha D. Kasper
description: Style the matrix (pivot table) visual in Power BI with theme JSON for headers, values, subtotals, and grid lines.
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

# Matrix
>[!hint]- A note about shared properties
>Depending on the chart type, some properties listed in [[Visual Styles]], can be customized for this chart type, too. While the respective code is in the JSON file, it is disabled and the chart will inherit the shared properties from the `"visualStyles"` section.
>This is done by adding a `_` to the property name.
>E.g.:
>Under `"visualStyles/*/*"`, there is a property called `"title"`.
>The same property can be customized for this chart. To inherit the settings from the `"visualStyles"` section, I renamed the property for in the chart section to `"title_"`. If you want to customize the `"title"` settings for this chart type, just rename it to `"title"` in the chart section of the JSON file.

If you are looking for a `"matrix"` section in the JSON file, you will be disappointed. It is - rather sneakily - called `"pivotTable"`.

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "pivotTable": {
			"*": {
				"stylePreset":[{ "name":"Minimal" }],
				"grid": [{
					"gridVertical": false,
					"gridVerticalColor": { "solid": { "color": "#B3B3B3" } },
					"gridVerticalWeight": 1,
					"gridHorizontal": false,
					"gridHorizontalColor": { "solid": { "color": "#B3B3B3" } },
					"gridHorizontalWeight": 2,
					"rowPadding": 1,
					"outlineColor": { "solid": { "color": "#FFB8DD" } },
					"outlineWeight": 0,
					"textSize": 10,
					"imageHeight": 100
				}],
				"columnHeaders": [{
					"fontColor": { "solid": { "color": "#DBDBDB" } },
					"backColor": { "solid": { "color": "#1B2631" } },
					"outline": "Frame",
					"autoSizeColumnWidth": false,
					"fontFamily": "Segoe UI Semibold",
					"fontSize": 10,
					"alignment": "Center",
					"titleAlignment": "Left",
					"urlIcon": true,
					"wordWrap": true
				}],
				"rowHeaders": [{
					"fontColor": { "solid": { "color": "#DBDBDB" } },
					"backColor": { "solid": { "color": "#1B2631" } },
					"outline": "Frame",
					"stepped": true,
					"steppedLayoutIndentation": 12,					
					"urlIcon": true,
					"wordWrap": false,
					"fontFamily": "Segoe UI Semibold",
					"fontSize": 10,
					"alignment": "Left", 
					"showExpandCollapseButtons":true
				}],
				"values": [{
					"fontColorPrimary": { "solid": { "color": "#FFFFFF" } },
					"backColorPrimary": { "solid": { "color": "#1B2631" } },
					"fontColorSecondary": { "solid": { "color": "#FFFFFF" } },
					"backColorSecondary": { "solid": { "color": "#29394B" } },
					"bandedRowHeaders": false,
					"valuesOnRow": false,
					"outline": "Frame",
					"urlIcon": true,
					"wordWrap": false,
					"fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
					"fontSize": 10
				}],
				"subTotals": [{
					"rowSubtotals": true,
					"columnSubtotals": true,
					"fontColor": { "solid": { "color": "#FFFFFF" } },
					"fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
					"backColor": { "solid": { "color": "#46607E" } },
					"fontSize": 10,
					"applyToHeaders": true,
					"rowSubtotalsPosition": "Bottom",
					"perRowLevel": true,
					"perColumnLevel": true					
				}],
				"total": [{
					"fontColor": { "solid": { "color": "#FFFFFF" } },
					"fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
					"backColor": { "solid": { "color": "#46607E" } },
					"applyToHeaders": true,
					"fontSize": 10
				}]
			}
        }
    }
}
```

## Effect
![[Matrix.webp]]

## Settings
>[!attention] With the chart selected

![[Matrix Settings.webp]]

Back to [[Included Visuals]]

# Related
[[Table]]
