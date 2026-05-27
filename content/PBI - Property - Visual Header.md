---
aliases:
  - Property - Visual Header
author:
  - Sascha D. Kasper
description: Configure the visual header bar for all Power BI visuals -- toggle buttons, set colors, and control visibility.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visual-styles
created: 2023-09-11T16:32
updated: 2025-12-11T09:11
---

# Visual Header
The '"visualHeader"' property can be defined for all visuals. It includes settings for
- visibility
- background color
- foreground color
- border color
- transparency
- to show or hide various buttons

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "visualHeader": [{
                    "show": true,
                    "background": { "solid": { "color": "#1C1C1C" } },
                    "foreground": {  "solid": { "color": "#25D0F7" } },
                    "border": { "solid": { "color": "#1C1C1C" } },
                    "transparency": 0,
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
![[Visual Header.webp]]

## Settings
![[Visual Header Settings.webp]]

Back to [[Visual Styles]]
