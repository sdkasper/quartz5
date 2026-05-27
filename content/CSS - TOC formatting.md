---
aliases:
  - obsidian/tweaks/css-toc-formatting
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---TOC-formatting
description: Color-code each heading level in Obsidian's outline view so it matches your note's heading colors.
cover:
date: 2023-12-25
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2023-12-25T11:32
updated: 2025-10-09T08:55
---


# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `TOC formatting.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable the `TOC formatting` one, and that should do it. If it does not, you may have to restart Obsidian.
# Result
With this snippet, the outline view in Obsidian will use the same colors for each heading level as in your actual note. The colors themselves can be customized via your theme settings or with yet another CSS snippet.
# Code
```css
:root {
    --h1-color: #7dd3fc;
    --h2-color: #a78bfa;
    --h3-color: #e879f9;
    --h4-color: #34d399;
    --h5-color: #facc15;
    --h6-color: #60a5fa;
  }
  
  [data-type="outline"] {
    /* h1 */
    .tree-item > .tree-item-self {
      color: var(--h1-color);
    }
  
    /* h2 */
    .tree-item .tree-item > .tree-item-self {
      color: var(--h2-color);
    }
  
    /* h3 */
    .tree-item .tree-item .tree-item > .tree-item-self {
      color: var(--h3-color);
    }
  
    /* h4 */
    .tree-item .tree-item .tree-item .tree-item > .tree-item-self {
      color: var(--h4-color);
    }
  
    /* h5 */
    .tree-item .tree-item .tree-item .tree-item .tree-item > .tree-item-self {
      color: var(--h5-color);
    }
  
    /* h6 */
    .tree-item .tree-item .tree-item .tree-item .tree-item .tree-item > .tree-item-self {
      color: var(--h6-color);
    }
  }
```

# Source
I found this one on Reddit, posted by user [stassinari](https://www.reddit.com/user/stassinari/).
