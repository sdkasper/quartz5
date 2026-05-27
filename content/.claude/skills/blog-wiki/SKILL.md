---
name: blog-wiki
description: Write new or restructure existing wiki posts for the LeanProductivity Quartz blog. Wiki posts are short, code-focused reference articles following the TPL - Blog Wiki template with Setup/Result/Code sections. Use when creating CSS snippets, Dataview queries, DataviewJS scripts, Bases formulas, Templater scripts, or theme tweaks for `$VAULT_PATH\09 Blog\`.
---

# Blog Wiki

Three modes: **New wiki**, **Restructure**, **Review**.

## Success Criteria

Before presenting output, verify all criteria are met. If not, iterate until they are.

- [ ] Title follows `PREFIX - Name` convention
- [ ] Frontmatter has `tags: wiki` (not `blog`), `author` is `- Sascha D. Kasper`, `categories` includes `obsidian`
- [ ] Has `# Code` section with correctly fenced code blocks (`css`, `text`, or blank for Bases)
- [ ] DVJS blocks use `text` fence with `dataviewjs` as first line inside (not as fence language)
- [ ] No "In a Nutshell" sections or float-right callouts (those are blog-post patterns)

Wiki posts are short technical reference articles — code snippets with just enough context to use them. They are NOT blog posts (use `/blog-post` for long-form content with "In a Nutshell" sections).

## Obsidian Markdown — MANDATORY

All wiki posts live in the Obsidian vault. Before writing or editing any post, load and follow `/obsidian-markdown` rules. Key constraints:

- No blank line before headings (content immediately precedes the `#` line)
- No double blank lines anywhere
- No horizontal rules in content
- Callout lists use `> *` not `> -`
- Internal vault references use `[[wikilinks]]`, not standard Markdown links
- Tags belong in frontmatter, not inline

## Expert Thinking

Before any mode, answer these questions:

- **What type of code is this?** The title prefix and categories depend on it: CSS snippet, Dataview query (DV), DataviewJS script (DVJS), Bases formula (BASES), Templater script, or Theme tweak (THEME).
- **Can the reader copy-paste and go?** Wiki posts succeed when the code is self-contained. If it requires significant setup, the Setup section must cover every prerequisite — don't assume the reader knows how to enable CSS snippets or install plugins.
- **Is this a wiki or a blog post?** If it needs more than 2 paragraphs of explanation per section, it's probably a blog post, not a wiki. Wiki posts are reference cards, not tutorials.

## Title Convention

Titles follow a strict `PREFIX - Descriptive Name` pattern:

| Code type | Prefix | Example |
|-----------|--------|---------|
| CSS snippet | `CSS -` | `CSS - Syntax Highlighting` |
| Dataview query | `DV -` | `DV - list empty notes` |
| DataviewJS script | `DVJS -` | `DVJS - Countdowns` |
| Bases formula | `BASES -` | `BASES - Absolute Progress Bars` |
| Templater script | `Templater Script -` | `Templater Script - Ask for Note Title` |
| Theme customization | `THEME -` | `THEME - Baseline Customization` |
| Tasks plugin | `Tasks` prefix or standalone | `Tasks Dashboard` |

The title IS the filename. Get it right — changing it later breaks links.

## Structure Rules

Three canonical sections, all H1. Section order may vary by content type, but all three should be present when applicable:

- `# Setup` — Prerequisites, installation steps, configuration. Use bullet lists or numbered steps. For CSS posts, include the standard snippet installation instructions (see reference).
- `# Result` — What the reader gets. Usually a screenshot (`![[filename.webp]]`) or brief description. Keep prose minimal.
- `# Code` — The actual code. Use fenced code blocks with the correct language tag (`css`, `text` for Dataview/DVJS, no tag for Bases formulas). Use H2 subsections to separate multiple snippets.
- `# Source` (optional) — Attribution when the code originated elsewhere. Link to the original author/post.

**H2 subsections** are allowed inside any section (e.g., `## Snippet 1`, `## Two Columns`, `## Countdown to Christmas`). H3 is acceptable in wiki posts for sub-variants but avoid going deeper.

## Categories

Always include `obsidian` as the first category. Second category matches the code type:

| Code type | Category |
|-----------|----------|
| CSS | `CSS` |
| DV / DVJS | `dataview` |
| BASES | `bases` |
| Templater | `templater` |
| Theme | `theme` |
| Tasks | `CSS` (uses CSS for layout) or specific plugin name |

## NEVER Do

- Tag with `blog` — wiki posts use `wiki` tag exclusively. Using `blog` makes it appear in blog-post listings.
- Write long prose explanations — if you need more than 2-3 sentences in Setup or Result, it's probably a blog post
- Skip the code language tag in fenced blocks — `css` for CSS, `text` for Dataview/DVJS (prevents Obsidian from trying to execute the query)
- Use `dataviewjs` as the code fence language — use `text` and put `dataviewjs` as the first line inside the block (this prevents auto-execution in Obsidian while showing the intent)
- Omit the Setup section for CSS snippets — readers need the snippet installation steps even if they seem obvious
- Invent screenshot filenames — use the Obsidian attachment naming convention: `![[PostTitle-timestamp.webp]]` or ask the user for the actual filename
- Add "In a Nutshell" sections or float-right callouts — those are blog-post patterns, not wiki patterns

## Workflow

### New Wiki

1. Ask for: the code/snippet, what it does, any prerequisites, and source attribution if applicable
2. **MANDATORY** — Read `references/wiki_structure.md` for the annotated examples
3. Determine the code type and set the title prefix accordingly
4. Generate frontmatter from `assets/frontmatter_template.md` — set `draft: true`, fill title/categories
5. Write `# Setup` with prerequisites (for CSS: use the standard snippet installation boilerplate from the reference)
6. Write `# Result` with a brief description; ask user for screenshot filename or leave `![[PLACEHOLDER.webp]]`
7. Write `# Code` with properly fenced code blocks; use H2 subsections if multiple snippets
8. Add `# Source` if the code was found elsewhere
9. Save to `$VAULT_PATH\09 Blog\{title}.md`

**Do NOT load** `references/wiki_structure.md` for simple frontmatter fixes or title questions.

### Restructure

1. Read the existing post
2. **MANDATORY** — Read `references/wiki_structure.md` for the annotated examples
3. Check: does this post have Setup/Result/Code sections? If not, identify which content maps to which section
4. Ensure title follows the `PREFIX - Name` convention
5. Fix frontmatter: `tags: wiki` (not `blog`), correct categories
6. Verify code blocks have correct language tags
7. Present a summary of structural changes made

**Do NOT load** `references/wiki_structure.md` for minor frontmatter-only fixes.

### Review

Use the checklist below. Only load `references/wiki_structure.md` if you need to verify a specific pattern.

**Must fix:**
- [ ] Title follows `PREFIX - Name` convention
- [ ] `tags` includes `wiki` (not `blog`)
- [ ] `categories` includes `obsidian` + code-type category
- [ ] Has `# Code` section with fenced code blocks
- [ ] Code blocks have correct language tag (`css`, `text`, or blank for Bases)
- [ ] Frontmatter has required fields (`title`, `author`, `date`, `draft`, `categories`, `tags`, `created`, `updated`)
- [ ] `author` is `- Sascha D. Kasper`

**Should fix:**
- [ ] Has `# Setup` section (especially for CSS snippets)
- [ ] Has `# Result` section with screenshot or description
- [ ] Code blocks use `text` (not `dataviewjs`) for DVJS scripts
- [ ] Has `# Source` if code is from external origin

**Nice to have:**
- [ ] Multiple code snippets separated into H2 subsections
- [ ] Screenshot uses `.webp` format
- [ ] Description field filled (often empty on wiki posts — acceptable but better with one)

Report deviations grouped by severity.

## Self-Verification

Before presenting output, verify:
- [ ] All images have descriptive alt text (`/alt-text`)

## Cross-References

- `/obsidian-markdown` — Obsidian-flavored Markdown rules (whitespace, wikilinks, callouts)
- `/obsidian-yaml-frontmatter` — Frontmatter property standards
- `/alt-text` — Image alt text auditing, creation, and review
