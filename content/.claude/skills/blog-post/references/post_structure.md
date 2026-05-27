# Blog Post Template — Annotated Example

This reference shows the exact template and a section-by-section breakdown of the canonical example post. Load this when writing a new post or restructuring an existing one.

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
  - blog
created:
updated:
---
# In a Nutshell
> [!important|float-r] Title
> Content
> with some text
> or an image

First paragraph: summary of the post.

# Heading 1
Content paragraph.
## Heading 2
Content paragraph.
```

## Annotated Example: "Guide to the Obsidian Web Clipper"

### Frontmatter

```yaml
title: Guide to the Obsidian Web Clipper
aliases:                          # empty — no alt slugs needed
author:
  - Sascha D. Kasper              # always this value
source: https://sascha-kasper.com/step-by-step-guide-to-the-obsidian-web-clipper/
description: Discover how to effectively use the Obsidian Web Clipper...  # ~150 chars
cover:                            # empty — no cover image
date: 2024-11-11                  # YYYY-MM-DD, past = published
draft: false                      # false = live on site
categories:
  - obsidian                      # primary topic
  - clipper                       # specific subtopic
cssclasses:                       # empty — no special CSS
tags:
  - blog                          # always include "blog"
created: 2024-11-11T00:00         # ISO timestamp, no timezone
updated: 2026-03-07T16:28:05+02:00  # ISO with timezone
```

**Category selection pattern**: Start with the tool/platform name (e.g., `obsidian`), then add the specific feature (e.g., `clipper`, `plugins`). Do NOT include `blog` as a category. Keep to 2-3 categories — they drive the CategoryNav sidebar.

### Section 1: `# In a Nutshell`

```markdown
# In a Nutshell

> [!important|float-r] Useful / Download
> * Tutorial: [YouTube](https://youtu.be/oEtSLrfEj5o)
> * Download: [Browser Extension](https://obsidian.md/clipper#more-browsers)
> * Download: [FREE Lean Starter Vault](https://kpr.me/lsv)
> * Wiki: [Lean Starter Vault](https://kspr.me/lsvwiki)
> * [More Obsidian Video Tutorials](playlist-url)
> * [Discord](https://discord.gg/sbMg6PP2vq)

The Obsidian Web Clipper is a browser extension that saves web content
directly into your vault. It supports custom templates, text highlighting,
and multiple vaults — so you can capture articles, videos, and research
without leaving your browser. This guide walks you through installation,
configuration, and everyday use.
```

**Why it works**: The callout gathers ALL resource links in one place (video, download, community). The summary answers the search intent in 3 sentences: what it is, what it does, what this post covers.

### Section 2: `# What You Get` (feature overview H1)

```markdown
# What You Get
When you install the Obsidian Web Clipper, you unlock a suite of features...

* **Quick Clipping:** Capture web pages or selected text instantly.
* **Custom Templates:** Create templates that suit your unique clipping needs.
* **Multiple Vault Support:** Work with different vaults...
```

**Pattern**: Intro paragraph + bulleted feature list. Each bullet: **Bold term:** followed by description. This section sets expectations before the how-to.

### Section 3: `# Step-by-Step Guide` (parent H1 + H2 steps)

```markdown
# Step-by-Step Guide

## Step 1: Installation
Installing the Obsidian Web Clipper is a straightforward process...
1. Open your preferred browser...
2. Click on the option to add the extension...

## Step 5: Custom Templates
...
> [!file|float-r] Links
> * [GitHub - Kepano's Clipper Template Repository](url)
> * [GitHub - Community collection](url)

## Step 6: Common Use Cases
* **Highlighting Important Text:** Use the highlighter mode...
```

**Pattern**: One H1 groups multiple H2 steps. Steps use numbered lists for procedures, bullets for options. The `[!file|float-r]` callout appears mid-section — placed BEFORE the paragraph that references it so the float renders alongside the right content.

### Section 4: `# FAQ`

```markdown
# FAQ

> [!file|float-r] Value your time?
> Download the templates for free.
> - [Take me there!](url)
> - [See it in action first!](url)

> [!question]- What is the Obsidian Web Clipper?
> The Obsidian Web Clipper is a browser extension that allows users to clip
> web content directly into their Obsidian vault...

> [!question]- Do I need a specific version of Obsidian to use the Web Clipper?
> Yes, you need to be on Obsidian version 1.7.2 or higher...
```

**Pattern**: Optional CTA callout at top. Each Q&A is a foldable `[!question]-` callout - question text is the callout title, answer is the callout body. 3-5 Q&A pairs is ideal.

## Callout Syntax Reference

YouTube embed:
```markdown
> [!scene|video-r] Tutorial
> ![](https://www.youtube.com/watch?v=VIDEO_ID)
```

Image embed:
```markdown
> [!image|float-r] Description
> ![[filename.png]]
```

Link list:
```markdown
> [!file|float-r] Links
> * [Link text](url)
> * [Link text](url)
```
