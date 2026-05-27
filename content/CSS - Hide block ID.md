---
aliases:
  - obsidian/tweaks/css-hide-block-id
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Hide-block-ID
description: Hide distracting block IDs in Obsidian and only show them when you click on that line.
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
updated: 2025-10-16T06:07
---

# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `hide block id.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable this one, and that should do it. If it does not, you may have to restart Obsidian.
# Result
This snippet will hide block IDs that are usually visible in preview mode, decluttering your notes. For example, when using buttons, it goes from this:

![[CSS - Hide block ID before.webp|Button element with a visible block ID reference below it]]

to this:

![[CSS - Hide block ID after.webp|Same button element with the block ID hidden by the CSS snippet]]

# Code
```css
/* Hide block IDs on inactive lines */
.cm-blockid {
    opacity: 0;
}
/* Show block IDs on active lines */
.cm-active .cm-blockid {
    opacity: 1;
}
```

# Source
I found this on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/xd0sir/hidden_block_id_snippet/), posted by user [hey_look_its_shiny](https://www.reddit.com/user/hey_look_its_shiny/).
