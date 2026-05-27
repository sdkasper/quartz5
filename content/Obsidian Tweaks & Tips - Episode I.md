---
aliases:
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Obsidian-Tweaks-&-Tips---Episode-I
description: Two quick Obsidian tweaks that make a real difference — a Templater-powered callout script and a CSS snippet to auto-hide properties until you need them.
cover:
date: 2023-10-26
updated: 2026-03-09T14:24:44+02:00
draft: false
categories:
  - obsidian
cssclasses:
tags:
  - obsidian
  - tweaks
created: 2023-10-26T00:00
---

# In a Nutshell

> [!important|float-r] Useful / Download  
> - [[09 Blog/Templater Script - Callouts|Templater Script - Callouts]]  
> - [[09 Blog/CSS - Show properties on hover|CSS - Show properties on hover]]  
> - [Free Starter Vault](https://kspr.me/lsv)  
> * Series:   
> [[Obsidian Tweaks & Tips - Episode II|Ep. II]]  
> [[Obsidian Tweaks & Tips - Episode III|Ep. III]]  
> [[Obsidian Tweaks & Tips - Episode IV|Ep. IV]]  
> [[Obsidian Tweaks & Tips - Episode V|Ep. V]]

Obsidian is great. Plugins are awesome. But there are more things to make Obsidian even better for you. Here are two of them.

## Install the Templater plugin

You need [Obsidian](https://obsidian.md) (duh!) which you can download for free, and the equally free community plugin called "Templater".

To install and enable the plugin, follow these steps:

* Go to **Obsidian Settings** by pressing the cog in the bottom left-hand corner
* Click on **Community Plugins** and **Browse**.

Click for larger image

* **Search** for "Templater"
* Click **install**
* **Enable** the plugin.

Click for larger image

* Back in Settings, go to Templater, and **enter the path to your templates**.
  This could be the root directory, but I recommend having a dedicated folder for your templates. If this folder does not exist, you have to create it first.

Click for larger image

## Make your Obsidian template smart

This comes from GitHub user [SilentVoid13](https://github.com/SilentVoid13/Templater/discussions/922). It is a templater script, that makes it really fast and easy to add callouts.

# Setup

## The template

For this to work, you need to create a new template in your designated templates folder. For example, `Template – Callouts.` Then copy/paste the templater code into it.

## The hotkey

Now, you need to define a hotkey for this template. As always, go to the Obsidian `Settings,` `Templater,` and `Add new hotkey for template.` Select the `Callouts` template and click on the `plus` icon next to it.

In the hotkey settings, search for `callouts,` click the `plus` symbol, and pick any shortcut you like that does not interfere with existing settings. For this demo, I will choose `CTRL + SHIFT + C.`

## The result

* Create a new note and press `CTRL + SHIFT + C` (or whatever hotkey you defined), and the script asks you several things:
* callout type
* folding state
* title
* content (can have multiple lines, but note that you need to hit `SHIFT + Enter` to create one).

Then, hit `Enter` or click the `Submit` button, and your callout is ready.

What I like most about this is that it's super fast and gives me a list of callout types to choose from. Combined with the `Callout Manager` plugin, this gives me full flexibility and makes the use of callouts very efficient.

You can [[09 Blog/Templater Script - Callouts|copy the script from here]]. When pasting the code, make sure to "Paste as Plain Text" -- otherwise, Templater will run into a parsing error.

# Temporarily Hide Properties

I found this one on Reddit, posted by user `[CharmingThunderstorm](https://www.reddit.com/r/ObsidianMD/comments/167hylo/how_to_partially_hide_properties).` It is a CSS snippet that hides the "Properties" in the reading view, shows them when hovering, and keeps them open if you click into any of them for editing. Let me show you how that works.

# Setup

Go to `Settings,` `Appearance,` and scroll all the way down to the `CSS snippets` section.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `hide-properties.css.` Make sure that the file extension is `css.` If you don't see your file extensions, click on `View,` `Show,` and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, return to Obsidian, and refresh the list of snippets. Enable the `hide-properties` one, and that should do it. If it does not, you may have to restart Obsidian.

# Result

Using this snippet, the `properties` will automatically be collapsed/hidden. When you hover, they expand, and -- if you don't click into one of them -- they will automatically collapse when you move the mouse away. If you edit a property, they stay open, of course.

You can [copy the snippet from here](https://wiki.sascha-kasper.com/obsidian/tweaks/css-show-properties-on-hover/).

# More in This Series

- Episode I -- Templater callout script, auto-hide properties
- [[Obsidian Tweaks & Tips - Episode II|Episode II]] -- Active tab color, hotkey sync, hide specific properties
- [[Obsidian Tweaks & Tips - Episode III|Episode III]] -- Styled TOC, find missing/empty notes, Plugin Groups
- [[Obsidian Tweaks & Tips - Episode IV|Episode IV]] -- Bad YAML finder, stacked tabs, dropdown fields, bullet threading
- [[Obsidian Tweaks & Tips - Episode V|Episode V]] -- Columns, floating callouts, table styles, tasks dashboard, help tooltip
