---
aliases:
  - Filter Card
author:
  - Sascha D. Kasper
description: Style the filter card's applied and available states with background, foreground, and border settings in theme JSON.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - general
created: 2023-09-11T16:32
updated: 2025-12-11T09:11
---

# Filter Card
The '"filterCard"' property can be defined for the whole report. Filter cards can have two states:
- `"Applied"`
- `"Available"`
defined by the `"$id"` attribute.

For each state, you can define the filter card's
- transparency
- background color
- foreground color
- text size
- border visibility
- border color
- input field color

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "filterCard": [{
                    "$id": "Applied",
                    "transparency": 0,
                    "backgroundColor": { "solid": { "color": "#18BC9C" } },
                    "foregroundColor": { "solid": { "color": "#000000" } },
                    "textSize": 10,
                    "border": true,
                    "borderColor": { "solid": { "color": "#000000" } },
                    "inputBoxColor": { "solid": { "color": "#FFFFFF" } }
                    },
                    {
                    "$id": "Available",
                    "transparency": 0,
                    "backgroundColor": { "solid": { "color": "#FFFFFF" } },
                    "foregroundColor": { "solid": { "color": "#000000" } },
                    "textSize": 10,
                    "border": true,
                    "borderColor": { "solid": { "color": "#000000" } },
                    "inputBoxColor": { "solid": { "color": "#FFFFFF" } }
                }]
            }
        }
    }
}
```

## Effect
![[Filter Cards.webp]]

## Settings
>[!attention] Make sure to have no visual selected.

![[Filter Cards Settings.webp]]

# Related


