---
aliases:
  - obsidian/tweaks/css-syntax-highlighting
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Syntax-Highlighting
description: Customize the syntax highlighting colors in Obsidian code blocks with this CSS snippet using simple variables.
cover:
date: 2024-08-13
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2024-04-14T12:53
updated: 2024-10-16T22:39
---

# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `syntax highlighting.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable this one, and that should do it. If it does not, you may have to restart Obsidian.
# Result
This snippet lets you customize the colors of elements in your code blocks.
# Code
```css
body {
	--code-white-space: pre-wrap;	 /* type: variable-select, default: pre-wrap, options: normal, nowrap, pre, pre-wrap, pre-line, break-spaces, collapse balance, preserve nowrap) */
	--code-radius: 4px;			     /* type: variable-number, default: 4, format: px */
	--code-size: 0.875em;			 /* type: variable-number, default: 0.875, format: em*/
	--code-background: #000000;	/* type: variable-themed-color, format: hex, opacity: true, default: '#000000' */
	--code-normal: #dbdbdb;		/* type: variable-themed-color, format: hex, opacity: true, default: '#dbdbdb' */
	--code-comment: #4c7aac;		/* type: variable-themed-color, format: hex, opacity: true, default: '#4c7aac' */
	--code-function: #ffed68;		/* type: variable-themed-color, format: hex, opacity: true, default: '#ffed68' */
	--code-important: #e9973f;		/* type: variable-themed-color, format: hex, opacity: true, default: '#e9973f' */
	--code-keyword: #18bc9c;		/* type: variable-themed-color, format: hex, opacity: true, default: '#18bc9c' */
	--code-operator: #fc3634;		/* type: variable-themed-color, format: hex, opacity: true, default: '#fc3634' */
	--code-property: #25d0f7;		/* type: variable-themed-color, format: hex, opacity: true, default: '#25d0f7' */
	--code-punctuation: #3498db;	/* type: variable-themed-color, format: hex, opacity: true, default: '#3498db' */
	--code-string: #44cf6e;		/* type: variable-themed-color, format: hex, opacity: true, default: '#44cf6e' */
	--code-tag: #fc3634;			/* type: variable-themed-color, format: hex, opacity: true, default: '#fc3634' */
	--code-value: #a991d4;			/* type: variable-themed-color, format: hex, opacity: true, default: '#a991d4' */
}
```

# Source
I found this on [Reddit]([Guide: adding icons to notes based on tag : r/ObsidianMD (reddit.com)](https://www.reddit.com/r/ObsidianMD/comments/1el35n9/guide_adding_icons_to_notes_based_on_tag/)), posted by user [pillowpotion](https://www.reddit.com/user/pillowpotion/).
