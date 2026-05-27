---
aliases:
  - Image
author:
  - Sascha D. Kasper
description: Customize the image visual in your Power BI theme JSON with scaling, title, border, and shadow settings.
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

# Image
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
		"image": {
			"*": {
				"imageScaling": [{
					"imageScalingType": "Normal"
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
				"spacing_": [{
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
![[Image\.webp]]

## Settings
>[!attention] With the chart selected

![[Image Settings.webp]]

Back to [[Included Visuals]]
