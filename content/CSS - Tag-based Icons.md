---
aliases:
author:
  - Sascha D. Kasper
source:
description: Automatically display custom icons next to note links in Obsidian based on their tags using CSS and SVGs.
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
updated: 2025-10-09T08:46
---

# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `tag based icons.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable this one, and that should do it. If it does not, you may have to restart Obsidian.

# Code
```css
/* General styles for all elements. Edit width/height to your liking. */
.data-link-icon::before {
    content: '';
    display: inline-block;
    width: 28px;
    height: 18px;
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center;
    vertical-align: middle;
    margin: 0 auto;
}

/* Specific styles for each tag (duplicate as needed) */
.data-link-icon[data-link-tags*="mytag1" i]::before {
    background-image: url("data:image/svg+xml;base64,base64gibberish1");
}

.data-link-icon[data-link-tags*="mytag2" i]::before {
    background-image: url("data:image/svg+xml;base64,base64gibberish2");
}

/* etc. */

/* Makes icons white when dark mode is active: */
.theme-dark .data-link-icon::before {
    filter: invert(1);
}
```

# Source
I found this on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/1el35n9/guide_adding_icons_to_notes_based_on_tag/), posted by user [pillowpotion](https://www.reddit.com/user/pillowpotion/).
