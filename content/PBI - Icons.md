---
aliases:
  - Icons
author:
  - Sascha D. Kasper
description: Add custom SVG icons to your Power BI theme JSON for use in conditional formatting across visuals.
cover:
date: 2023-09-11
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - general
created: 2023-09-11T11:45
updated: 2025-12-11T09:11
---

# Icons
Power BI comes with a set of pre-defined icons that can be used in various visuals. It also allows you to use your own icons. In this section, you can define those icons.

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "icons": [
        {
            "description": "Green Dash",
            "url": "data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 15 15'> <rect x='0.5' y='5.5' fill='%2384C28A' width='14' height='4'/> <path fill='%23449E44' d='M0,5v5h15V5H0z M14,9.001H1V6h13V9.001z'/> </svg>"
        },
        {
            "description": "Yellow Dash",
            "url": "data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 15 15'> <rect x='0.5' y='5.5' fill='%23F9D087' width='14' height='4'/> <path fill='%23F9B23E' d='M0,5v5h15V5H0z M14,9.001H1V6h13V9.001z'/> </svg>"
        },
        {
            "description": "Red Dash",
            "url": "data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 15 15'> <rect x='0.5' y='5.5' fill='%23F78272' width='14' height='4'/> <path fill='%23F25021' d='M0,5v5h15V5H0z M14,9.001H1V6h13V9.001z'/> </svg>"
        }
    ],
}
```

## Effect
Icons defined in this way, will be available for conditional formatting.
![[Icons.webp]]

![[Icons Conditional Formatting.webp]]

# Related



Icon definitions from: [Icons upon Icons - (powerbi.tips)](https://powerbi.tips/2019/07/icons-upon-icons/#:~:text=To%20add%20these%20additional%20icons%20follow%20these%20steps%3A,PowerBITips%20Icons%20v1.json%20file%20that%20you%20downloaded%20earlier.)
