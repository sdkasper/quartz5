---
aliases:
  - obsidian/tweaks/css-hoverable-drop-down-fields
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/CSS---Hoverable-drop-down-fields
description: Build a multi-level hoverable dropdown navigation menu inside your Obsidian notes using callouts and CSS.
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
created: 2024-04-14T10:04
updated: 2025-10-17T17:44
---

# Setup
## Copy and activate the snippet
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `hover drop down.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable the `hover drop down` one, and that should do it. If it does not, you may have to restart Obsidian.
## Apply the snippet in a note
Create a new note and insert a callout with a bullet list, like so:

```text
> [!navmenu|Blue_gradient_1] 
> - [🏠 Home](https://wiki.sascha-kasper.com/)
> - Modules
>     - [[Lean CRM Vault]]
>     - [[Lean Travel Vault]]
> - Tweaks
>     - CSS
>         - [[CSS - Change active tab color]]
>         - [[CSS - Formatting stacked tabs]]
>         - [[CSS - Hide certain properties]]
>         - [[CSS - Hide Properties on Specific Notes]]
>         - [[CSS - Show properties on hover]]
> 	- Dataview
> 		- [[DV - list empty notes]]
> 		- [[DV - list missing notes]]
> 	- DataviewJS
> 		- [[DVJS - Find bad YAML]]
> 		- [[DVJS - Interactive Tables]]
> 	- Templater
> 		- [[Templater Script - Ask for Note Title]]
> 		- [[Templater Script - Callouts]]
```

# Result
Using this snippet, you can easily change your field's appearance.


![[CSS - Hoverable drop-down.webp|Multi-level dropdown navigation menu with Home, Modules, and Tweaks expanding on hover]]

# Code
```css
/* based on original design by FeikeB:
   https://forum.obsidian.md/t/want-a-multi-level-dropdown-menu-inside-your-notes-you-can-i-built-one/40501
   converted (badly) to callout by sailKite */
.callout[data-callout="navmenu"] {

    /* Gradient color selections */
    &[data-callout-metadata*="Blue_gradient_1"] { --custom-background-color: #2D22C6; }
    &[data-callout-metadata*="Blue_gradient_2"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_3"] { --custom-background-color: #25D0F7; }
    &[data-callout-metadata*="Blue_gradient_4"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_5"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_6"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_7"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_8"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_9"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_10"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_11"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_12"] { --custom-background-color: #FFFFFF; }
    &[data-callout-metadata*="Blue_gradient_13"] { --custom-background-color: #FFFFFF; }

    --item-gap: 6px;
    background-color: transparent;
    --link-color: var(--custom-background-color);
    --link-color-hover: var(--custom-background-color);
    margin: 0;
    border: 0;
    padding: 0;
    overflow: visible;
    z-index: 10;

    & > .callout-content ul li a {
        pointer-events: auto;
    }

    & .callout-content a {
        position: relative;
    }

    & * {
        pointer-events: auto;
        
        :is(:hover > *) {
            transition-delay: 500ms !important;
        }
    }

    & > .callout-title { display: none; }

    & > .callout-content {
        overflow: visible;
        isolation: isolate;
        z-index: 10;

        & :is(.list-bullet, .list-collapse-indicator) { display: none; }

        & ul {
            display: flex;
            position: relative;
            padding-inline-start: 0;
            z-index: 10;

            &::before, &::after { display: none; }

            &::before {
                content: "";
                display: block;
                position: absolute;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
                bottom: unset;
                border: unset;
            }

            & li {
                background: #2D22C6;
                border: 1px solid var(--custom-background-color); /* Border color #2D22C6 */
                color: var(--custom-background-color); !important; /* Text color #2D22C6 */
                font-weight: bold;
                min-width: 200px;
                min-height: 30px;
                transition: background 0.2s, color 0.2s, transform 0.2s;
                margin: 0px var(--item-gap) var(--item-gap) 0px;
                padding-top: 10px;
                padding-bottom: 10px;
                box-sizing: border-box;
                border-radius: 3px;
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);
                position: relative;
                text-align: center;
                list-style: none;
                display: block;
                z-index: 10;

                &:not(:hover, :has(:hover)) {
                    overflow: hidden;
                }

                & > ul > li {
                    transition: transform 0.2s, opacity 0.2s;
                    transform: translateY(150%);
                    opacity: 0;
                }

                &:is(:hover, :has(:hover)) {
                    &::before {
                        content: "";
                        position: absolute;
                        inset: 0;
                        width: calc(100% + var(--item-gap));
                        height: calc(100% + var(--item-gap));
                    }
                    & > ul > li {
                        transform:translateX(0%);
                        opacity: 1;
                    }
                }
            }

            & ul {
                position: absolute;
                flex-direction: column;
                top: calc(100% + var(--item-gap));

                & > li > ul {
                    top: 0;
                    left: calc(100% + var(--item-gap));
                    
                    & > li {
                        transform: translateX(195px);
                    }
                }
            }
        }
    }

    .markdown-source-view.mod-cm6 .cm-content > [contenteditable=false]:has(> .markdown-rendered > &) {
        contain: none !important;

        &:hover {
            contain: none !important;
            overflow: visible;
        }
    }
}
```

# Source
I found this on [Reddit](https://www.reddit.com/r/ObsidianMD/comments/1by3wau/enough_with_plugins_what_isare_your_favorite/) from user [OnionOk776](https://www.reddit.com/user/OnionOk776/)
