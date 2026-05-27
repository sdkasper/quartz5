---
aliases:
  - Property - Spacing
author:
  - Sascha D. Kasper
description: Control vertical spacing between title, subtitle, and content area for all Power BI visuals in theme JSON.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - visual-styles
created: 2023-09-11T16:33
updated: 2025-12-11T09:11
---

# Spacing
The '"spacing"' property can be defined for all visuals. It includes settings for 
- individual spacing (vs same spacing for all properties)
- vertical spacing
- space below the visual's title
- space below the visual's subtitle
- space below the title area

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "spacing": [{
                    "customizeSpacing": false,
                    "verticalSpacing": 5,
                    "spaceBelowTitle": 5,
                    "spaceBelowSubTitle": 5,
                    "spaceBelowTitleArea": 5
                }]
            }
        }
    }
}
```

## Effect
![[Spacing.webp]]

## Settings
![[Spacing Settings.webp]]

Back to [[Visual Styles]]
