---
aliases:
  - Property - Lock Aspect
author:
  - Sascha D. Kasper
description: Lock or unlock the aspect ratio for all Power BI visuals using the shared lockAspect property in theme JSON.
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

# Lock Aspect

The '"lockAspect"' property can be defined for all visuals. It includes settings for locking and unlocking a visuals aspect ratio.

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "lockAspect": [{
                    "show": false
                }]
            }
        }
    }
}
```

## Settings
![[Lock Aspect Settings.webp]]

Back to [[Visual Styles]]
