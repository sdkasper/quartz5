---
name: blog-post
description: Write new or restructure existing blog posts for the LeanProductivity Quartz blog. Follows the TPL - Blog Content template: H1 sections, H2 subsections, "In a Nutshell" opener with float-right callout, standardized frontmatter. Use when creating, updating, or restructuring Markdown posts in `$VAULT_PATH\09 Blog\`.
---

# Blog Post

Three modes: **New post**, **Restructure**, **Review**.

## Success Criteria

Before presenting output, verify all criteria are met. If not, iterate until they are.

- [ ] Frontmatter has all required fields, `author` is `- Sascha D. Kasper`, `tags` includes `- blog`
- [ ] First section is `# In a Nutshell` with `[!important|float-r]` callout + 1-3 summary paragraphs
- [ ] No H4 (`####`) or deeper headings (H1/H2/H3 are all allowed)
- [ ] No "we"/"our" language — only "you"/"your"
- [ ] No invented URLs — all links are real or marked `[PLACEHOLDER](URL)`
- [ ] Callouts use `> *` list syntax, not `> -`

## Obsidian Markdown — MANDATORY

All blog posts live in the Obsidian vault. Before writing or editing any post, load and follow `/obsidian-markdown` rules. Key constraints:

- No blank line before headings (content immediately precedes the `#` line)
- No double blank lines anywhere
- No horizontal rules in content
- Callout lists use `> *` not `> -`
- Internal vault references use `[[wikilinks]]`, not standard Markdown links
- Tags belong in frontmatter, not inline

## Expert Thinking

Before any mode, answer these questions:

- **What's the ONE thing?** If the reader leaves after "In a Nutshell", what must they take away? That answer shapes the summary paragraphs and the float-right resource callout.
- **What resources exist?** Gather YouTube links, download URLs, related posts BEFORE writing. The `[!important|float-r]` callout in "In a Nutshell" is the resource hub — don't scatter links through prose when they belong there.
- **What's the search intent?** The description (120-160 chars) and the "In a Nutshell" summary must answer the query that brought someone here. Write the description as if it's the Google snippet.

## Structure Rules

- `#` (H1) for major sections, `##` (H2) for subsections, `###` (H3) for further detail when needed — **never H4 or deeper**
- First section is always `# In a Nutshell` with a `[!important|float-r]` callout
- Last section may be `# FAQ` - each Q&A is a foldable `[!question]-` callout: `> [!question]- Question text` with answer on the next `>` line
- Callouts always float right. Use `> * item` for lists inside callouts (not `> -`; the CSS targets `*` for correct spacing)

## Callout Decision

| You want to show... | Use |
|---------------------|-----|
| Key resources, downloads, tutorials | `> [!important\|float-r]` |
| GitHub repos, file links | `> [!file\|float-r]` |
| Embedded YouTube video | `> [!scene\|video-r]` |
| Screenshot or image | `> [!image\|float-r]` |

Place callouts BEFORE the paragraph that references them — the float-right renders alongside the following content. Max 1 callout per H1/H2 section to avoid layout collisions on mobile.

## Writing Style

- **Second person** — "you"/"your", never "we"/"our" (solo creator brand)
- **Conversational-professional tone** — approachable but knowledgeable
- **Short paragraphs** — 2-4 sentences max
- **Bold key terms** on first mention, `==highlight==` sparingly for critical values
- **Action-oriented headings** — "Step 1: Install the Extension" not "About Installation"

## NEVER Do

- Use H4 (`####`) or deeper — H1/H2/H3 are fine, but H4+ renders poorly on the blog
- Skip "In a Nutshell" — it's the mandatory first section, maps to the blog's content preview
- Use "we" or "our" — solo brand, always second person
- Leave frontmatter fields undefined — use empty value if unknown (Quartz crashes on missing `date`)
- Set `draft: true` without telling the user
- Invent URLs — ask the user or write `[PLACEHOLDER](URL)`
- Use `> -` in callouts — use `> *` (CSS spacing depends on it)
- Put a callout at the start of a post before the first H1 (it renders outside the content container)
- Change existing content meaning during restructure — only reformat structure
- Add content the user didn't provide or approve (in restructure mode)

## Workflow

### New Post

1. Ask for: topic, key points or outline, any URLs/resources to include
2. **MANDATORY** — Read `references/post_structure.md` for the annotated example
3. Generate frontmatter from `assets/frontmatter_template.md` — set `draft: true`, fill title/description/categories/tags. Do NOT include `blog` as a category (it belongs in tags only). Write the `description` as a Google snippet: what + who it's for + benefit, 120-160 chars.
4. Write `# In a Nutshell`: gather ALL resource links into the float-right callout first, then write 1-3 summary paragraphs answering the search intent
5. Plan section structure — decide how many H1 sections and whether they need H2 subsections:
   - Tutorial/guide topics: one parent H1 ("Step-by-Step Guide") with H2 steps
   - Concept/opinion topics: multiple H1 sections, each self-contained
   - Avoid more than 6 H1 sections — if you need more, consolidate with H2 subsections
6. Write content sections with H1/H2 hierarchy
7. Add `# FAQ` if the topic has common questions (3-5 Q&A pairs is ideal)
8. Save to `$VAULT_PATH\09 Blog\{title}.md`

**Do NOT load** `references/post_structure.md` if you're only being asked for a title or outline — the reference is for full post writing.

### Restructure

1. Read the existing post
2. **MANDATORY** — Read `references/post_structure.md` for the annotated example
3. Identify structural deviations (heading levels, missing sections, callout formatting)
4. Handle heading demotion decisions:
   - Existing H3 under an H2 → keep as H3 if it adds useful structure, otherwise promote to H2
   - Existing H4+ → promote to H3, or fold into prose/bullets if too granular
5. If no "In a Nutshell" exists, synthesize one from the post's introduction or first paragraph — don't invent new content, repurpose what's there
6. Fix frontmatter: add missing fields, normalize formats (see `assets/frontmatter_template.md`)
7. Present a summary of structural changes made

**Do NOT load** `references/post_structure.md` for minor frontmatter-only fixes.

### Review

Use the checklist below. Only load `references/post_structure.md` if you need to verify a specific pattern against the annotated example.

**Must fix:**
- [ ] First section is `# In a Nutshell` with `[!important|float-r]` callout
- [ ] No H4 (`####`) or deeper headings anywhere (H3 is allowed)
- [ ] Frontmatter has all required fields (`title`, `author`, `description`, `date`, `draft`, `categories`, `tags`, `created`, `updated`)
- [ ] `author` is `- Sascha D. Kasper`
- [ ] `tags` includes `- blog`
- [ ] `date` is `YYYY-MM-DD` format
- [ ] No "we"/"our" language

**Should fix:**
- [ ] "In a Nutshell" has 1-3 summary paragraphs after the callout
- [ ] Callouts use correct type and `> *` list syntax
- [ ] All major sections use H1, subsections use H2
- [ ] FAQ uses `> [!question]-` foldable callouts (if FAQ exists)
- [ ] No invented URLs

**Nice to have:**
- [ ] `description` is 120-160 characters
- [ ] Paragraphs are 2-4 sentences
- [ ] Bold key terms on first mention
- [ ] Max 1 callout per section

Report deviations grouped by severity.

## Self-Verification

Before presenting output, verify:
- [ ] All images have descriptive alt text (`/alt-text`)

## Cross-References

- `/obsidian-markdown` — Obsidian-flavored Markdown rules (whitespace, wikilinks, callouts)
- `/obsidian-yaml-frontmatter` — Frontmatter property standards
- `/alt-text` — Image alt text auditing, creation, and review
