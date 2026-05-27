---
aliases:
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Obsidian-asks-for-title-BEFORE-note-creation
description: Learn how to create Obsidian Templater templates that ask for a note title before creating the note, plus a free meeting template download.
cover:
date: 2023-08-25
updated: 2026-03-09T17:35:38+02:00
draft: false
categories:
  - obsidian
  - templater
cssclasses:
tags:
  - obsidian
  - templater
created: 2023-08-25T00:00
---

# In a Nutshell

> [!important|float-r] Useful / Download
> - [Copy the script](https://wiki.sascha-kasper.com/obsidian/tweaks/templater-script-ask-for-note-title/)
> - [Free Meeting Template](https://shop.sascha-kasper.com/b/tplmeeting1)

Learn how to create Obsidian templates based on the Templater plugin asking you for a note title ***BEFORE*** creating the note.

A download link is at the end of the post.

If you want to build even smarter Obsidian templates, take a look at this video. In less than 10 minutes, you will learn how to level up your templates.

Every Obsidian user discovers the power of templates -- especially with the Templater plugin -- sooner or later. This extremely useful plugin allows you to make your note creation easier and more efficient.

# Install the Templater plugin

You need [Obsidian](https://obsidian.md) (duh!) which you can download for free, and the equally free community plugin called "Templater".

To install and enable the plugin, follow these steps:

* Go to **Obsidian Settings** by pressing the cog in the bottom left-hand corner
* Click on **Community Plugins** and **Browse**.

* **Search** for "Templater"
* Click **install**
* **Enable** the plugin.

* Back in Settings, go to Templater, and **enter the path to your templates**.
  This could be the root directory, but I recommend having a dedicated folder for your templates. If this folder does not exist, you have to create it first.

# How to use Templater

## Make your Obsidian template smart
As you may know, "Templater defines a templating language that lets you insert variables and functions results into your notes. It will also let you execute JavaScript code manipulating those variables and functions. It allows you to execute arbitrary JavaScript code and system commands."

This can be fairly simple one-line snippets like inserting the creation date of a new note, like so:

`Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>`

To make Obsidian ask for a note's title BEFORE creating the note, you need to add the code snippet on the right (or below if you read this on a mobile) **to your template's frontmatter**.

You can [copy the script from here](https://wiki.sascha-kasper.com/obsidian/tweaks/templater-script-ask-for-note-title/). When pasting the code, make sure to "Paste as Plain Text" -- otherwise, Templater will run into a parsing error.

## The result
If you then create a new note based on this template, the following things will happen:

1. Obsidian will ask you for the note's title.
2. Obsidian will create the note with the provided title.
3. The new note's frontmatter will be filled with these tags:
   1. "Created:" the date when you created the note.
   2. "Modified:" the date when the note was modified. Unfortunately, this does not update automatically when you do changes later.
      If anybody knows how to do that, please let me know.
   3. "Alias:" allows you to specify one or more alternative titles that will be found when you search for the note.
   4. "Tags:" lets you categorize your note with one or more tags -- very helpful for keeping notes organized.
4. Outside the frontmatter section, the chosen title will automatically be added as a level 1 heading.
5. Last but not least, Templater will mark cursor positions for you. After creating the note, press the TAB key to jump to the next one. This allows you to start typing right away.

## Bonus for you
I prepared a template for taking notes during meetings that uses Templater and the exact method I just described.

You can [download it for free](https://shop.sascha-kasper.com/b/tplmeeting1) and drag it into your vault's template folder.

This template will give you notes like the one in the image to the right.
