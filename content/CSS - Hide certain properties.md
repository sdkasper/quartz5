---
aliases:
  - obsidian-course/css-hide-certain-properties
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Hide-certain-properties
description: Selectively hide specific frontmatter properties from Obsidian's reading and preview mode with one CSS rule.
cover:
date: 2023-11-07
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2023-11-07T14:19
updated: 2025-10-03T08:30
---


# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `hide properties.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable the `hide properties` one, and that should do it. If it does not, you may have to restart Obsidian.

# Result
Using this snippet, you can easily control which properties on your notes shall be displayed or hidden when in preview or read mode. 

# Code
```css
div.metadata-properties > div.metadata-property[data-property-key="Property Name"] {
  display: none;
}
```

# Source
I found this on Reddit, posted by user [TSPhoenix](https://www.reddit.com/r/ObsidianMD/comments/17f1h9h/is_there_a_way_to_hide_just_some_properties/). 
