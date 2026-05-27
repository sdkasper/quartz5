---
aliases:
  - obsidian-course/css-show-properties-on-hover
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Show-properties-on-hover
description: Auto-collapse Obsidian's properties section and expand it on hover, keeping your notes clean until you need metadata.
cover:
date: 2023-10-20
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2023-10-17T16:51
updated: 2025-09-11T11:43
---


# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `hide-properties.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable the `hide-properties` one, and that should do it. If it does not, you may have to restart Obsidian.

# Result
Using this snippet, the `properties` will automatically be collapsed/hidden. When we hover, they expand, and – if we don't click into one of them – they will automatically collapse when we move the mouse away. If we edit a property, they stay open, of course.

# Code
```css
@media screen and (min-width: 1024px) {
    .workspace-split.mod-vertical.mod-root .view-content {
        .metadata-container {
            max-height: 2.7rem;
            opacity: 0.6;
            overflow: hidden;
            transition: max-height 250ms ease-in-out, opacity 250ms;
            margin-bottom: 0;
        }
        .metadata-container:hover,
        .metadata-container:focus-within {
            max-height: 1000px;
            opacity: 1;
            transition: max-height 300ms ease-in-out,
            opacity 300ms;
            transition-delay: 0.5s;
        }
    }
}
```

# Source
I found this on Reddit, posted by user [CharmingThunderstorm](https://www.reddit.com/r/ObsidianMD/comments/167hylo/how_to_partially_hide_properties).
Based on the original, a friendly YouTube viewer ([Ruben Khachaturov](https://www.youtube.com/@RubenKhachaturov-v9c))sent me the updated version below. The difference is that the updated one only applies to the main window and leaves the properties in the side pane visible instead of hiding them, too. This makes it even better.
