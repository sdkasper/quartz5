---
aliases:
  - obsidian-course/css-change-active-tab-color
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Change-active-tab-color
description: Change the background color, outline, font size, and weight of your active tab in Obsidian.
cover:
date: 2023-11-07
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2023-11-07T10:54
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
 body {
	--tab-background-active: #f3dbdb;
    --tab-outline-color: #935a5a;
    --tab-font-size: 0.85em;
}

.workspace-tab-header.is-active {
	font-weight: 500;
}
```

# Source
I found this on Reddit, posted by user [Tanto_Monta](https://www.reddit.com/r/ObsidianMD/comments/17nku2v/active_tab_color_snippet/).
