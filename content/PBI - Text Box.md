---
aliases:
  - Text Box
author:
  - Sascha D. Kasper
description: Customize the text box visual in your Power BI theme JSON with font, background, border, and shadow settings.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visuals
created: 2023-09-11T16:30
updated: 2025-12-11T09:11
---

# Text Box
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
		"textbox": {
			"*": {
				"*": [{
					"fontSize": 10,
					"fontFamily": "Segoe UI",
					"wordWrap": true,
					"color": { "solid": { "color": "#FFFFFF" } }
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
				"divider": [{
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
				"background": [{
					"show": true,
					"color": { "solid": { "color": "#1B2631" } },
					"transparency": 0
				}],
				"border": [{
					"color": { "solid": { "color": "#46607E" } },
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
![[Text Box.webp]]

## Settings
>[!attention] With the chart selected

![[Text Box Settings.webp]]

Back to [[Included Visuals]]
