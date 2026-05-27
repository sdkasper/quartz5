---
aliases:
  - Property - Data Point
author:
  - Sascha D. Kasper
description: Configure default data point fill colors and visibility for all Power BI visuals using the shared dataPoint property.
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
updated: 2025-10-03T08:30
---

# Data Point
The `"datapoint"` property controls the styling and configurations of individual data points within visualizations. These data points refer to points on a scatter plot, bars, columns, or slices in a pie chart, or data cells in a table.

The '"datapoint"' property can be defined for all visuals. It includes settings for
- showing all datapoints
- default fill color

## Syntax
```JSON
{
    "name": "LeanProductivity",
    "visualStyles": {
        "*": {
            "*": {
                "dataPoint": [{
                    "showAllDataPoints": false,
                    "fill": { "solid": { "color": "#25D0F7" } }
                }]
            }
        }
    }
}
```

Back to [[Visual Styles]]
