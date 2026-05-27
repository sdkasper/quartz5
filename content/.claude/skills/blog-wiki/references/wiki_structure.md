# Wiki Post Template — Annotated Examples

This reference shows the exact template and section-by-section breakdowns of canonical wiki posts. Load this when writing a new wiki post or restructuring an existing one.

## Verbatim Template

```markdown
---
title:
aliases:
author:
  - Sascha D. Kasper
source:
description:
cover:
date: YYYY-MM-DD
draft: true
categories:
cssclasses:
tags:
  - wiki
created:
updated:
---
# Setup
-

# Result

# Code
` ` `
` ` `
```

## CSS Snippet Installation Boilerplate

Most CSS wiki posts start Setup with this standard paragraph. Copy it verbatim for new CSS posts:

```markdown
# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `FILENAME.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable this one, and that should do it. If it does not, you may have to restart Obsidian.
```

Replace `FILENAME` with a sensible name for the snippet. This boilerplate is reused across all CSS wiki posts.

## Example 1: CSS Post — "CSS - Syntax Highlighting"

**Simple pattern: Setup + Result + Code + Source**

### Frontmatter

```yaml
title: CSS - Syntax Highlighting           # PREFIX - Name
categories:
  - obsidian                                # always first
  - CSS                                     # code type
tags:
  - wiki                                    # always wiki, never blog
```

### Sections

```markdown
# Setup
[CSS snippet installation boilerplate — see above]

# Result
This snippet lets you customize the colors of elements in your code blocks.

# Code
` ` `css
body {
    --code-background: #000000;
    --code-normal: #dbdbdb;
    --code-comment: #4c7aac;
    ...
}
` ` `

# Source
I found this on [Reddit](url), posted by user [pillowpotion](url).
```

**Pattern**: Setup has the standard CSS boilerplate. Result is one sentence. Code has a single `css` fenced block. Source gives attribution.

## Example 2: DVJS Post — "DVJS - Countdowns"

**Multiple code variants with H2 subsections, no Setup section**

### Frontmatter

```yaml
title: DVJS - Countdowns
categories:
  - obsidian
  - dataview                                # DVJS uses "dataview" category
tags:
  - wiki
```

### Sections

```markdown
# Code
Don't forget to start and end the code block with three backticks.

## Countdown to the same date every year (e.g. anniversary)
` ` `text
dataviewjs
const now = new Date();
const ax = new Date(now.getFullYear(), 11, 12);
...
` ` `

## Countdown to Christmas
` ` `text
dataviewjs
...
` ` `

## Countdown to fixed date
` ` `text
dataviewjs
...
` ` `

# Result
![[DVJS - Countdowns-20241205133948464.webp]]
```

**Why `text` not `dataviewjs`**: Using `dataviewjs` as the fence language would cause Obsidian to try to execute the code in reading mode. Using `text` with `dataviewjs` on the first line inside the block shows the intent without auto-execution.

**Pattern**: Code comes first (it's the main content). H2 subsections separate variants. Result is just a screenshot. No Setup needed — DataviewJS is self-explanatory for the audience.

## Example 3: BASES Post — "BASES - Absolute Progress Bars"

**Multi-step setup with H2 code subsections**

### Frontmatter

```yaml
title: BASES - Absolute Progress Bars
cover: /zAttachments/BASES - Absolute Progress Bars.webp  # cover image for wiki cards
categories:
  - obsidian
  - bases
tags:
  - wiki
```

### Sections

```markdown
# Setup
- You need two numeric properties (e.g. `estimatedEffort` and `currentEffort`) in your notes
- In your base, click on **Properties**, **Add Formula**, and give it a name (e.g. `fProgressPct`)
    - Copy/paste the first code snippet from below
- Create another property (e.g., `fProgressTxt`)
    - Copy/paste the second code snippet from below
- Create another property (e.g., `fProgressBar`)
    - Copy/paste the third code snippet from below
- You can replace the icons in the formula with whatever you prefer

# Result
You get a view like this:
![[zAttachments/BASES - Absolute Progress Bars.webp]]

# Code
## Snippet 1 - `fProgressPct`
` ` `
progress / 100
` ` `
## Snippet 2 - `fProgressTxt`
` ` `
if(formula.fProgressPct> 0, (formula.fProgressPct * 100).round(), "0") + " %"
` ` `
## Snippet 3 - `fProgressBar`
` ` `
if(formula.fProgressPct * 10 > 0, "▰".repeat(...))...
` ` `
```

**Pattern**: Setup uses bullet list with nested steps referencing numbered code snippets. Result shows a screenshot. Code uses H2 subsections with descriptive names matching the Setup steps. Bases formulas use no language tag on the fence.

## Example 4: CSS Post with Callout — "CSS - Columns Layout"

**Setup includes a callout for application instructions**

```markdown
# Setup
[CSS snippet installation boilerplate]

> [!attention] Apply CSS to note
> To apply the respective style to a note, the note's frontmatter must include `cssclasses: columns2` or `cssclasses: columns3`.

# Result
## Two Columns
![[CSS - Columns Layout-20241109211455449.webp]]
## Three Columns
![[CSS - Columns Layout-20241109211520481.webp]]

# Code
` ` `css
/* Two-column layout for Obsidian notes with "columns2" cssclass */
.markdown-preview-view.columns2 .markdown-preview-section {
    column-count: 2;
    ...
}
` ` `

# Source
User "Kapirklaa" on the [Obsidian Discord Server](url)...
```

**Pattern**: Callouts in wiki posts are NOT float-right (unlike blog posts). They appear inline to highlight important prerequisites or warnings. Result uses H2 subsections for multiple screenshots.

## Section Order Flexibility

The template says Setup → Result → Code, but real wiki posts vary:

| When to reorder | Preferred order | Why |
|-----------------|-----------------|-----|
| Code is the star (most DVJS/DV) | Code → Result | Readers want the code first, screenshot confirms it works |
| Setup is critical (CSS, Bases) | Setup → Result → Code | Readers need context before the code makes sense |
| Code needs no setup (simple DV) | Code → Result (skip Setup) | No prerequisites to explain |

All three sections should be present when applicable, but omitting Setup is acceptable when the code is truly self-explanatory.

## Code Fence Language Tags

| Code type | Fence language | Why |
|-----------|---------------|-----|
| CSS | `css` | Syntax highlighting, no execution risk |
| Dataview (DQL) | `text` | Prevents Obsidian from executing; `dataview` fence would auto-run |
| DataviewJS | `text` | Same reason; put `dataviewjs` as first line inside block |
| Bases formulas | (none) | No standard language tag; Bases expressions aren't a fenced language |
| Templater | `text` | Prevents Templater from processing the code block |
| Tasks queries | `text` | Same pattern — `text` fence with `tasks` as context inside |
