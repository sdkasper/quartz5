---
aliases:
  - obsidian-course/ask-for-note-title-templater-script
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Templater-Script---Ask-for-Note-Title
description: Auto-prompt for a note title when creating new notes from a Templater template in Obsidian.
cover:
date: 2023-10-20
draft: false
categories:
  - obsidian
  - templater
cssclasses:
tags:
  - obsidian
  - templater
created: 2023-10-26T21:24
updated: 2025-09-11T11:43
---

# Setup
For this to work, we need to create a new template in our designated templates folder. For example, `Template - Dummy`. Then we need to copy/paste the templater code into it.
# Result
If you have a hotkey for creating a new note from a template (in my case, that's `ALT + N`), then Obsidian will ask for the template. Choose the `Template - Dummy` and you will be prompted for a title before the note is created.

Alternatively, you can create a new note and then insert the `Template - Dummy` template. If you do that, you will have to run the templater script manually – for me, this is the hotkey `ALT + R`. The end result is the same.
# Code
```text
	---
	aliases:
	tags:
	---
	
	# Templater Script - Callouts
	
	<% tp.file.cursor(1) %>
```

# Source
I found this on Reddit but cannot find the OP anymore – if it's you, or you know who it is, kindly let me know, and I will happily give credit where credit is due.
