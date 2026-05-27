---
aliases:
  - obsidian-course/tweaks/css-hide-properties-on-specific-notes
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Hide-Properties-on-Specific-Notes
description: Hide the entire properties section on specific Obsidian notes in reading view using a cssclass toggle.
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
created: 2024-02-02T10:23
updated: 2025-10-03T08:30
---


# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `active tab color.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable the `hide-properties` one, and that should do it. If it does not, you may have to restart Obsidian.

Then, add the property `cssclasses` to your frontmatter and add the value "hide-properties", like so:

```css
cssclasses: hide-properties
```
# Result
When called in the `cssclasses` property, this snippet will hide the note's properties in reading view.
# Code
```css
.hide-properties{
    --metadata-display-reading: none;
}
```
