---
aliases:
  - File Structure
author:
  - Sascha D. Kasper
description: "Understand the four major sections of a Power BI theme JSON file: theme colors, structural colors, text classes, and visual styles."
cover:
date: 2023-09-08
draft: false
categories:
  - powerbi
cssclasses:
tags:
  - powerbi
  - structure
created: 2023-09-08T14:48
updated: 2025-10-03T08:30
---

# File Structure

The JSON file comprises four major sections:

1. [[Theme colors]]
2. [[Structural Colors]]
3. [[Text Classes]]
4. [[Visual Styles]]

The Power BI Theme JSON file has a specific structure that must be followed. It consists of a root object with several key-value pairs. Here's a simplified example:

```JSON
{
   "name": "MyCustomTheme",
   "dataColors": ["#0078d4", "#01b8aa", "#374649"],
   "visualStyles": {
      "visualStylesDefault": {
         "visualBackgroundImage": null,
         "visualGridlinesColor": "#eaeaea"
      }
   }
}
```

- `"name"`: This key specifies the name of the theme.
- `"dataColors"`: An array containing color codes that define the color palette for visuals.
- `"visualStyles"`: This section contains sub-properties related to the visual styles applied.

# Related


