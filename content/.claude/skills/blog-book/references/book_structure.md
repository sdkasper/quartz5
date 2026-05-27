# Book Review Template — Annotated Example

This reference shows the exact template and a section-by-section breakdown of the canonical example post. Load this when writing a new book review or restructuring an existing one.

## Verbatim Template

```markdown
---
title: {Book Title} - Review
aliases:
author:
  - Sascha D. Kasper
source:
description:
cover:
date: YYYY-MM-DD
draft: true
categories:
  - blog
  - books
cssclasses:
tags:
  - blog
created:
updated:
---

# Summary

> [!success|float-r] Rating
> ★★★★★
> 5 out of 5

Summary paragraph describing the book's thesis...

Optional second paragraph with overall impression.

# Main Takeaways

1. First key point.
2. Second key point.
3. Third key point.

## First Takeaway Title

> [!quote|float-r]
> Short quote from
> the book that fits
> within 30 chars.
> — Author Name

Explanation paragraph...

[Buy the book on Amazon](URL) or – if you prefer listening – [get the audiobook](URL).

## Second Takeaway Title

> [!important|float-r]
> Key insight distilled
> to a short phrase.

Explanation paragraph...

## Third Takeaway Title

> [!question|float-r]
> A thought-provoking
> question related
> to this takeaway?

Explanation paragraph...

# Practical Lessons

1. First practical lesson.
2. Second practical lesson.
3. Third practical lesson.

# My Top 3 Quotes

> First quote text here.
> — Author Name, "Book Title"

> Second quote text here.
> — Author Name

> Third quote text here.
> — Author Name
```

## Annotated Example: "Range by David Epstein - Review"

### Frontmatter

```yaml
title: Range by David Epstein - Review
aliases:                          # empty — no alt slugs needed
author:
  - Sascha D. Kasper              # always this value
source: https://sascha-kasper.com/range-by-david-epstein-review/
description: My main learnings, practical lessons, favorite quotes, and summary of "Range" by David Epstein.
cover:                            # empty — no cover image
date: 2023-02-02                  # YYYY-MM-DD
draft: false                      # false = live on site
categories:
  - books                         # always include "books" for book reviews
cssclasses:                       # empty — no special CSS
tags:
  - blog                          # always include "blog"
created: 2023-02-02T00:00         # ISO timestamp, no timezone
updated: 2026-03-08T18:36:45+02:00  # ISO with timezone
```

**Title pattern**: Always `{Book Title} - Review` or `{Book Title} by {Author} - Review`. The title IS the filename.

**Category pattern**: `books` is always included. Do NOT add `blog` as a category. No additional categories needed for book reviews.

### Section 1: `# Summary`

```markdown
# Summary

> [!success|float-r] Rating
> ★★★★★                        ← two trailing spaces after stars
> 5 out of 5

In "Range", David Epstein debunks the myth that early specialization
and deliberate practice are the keys to success. Instead, he argues
that generalists, who have a diverse range of experiences and
cross-disciplinary knowledge, are better equipped to succeed in
today's rapidly changing world.

This book is a must-read for anyone looking to thrive in an uncertain
future and offers practical lessons for individuals, educators, and
society as a whole.
```

**Why it works**: The rating callout gives the reader an instant signal. The two paragraphs cover what the book argues (thesis) and who should read it (recommendation). No fluff, no "I recently read..." boilerplate.

**Rating callout formatting**: The `★★★★★` line MUST end with two trailing spaces to create a line break before "5 out of 5". Use `★` for filled stars and `☆` for empty stars.

### Section 2: `# Main Takeaways`

```markdown
# Main Takeaways

1. Generalists, not specialists, are better equipped to succeed
   in today's rapidly changing world.
2. Deliberate practice and early specialization are overrated.
3. A diversity of experiences and cross-disciplinary knowledge is
   crucial to problem-solving and innovation.

## Generalists Outperform Specialists

> [!quote|float-r]
> In most fields,            ← two trailing spaces
> generalists, not           ← two trailing spaces
> specialists, are primed    ← two trailing spaces
> to succeed.                ← two trailing spaces
> — David Epstein

Generalists, who have a broad range of experiences and
cross-disciplinary knowledge, are better equipped to succeed in
novel and rapidly changing fields...

[Buy the book on Amazon](URL) or – if you prefer listening –
[get the audiobook](URL).

## The Need for a Revised Education System

> [!important|float-r]
> A diversity of experiences
> and cross-disciplinary
> knowledge is key to
> problem-solving and
> innovation.

The education system should be revised to encourage a broad range
of studies and experiences...

## The Limitations of Deliberate Practice

> [!question|float-r]
> Is deliberate practice
> really the path to mastery
> in every field?

Contrary to popular belief, deliberate practice is only necessary
for highly specialized and predictable fields...
```

**Pattern**: Numbered overview list → H2 subsections expanding each point. Each H2 gets a different callout type: `quote` → `important` → `question`. Amazon link goes after the FIRST subsection's body text. If there are more than 3 subsections, continue rotating the callout types.

**Callout line length**: Every line after `> ` must be ≤30 characters. Count the text AFTER the `> ` prefix. Break longer text across multiple lines.

**Trailing spaces**: Every non-final line in a callout must end with exactly two spaces (`  `) to trigger a line break on the website. The LAST line of each callout does NOT need trailing spaces.

### Section 3: `# Practical Lessons`

```markdown
# Practical Lessons

1. Pursue a diverse range of experiences and subjects.
2. Don't be afraid to switch careers or try new things.
3. Encourage the people around you to do the same.
```

**Pattern**: Simple numbered list, 2-4 items. An optional prose intro is acceptable but keep it to one sentence. These are actionable lessons the reader can apply, not summaries of the book.

### Section 4: `# My Top 3 Quotes`

```markdown
# My Top 3 Quotes

> In most fields, generalists, not specialists, are primed to succeed.  ← two trailing spaces
> — David Epstein, "Range"

> The reason generalists do so well is that they are the ones best  ← two trailing spaces
> equipped to handle the unexpected.  ← two trailing spaces
> — David Epstein, "Range"

> It is not just what we know but what we don't know that matters.  ← two trailing spaces
> — David Epstein, "Range"
```

**Pattern**: Three blockquotes separated by blank lines. Attribution on a new line starting with `> — `. The book title in the attribution is optional but preferred.

**Note**: These quotes are NOT inside float-right callouts, so the 30-character limit does not apply here. They are full-width blockquotes. However, every non-final line in a blockquote still needs two trailing spaces for line breaks.

**Trailing spaces in blockquotes**: Even in full-width blockquotes, every non-final line must end with two trailing spaces (`  `) to trigger a line break. Without them, `> line one` and `> line two` render as a single paragraph.

**Correct:**
```
> In most fields, generalists, not specialists, are primed to succeed.
> — David Epstein, "Range"
```
(Both the quote line and the attribution line would be separate visible lines because the quote line ends with `  `.)

**Wrong:**
```
> In most fields, generalists, not specialists, are primed to succeed.
> — David Epstein, "Range"
```
(Without trailing spaces, these run together as one paragraph.)

## Callout Formatting Examples

**Correct float-right callout** (≤30 chars per line, trailing two spaces on non-final lines):
```
> [!quote|float-r]
> In most fields,
> generalists, not
> specialists, are primed
> to succeed.
> — David Epstein
```

**Wrong** (single long line, will overflow the float-right box):
```
> [!quote|float-r]
> In most fields, generalists, not specialists, are primed to succeed.
> — David Epstein
```

**Counting characters**: Count text AFTER the `> ` prefix. `> In most fields,` = 16 chars. `> generalists, not` = 17 chars. Both are under 30.

**Special characters**: Em dashes (`—`), star characters (`★`), and other multi-byte characters count as 1 character for the 30-char limit but may render wider. Be conservative with lines containing these characters.

## Second Example: "A Guide to the Good Life - Review"

This example shows a 4-star rating and a review with more subsections under Main Takeaways.

```markdown
# Summary

> [!success|float-r] Rating
> ★★★★☆
> 4 out of 5

"A guide to the good life" attempts to apply Stoical ideals and ideas
to modern life...

# Main Takeaways

## Why Stoicism?
> [!quote|float-r]
> A life filled with
> negative emotions will
> not be a good life.
> -- Stoics everywhere

...

[Buy the book on Amazon](URL) or – if you prefer listening –
[get the audiobook](URL).

## Trichotomy of Control

> [!important|float-r] There are things over
> which we have
> * complete control,
> * no control at all, and
> * some but not full control.

...
```

**Key differences**: No numbered list before the subsections (acceptable when the takeaways don't lend themselves to a numbered overview). The `[!important|float-r]` callout uses a title and bullet list inside the callout — both are valid patterns. The `--` attribution style (instead of `—`) is acceptable but prefer the em dash `—`.

## Common Restructuring Patterns

When converting old-format book reviews to the new template:

| Old Format | New Format |
|---|---|
| Intro boilerplate ("I recently read...", bullet list, "As always...") | **Remove entirely** |
| `My rating: ★★★★★` inline text | `# Summary` with `> [!success\|float-r] Rating` callout |
| Old `# Summary` near bottom | **Move content up** as paragraph under `# Summary` |
| `## Key message/finding` | `# Main Takeaways` |
| `### Subsection` under Key message | `## Subsection` (promote one level) + add float-right callout |
| Amazon link placed mid-content | Move to **after first takeaway subsection** |
| `# Top 3 Quotes` with bare text | `# My Top 3 Quotes` with `> quote\n> — Author` blockquotes |
| Old `# Summary` section | **Delete** (content already moved to top) |
| Broken URLs (`ttps://` etc.) | Fix to `https://` |
| Split link blocks across lines | Consolidate to single line |
