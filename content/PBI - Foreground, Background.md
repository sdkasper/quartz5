---
aliases:
  - Foreground, Background
author:
  - Sascha D. Kasper
description: Set foreground, background, and their secondary/tertiary variants to create visual hierarchy in Power BI themes.
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

# Foreground, Background

## Foreground
The `"foreground"` property is used to define the primary text and foreground color for visuals and elements within your reports and dashboards.

This helps create a visually cohesive and user-friendly experience for both technical and non-technical users when interacting with your Power BI reports and dashboards.

## ForegroundNeutralSecondary
While the `"foreground"` color is generally applied to primary text and prominent elements, `"ForegroundNeutralSecondary"` allows you to define a distinct color for secondary text, labels, or other less emphasized foreground elements.

This property helps create a hierarchy of visual importance within your Power BI visuals, ensuring that primary content stands out while secondary information maintains a consistent and visually pleasing appearance.

## ForegroundNeutralTertiary
While the `"ForegroundNeutralSecondary"` property addresses secondary elements, `"ForegroundNeutralTertiary"` is used for even less emphasized components like fine print, annotations, or less important details.

By defining a distinct color for` "ForegroundNeutralTertiary"`, you can establish a consistent and visually pleasing appearance for these tertiary elements, ensuring that they remain readable and harmonious with the overall design.

## Background
The `"Background"` property plays a fundamental role by establishing a consistent and visually coherent backdrop against which your data and content are presented. By specifying the `"Background"` color, you can ensure that all visual elements within your Power BI assets share a unified and aesthetically pleasing background, contributing to a harmonious and professional design.

This property is particularly essential for maintaining a cohesive visual theme and ensuring that your reports and dashboards are visually engaging.

## BackgroundNeutral
While the `"Background"` color sets the primary backdrop, `"BackgroundNeutral"` allows you to define a distinct background color for less emphasized sections or elements, such as sidebars, footers, or secondary panels. 

## BackgroundLight
The `"BackgroundLight"` property is employed to specify a lighter shade of background color, typically used for specific visual elements or areas where a subtle contrast is desired.

`"BackgroundLight"` is often applied to elements like tooltips, minor borders, or highlights to draw attention to specific content or interactions while maintaining overall visual consistency.

## Syntax
```JSON
{
	"name": "LeanProductivity",
    "foreground": "#FFFFFF",
    "foregroundNeutralSecondary": "#B3B3B3",
    "foregroundNeutralTertiary": "#B3B3B3",
    "background": "#1B2631",
    "backgroundNeutral": "#808080",
    "backgroundLight": "#25D0F7",	
}
```

## Settings
![[Foreground, Background Settings.webp]]

# Related



[Structural Colors in Power BI Desktop | Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#set-structural-colors)
