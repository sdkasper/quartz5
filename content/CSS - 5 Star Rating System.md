---
aliases:
  - Obsidian Star Rating CSS
author:
  - Sascha D. Kasper
source: https://www.reddit.com/r/ObsidianMD/comments/1s6rfuy/my_progressbar_css_snippet
description: A CSS snippet that displays color-coded 5-star ratings in Obsidian using HTML progress bars. Supports half-stars, Meta Bind integration, and five color zones from red to green.
cover: zAttachments/CSS - 5 Star Rating System.webp
date: 2026-03-31
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2026-03-31T13:10
updated: 2026-04-01T09:27:24+03:00
---

This CSS snippet turns a standard HTML `<progress>` element into a visual 5-star rating inside Obsidian. Stars change color across five zones — from red (1 star) to green (5 stars) — and support half-star increments like 3.5. It works in both Reading and Live Preview modes, and pairs with Meta Bind to drive ratings from frontmatter properties.
# How to Install the Star Rating CSS Snippet
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `advanced-star-rating-5.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable this one, and that should do it. If it does not, you may have to restart Obsidian.
## How to Use It
Add a `<progress>` HTML element anywhere in your note with the `star5` class:

```text
<progress class="star5" value="4" max="5"></progress>
```

The `value` attribute sets how many stars are filled (supports half-steps like `3.5`). The `max` is always `5`.
To drive the rating from frontmatter, add a numeric `rating` property and use Meta Bind to render it:

```text
Rating: `VIEW[<progress class="star5" value="{rating}" max="5"></progress>][text(renderMarkdown)]`
```
## What Do the Star Colors Mean?
Stars change color based on the rating value:

| Rating | Color | Name |
|--------|-------|------|
| 0.x - 1.x | Red | Vermilion (#FC3634) |
| 2.x | Orange | Burnt Sienna (#CC7859) |
| 3.x | Yellow | Gold (#FFD700) |
| 4.x | Teal | Mint (#18BC9C) |
| 5 | Green | Mantis (#77C66B) |

Unfilled stars are shown in dark slate (#3A4A5C).
# Result
<progress class="star5" value="1" max="5"></progress> 1
<progress class="star5" value="1.5" max="5"></progress> 1.5
<progress class="star5" value="2" max="5"></progress> 2
<progress class="star5" value="2.5" max="5"></progress> 2.5
<progress class="star5" value="3" max="5"></progress> 3
<progress class="star5" value="3.5" max="5"></progress> 3.5
<progress class="star5" value="4" max="5"></progress> 4
<progress class="star5" value="4.5" max="5"></progress> 4.5
<progress class="star5" value="5" max="5"></progress> 5
# Code
```css
/*
--- 5 STAR RATING SYSTEM (LeanProductivity Brand Colors) ---
Adapted from: https://www.reddit.com/r/ObsidianMD/comments/1s6rfuy/my_progressbar_css_snippet
*/

:is(
  .markdown-preview-view,
  .markdown-rendered,
  .markdown-source-view.is-live-preview
)
progress.star5 {
  --total-number-of-stars: 5;
  height: 20px;
  width: 100px;
  vertical-align: middle;
  appearance: none !important;
  -webkit-appearance: none !important;
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
}

:is(
  .markdown-preview-view,
  .markdown-rendered,
  .markdown-source-view.is-live-preview
)
progress[value].star5::-webkit-progress-bar {
  container: starprog5 / inline-size;
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%233A4A5C' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'/%3E%3C/svg%3E") !important;
  background-size: 20% 100% !important;
  background-repeat: repeat-x !important;
}

:is(
  .markdown-preview-view,
  .markdown-rendered,
  .markdown-source-view.is-live-preview
)
progress[value].star5::-webkit-progress-value {
  background-color: transparent !important;
  background-size: calc(100cqw / var(--total-number-of-stars)) 100% !important;
  background-repeat: repeat-x !important;
}

/* --- PALETTE: 5 ZONES --- */

/* 0 - Initial state: Vermilion (for 0.84 etc.) */
progress.star5[value^="0."]::-webkit-progress-value {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23FC3634' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'/%3E%3C/svg%3E") !important;
}

/* 1 - Bad: Vermilion (#FC3634) */
progress.star5[value^="1"]::-webkit-progress-value {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23FC3634' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'/%3E%3C/svg%3E") !important;
}

/* 2 - Poor: Burnt Sienna (#CC7859) */
progress.star5[value^="2"]::-webkit-progress-value {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23CC7859' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'/%3E%3C/svg%3E") !important;
}

/* 3 - Neutral: Gold (#FFD700) */
progress.star5[value^="3"]::-webkit-progress-value {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23FFD700' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'/%3E%3C/svg%3E") !important;
}

/* 4 - Good: Mint (#18BC9C) */
progress.star5[value^="4"]::-webkit-progress-value {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2318BC9C' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'/%3E%3C/svg%3E") !important;
}

/* 5 - Excellent: Mantis (#77C66B) */
progress.star5[value^="5"]::-webkit-progress-value,
progress.star5[value^="6"]::-webkit-progress-value,
progress.star5[value^="7"]::-webkit-progress-value,
progress.star5[value^="8"]::-webkit-progress-value,
progress.star5[value^="9"]::-webkit-progress-value,
progress.star5[value="100"]::-webkit-progress-value {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2377C66B' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'/%3E%3C/svg%3E") !important;
}

/* --- EXCEPTIONS BLOCK --- */

/* Active state: ensure transparent background behind colored stars */
progress.star5[value*="0."]::-webkit-progress-value,
progress.star5[value*="1"]::-webkit-progress-value,
progress.star5[value*="2"]::-webkit-progress-value,
progress.star5[value*="3"]::-webkit-progress-value,
progress.star5[value*="4"]::-webkit-progress-value,
progress.star5[value*="5"]::-webkit-progress-value,
progress.star5[value*="6"]::-webkit-progress-value,
progress.star5[value*="7"]::-webkit-progress-value,
progress.star5[value*="8"]::-webkit-progress-value,
progress.star5[value*="9"]::-webkit-progress-value {
  background-color: unset !important;
}
```
# Source
Adapted from a [progress bar CSS snippet](https://www.reddit.com/r/ObsidianMD/comments/1s6rfuy/my_progressbar_css_snippet) shared on the Obsidian subreddit. Modified with LeanProductivity brand colors and dark unfilled-star backgrounds.

# FAQ

> [!question]- Does this work in Live Preview mode?
> Yes. The CSS targets `.markdown-source-view.is-live-preview`, `.markdown-preview-view`, and `.markdown-rendered`, so stars render in both Live Preview and Reading mode.

> [!question]- Can I use half-star ratings like 3.5?
> Yes. Set `value="3.5"` on the progress element. The filled portion scales proportionally, giving you a visual half-star.

> [!question]- How do I drive the rating from a frontmatter property?
> Add a `rating` property to your frontmatter, then use a Meta Bind `VIEW` expression to render the progress bar with the property value. See the Usage section above for the exact syntax.

> [!question]- Can I customize the colors?
> Yes. Each color zone is a separate CSS rule. Replace the hex color in the SVG `stroke` attribute for the zone you want to change. The five zones are defined in the Palette section of the code.
