---
aliases:
  - Action Button
author:
  - Sascha D. Kasper
description: Style Power BI action buttons across default, hover, selected, and disabled states with theme JSON.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visuals
created: 2023-09-11T16:22
updated: 2025-12-11T09:11
---

# Action Button
>[!hint]- A note about shared properties
>Depending on the chart type, some properties listed in [[Visual Styles]], can be customized for this chart type, too. While the respective code is in the JSON file, it is disabled and the chart will inherit the shared properties from the `"visualStyles"` section.
>This is done by adding a `_` to the property name.
>E.g.:
>Under `"visualStyles/*/*"`, there is a property called `"title"`.
>The same property can be customized for this chart. To inherit the settings from the `"visualStyles"` section, I renamed the property for in the chart section to `"title_"`. If you want to customize the `"title"` settings for this chart type, just rename it to `"title"` in the chart section of the JSON file.

The `"actionButton"` section comes with a lot of properties because you can define the same things (font styles, colors, shapes, etc.) for four different states:
- default
- hover
- selected
- disabled

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
		"actionButton": {
			"*": {
				"text": [{
					"$id": "default",
					"text": "text",
					"fontColor": { "solid": { "color": "#FFFFFF" } },
					"fontSize": 10,
					"fontFamily": "Segoe UI",
					"bold": false,
					"italic": false,
					"underline": false,
					"verticalAlignment": "middle",
					"horizontalAlignment": "center",
					"rightMargin": 0,
					"leftMargin": 0,
					"topMargin": 0,
					"bottomMargin": 0
					},
					{
						"$id": "hover",
						"text": "text",
						"fontColor": { "solid": { "color": "#FFFFFF" } },
						"fontSize": 10,
						"fontFamily": "Segoe UI",
						"bold": false,
						"italic": false,
						"underline": false,
						"verticalAlignment": "middle",
						"horizontalAlignment": "center",
						"rightMargin": 0,
						"leftMargin": 0,
						"topMargin": 0,
						"bottomMargin": 0
					},
					{
						"$id": "selected",
						"text": "text",
						"fontColor": { "solid": { "color": "#000000" } },
						"fontSize": 10,
						"fontFamily": "Segoe UI",
						"bold": false,
						"italic": false,
						"underline": false,
						"verticalAlignment": "middle",
						"horizontalAlignment": "center",
						"rightMargin": 0,
						"leftMargin": 0,
						"topMargin": 0,
						"bottomMargin": 0
					},
					{
						"$id": "disabled",
						"text": "text",
						"fontColor": { "solid": { "color": "#000000" } },
						"fontSize": 10,
						"fontFamily": "Segoe UI",
						"bold": false,
						"italic": false,
						"underline": false,
						"verticalAlignment": "middle",
						"horizontalAlignment": "center",
						"rightMargin": 0,
						"leftMargin": 0,
						"topMargin": 0,
						"bottomMargin": 0
					},
					{
					"show": true
				}],
				"icon": [{
					"$id": "default",
					"shapeType": "help",
					"padding": 4,
					"placement": "custom",
					"verticalAlignment": "middle",
					"horizontalAlignment": "center",
					"lineColor": { "solid": { "color": "#FFFFFF" } },
					"lineTransparency": 0,
					"lineWeight": 3,
					"rightMargin": 0,
					"leftMargin": 0,
					"topMargin": 0,
					"bottomMargin": 0,
					"iconSize": 0
					},
					{
					"$id": "hover",
					"shapeType": "help",
					"padding": 4,
					"placement": "custom",
					"verticalAlignment": "middle",
					"horizontalAlignment": "center",
					"lineColor": { "solid": { "color": "#FFFFFF" } },
					"lineTransparency": 0,
					"lineWeight": 3,
					"rightMargin": 0,
					"leftMargin": 0,
					"topMargin": 0,
					"bottomMargin": 0,
					"iconSize": 0
					},
					{
					"$id": "selected",
					"shapeType": "help",
					"padding": 4,
					"placement": "custom",
					"verticalAlignment": "middle",
					"horizontalAlignment": "center",
					"lineColor": { "solid": { "color": "#000000" } },
					"lineTransparency": 0,
					"lineWeight": 3,
					"rightMargin": 0,
					"leftMargin": 0,
					"topMargin": 0,
					"bottomMargin": 0,
					"iconSize": 0
					},
					{
					"$id": "disabled",
					"shapeType": "help",
					"padding": 4,
					"placement": "custom",
					"verticalAlignment": "middle",
					"horizontalAlignment": "center",
					"lineColor": { "solid": { "color": "#000000" } },
					"lineTransparency": 0,
					"lineWeight": 3,
					"rightMargin": 0,
					"leftMargin": 0,
					"topMargin": 0,
					"bottomMargin": 0,
					"iconSize": 0
					},
					{
					"show": true
				}],
				"outline": [{
					"$id": "default",
					"roundEdge": 0,
					"lineColor": { "solid": { "color": "#1C1C1C" } },
					"weight": 1,
					"transparency": 0
					},
					{
					"$id": "hover",
					"roundEdge": 0,
					"lineColor": { "solid": { "color": "#0D6ABF" } },
					"weight": 1,
					"transparency": 0
					},
					{
					"$id": "selected",
					"roundEdge": 0,
					"lineColor": { "solid": { "color": "#25D0F7" } },
					"weight": 1,
					"transparency": 0
					},
					{
					"$id": "disabled",
					"roundEdge": 0,
					"lineColor": { "solid": { "color": "#B3B3B3" } },
					"weight": 1,
					"transparency": 0
					},
					{
					"show": true
				}],
				"fill": [{
					"$id": "default",
					"image": { "name": "", "url": "", "scaling": "Normal" },
					"fillColor": { "solid": { "color": "#1C1C1C" } },
					"transparency": 0
					},
					{
					"$id": "hover",
					"image": { "name": "", "url": "", "scaling": "Normal" },
					"fillColor": { "solid": { "color": "#0066FF" } },
					"transparency": 0
					},
					{
					"$id": "selected",
					"image": { "name": "", "url": "", "scaling": "Normal" },
					"fillColor": { "solid": { "color": "#25D0F7" } },
					"transparency": 0
					},
					{
					"$id": "disabled",
					"image": { "name": "", "url": "", "scaling": "Normal" },
					"fillColor": { "solid": { "color": "#B3B3B3" } },
					"transparency": 0
					},
					{
					"show": true
				}],
				"shadow": [{
					"$id": "default",
					"color": { "solid": { "color": "#000000" } },
					"transparency": 0,
					"shadowBlur": 0,
					"shadowPositionPreset": "bottomRight",
					"angle": 45,
					"shadowDistance": 50
					},
					{
					"$id": "hover",
					"color": { "solid": { "color": "#000000" } },
					"transparency": 0,
					"shadowBlur": 0,
					"shadowPositionPreset": "bottomRight",
					"angle": 45,
					"shadowDistance": 50
					},
					{
					"$id": "selected",
					"color": { "solid": { "color": "#000000" } },
					"transparency": 0,
					"shadowBlur": 0,
					"shadowPositionPreset": "bottomRight",
					"angle": 45,
						"shadowDistance": 50
					},
					{
					"$id": "disabled",
					"color": { "solid": { "color": "#000000" } },
					"transparency": 0,
					"shadowBlur": 0,
					"shadowPositionPreset": "bottomRight",
					"angle": 45,
					"shadowDistance": 50
					},
					{
					"show": false
				}],
				"glow": [{
					"$id": "default",
					"color": { "solid": { "color": "#118DFF" } },
					"transparency": 0,
					"shadowBlur": 40
					},
					{
					"$id": "hover",
					"color": { "solid": { "color": "#118DFF" } },
					"transparency": 0,
					"shadowBlur": 40
					},
					{
					"$id": "selected",
					"color": { "solid": { "color": "#118DFF" } },
					"transparency": 0,
					"shadowBlur": 40
					},
					{
					"$id": "disabled",
					"color": { "solid": { "color": "#118DFF" } },
					"transparency": 0,
					"shadowBlur": 40
					},
					{
					"show": false
				}],
				"title": [{
					"show": false,
					"heading": "Normal",
					"titleWrap": true,
					"fontColor": { "solid": { "color": "#DBDBDB" } },
					"background": { "solid": { "color": "#1C1C1C" } },
					"alignment": "left",
					"fontSize": 14,
					"fontFamily": "Segoe UI",
					"bold": false,
					"italic": false,
					"underline": false
				}],
				"subTitle": [{
					"show": false,
					"heading": "Normal",
					"fontFamily": "Segoe UI",
					"fontSize": 10,
					"bold": false,
					"italic": false,
					"underline": false,
					"fontColor": { "solid": { "color": "#605e5c" } },
					"alignment": "left",
					"titleWrap": true
				}],
				"divider": [{
					"show": false,
					"color": { "solid": { "color": "#605E5C" } },
					"style": "solid",
					"width": 1,
					"ignorePadding": true
				}],
				"spacing": [{
					"customizeSpacing": false,
					"verticalSpacing": 5,
					"spaceBelowTitle": 5,
					"spaceBelowSubTitle": 5,
					"spaceBelowTitleArea": 5
				}],
				"lockAspect_": [{
					"show": false
				} ],
				"background": [{
					"show": false
				}],
				"border": [{
					"color": { "solid": { "color": "#46607E" } },
					"show": false,
					"radius": 5
				}],
				"dropShadow": [{
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
				"visualHeader": [{
					"show": false,
					"showVisualInformationButton": true,
					"showVisualWarningButton": true,
					"showVisualErrorButton": true,
					"showDrillRoleSelector": true,
					"showDrillUpButton": true,
					"showDrillToggleButton": true,
					"showDrillDownLevelButton": true,
					"showDrillDownExpandButton": true,
					"showPinButton": true,
					"showFocusModeButton": true,
					"showFilterRestatementButton": true,
					"showSeeDataLayoutToggleButton": true,
					"showOptionsMenu": true,
					"showTooltipButton": false,
					"showCommentButton": false,
					"showPersonalizeVisualButton": false,
					"showSmartNarrativeButton": false
				}],
				"visualTooltip": [{
					"show": false,
					"type": "Canvas",
					"fontSize": 12,
					"fontFamily": "Segoe UI",
					"bold": false,
					"italic": false,
					"underline": false,
					"transparency": 5,
					"page": "Auto"
				}]
			}
		}
    }
}
```

## Effect
![[Action Button.webp]]

## Settings
>[!attention] With the chart selected

![[Action Button Settings.webp]]

Back to [[Included Visuals]]

# Related
[[Shape]]
