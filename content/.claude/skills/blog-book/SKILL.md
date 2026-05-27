---
name: blog-book
description: Write new or restructure existing book review posts for the LeanProductivity Quartz blog. Follows the book review template with Summary/Rating callout, Main Takeaways with float-right callouts, Practical Lessons, and My Top 3 Quotes. This skill should be used when creating, updating, or restructuring book review Markdown posts in `$PROJECTS_PATH\quartz-blog\content\`. Trigger on "book review", "book post", or posts with `- books` category.
---

# Blog Book

Three modes: **New review**, **Restructure**, **Review**.

## Success Criteria

Before presenting output, verify all criteria are met. If not, iterate until they are.

- [ ] Frontmatter has all required fields, `author` is `- Sascha D. Kasper`, `categories` includes `books` (not `blog`), `tags` includes `- blog`
- [ ] Title follows `{Book Title} - Review` convention
- [ ] First section is `# Summary` with `[!success|float-r] Rating` callout containing star rating + "N out of 5"
- [ ] Has `# Main Takeaways` with numbered list + `##` subsections, each with a float-right callout
- [ ] Float-right callout lines are ≤30 characters each and all non-final lines end with two trailing spaces (`  `) for line breaks
- [ ] Amazon link appears after first takeaway subsection
- [ ] Has `# Practical Lessons` with numbered list
- [ ] Has `# My Top 3 Quotes` with proper blockquote format; non-final lines end with two trailing spaces
- [ ] No "we"/"our" language — only "you"/"your" or third person
- [ ] No invented URLs — all links are real or marked `[PLACEHOLDER](URL)`

## Expert Thinking

Before any mode, answer these questions:

- **What's the core thesis?** The `# Summary` must convey the book's central argument in 1-2 paragraphs. If the reader stops here, what must they take away?
- **What are the 2-4 key takeaways?** These become the numbered list and `##` subsections under `# Main Takeaways`. Each subsection gets a float-right callout with a relevant quote or insight.
- **What's the rating?** 1-5 stars using `★` (filled) and `☆` (empty). The rating callout goes inside `# Summary`.

## Judgment Calls

When restructuring or writing, apply these expert decisions:

- **Picking callout quotes**: Choose the quote that best captures the subsection's argument, not just the most famous line. If no perfect quote exists for a subsection, use an `[!important]` or `[!question]` callout with an original insight distilled from the text instead.
- **Summary writing vs. moving**: In restructure mode, the old summary text can be moved as-is if it's well-written. If the old summary is weak or generic, rewrite it to convey the book's core thesis clearly — but flag this change to the user.
- **Takeaway titles**: Rename vague subsection titles ("Key Finding #1") to descriptive ones ("Generalists Outperform Specialists"). The title should communicate the takeaway without reading the body.
- **Books with fewer than 3 takeaways**: Use as many subsections as the content supports (minimum 2). Do not pad with weak takeaways. The numbered list should match the number of subsections.
- **Missing quotes**: If the user doesn't provide quotes, ask for them. Do not invent quotes or attribute made-up text to authors.

## Section Structure

Book reviews follow a fixed 4-section structure (all H1), with H2 subsections inside Main Takeaways. See `references/book_structure.md` for annotated examples.

| Section | Contains | Notes |
|---------|----------|-------|
| `# Summary` | Rating callout + 1-2 paragraphs | Rating: `[!success\|float-r]` with stars + "N out of 5" |
| `# Main Takeaways` | Numbered list + `##` subsections | Each `##` gets a float-right callout; Amazon link after first `##` |
| `# Practical Lessons` | Numbered list (2-4 items) | Actionable lessons, not book summaries |
| `# My Top 3 Quotes` | Three `>` blockquotes with `> — Author` | Full-width blockquotes, NOT float-right callouts |

**Callout rotation** across `##` subsections:
1. `[!quote|float-r]` — a relevant quote from the book
2. `[!important|float-r]` — a key insight distilled to a phrase
3. `[!question|float-r]` — a thought-provoking question
4. If more than 3 subsections, continue rotating from `[!quote|float-r]`

**Amazon link placement**: After the first `##` subsection's body text, before the second `##`. Format: `[Buy the book on Amazon](URL) or – if you prefer listening – [get the audiobook](URL).`

## Line Break Rules

**This applies everywhere inside `>` blocks** — both float-right callouts AND blockquotes in "My Top 3 Quotes".

**Trailing spaces**: Every non-final line inside a `>` block must end with two trailing spaces (`  `) to trigger a visible line break on the website. Without them, consecutive `>` lines render as a single wrapped paragraph.

**Float-right callout line length**: Every line inside a float-right callout must be ≤30 characters (after the `> ` prefix). If the text is longer, insert manual line breaks. This limit does NOT apply to full-width blockquotes in "My Top 3 Quotes".

## Writing Style

- **Second person or third person** — "you"/"your" or factual descriptions, never "we"/"our" (solo creator brand)
- **Conversational-professional tone** — approachable but knowledgeable
- **Short paragraphs** — 2-4 sentences max
- **Bold key terms** on first mention where helpful

## NEVER Do

- Use H3 (`###`) or deeper — book reviews use only H1 and H2
- Skip `# Summary` or `# My Top 3 Quotes` — both are mandatory sections
- Use "we" or "our" — solo brand, always second person or third person
- Leave frontmatter fields undefined — use empty value if unknown
- Invent URLs — ask the user or write `[PLACEHOLDER](URL)`
- Invent or fabricate quotes — ask the user for real quotes from the book
- Put the Amazon link at the bottom or in a random spot — it goes after the first takeaway subsection
- Write callout lines longer than 30 characters — break them manually
- Forget trailing two spaces on non-final lines inside ANY `>` block (callouts AND blockquotes)
- Use bare text for quotes in "My Top 3 Quotes" — always use `>` blockquote syntax
- Include intro boilerplate like "I recently read..." or bullet lists of what the post contains
- Add content the user did not provide or approve (in restructure mode)

## Workflow

### New Review

1. Ask for: book title, author, rating (1-5), key takeaways, favorite quotes, Amazon link(s)
2. **MANDATORY** — Read `references/book_structure.md` for the annotated example
3. Generate frontmatter from `assets/frontmatter_template.md` — set `draft: true`, fill title as `{Book Title} - Review`, category `books` (do NOT include `blog` as a category), description as a Google snippet (120-160 chars). Set `source` to the old WordPress URL if known, otherwise leave empty.
4. Write `# Summary` with rating callout + 1-2 paragraphs
5. Write `# Main Takeaways` with numbered list + `##` subsections with rotating float-right callouts
6. Place Amazon link after first subsection
7. Write `# Practical Lessons` numbered list
8. Write `# My Top 3 Quotes` with blockquote formatting
9. Verify all `>` block lines have trailing two spaces on non-final lines; verify callout lines ≤30 chars
10. Save to `$PROJECTS_PATH\quartz-blog\content\{Book Title} - Review.md`

**Do NOT load** `references/book_structure.md` if only asked for a title or outline.

### Restructure

1. Read the existing post
2. **MANDATORY** — Read `references/book_structure.md` for the annotated example
3. Identify structural deviations from the book review template
4. Common restructuring tasks:
   - Remove intro boilerplate ("I recently read...", bullet lists, "As always...")
   - Move inline rating to `[!success|float-r] Rating` callout inside `# Summary`
   - Move old `# Summary` content to the new `# Summary` position (top of post)
   - Rename `## Key message/finding` → `# Main Takeaways`
   - Promote `###` subsections → `##` and add float-right callouts
   - Rename vague subsection titles to descriptive ones (flag rewordings to the user)
   - Move Amazon link to after first takeaway subsection
   - Fix broken URLs (e.g., `ttps://` → `https://`)
   - Consolidate split link blocks into single lines
   - Rename `# Top 3 Quotes` → `# My Top 3 Quotes` and format as blockquotes
   - Delete the old `# Summary` section after moving its content
5. Fix frontmatter: add `updated` field, normalize formats
6. Verify all `>` block lines have trailing two spaces on non-final lines; verify callout lines ≤30 chars
7. Present a summary of structural changes made

**Do NOT load** `references/book_structure.md` for minor frontmatter-only fixes.

### Review

Use the checklist below. Only load `references/book_structure.md` if verifying a specific pattern.

**Must fix:**
- [ ] Title follows `{Book Title} - Review` convention
- [ ] First section is `# Summary` with `[!success|float-r] Rating` callout
- [ ] Rating callout has stars + "N out of 5" on separate lines with trailing two spaces on the stars line
- [ ] Has `# Main Takeaways` with numbered list + `##` subsections
- [ ] Each `##` subsection has a float-right callout (rotating types: quote/important/question)
- [ ] All float-right callout lines ≤30 characters with trailing two spaces on non-final lines
- [ ] All blockquote lines in "My Top 3 Quotes" have trailing two spaces on non-final lines
- [ ] Amazon link appears after first takeaway subsection
- [ ] Has `# Practical Lessons`
- [ ] Has `# My Top 3 Quotes` with `>` blockquote syntax and `> — Author` attribution
- [ ] Frontmatter has required fields (`title`, `author`, `description`, `date`, `draft`, `categories`, `tags`, `created`, `updated`)
- [ ] `categories` includes `books` (not `blog`)
- [ ] `tags` includes `- blog`
- [ ] No H3+ headings
- [ ] No "we"/"our" language

**Should fix:**
- [ ] Summary has 1-2 paragraphs after the rating callout
- [ ] Numbered takeaway list has 2-4 items
- [ ] 2-3 subsections under Main Takeaways
- [ ] Subsection titles are descriptive (not "Key Finding #1")
- [ ] No intro boilerplate
- [ ] No invented URLs or quotes

**Nice to have:**
- [ ] `description` is 120-160 characters
- [ ] Paragraphs are 2-4 sentences
- [ ] Practical Lessons has 2-4 items

Report deviations grouped by severity.

## Self-Verification

Before presenting output, verify all success criteria are met. If not, iterate until they are.
- [ ] All images have descriptive alt text (`/alt-text`)
