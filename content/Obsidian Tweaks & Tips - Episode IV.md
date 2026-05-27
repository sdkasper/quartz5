---
aliases:
author:
  - Sascha D. Kasper
source:
description: Four Obsidian tweaks covering bad YAML detection, stacked tab formatting, hoverable multi-level dropdowns, and bullet threading.
cover:
date: 2026-03-09
draft: false
categories:
  - obsidian
cssclasses:
tags:
  - obsidian
  - tweaks
created: 2026-03-09T00:00
updated: 2026-03-09T14:26:34+02:00
---

# In a Nutshell

> [!important|float-r] Useful / Download  
> - [Bad YAML finder](https://wiki.sascha-kasper.com/obsidian/tweaks/dvjs-find-bad-yaml/)  
> - [Stacked tabs CSS](https://wiki.sascha-kasper.com/obsidian/tweaks/css-formatting-stacked-tabs/)  
> - [Dropdown fields CSS](https://wiki.sascha-kasper.com/obsidian/tweaks/css-hoverable-dropdown-fields/)  
> - [Bullet threading CSS](https://wiki.sascha-kasper.com/obsidian/tweaks/css-bullet-threading/)  
> - [Hide properties CSS](https://wiki.sascha-kasper.com/obsidian/tweaks/css-hide-properties-on-specific-notes/)  
> * Series:  
> [[Obsidian Tweaks & Tips - Episode I|Ep. I]]  
> [[Obsidian Tweaks & Tips - Episode II|Ep. II]]  
> [[Obsidian Tweaks & Tips - Episode III|Ep. III]]  
> [[Obsidian Tweaks & Tips - Episode V|Ep. V]]

Welcome to episode four of the Obsidian Tweaks & Tips series. If you missed the earlier episodes, check out [[Obsidian Tweaks & Tips - Episode I|Episode I]], [[Obsidian Tweaks & Tips - Episode II|Episode II]], and [[Obsidian Tweaks & Tips - Episode III|Episode III]]. This time, we have four more community-sourced tweaks covering bad YAML detection, stacked tab formatting, hoverable dropdown fields, and bullet threading.

# Find Notes with Bad YAML

Occasionally, some of your files might have incorrectly formatted frontmatter. If you don't notice it immediately, it can be cumbersome to find those files later on.

This DataviewJS script makes it easier. I found it on the Obsidian forum, shared by user [holroy](https://forum.obsidian.md/u/holroy/summary).

While the details are complex, the script basically checks whether any frontmatter exists and -- if so -- whether any parts of it are faulty. If a problem is found, it categorizes it as `Not valid`, `NO yaml`, or `Empty`.

As a result, you get a table with the linked file name of notes with bad YAML code, the status, and the faulty code's start and end positions.

You can [copy the script from here](https://wiki.sascha-kasper.com/obsidian/tweaks/dvjs-find-bad-yaml/).

# Format Stacked Tabs

As you probably know, Obsidian lets you change how tabs of multiple open notes are displayed. By default, they are aligned horizontally. If you click on the little arrow and change the setting to "Stack Tabs", they get aligned vertically.

With the following CSS snippet, you can adjust the stacked tab appearance. I found this on the [Obsidian Forum](https://forum.obsidian.md/t/css-formatting-stacked-tabs/77787), posted by user [ariehen](https://forum.obsidian.md/u/ariehen/summary).

## Setup

Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. Click on the folder icon to open the local snippets folder. Create a new file -- for example, `format stacked tabs.css`. Make sure the file extension is `css`.

Open the file, copy the CSS code into it, save, go back to Obsidian, and refresh the list of snippets. Enable the `format stacked tabs` snippet, and that should do it. If it does not, you may have to restart Obsidian.

## Result

Once activated, the CSS definitions are applied right away. You can play around with the values to make your stacked tabs look exactly the way you want them to. Whenever you change the CSS file and save it, the changes are applied in Obsidian instantly.

You can [copy the snippet from here](https://wiki.sascha-kasper.com/obsidian/tweaks/css-formatting-stacked-tabs/).

# Hoverable Multi-Level Dropdowns

Did you know that you can create hoverable fields in any note -- and customize their appearance with a CSS file? I learned about this on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/1by3wau/enough_with_plugins_what_isare_your_favorite/) from user [OnionOk776](https://www.reddit.com/user/OnionOk776/).

These fields can have multiple levels, which makes them convenient for navigation. Each entry can link to a specific target.

## Setup

First, add another CSS snippet to your snippets folder -- the setup process is the same as described in the "Format Stacked Tabs" section above.

Inside the CSS file, you will find a block called "Gradient color selections" with 13 pre-defined gradients. Each has a name and a background color value.

Once the snippet is activated, create a new note. Inside it, add a simple callout and give it the name of one of the pre-defined gradients -- for example, `Blue_gradient_1`. Then define the structure using a simple bullet list. These are just links to existing notes, and by using proper indentation, you can quickly create any navigation tree you want.

If you don't like how it looks, pick a different gradient style or adjust attributes such as padding, font color, and field color directly in the CSS.

## Bonus: Hide Properties on Specific Notes

Here is a bonus tip from [[Obsidian Tweaks & Tips - Episode I|Episode I]]: if you want to hide the properties section on a specific note only, you can use [another CSS snippet](https://wiki.sascha-kasper.com/obsidian/tweaks/css-hide-properties-on-specific-notes/) and add the field `cssclasses` to the frontmatter with the value `hide-properties`. This gives the note a cleaner look.

You can [copy the dropdown snippet from here](https://wiki.sascha-kasper.com/obsidian/tweaks/css-hoverable-dropdown-fields/).

# Bullet Threading

If you are like me, you like making lists. Many of them might be very long and have multiple levels. With such long and deep lists, it can be a challenge to keep track of what belongs to which level. This CSS snippet helps by adding "bullet threading" -- visual lines that connect parent and child items.

I found this on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/1by3wau/comment/kyh7j9r/), posted by user [seashoreandhorizon](https://www.reddit.com/user/seashoreandhorizon/).

## Setup

Add the snippet and activate it -- the setup process is the same as described in the "Format Stacked Tabs" section above.

## Result

Once active, create a bullet list and when you hover your mouse over a list item, you get a highlight of the path from the top level to the current item. The appearance of this path can be adapted in the CSS file. Depending on the theme you use, you may have to adjust the offset values so the line does not overlap with the text.

You can [copy the snippet from here](https://wiki.sascha-kasper.com/obsidian/tweaks/css-bullet-threading/).

# More in This Series

- [[Obsidian Tweaks & Tips - Episode I|Episode I]] -- Templater callout script, auto-hide properties
- [[Obsidian Tweaks & Tips - Episode II|Episode II]] -- Active tab color, hotkey sync, hide specific properties
- [[Obsidian Tweaks & Tips - Episode III|Episode III]] -- Styled TOC, find missing/empty notes, Plugin Groups
- Episode IV -- Bad YAML finder, stacked tabs, dropdown fields, bullet threading
- [[Obsidian Tweaks & Tips - Episode V|Episode V]] -- Columns, floating callouts, table styles, tasks dashboard, help tooltip
