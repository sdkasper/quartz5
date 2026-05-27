---
aliases:
author:
  - Sascha D. Kasper
description: Learn how to generate Bases, CSS snippets, and Templater templates for Obsidian — no coding required — using the free Lean Obsidian Studio web app.
cover:
date: 2026-03-14
draft: true
categories:
  - obsidian
cssclasses:
tags:
  - blog
created: 2026-03-14T12:00
updated: 2026-03-15T16:21:53+02:00
---
# In a Nutshell

> [!important|float-r] Resources
> * [Watch the tutorial](https://kspr.me/yts)  
> * [Sign up (free Explorer tier)](https://kspr.me/los)
> * [Obsidian templates & vaults](https://kspr.me/store)  
> * [Join the Discord](https://kspr.me/discord)  

**Lean Obsidian Studio** is a free web app that generates Bases queries, CSS snippets, and Templater templates for Obsidian. You describe what you want in plain English — or use a guided wizard — and get validated, ready-to-paste code. No YAML, CSS, or Templater syntax required.
# The Problem

If you use Obsidian, you already know the frustration. You want a custom view of your notes, a snippet that changes how your callouts look, or a template that actually works with Templater. But then the YAML for Bases breaks if you miss one colon, CSS selectors don't match your theme, and Templater code works — until it doesn't.

The learning curve is real. YAML syntax, CSS selectors, Templater's async/await patterns — each module has its own language that takes time to learn. Most people give up or waste hours debugging code they found on a forum.

Lean Obsidian Studio was built to fix that. It's a web app with three modules — **Bases**, **CSS Snippets**, and **Templates** — and each one lets you describe what you want and get working code you can paste straight into Obsidian.
# How Lean Obsidian Studio Works

Every module offers three input modes:
- **Starter Cards** — one-click presets that generate instantly, no AI credits needed
- **Chat** — describe what you want in plain English, then iterate with follow-ups
- **Guided Wizard** — step-by-step form that builds the code without writing a single prompt
## Bases Builder

The **Bases Builder** generates YAML code for Obsidian's Bases feature — the built-in database view that lets you query, filter, group, and sort your notes.

**Starter Cards** give you six ready-made starting points like Reading List, Recipe Collection, and Subscription Tracker. Click one, hit Generate, and the result appears instantly. Every output includes a green validation badge (seven automated checks covering view structure, filter logic, formula references, and circular dependencies) plus a plain-English explainer of what the code does.

The **Demo Notes** feature is especially useful. Click the button and download a zip file containing realistic sample notes that match the query. Drop them into Obsidian and see the Base working immediately — no need to create test notes yourself.

In **Chat mode**, type exactly what you need: "Show me all notes in my Projects folder with a status property, displayed as cards grouped by status." Hit Generate, get validated YAML. Type a follow-up to refine — "also add a formula that shows days since last modified" — and it updates in context without starting over.

The **Guided Wizard** walks you through five steps: choose your source folder and tags, pick a view type (Table, Cards, List, or Map), select properties to display, set sort and group options, and add formulas. An optional "Enhance with AI" checkbox lets you build locally without using AI credits.
## CSS Snippets

The **CSS Snippets** module handles visual customization — callout colors, heading styles, tag styling, checkbox variants, and more — without writing a single CSS selector.

**Starter Cards** cover the most common requests: Custom Callouts, Alternative Checkboxes, Heading Styles, Color Scheme, Hide UI Elements, and Tag Colors. Each generates validated CSS with an explainer.

In **Chat mode**, describe the exact look you want: "Make my callouts color-coded — warnings orange, tips green, danger red. Also style my tags with rounded backgrounds." Generate, copy the snippet, and enable it in Obsidian under Settings > Appearance > CSS Snippets. Then iterate — "Make the warning callouts use a gradient background instead" — and the AI refines in context.

The **Guided Wizard** is visual. Step one shows a grid of ten targets (Callouts, Checkboxes, Colors, Headings, Links, Sidebar, and more). Step two lets you choose Dark Only, Light Only, or Both themes. Step three is where it gets interesting — for callouts, you get color pickers and a searchable **Lucide icon picker** with live SVG previews. For headings, individual color pickers for H1 through H6.
## Templates

The **Templates** module generates both Core Templates and Templater templates, with a toggle at the top that adapts the entire output.

With **Templater** selected, a Daily Note starter card generates a template with `tp.date` calls, cursor placement, and frontmatter. Switch to **Core Templates**, click the same card, and the output changes to double-brace syntax with no Templater dependencies.

**Smart validation** catches issues that would silently break in Obsidian. For Templater, it verifies that async functions like `tp.system.prompt` use `await`. It warns if Core Templates syntax appears in a Templater file, or vice versa.

In **Chat mode**, describe what you need — "Weekly review template with wins, lessons, next week's priorities, and a link back to this week's daily notes using Templater" — and get a full template with frontmatter, sections, dynamic content, and cursor positions.

The **Guided Wizard** walks you through plugin selection, purpose, frontmatter fields, body structure, and Templater-specific options like prompts, cursor positions, and date formats.
# Why Not Just Use ChatGPT?

You might be thinking — can't I just ask ChatGPT to generate this? Sure, and the output looks right until you paste it into Obsidian and nothing works.

Generic AI doesn't know the exact YAML format Bases requires. It doesn't know which CSS selectors Obsidian actually uses. It mixes up Core Templates and Templater syntax constantly.

Lean Obsidian Studio is **purpose-built**. The prompts are tuned for Obsidian output. Every result is **validated client-side** before you see it. And with the guided wizards, you don't even need to know how to write a good prompt.
# Get Started

Lean Obsidian Studio is live and free to use. The Explorer tier gives you 5 AI generations per day - all starter cards and guided wizards included, no credit card required.

[Sign up for free](https://kspr.me/los)

Try it and use the feedback button in the app to tell the team what to build next. For a full walkthrough, see [[LOS - Getting Started]].
# FAQ

> [!question]- What is Lean Obsidian Studio?
> A free web app that generates Bases queries, CSS snippets, and Templater/Core templates for Obsidian. You describe what you want in plain English or use a guided wizard, and get validated code ready to paste into your vault.

> [!question]- Is it free?
> The Explorer tier is free with 5 AI generations per day. Pro ($8/mo) gives 50 per day, and Power ($12/mo) is unlimited. Starter cards and local wizard generation are always free on every tier - no credit card required to start.

> [!question]- Do I need to know CSS, Dataview, or Templater?
> No. Each module is designed so you can describe what you want in plain English. The guided wizards don't even require writing a prompt — just click through the steps.

> [!question]- What's the difference between Starter Cards, Chat, and Wizard?
> **Starter Cards** are one-click presets that generate instantly without AI credits. **Chat** lets you type a custom description and iterate with follow-ups. The **Guided Wizard** walks you through a step-by-step form to build the code without writing any prompt.

> [!question]- Does it work with both Core Templates and Templater?
> Yes. The Templates module has a toggle at the top. Select your plugin and the entire output adapts — including validation rules that catch cross-syntax mistakes.
