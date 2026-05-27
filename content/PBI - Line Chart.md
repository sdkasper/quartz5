---
aliases:
  - Line Chart
author:
  - Sascha D. Kasper
description: Style the line chart in your Power BI theme JSON with axes, gridlines, labels, totals, and data point settings.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visuals
created: 2023-09-11T16:23
updated: 2025-12-11T09:11
---

# Line Chart
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
		"lineChart": {
			"*": {
			  "general_": [{
				  "responsive": true,
				  "keepLayerOrder": true,
				  "outlineColor": {	"solid": { "color": "#1B2631" } },
				  "outlineWeight": 2,
				  "orientation": 0
				}],
				"legend_": [{
					"show": true,
					"position": "Top",
					"showTitle": false,
					"labelColor": { "solid": { "color": "#B3B3B3"	} },
					"fontFamily": "Segoe UI",
					"fontSize": 10,
					"bold": false,
					"italic": false,
					"underline": false
				}],
				"valueAxis": [{
					"position": "Left",
					"show": true,
					"axisType": "Scalar",
					"axisScale": "linear",
					"invertAxis": false,
					"labelColor": { "solid": { "color": "#B3B3B3"	} },
					"fontSize": 10,
					"fontFamily": "Segoe UI",
					"bold": false,
					"italic": false,
					"underline": false,
					"labelDisplayUnits": 0,
					"labelPrecision": 0,
					"preferredCategoryWidth": 20,
					"maxMarginFactor": 25,
					"innerPadding": 20,
					"concatenateLabels": false,
					"showAxisTitle": true,
					"titleColor": { "solid": { "color": "#B3B3B3"	} },
					"titleFontSize": 11,
					"titleFontFamily": "Segoe UI",
					"titleBold": false,
					"titleItalic": false,
					"titleUnderline": false,
					"gridlineShow": true,
					"gridlineColor": { "solid": { "color": "#B3B3B3" } },
					"gridlineThickness": 1,
					"gridlineStyle": "dotted"
				}],
				"categoryAxis": [{
					"position": "Left",
					"gridlineShow": true,
					"show": true,
					"axisScale": "linear",
					"invertAxis": false,
					"labelColor": { "solid": { "color": "#B3B3B3" } },
					"fontSize": 10,
					"fontFamily": "Segoe UI",
					"bold": false,
					"italic": false,
					"underline": false,
					"switchAxisPosition": false,
					"labelDisplayUnits": 0,
					"labelPrecision": 0,
					"showAxisTitle": true,
					"axisStyle": "showTitleOnly",
					"titleColor": { "solid": { "color": "#B3B3B3"	} },
					"titleFontSize": 11,
					"titleFontFamily": "Segoe UI",
					"titleBold": false,
					"titleItalic": false,
					"titleUnderline": false,
					"gridlineColor": { "solid": { "color": "#B3B3B3" } },
					"gridlineThickness": 1,
					"gridlineStyle": "dotted"
				}],
				"zoom_": [{
					"show": false,
					"showOnCategoryAxis": true,
					"showOnValueAxis": true,
					"showLabels": false,
					"showTooltip": false
				}],
				"dataPoint_": [{
					"showAllDataPoints": false,
					"fill": { "solid": { "color": "#25D0F7" } }
				}],
				"labels_": [{
					"color": { "solid": { "color": "#FFFFFF" } },
					"labelDisplayUnits": 0,
					"labelPrecision": 0,
					"fontSize": 10,
					"fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
					"bold": false,
					"italic": false,
					"underline": false,
					"show": true,
					"labelPosition": "Auto",
					"labelOverflow": false,
					"labelDensity": 50,
					"enableBackground": false,
					"backgroundColor": { "solid": { "color": "#FFFFFF" } },
					"backgroundTransparency": 90
				}],
				"totals": [{
					"show": true,
					"color": { "solid": { "color": "#FC3634"	} },
					"labelDisplayUnits": 0,
					"labelPrecision": 0,
					"fontSize": 10,
					"fontFamily": "wf_standard-font, helvetica, arial, sans-serif",
					"enableBackground": false,
					"backgroundColor": { "solid": { "color": "#252423" } },
					"backgroundTransparency": 90,
					"showPositiveAndNegative": false
				}],
				"plotArea_": [{
					"image": { "name": "", "url": "", "scaling": "Normal" },
					"transparency": 0
				}],
				"title_": [{
					"show": true,
					"heading": "Heading3",
					"titleWrap": true,
					"fontColor": { "solid": { "color": "#DBDBDB" } },
					"background": { "solid": { "color": "#003E80"	} },
					"alignment": "left",
					"fontSize": 11,
					"fontFamily": "Segoe UI Semibold",
					"bold": false,
					"italic": false,
					"underline": false
				}],
				"subTitle_": [{
					"show": true,
					"heading": "Heading4",
					"fontFamily": "Segoe UI",
					"fontSize": 9,
					"bold": false,
					"italic": false,
					"underline": false,
					"fontColor": { "solid": { "color": "#DBDBDB" } },
					"alignment": "left",
					"titleWrap": true
				}],
				"divider_": [{
					"show": true,
					"color": { "solid": { "color": "#003E80" } },
					"style": "dotted",
					"width": 1,
					"ignorePadding": true
				}],
				"spacing_": [{
					"customizeSpacing": false,
					"verticalSpacing": 5,
					"spaceBelowTitle": 5,
					"spaceBelowSubTitle": 5,
					"spaceBelowTitleArea": 5
				}],
				"background_": [{
					"show": true,
					"color": { "solid": { "color": "#1B2631" } },
					"transparency": 0
				}],
				"lockAspect_": [{
					"show": false
				} ],
				"border_": [{
					"color": { "solid": { "color": "#1B2631" } },
					"show": true,
					"radius": 5
				}],
				"dropShadow_": [{
					"show": false,
					"color": { "solid": { "color": "#252423" } },
					"position": "Outer",
					"preset": "BottomRight",
					"shadowSpread": 3,
					"shadowBlur": 10,
					"angle": 45,
					"shadowDistance": 10,
					"transparency": 70
				}],
				"visualTooltip_": [{
					"show": true,
					"type": "Canvas",
					"titleFontColor": { "solid": { "color": "#FFFFFF"	} },
					"valueFontColor": { "solid": { "color": "#FFFFFF" } },
					"actionFontColor": { "solid": { "color": "#25D0F7" } },
					"fontSize": 12,
					"fontFamily": "Segoe UI",
					"bold": false,
					"italic": false,
					"underline": false,
					"background": { "solid": { "color": "#1C1C1C" } },
					"transparency": 5,
					"page": "Auto"
				}],
				"visualHeader_": [{
					"show": true,
					"background": { "solid": { "color": "#1C1C1C"	} },
					"border": { "solid": { "color": "#1C1C1C"	} },
					"transparency": 0,
					"foreground": { "solid": { "color": "#25D0F7" } },
					"showVisualInformationButton": false,
					"showVisualWarningButton": false,
					"showVisualErrorButton": true,
					"showDrillRoleSelector": true,
					"showDrillUpButton": true,
					"showDrillToggleButton": true,
					"showDrillDownLevelButton": true,
					"showDrillDownExpandButton": true,
					"showPinButton": true,
					"showFocusModeButton": true,
					"showFilterRestatementButton": true,
					"showSeeDataLayoutToggleButton": false,
					"showOptionsMenu": true,
					"showTooltipButton": false,
					"showCommentButton": false,
					"showPersonalizeVisualButton": true,
					"showSmartNarrativeButton": false
				}]
			}
		}
    }
}
```

## Effect
![[Line Chart.webp]]

## Settings
>[!attention] With the chart selected

![[Line Chart Settings.webp]]

Back to [[Included Visuals]]

# Related
[[Line Stacked Column Combo Chart]]
[[Line Clustered Column Combo Chart]]
[[Ribbon Chart]]
