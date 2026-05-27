---
aliases:
  - obsidian/tweaks/theme-baseline-customization
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/THEME---Baseline-Customization
description: Get the exact Baseline theme look from my videos with this ready-to-import Style Settings CSS snippet.
cover:
date: 2025-10-09
draft: false
categories:
  - obsidian
  - theme
cssclasses:
tags:
  - obsidian
  - css
created: 2025-10-17T12:53
updated: 2025-10-17T17:44
---


I am using the "Baseline" theme with some customizations. If you want the same look & feel, follow these instructions
# Setup
1. Go to `Settings`, `Appearance`, `Themes` and click on `Manage`. Search for "Baseline", install, and enable the theme.
2. Do the same for the "Style Settings" plugin.
3. Copy the CSS code below.
4. Go to `Settings`, `Style Settigs` and click on `Import`.
# Result
This will apply the colors and styles that you see in  my videos to your vault.


> [!info] About the font
> I am using the font "JetBrains Mono". This is not controlled via the theme, but defined under `Settings`, `Appearance`, `Font`. If you want to use this font, you need to install it first.
> You can [download it here](https://www.jetbrains.com/lp/mono/).
# Code
```css
{
  "baseline-style@@accented-interface": true,
  "baseline-style@@color-scheme-dark": "default-dark",
  "baseline-style@@background-contrast-dark": "contrast-dark",
  "baseline-style@@background-primary@@dark": "#1B2631",
  "baseline-style@@background-primary-alt@@dark": "#000000",
  "baseline-style@@background-secondary@@dark": "#181B21",
  "baseline-style@@interactive-normal@@dark": "#007BFF",
  "baseline-style@@background-modifier-border-hover@@dark": "#FFED68",
  "baseline-style@@background-modifier-border-focus@@dark": "#FC3634",
  "baseline-style@@color-red@@dark": "#FC3634",
  "baseline-style@@color-orange@@dark": "#FFD700",
  "baseline-style@@color-yellow@@dark": "#FFED68",
  "baseline-style@@color-green@@dark": "#18BC9C",
  "baseline-style@@color-cyan@@dark": "#25D0F7",
  "baseline-style@@color-blue@@dark": "#007BFF",
  "baseline-style@@color-purple@@dark": "#A991D4",
  "baseline-style@@color-pink@@dark": "#D34AF4",
  "baseline-style@@icon-color@@dark": "#25D0F7",
  "baseline-style@@icon-color-hover@@dark": "#FC3634",
  "baseline-style@@icon-color-active@@dark": "#FFED68",
  "baseline-style@@icon-color-focused@@dark": "#FC3634",
  "baseline-style@@text-normal@@dark": "#FFFFFF",
  "baseline-style@@text-faint@@dark": "#929699",
  "baseline-style@@italic-color@@dark": "#18BC9C",
  "baseline-style@@bold-color@@dark": "#007BFF",
  "baseline-style@@code-comment@@dark": "#4C7AAC",
  "baseline-style@@code-function@@dark": "#FFED68",
  "baseline-style@@code-keyword@@dark": "#18BC9C",
  "baseline-style@@code-important@@dark": "#E9973F",
  "baseline-style@@code-operator@@dark": "#FC3634",
  "baseline-style@@code-property@@dark": "#25D0F7",
  "baseline-style@@code-punctuation@@dark": "#3498DB",
  "baseline-style@@code-string@@dark": "#44CF6E",
  "baseline-style@@code-tag@@dark": "#FC3634",
  "baseline-style@@code-value@@dark": "#A991D4",
  "baseline-style@@layout-style": "layout-cards",
  "baseline-style@@input-style": "input-obsidian",
  "baseline-style@@status-bar-style": "status-bar-default",
  "baseline-style@@anim-motion-baseline": "cubic-bezier(0.32, 0.72, 0, 1)",
  "baseline-style@@tabs-style": "tabs-default",
  "baseline-style@@labeled-tabs": "labeled-tabs-off",
  "baseline-style@@stacked-nav-off": true,
  "baseline-style@@compact-actions-off": true,
  "baseline-style@@compact-tabs-off": true,
  "baseline-style@@nav-item-active-style": "nav-item-strong",
  "baseline-style@@colorful-folders": "colorful-folders-off",
  "baseline-style@@hide-vault-switcher-off": true,
  "baseline-style@@file-header-visibility": "view-header-title-always",
  "baseline-style@@file-header-font-size": "0.7em",
  "baseline-style@@active-line-style": "active-line-side",
  "baseline-style@@inline-title-font": "JetBrains Mono",
  "baseline-style@@inline-title-size": "1.8em",
  "baseline-style@@inline-title-weight": 400,
  "baseline-style@@colorful-headings": "colorful-headings-off",
  "baseline-style@@h1-color@@dark": "#25D0F7",
  "baseline-style@@h1-font": "JetBrains Mono",
  "baseline-style@@h1-size": "1.8em",
  "baseline-style@@h1-weight": 500,
  "baseline-style@@h1-variant": "small-caps",
  "baseline-style@@h2-color@@dark": "#FC3634",
  "baseline-style@@h2-font": "JetBrains Mono",
  "baseline-style@@h2-size": "1.5em",
  "baseline-style@@h2-weight": 400,
  "baseline-style@@h3-color@@dark": "#FFED68",
  "baseline-style@@h3-font": "JetBrains Mono",
  "baseline-style@@h3-size": "1.4em",
  "baseline-style@@h3-weight": 400,
  "baseline-style@@h4-color@@dark": "#18BC9C",
  "baseline-style@@h4-font": "JetBrains Mono",
  "baseline-style@@h4-size": "1.3em",
  "baseline-style@@h4-weight": 400,
  "baseline-style@@h5-color@@dark": "#007BFF",
  "baseline-style@@h5-font": "JetBrains Mono",
  "baseline-style@@h5-size": "1.2em",
  "baseline-style@@h5-weight": 400,
  "baseline-style@@h6-color@@dark": "#A991D4",
  "baseline-style@@h6-font": "JetBrains Mono",
  "baseline-style@@h6-size": "1.1em",
  "baseline-style@@h6-weight": 400,
  "baseline-style@@metadata-style": "metadata-default",
  "baseline-style@@blockquote-border-thickness": 3,
  "baseline-style@@blockquote-font-style": "italic",
  "baseline-style@@blockquote-background-color@@dark": "#000000",
  "baseline-style@@callouts-style": "callouts-outlined",
  "baseline-style@@code-size": "1em",
  "baseline-style@@code-line-numbers": true,
  "baseline-style@@link-external-decoration": "underline",
  "baseline-style@@img-grid": true,
  "baseline-style@@media-radius": 5,
  "baseline-style@@tag-radius": "8px"
}
```
