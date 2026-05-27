---
aliases:
author:
  - Sascha D. Kasper
source:
description: Apply custom background colors to specific Obsidian notes using cssclasses like blue, red, green, or yellow.
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
created: 2024-04-14T12:53
updated: 2024-10-16T22:42
---

# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `note background.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable this one, and that should do it. If it does not, you may have to restart Obsidian.
# Result


# Code
```css
.blue {
    background-color: #25D0F7;
}

.red {
    background-color: #FC3634;
}

.green {
    background-color: #18BC9C;
}

.yellow {
    background-color: #FFED68;
    color: #000;
}
```

# Source
