---
aliases:
  - obsidian/tweaks/css-bullet-threading
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Bullet-threading
description: Add colorful connecting lines between nested list items on hover in both the editor and outline view.
cover:
date: 2024-04-14
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2024-04-14T11:33
updated: 2025-10-17T17:44
---

# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `bullet threading.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable the `bullet threading` one, and that should do it. If it does not, you may have to restart Obsidian.

# Result
This snippet will automatically add a "guiding line" from the top level entry in a list to the entry over which you are hovering your mouse:


![[CSS - Bullet threading.webp|Nested bullet list with colorful guide lines connecting parent and child items on hover]]

# Code

```css
//comment
.HyperMD-list-line-1:not(:has(~ .HyperMD-list-line-1 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4, .HyperMD-list-line-3, .HyperMD-list-line-2):hover)::after,
.HyperMD-list-line-1:not(:has(~ .HyperMD-list-line-1 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-2:hover, ~ .HyperMD-list-line-2 ~ :is(.HyperMD-list-line-3, .HyperMD-list-line-4, .HyperMD-list-line-5, .HyperMD-list-line-6):hover)::before,
.HyperMD-list-line-2:not(:has(~ .HyperMD-list-line-2 ~ .HyperMD-list-line:hover)):is(:hover, :has(~ :is(.HyperMD-list-line-3, .HyperMD-list-line-4, .HyperMD-list-line-5, .HyperMD-list-line-6):hover))::before {
  --list-threading-color: hsl(23, 100%, 45%, 1);
  --list-threading-offset: calc(4px + 0.15em);
}

.HyperMD-list-line-2:not(:has(~ .HyperMD-list-line-2 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4, .HyperMD-list-line-3):hover)::after,
.HyperMD-list-line-2:not(:has(~ .HyperMD-list-line-2 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-3:hover, ~ .HyperMD-list-line-3 ~ :is(.HyperMD-list-line-4, .HyperMD-list-line-5, .HyperMD-list-line-6):hover)::before,
.HyperMD-list-line-3:not(:has(~ .HyperMD-list-line-3 ~ .HyperMD-list-line:hover)):is(:hover, :has(~ :is(.HyperMD-list-line-4, .HyperMD-list-line-5, .HyperMD-list-line-6):hover))::before {
  --list-threading-color: hsl(46, 100%, 45%, 1);
  --list-threading-offset: calc(4px + 0.15em + 2em);
}

.HyperMD-list-line-3:not(:has(~ .HyperMD-list-line-3 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4):hover)::after,
.HyperMD-list-line-3:not(:has(~ .HyperMD-list-line-3 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-4:hover, ~ .HyperMD-list-line-4 ~ :is(.HyperMD-list-line-5, .HyperMD-list-line-6):hover)::before,
.HyperMD-list-line-4:not(:has(~ .HyperMD-list-line-4 ~ .HyperMD-list-line:hover)):is(:hover, :has(~ :is(.HyperMD-list-line-5, .HyperMD-list-line-6):hover))::before {
  --list-threading-color: hsl(70, 100%, 45%, 1);
  --list-threading-offset: calc(4px + 0.15em + 2 * 2em);
}

.HyperMD-list-line-4:not(:has(~ .HyperMD-list-line-4 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5):hover)::after,
.HyperMD-list-line-4:not(:has(~ .HyperMD-list-line-4 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-5:hover, ~ .HyperMD-list-line-5 ~ :is(.HyperMD-list-line-6):hover)::before,
.HyperMD-list-line-5:not(:has(~ .HyperMD-list-line-5 ~ .HyperMD-list-line:hover)):is(:hover, :has(~ :is(.HyperMD-list-line-6):hover))::before {
  --list-threading-color: hsl(105, 100%, 45%, 1);
  --list-threading-offset: calc(4px + 0.15em + 3 * 2em);
}

.HyperMD-list-line-5:not(:has(~ .HyperMD-list-line-5 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6):hover)::after,
.HyperMD-list-line-5:not(:has(~ .HyperMD-list-line-5 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-6:hover)::before,
.HyperMD-list-line-6:not(:has(~ .HyperMD-list-line-6 ~ .HyperMD-list-line:hover)):is(:hover)::before {
  --list-threading-color: hsl(187, 100%, 45%, 1);
  --list-threading-offset: calc(4px + 0.15em + 4 * 2em);
}

/* tails */
.HyperMD-list-line-1:not(:has(~ .HyperMD-list-line-1 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4, .HyperMD-list-line-3, .HyperMD-list-line-2):hover)::after,
.HyperMD-list-line-2:not(:has(~ .HyperMD-list-line-2 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4, .HyperMD-list-line-3):hover)::after,
.HyperMD-list-line-3:not(:has(~ .HyperMD-list-line-3 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4):hover)::after,
.HyperMD-list-line-4:not(:has(~ .HyperMD-list-line-4 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5):hover)::after,
.HyperMD-list-line-5:not(:has(~ .HyperMD-list-line-5 ~ .HyperMD-list-line:hover)):has(~ :is(.HyperMD-list-line-6):hover)::after {
  content: "";
  position: absolute;
  left: var(--list-threading-offset);
  bottom: 0;
  height: 0.8em;
  width: 2px;
  background-color: var(--list-threading-color);
}
.HyperMD-list-line.HyperMD-task-line::after {
  max-height: 0.275em;
}

/* in-between lines */
.HyperMD-list-line-1:not(:has(~ .HyperMD-list-line-1 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-2:hover, ~ .HyperMD-list-line-2 ~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4, .HyperMD-list-line-3):hover)::before,
.HyperMD-list-line-2:not(:has(~ .HyperMD-list-line-2 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-3:hover, ~ .HyperMD-list-line-3 ~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4):hover)::before,
.HyperMD-list-line-3:not(:has(~ .HyperMD-list-line-3 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-4:hover, ~ .HyperMD-list-line-4 ~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5):hover)::before,
.HyperMD-list-line-4:not(:has(~ .HyperMD-list-line-4 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-5:hover, ~ .HyperMD-list-line-5 ~ :is(.HyperMD-list-line-6):hover)::before,
.HyperMD-list-line-5:not(:has(~ .HyperMD-list-line-5 ~ .HyperMD-list-line:hover)) ~ .HyperMD-list-line:has(~ .HyperMD-list-line-6:hover)::before {
  content: "";
  position: absolute;
  left: var(--list-threading-offset);
  top: 0;
  height: 100%;
  width: 2px;
  background-color: var(--list-threading-color);
}

/* elbows */
.HyperMD-list-line-2:not(:has(~ .HyperMD-list-line-2 ~ .HyperMD-list-line:hover)):is(:hover, :has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4, .HyperMD-list-line-3):hover))::before,
.HyperMD-list-line-3:not(:has(~ .HyperMD-list-line-3 ~ .HyperMD-list-line:hover)):is(:hover, :has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5, .HyperMD-list-line-4):hover))::before,
.HyperMD-list-line-4:not(:has(~ .HyperMD-list-line-4 ~ .HyperMD-list-line:hover)):is(:hover, :has(~ :is(.HyperMD-list-line-6, .HyperMD-list-line-5):hover))::before,
.HyperMD-list-line-5:not(:has(~ .HyperMD-list-line-5 ~ .HyperMD-list-line:hover)):is(:hover, :has(~ :is(.HyperMD-list-line-6):hover))::before,
.HyperMD-list-line-6:not(:has(~ .HyperMD-list-line-6 ~ .HyperMD-list-line:hover)):is(:hover)::before {
  content: "";
  position: absolute;
  left: var(--list-threading-offset);
  width: 2em;
  top: 0;
  height: calc(100% - 0.825em - var(--outline-guideline-width) / 2);
  border-bottom-left-radius: var(--radius-m);
  border-bottom: 3px solid var(--list-threading-color);
  border-left: 3px solid var(--list-threading-color);
}
.HyperMD-list-line.HyperMD-task-line::before {
  max-width: calc(2em - 0.35em);
}



body {
  --outline-guideline-width: var(--size-2-1);
  --outline-guideline-color: var(--color-accent);
  --outline-item-height: calc(var(--nav-item-size) * 1.8);
}

li {
  position: relative;
}

/* In-between items */

li:hover > ul > li:has(~li:hover)::before {
  content: "";
  width: 3px;
  position: absolute;
  background-color: var(--outline-guideline-color);
  top: calc(var(--outline-item-height) / 2 * -1);
  left: calc(-2px - 2em - var(--size-4-4));
  height: calc(100% - var(--outline-item-height) + var(--size-4-8) + 2px);
}

/* Elbows items */

li:hover > ul > li:hover::before {
  content: "";
  position: absolute;
  top: calc(var(--outline-item-height) / 2 * -1);
  left: calc(-2px - 2em - var(--size-4-4));
  bottom: calc(100% - (var(--outline-item-height) + var(--size-4-2)) / 2 + 1px);
  width: calc(1em + var(--size-4-4) - 2px);
  border-bottom-left-radius: var(--radius-m);
  border-bottom: 3px solid var(--outline-guideline-color);
  border-left: 3px solid var(--outline-guideline-color);
}

/* Outline Bullet Threading*/

body {
  --accent-active: var(--color-accent);
  /* 引导线粗细 */
  --outline-guideline-width: 3px;
  /* 引导线颜色 */
  --outline-guideline-color: var(--accent-active);
  /* 一行高度 */
  --outline-item-height: calc(var(--nav-item-size) * 1.8);
}

.workspace-leaf-content[data-type=outline] .view-content .outline {
  --line-height-tight: var(--outline-item-height);
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item {
  position: relative;
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-self {
  position: relative;
  margin-bottom: 0;
  white-space: nowrap;
  margin-top: -1px;
  /* fix item gap */
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-self::before {
  content: "";
  width: var(--size-4-5);
  height: calc(var(--outline-item-height) + var(--size-4-2));
  position: absolute;
  left: calc(var(--size-4-4) * -1);
  top: 0;
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-self .tree-item-inner {
  padding-left: var(--size-4-1);
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-self .tree-item-inner::before {
  content: "";
  width: var(--size-4-1);
  height: var(--size-4-1);
  border: var(--size-2-1) solid var(--outline-guideline-color);
  border-radius: 50%;
  position: absolute;
  top: 50%;
  transform: translate(calc(-1 * var(--size-4-5)), -50%);
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-self .tree-item-icon ~ .tree-item-inner {
  padding-left: var(--size-4-1);
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-self .tree-item-icon ~ .tree-item-inner::before {
  content: none;
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item.is-collapsed .tree-item-icon::before {
  box-shadow: 0 0 0 var(--size-4-1) var(--background-modifier-hover);
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item::after {
  content: "";
  width: var(--outline-guideline-width);
  position: absolute;
  background-color: transparent;
  top: calc(var(--outline-item-height) / 2 * -1);
  left: -14px;
  height: calc(100% - var(--outline-item-height) + var(--size-4-8));
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-icon {
  cursor: pointer;
  transform: translateY(var(--size-2-3));
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-icon::before {
  width: var(--size-4-2);
  height: var(--size-4-2);
  background-color: var(--outline-guideline-color);
  border-radius: 50%;
  position: absolute;
  left: 3px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-icon svg path {
  display: none;
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item:hover > .tree-item-children > .tree-item::after {
  background-color: var(--outline-guideline-color);
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item:hover > .tree-item-self:hover + .tree-item-children .tree-item::after {
  background-color: transparent;
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item:hover > .tree-item-children > .tree-item:hover::after, .workspace-leaf-content[data-type=outline] .view-content .outline .tree-item:hover > .tree-item-children > .tree-item:hover ~ .tree-item::after {
  background-color: transparent;
}
.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item:hover > .tree-item-children > .tree-item:hover::before {
  content: "";
  position: absolute;
  top: calc(var(--outline-item-height) / 2 * -1);
  left: -14px;
  bottom: calc(100% - (var(--outline-item-height) + var(--size-4-2)) / 2 - 1px);
  width: var(--size-4-6);
  border-bottom-left-radius: var(--radius-m);
  border-bottom: var(--outline-guideline-width) solid var(--outline-guideline-color);
  border-left: var(--outline-guideline-width) solid var(--outline-guideline-color);
  z-index: 9;
}
.workspace-leaf-content[data-type=outline] .view-content .outline :is(.tree-item-children, .tree-item-self) {
  padding-left: 28px !important;
  margin-left: 0 !important;
  border-left: none;
}

.workspace-leaf-content[data-type=outline] .view-content .outline .tree-item-inner:empty {
  height: var(--outline-item-height);
}
Bullet Threading.css
Displaying Bullet Threading.css.

```

# Source
I found this on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/1by3wau/comment/kyh7j9r/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button), posted by user [seashoreandhorizon](https://www.reddit.com/user/seashoreandhorizon/). 
