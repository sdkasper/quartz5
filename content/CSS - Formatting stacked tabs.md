---
aliases:
  - obsidian/tweaks/css-formatting-stacked-tabs
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Formatting-stacked-tabs
description: Style the background color, text orientation, and font of stacked tabs in Obsidian with this CSS snippet.
cover:
date: 2024-04-14
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2024-04-14T09:48
updated: 2025-10-03T08:30
---

# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `active tab color.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable the `active tab color` one, and that should do it. If it does not, you may have to restart Obsidian.
# Result
Using this snippet, you can easily change your active tab's appearance in terms of background color, outline color, font type, size, and font color.
# Code
```css
/* stacked tabs background color */
.workspace .mod-root .mod-stacked .workspace-tab-header-inner {
    background-color: rgb(224,224,224);
}

/* stacked tabs background color on hover */
.workspace .mod-root .workspace-tabs.mod-stacked .workspace-tab-container .workspace-tab-header {
     background-color: rgb(232,232,232);
}

/* stacked tabs - text orientation, font-weight, color */
.workspace .mod-root .workspace-tabs.mod-stacked .workspace-tab-container .workspace-tab-header-inner-title {
    text-orientation: upright;
    font-weight: 600;
    color: red;
}
```

# Source
I found this on the Obsidian forum, posted by user [ariehen](https://forum.obsidian.md/u/ariehen/summary) on the [Obsidian Forum](https://forum.obsidian.md/t/css-formatting-stacked-tabs/77787).
