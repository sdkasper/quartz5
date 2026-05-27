---
aliases:
  - obsidian-course/callouts-templater-script
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Templater-Script---Callouts
description: Insert fully formatted callouts in seconds with this Templater script that prompts you for type, fold state, title, and content.
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
created: 2023-10-17T16:43
updated: 2025-09-11T11:44
---

# Setup
## The template
For this to work, we need to create a new template in our designated templates folder. For example, `Template - Callouts`. Then we need to copy/paste the templater code into it.

## The hotkey
Now we need to define a hotkey for this template. As always, we go to the Obsidian `Settings`, `Templater`, and `Add new hotkey for template`. We select the `Callouts` template and click on the `plus` icon next to it.

In the hotkey settings, search for `callouts`, click the `plus` symbol and pick any shortcut you like that does not interfere with existing settings. For this demo, I will choose `CTRL + SHIFT + C`.
# Result
Create a new note and press `CTRL + SHIFT + C` (or whatever hotkey you defined) and the script asks you several things:
- callout type
- folding state
- title
- content (can have multiple lines, but note that you need to hit `SHIFT + Enter` to create one)

Then hit `Enter` or click the `Submit` button and your callout is ready.

What I like most about this, is that it's superfast and gives me a list of callout types to choose from. Combined with the `Callout Manager` plugin, this gives me full flexibility and makes the use of callouts very efficient.
# Code
```templater
<%_* let calloutType = await tp.system.suggester(["Abstract", "Attention", "Bug", "Caution", "Check", "Cite", "Danger", "Done", "Error", "Example", "Fail", "Failure", "FAQ", "Help", "Hint", "Important", "Info", "Missing","Note", "Question", "Quote", "Success", "Summary", "Tip", "TLDR", "Todo", "Warning"], ["abstract", "attention", "bug", "caution", "check", "cite", "danger", "done", "error", "example", "fail", "failure", "faq", "help", "hint", "important", "info", "missing","note", "question", "quote", "success", "summary", "tip", "tldr", "todo", "warning"], false, "Which type of callout do you want to insert?")%>

<%_* let foldState = await tp.system.suggester(["Not Foldable", "Default Expanded", "Default Collapsed"], ["", "+", "-"], false, "Folding state of callout?")%>

<%_*
  let title = await tp.system.prompt("Optional Title Text", "")
%>

<%_*
  let calloutContent = await tp.system.prompt("Optional Content Text (Shift Enter to Insert New Line)", "", false, true)
  calloutContent = calloutContent.replaceAll("\n", "\n> ")
%>

<%-*
if (calloutType != null) {
  let content = '> [!' + calloutType + ']' + foldState + ' ' + title + '\n> ' + calloutContent + '\n'
  tR+=content
}
%>
```

# Source
This comes from GitHub user [SilentVoid13](https://github.com/SilentVoid13/Templater/discussions/922). It is a templater script, that makes it really fast and easy to add callouts.
