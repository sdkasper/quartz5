---
aliases:
  - Key Drivers Visual
author:
  - Sascha D. Kasper
description: Theme the key influencers (key drivers) visual in Power BI with colors for canvas, fonts, and drill charts.
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

# Key Drivers Visual
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
		"keyDriversVisual": {
			"*": {
				"keyDrivers": [{
					"allowKeyDrivers": true,
					"allowProfiles": true,
					"selectedNumericAnalysis": "Continuous",
					"allowKeyDriversCounting": true,
					"countType": "absolute"
				}],
				"keyInfluencersVisual": [{
					"primaryColor": { "solid": { "color": "#25D0F7" } },
					"primaryFontColor": { "solid": { "color": "#1C1C1C" } },
					"secondaryColor": { "solid": { "color": "#B3B3B3" } },
					"secondaryFontColor": { "solid": { "color": "#FFFFFF" } },
					"canvasColor": { "solid": { "color": "#1B2631" } },
					"fontColor": { "solid": { "color": "#FFFFFF" } }
				}],
				"keyDriversDrillVisual": [{
					"defaultColor": { "solid": { "color": "#25D0F7" } },
					"referenceLineColor": { "solid": { "color": "#007BFF" } }
				}],
				"general_": [{
					"responsive": true,
					"keepLayerOrder": true,
					"outlineColor": {	"solid": { "color": "#1B2631" } },
					"outlineWeight": 2,
					"orientation": 0
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
![[Key Drivers Visual.webp]]

## Settings
>[!attention] With the chart selected

![[Key Drivers Visual Settings.webp]]

Back to [[Included Visuals]]

# Related
[[Decomposition Tree]]
[[Q&A Visual]]
