---
aliases:
  - Outspace Pane
author:
  - Sascha D. Kasper
description: Control the outspace pane color and transparency around your Power BI report pages via theme JSON.
cover:
date: 2023-09-16
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - general
created: 2023-09-16T19:09
updated: 2025-12-11T09:11
---

# Outspace Pane
The '"outspacePane"' property under [[Page]] can be defined for all or individual pages. It includes settings for 
- outspace color and transparency

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "page": {
                "*": {
                    "outspace": [{
                        "color": { "solid": { "color": "#1B2631" } },
                        "transparency": 0
                    }]
                }
            }
        }
    }
}
```

## Effect
>[!attention] Make sure to have no visual selected.

![[Outspace Pane.webp]]

## Settings
![[Outspace Pane Settings.webp]]

# Related


