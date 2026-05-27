---
aliases:
author:
  - Sascha D. Kasper
source:
description: Eight Obsidian tweaks covering columns layout, floating callouts, table styles, a tasks dashboard, longest notes finder, help tooltips, and Web Clipper templates.
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
updated: 2026-03-09T14:26:30+02:00
---

# In a Nutshell

> [!important|float-r] Useful / Download  
> - [Columns CSS](https://wiki.sascha-kasper.com/obsidian/tweaks/css-columns-layout/)  
> - [Floating callouts CSS](https://wiki.sascha-kasper.com/obsidian/tweaks/css-embedded-callout/)  
> - [Table styles CSS](https://wiki.sascha-kasper.com/obsidian/tweaks/css-table-styles/)  
> - [Tasks dashboard](https://wiki.sascha-kasper.com/obsidian/tweaks/tasks-dashboard/)  
> - [Longest notes query](https://wiki.sascha-kasper.com/obsidian/tweaks/dvjs-find-longest-notes-in-vault/)  
> - [Web Clipper templates](https://kspr.me/cliptpl)  
> * Series:  
> [[Obsidian Tweaks & Tips - Episode I|Ep. I]]  
> [[Obsidian Tweaks & Tips - Episode II|Ep. II]]  
> [[Obsidian Tweaks & Tips - Episode III|Ep. III]]  
> [[Obsidian Tweaks & Tips - Episode IV|Ep. IV]]  

This is the fifth installment of the Obsidian Tweaks & Tips series -- and it is a packed one. If you are just joining, check out [[Obsidian Tweaks & Tips - Episode IV|Episode IV]] and the earlier episodes linked above. This time, we cover columns layout, floating callouts, table styles, a tasks dashboard, finding your longest notes, a help tooltip, and Web Clipper templates.

# Columns Layout

Like so many other visual things, the columns layout can be achieved with a CSS snippet. This one comes from user "Kapirklaa" on the Obsidian Discord Server.

If you don't know how to add CSS snippets to Obsidian, check the [step-by-step guide](https://help.obsidian.md/Extending+Obsidian/CSS+snippets).

## Setup

Go to `Settings`, `Appearance`, scroll down to `CSS Snippets` and click the folder icon to open the snippets folder. Create a new file called `columns.css`, copy the CSS code into it, save, go back to Obsidian, click refresh, and enable the snippet.

The CSS defines two classes: `columns2` and `columns3`. To use them, add the `cssclasses` property to a note's frontmatter with the value `columns2` or `columns3`.

## Result

The column layout is only applied in reading view. While editing in source or preview mode, you still see everything in a single column. Switch to reading view with `Ctrl+E` and the layout changes accordingly.

You can [copy the snippet from here](https://wiki.sascha-kasper.com/obsidian/tweaks/css-columns-layout/).

# Floating Callouts

Next up: how to embed callouts and let your text float around them. By default, callouts sit in their own lines across the whole width of the note. If your callouts don't contain a lot of text, this wastes space.

## Setup

Add a CSS file to your snippets folder and enable it. The CSS defines two classes: `float-r` and `float-l` for aligning callouts to the right or left respectively. Each has values for size, position, color, and border.

Unlike the columns layout, you don't apply these classes to the whole note. Instead, add them to individual callouts by appending `|float-r` or `|float-l` to the callout type. For example: `> [!important|float-r]`.

## Result

In reading view, the callout floats to the specified side and text wraps around it. If you make the callouts foldable, you can even minimize them and the text adapts nicely. You can see this pattern in action throughout the posts on this blog.

You can [copy the snippet from here](https://wiki.sascha-kasper.com/obsidian/tweaks/css-embedded-callout/).

# Table Styles

Do you use a lot of tables in Obsidian and feel they could look better? User [DeaconLight](https://forum.obsidian.md/) shared some helpful table styles on the Obsidian forum.

## Setup

After adding and enabling the CSS snippet, you can pick one of several pre-defined layouts per note. Any layout you pick applies to all tables on that note.

The first part of the CSS defines "custom hacks" for table width, text alignment, cell sizes, and more. After that, you find the classes for six pre-defined table styles:

- `purpleRed`
- `flatBlue`
- `academia`
- `whiteRed`
- `whiteRed-rounded`
- `yellowCab`

Add the desired class to the note's `cssclasses` property to apply the style. You can combine these with the custom hack classes.

You can [copy the snippet from here](https://wiki.sascha-kasper.com/obsidian/tweaks/css-table-styles/).

# Tasks Dashboard

This tweak combines CSS and task queries. I found it on the Obsidian forum, posted by user "SenRVA". To make it work, you need the [MCL Multi Column CSS](https://github.com/efemkay/obsidian-modular-css-layout/blob/main/MCL%20Multi%20Column.css) and the [Tasks](obsidian://show-plugin?id=obsidian-tasks-plugin) community plugin.

## Setup

The dashboard uses four task queries wrapped in callouts inside a multi-column callout:

- **Overdue** -- tasks that are "not done" and were due "before today"
- **Due Today** -- tasks due today, sorted by priority
- **Due This Week** -- tasks due "after today" and "this week", sorted by due date and priority
- **Upcoming** -- tasks due "after this week", sorted by due date

Each query uses the Tasks plugin's query syntax and includes `hide edit button`, `hide backlink`, and `short mode` for a compact view. Wrap each query block in a callout (e.g., `[!important]` for overdue, `[!note]` for the rest), then wrap all four callouts inside a `[!multi-column]` callout.

## Result

In reading view, you get a compact four-column dashboard showing your tasks grouped by urgency. You can adapt the queries, callout types, and layout to your needs.

You can [copy the full dashboard code from here](https://wiki.sascha-kasper.com/obsidian/tweaks/tasks-dashboard/).

# Find the Longest Notes

This tweak comes from the Obsidian forum, posted by user "Feralflora". It uses DataviewJS and the [Better Word Count](obsidian://show-plugin?id=better-word-count) plugin.

The script fetches all markdown pages in your vault, gets the word count for each via the Better Word Count API, sorts them in descending order, and displays the top 10 in a table with the note name, word count, and last modified date.

You can [copy the script from here](https://wiki.sascha-kasper.com/obsidian/tweaks/dvjs-find-longest-notes-in-vault/).

# Help Tooltip

This tweak comes from Reddit, posted by user "Content_Trouble". It is a CSS snippet that creates a pop-up when you hover over the "help" (question mark) icon in the bottom of Obsidian's left-hand panel.

You can use it to display anything you like -- I use it to remind myself of the different callout types, their names, symbols, and colors, as well as different task types in my vault.

## Setup

The CSS file itself is long, but most of its content is the encoded version of the pop-up image. The actual CSS code for the tooltip is quite short.

To convert an image for use in the CSS, you need it in SVG format. Use an online tool like [CSS Pro](https://csspro.com/svg-to-background-image-css/) to convert the SVG into an encoded CSS URL string, then paste that into the CSS file.

## Result

When you hover over the help icon, you get a tooltip with your custom image. It takes a bit of effort to set up, but having relevant reference content one hover away is well worth the time.

# Obsidian Web Clipper Templates

The Obsidian Web Clipper received a massive update with support for templates, allowing you to customize how web content is captured and formatted when you clip it into your vault.

If you want to learn more about the Web Clipper, check my [tutorial](https://kspr.me/clip).

I also collected a few of my own templates that I find particularly useful. The template pack includes templates for adding URLs to a "URLs to check" list, capturing posts from Twitter, Wikipedia, Reddit, and Medium, and two YouTube templates -- one that embeds the video with its description and transcript, and another that captures just the link and timestamp.

You can [download the free template pack here](https://kspr.me/cliptpl).

# More in This Series

- [[Obsidian Tweaks & Tips - Episode I|Episode I]] -- Templater callout script, auto-hide properties
- [[Obsidian Tweaks & Tips - Episode II|Episode II]] -- Active tab color, hotkey sync, hide specific properties
- [[Obsidian Tweaks & Tips - Episode III|Episode III]] -- Styled TOC, find missing/empty notes, Plugin Groups
- [[Obsidian Tweaks & Tips - Episode IV|Episode IV]] -- Bad YAML finder, stacked tabs, dropdown fields, bullet threading
- Episode V -- Columns, floating callouts, table styles, tasks dashboard, help tooltip
