---
aliases:
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Obsidian-for-logging-helps-with-journaling
description: Discover a structured approach and learn how logging helps with journaling using Obsidian’s logging system.
cover:
date: 2025-02-18
draft: false
categories:
  - obsidian
  - plugins
cssclasses:
tags:
  - obsidian
  - plugins
created: 2026-03-02T14:59
updated: 2026-03-08T17:36:39+02:00
---

# In a Nutshell

> [!scene|video-r] Tutorial
> ![](https://www.youtube.com/watch?v=GK7TLrILmjE)

Many people have difficulties with writing in a conventional journal every day.

This post – and the related video tutorial – will teach you how to create an easy and fast logging system in Obsidian. You can jot down events using bullet points or write short notes instead of getting a headache trying to compose long paragraphs. The system lets you instantly write down your ideas or feelings, growing with you as a versatile tool.

Journaling is sometimes considered tedious, but it is not always the case. By using Obsidian, you can quickly log your thoughts. I will introduce you to a practical process of creating and examining your log entries in Obsidian. This method of logging helps with journaling, too. This technique will serve you whether you wish to note your daily thoughts or may later turn your log into a full-fledged journal.
# Journaling
You are not the only one who has ever sat down to write in a diary but found themselves looking at a blank page. Regular journaling can be very stressful. You usually think you must write something very deep or essential, which becomes annoying. Rather, think of a different, structured, and more effective way to document your thoughts. Turning the journaling to logging allows you to note key events without writing flawless sentences.

- **Pressure to Write Deeply:** The expectation to craft meaningful prose can be overwhelming.
- **Time Constraints:** Life moves fast, and you often don’t have time to write long entries.
- **Lack of Structure:** Without a clear format, consistency becomes difficult.
- **Frustrating Reviews:** Sifting through pages of rambling thoughts can be tedious.

# Logging
These are the main reasons logging is becoming popular. Its structured and concise format allows you to capture the core of your memories without the strain of elaborate writing.

Log entries could be formulated quickly and broadly or manually and randomly structured. Unlike long, dreadful paragraphs, bullet points will enable you to distinctly detail events you want to learn and reflect on. Using this technique lessens the pressure and helps you to write in a coherent and easy-to-check way. By tagging your entries, you can uncover and learn from them with the help of Obsidian’s Dataview plugin.

The **Publish** plugin allows you to share your notes online efficiently. It enables publishing based on specific criteria such as tags or properties, making it easy to manage content directly from Obsidian. However, it’s essential to note that some plugins may not be compatible with publishing features, which can be a consideration if you rely on certain functionalities.

[Jump directly to the related chapter in the video tutorial](https://www.youtube.com/watch?v=GK7TLrILmjE&t=212s).
# Setup

> [!image|float-r] Folder structure and "Templates Folder"
> ![[folder-structure.png|Journal folder tree with Daily, Weekly, and Monthly subfolders by year]] ![[templates.png|Templates folder showing BJ Daily, Monthly, and Weekly Notes templates]]

# Folder structure
A folder structure and templates are what you should create first to properly set up your logging system in Obsidian. The way I arrange my folders is shown in the screenshot to the right.

In the “90 Organize/Templates” folder, I create templates for daily, weekly, and monthly notes.
These templates contain front-matter fields, navigation items, and sections for logging thoughts, habits, and reflections.

# Plugins
The subsequent plugins to be installed are as follows in case you want to have the best logging experience in Obsidian:

- **Hotkeys:** This is for quickly creating log entries.
- **QuickAdd:** Creates log entries in the right location and format.
- **Dataview:** Necessary for querying and analyzing your log entries.
- **Journals:** For managing daily, weekly, and monthly notes.
- **Dynamic Embed:** To easily embed queries and other elements in your notes.
- **Templater:** For advanced templating capabilities.

Except for “Hotkeys,” a core plugin, you can install all these plugins directly from the community plugins section on the Obsidian settings.

When the plugins have been installed, the next step is configuring them correctly. You can find [detailed instructions in the video tutorial](https://www.youtube.com/watch?v=GK7TLrILmjE&t=579s). Here is a short summary:

- For **Dataview**, enable options for inline queries and javascript queries.
- **Dynamic Embed** requires no additional configuration—just enable it.
- For the **Journals** plugin, define the first day of the week and set up your journal folder structure.
- In **QuickAdd**, create an action for logging entries that formats the output correctly.
- Configure **Hotkeys** to quickly access the logging command – I use “ALT+L”.
- In **Templater**, set the templates folder location for your log templates.

These configurations will ensure a smooth logging experience from the start.

# Demo
Take a look at the [live demo in the tutorial](https://www.youtube.com/watch?v=GK7TLrILmjE&t=935s). After creating your daily note, you can instantly insert log entries through the hotkey.

For instance, if I press “ALT+L,” I can enter my text that will be automatically added to my “Log” section with a timestamp. This is a fast thought-capture method; you can even use emojis and links to other notes.

If you add a tag to your log entries, you can use Dataview queries to analyze and learn from them.

[Watch the related chapter in the video tutorial](https://sascha-kasper.com/why-obsidian-logging-helps-with-journaling/Watch%20the%20related%20chapter%20in%20the%20video%20tutorial.).

> [!tip|float-l] A little help
> Here’s a [DataviewJS query](https://wiki.sascha-kasper.com/obsidian/tweaks/dvjs-log-review-and-analysis/)
> 
> for you to start with.

Thanks to the Dataview plugin, you can list, filter, review, and analyze your entries based on tags or keywords. This feature allows you to check for patterns and reflect on your development.

Using this query, you can create a table reflecting all your victories – entries tagged with “#win,” for example – which will assist you in tracking your progress and celebrating your accomplishments.

You can quickly adapt the query to work with other tags.

[Watch the related chapter in the video tutorial](https://www.youtube.com/watch?v=GK7TLrILmjE&t=1249s).

Embedding elements can significantly improve your vault’s robustness. You can create a standalone note for your query and embed it wherever needed, making query maintenance much more manageable. Any original note modifications will be automatically present in all the embedded instances.

Suppose you have a question about monitoring overdue tasks. You can create a note containing that query and incorporate it into your daily notes. This will enable all the daily notes to be up to date every time you change the query without requiring you to change each one manually.

# Benefits
# Fast
This system can be established quickly, and you can record your ideas without hassle. Instead of classical journaling, you can capture your ideas fast through structured logging in Obsidian. This technique is about the positive experience of journaling and its persistent usage.

Logging is faster than journaling, which usually consists of longer, more introspective writing. Using logging instead of journaling reduces the level of pressure and boosts consistency.
# Frictionless
You can still create a basic log system by manually organizing notes into folders. However, plugins such as Dataview and QuickAdd can enhance the logging experience and lower the effort, making it more likely that you will stick to it.

You can arrange your logs by creating a folder structure and effectively utilizing templates and tags. Regularly reviewing and updating your entries will also help you have a clear overview of your thoughts and progress.

# Beginner-friendly

> [!tip|float-r] There is more
> You can find free and paid
> 
> templates on various websites,
> 
> such as [LeanProductivity](https://kspr.me/store).

Is this method suitable for beginners?

Of course! This logging system has been developed to be user-friendly, and novices can configure it easily.
Follow the [video tutorial](https://youtu.be/GK7TLrILmjE) or download the free  [Lean Starter Vault](https://kspr.me/lsv), which includes all the templates, scripts, and configuration.




