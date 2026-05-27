---
aliases:
  - Slicer
author:
  - Sascha D. Kasper
description: Customize the slicer visual in your Power BI theme JSON with selection controls, fonts, and header settings.
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

# Slicer
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
        "slicer": {
            "*": {
                "general_": [{
                    "responsive": false,
                    "outlineColor": { "solid": { "color": "#000000" } },
                    "outlineWeight": 2,
                    "orientation": 0,
					"background": { "solid": { "color": "#003E80" } }
                }],                
                "selection": [{
                    "singleSelect": false,
                    "selectAllCheckboxEnabled": true
                }],
                "data": [{
                    "mode": "Basic"
                }],	
                "header": [{
                    "show": false,
                    "fontColor": { "solid": { "color": "#DBDBDB" } },
                    "background": { "solid": { "color": "#1C1C1C" } },
                    "outline": "None",
                    "textSize": 10,
                    "fontFamily": "Segoe UI"
                }],
                "title": [{
					"show": true
                }],
				"items": [{
					"fontColor": { "solid": { "color": "#FFFFFF" } },
					"background": { "solid": { "color": "#1B2631" } },
					"outline": "None",
					"textSize": 10,
					"fontFamily": "Segoe UI"
                }],
                "slider": [{ "color": { "solid": { "color": "#25D0F7" } } } ],
				"visualHeader": [{ "show": false }]
            }
        }
    }
}
```

## Effect
![[Slicer.webp]]

## Settings
>[!attention] With the chart selected

![[Slicer Settings.webp]]

Back to [[Included Visuals]]
