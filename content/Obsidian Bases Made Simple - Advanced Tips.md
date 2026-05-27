---
aliases:
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Obsidian-Bases-Made-Simple---Advanced-Tips
description: Turn numeric ratings into visual stars, auto-detect card covers, build dynamic MoCs, and pick up essential quick tips for Obsidian Bases.
cover: zAttachments/Obsidian Bases Made Simple - Advanced Tips.webp
date: 2026-03-09
draft: false
categories:
  - obsidian
  - bases
cssclasses:
tags:
  - obsidian
  - bases
created: 2026-03-09T00:00
updated: 2026-03-15T18:40:25+02:00
---
# In a Nutshell

> [!important|float-r] Useful
> * Tutorial: [YouTube](https://youtu.be/34NAe62IH-M)
> * Docs: [Bases Documentation](https://help.obsidian.md/bases)
> * Icons: [Lucide Icons](https://lucide.dev/)
> * Download: [Obsidian Templates & Vaults](https://kspr.me/store)
> * Wiki: [Snippets & Examples](https://kspr.me/wiki)
> * [Discord](https://kspr.me/discord)

This is Part 3 of a 4-part series on Obsidian Bases. [[Obsidian Bases Made Simple - Getting Started|Part 1]] covered the fundamentals — enabling the plugin, views, and progress bars. [[Obsidian Bases Made Simple - Visual Use Cases|Part 2]] walked through recipe cards, travel maps, dates, and a birthday tracker.

Here you will learn how to visualize numeric ratings, automatically use the first image in a note as a card cover, build a dynamic Map of Content that adapts to any folder, and pick up a collection of quick tips that make daily work with Bases faster.

# Visualizing Ratings

If you have ratings in your notes — books, recipes, travel — you probably store them as numbers. That is the right call. Numeric ratings are easier to sort, filter, and use in calculations than emoji-based ones.

The question is: how do you keep the data numeric and still get a nice visual result? Formulas.
## Emoji-Based Ratings

Create a formula property called `fVisualRating1`. This uses nested `if` statements to check the value of `myRating` and return the matching number of stars. It also appends the numeric value at the end — remove the `+ [myRating]` parts if you do not want that.

```
if([myRating] >= 9, "⭐⭐⭐⭐⭐ " + [myRating],
 if([myRating] >= 7, "⭐⭐⭐⭐⚫ " + [myRating],
 if([myRating] >= 5, "⭐⭐⭐⚫⚫ " + [myRating],
 if([myRating] >= 3, "⭐⭐⚫⚫⚫ " + [myRating],
 if([myRating] >= 1, "⭐⚫⚫⚫⚫ " + [myRating],
 "⚫⚫⚫⚫⚫ " + [myRating]
 )))))
```

You can replace the stars and dots with any symbols you prefer. Once this formula is in place, you no longer need the raw `myRating` column in your table.

## Icon-Based Ratings

For a second version, create a formula property called `fVisualRating2`. Instead of emojis, this uses [Lucide icons](https://lucide.dev/) — the same icon set Obsidian uses internally. This gives you more control over the visual style.

```
if(myRating.isEmpty() || myRating < 1 || myRating > 10, "11111".split("").map(icon("star-off")), "11111".split("").slice(0, number(myRating/2).floor()).map(icon("star")) + if(number(myRating/2) - number(myRating/2).floor() >= 0.5, [icon("star-half")], []))
```

To find icon names, search on the [Lucide website](https://lucide.dev/). Every icon listed there works in Obsidian. Search for a term like "star", click the preview, and the name is copied to your clipboard.

The key takeaway: keep ratings numeric for clean data and flexibility, and add visualization with formulas. These visual ratings also work in the Cards View.

# First Image as Cover

In [[Obsidian Bases Made Simple - Visual Use Cases|Part 2]], you used a dedicated `featureImage` property to show thumbnails in the Cards View. But manually adding an image property to every note is tedious.

This method removes that friction. It automatically uses the first embedded image in any note as the card cover — zero extra setup.

Create a formula property called `fFirstImage`. This scans the note's embedded files and checks whether the first one matches common image types:

```
if(file.embeds[0].containsAny("jpg","gif","webp","jpeg","avif","png"), file.embeds[0])
```

The index starts at zero, so `file.embeds[0]` references the first embedded file. If it matches an image type, the formula returns the filename. If not, it returns nothing.

Switch your view to Cards and select `fFirstImage` as the image property. The first embedded image in each note becomes the card cover automatically.

This is a great solution for notes where images already exist in the content — articles with screenshots, travel notes with photos, or reference notes with diagrams. You keep your notes clean, avoid duplicate metadata, and still get a rich visual overview.

# Dynamic Map of Content

Many vaults use Maps of Content (MoCs) to navigate between notes. The problem is that manual MoCs are hard to maintain. Notes change, folders grow, and links quickly go out of sync.

Plugins like Waypoint or Dataview can help, but each has limitations. Waypoint is not easily customizable, and Dataview can become slow in larger vaults. If you want to modify your content maps, you have to touch each one individually.

Bases gives you a faster and more flexible alternative: a single Base file that adapts automatically to the current folder.

## Building It

Create a new view in a Base, filter it to markdown files, then switch to "advanced filter" and insert this formula:

```
file.inFolder(this.file.folder)
```

This uses the `this` context — the Base adapts depending on which note is currently active.

## Using It

You can embed this Base in any folder note. It automatically lists all notes in that folder. The same Base file works everywhere — no duplication needed.

Alternatively, drag the Base file into the side panel. In that position, it always shows the notes belonging to the same folder as the currently active note — instant context switching.

This method is not limited to folders. You can use the same idea for tags, project contexts, or any situation where `this` defines the scope:

- No manual updates
- No duplicated queries
- Instant context switching

# Quick Tips

None of these are required, but together they make working with Bases faster, cleaner, and more enjoyable.

## Hide the Header When Embedding

When embedding a Base in a note, you may not want to see the header and toolbar — especially for dashboards and compact overviews.

Add `|no-header` to the embed reference (for example, `![[MyBase.base#ViewName|no-header]]`). For this to work, create a CSS snippet. Go to **Settings** → **Appearance**, scroll to "Snippets", click the folder icon, and create a file called `Bases - no header.css` with this content:

```css
.bases-embed[alt~="no-header"] {
    .bases-header {
    display: none;
    }
}
```

Back in Obsidian, refresh the snippet list and activate it.

## Column Summaries

Right-click on a column header and choose "Summarize" to calculate a sum, average, count, or other operation. The result appears below the column.

By default, blank values are included in average calculations. To ignore blanks, click "Add summary" and use this custom formula:

```
(values.sum() / values.filter(value.toString().trim() != "null").length).round(1)
```

## Embed a Specific View

When embedding a Base, Obsidian shows the default view. To show a specific view instead, add `#ViewName` to the Base file reference — the same syntax as referencing a heading in an embedded note. This makes it easy to embed multiple views from the same Base in different places.

## Change the Default View

Click on the current view's name, hover over the icon of the view you want as default, and drag it to the top of the list.

## Quick Edit Views

To configure a view, you can click the views dropdown and then the arrow next to the view's name. Or — much faster — right-click directly on the view name. Same result.

## Row Height

Right-click the view name to change the row height: short, medium, tall, or extra tall. Useful because Bases does not yet support dynamic row heights based on content.

## Auto-Fit Columns

Drag column borders to resize manually, or double-click a column border to auto-fit the content width.

## Limit Results

The result count in the view header is interactive. Click on it to limit the number of results. Combined with sorting, this is perfect for "Top N" or "Bottom N" views.

## Export Data

From the same menu, export the current view as a CSV file or copy it to the clipboard as a static table — great for snapshots or sharing data outside Obsidian.

# FAQ

*Can I use Bases with inline fields?*

No. Inline fields are a Dataview feature. Bases only reads frontmatter properties — this is by design, keeping things simpler, faster, and more predictable.

The recommended approach is to move those values into frontmatter. If you want to keep your inline fields, the [Dataview to Properties](https://github.com/Mara-Li/obsidian-dataview-properties) plugin can copy inline field values into frontmatter and keep them synchronized automatically. As with any tool that modifies metadata in bulk, back up your vault first.

*Why does my formula return nothing?*

Check that the property names in the formula match exactly — including capitalization. Also verify the property exists in the notes you are filtering. Missing or misspelled properties return blank results silently.

*Can I use Bases and Dataview together?*

Yes. They read the same frontmatter properties and do not interfere with each other. You can migrate gradually — replace Dataview queries with Bases views one at a time.

# What's Next

In [[Obsidian Bases Made Simple - Content Maps|Part 4]], you will learn how to turn Bases into a full content management system — tracking blog posts, video projects, and ideas from a single dashboard.

All formulas from this series — and many more — are available on the [wiki](https://kspr.me/wiki). If you have questions, the [Discord](https://kspr.me/discord) is the best place to ask.
