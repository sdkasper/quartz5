---
aliases:
  - obsidian/tweaks/css-embedded-callout
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Embedded-Callout
description: Make callouts float left or right inside your Obsidian notes so text wraps around them like sidenotes.
cover:
date: 2024-11-09
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2024-11-09T12:53
updated: 2026-03-24T17:53:48+02:00
---

# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable this one, and that should do it. If it does not, you may have to restart Obsidian.
# Result
This snippet will embed you callouts into your text, making the text float around it. In the CSS, you can change various attributes such as the callout size, border color, etc.

Use the qualifiers `float-l` or `float-r` in combination with you callout type, respectively.

```text
> [!important|float-r] Right Float
> ### Sidenotes Content
> Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

```text
> [!info|float-l]+
> ### Left Float Collapsible
> Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

It will look like this:

---
![[CSS - Embedded Callout.webp|Note text wrapping around a right-floated and a left-floated callout]]

---

# Code
```css
/* right float */
.callout[data-callout-metadata*="float-r"] {
  position: relative;
  float: right;
  width: 20%; /* Set the width of the sidenote */
  margin: 5px; /* Adjust margins to control spacing */
  padding: 10px; /* Optional padding inside the sidenote */
  background-color: var(--background-primary) !important;
  border: 1px solid #25D0F7; /* Optional border */
  border-radius: 5px; /* Rounded corners */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Optional shadow */
}

/* left float */
.callout[data-callout-metadata*="float-l"] {
  position: relative;
  float: left;
  width: 20%; /* Set the width of the sidenote */
  margin: 5px; /* Adjust margins to control spacing */
  padding: 10px; /* Optional padding inside the sidenote */
  background-color: var(--background-primary) !important;
  border: 1px solid #25D0F7; /* Optional border */
  border-radius: 5px; /* Rounded corners */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Optional shadow */
}

/* Optional styling to manage the flow around the sidenote for the main content */
.markdown-content {
  overflow: hidden; /* Clear floats to ensure content below flows correctly */
}
```
