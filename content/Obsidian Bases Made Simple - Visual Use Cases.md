---
aliases:
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Obsidian-Bases-Made-Simple---Visual-Use-Cases
description: Build recipe cards, interactive travel maps, date-based views, and a birthday tracker in Obsidian Bases — all with copy-paste formulas.
cover:
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
updated: 2026-03-09T11:01:05+02:00
---
# In a Nutshell

> [!important|float-r] Useful
> * Tutorial: [YouTube](https://youtu.be/34NAe62IH-M)
> * Docs: [Bases Documentation](https://help.obsidian.md/bases)
> * Maps: [Map View Backgrounds](https://help.obsidian.md/bases/views/map)
> * Download: [Obsidian Templates & Vaults](https://kspr.me/store)
> * Wiki: [Snippets & Examples](https://kspr.me/wiki)
> * Support: [Discord](https://kspr.me/discord)

This is Part 2 of a 3-part series on Obsidian Bases. [[Obsidian Bases Made Simple - Getting Started|Part 1]] covered the fundamentals — enabling the plugin, understanding views, and building progress bars. Here you will put that knowledge to work with four visual use cases: browsing recipes as image cards, plotting trips on interactive maps, working with dates in formulas, and building a birthday tracker that counts down automatically.

[[Obsidian Bases Made Simple - Advanced Tips|Part 3]] covers advanced techniques like visual star ratings, using the first image as a card cover, dynamic Maps of Content, and quick tips.

# Cards View: Recipes

Tables are great for structured data, but sometimes you want something more visual — a way to browse a collection like a gallery. That is where the Cards View shines.

Recipes are the example here, but this approach works for anything with an image: books, films, collections, mood boards, or inspiration notes.

## Setting Up Recipe Notes

Each recipe note needs frontmatter properties that describe the dish. A typical set looks like this:

- `difficulty` — how hard the recipe is
- `rating` — your personal score
- `lastCooked` — when you last made it
- `totalTime` — how long it takes
- `featureImage` — the filename of the image to display

That `featureImage` property is the key to making cards work visually. It should contain the name of an image file stored in your vault (for example, `pasta-carbonara.jpg`).

## Building the Cards View

Start with a new view in your Base and filter it to the relevant notes — by tag, folder, or any other property. Add the properties you want to display on each card: `difficulty`, `rating`, `lastCooked`, `totalTime`.

At this point, you are looking at a table. To switch to cards, right-click on the view name and change the layout from "table" to "cards". The Base immediately switches to a card layout, but you will not see images yet.

To fix that, scroll down to the "image property" field and select `featureImage` from the list. You can choose your preferred image fit — "cover" works well for most cases — and adjust the aspect ratio to taste.

Just like tables, cards support grouping, sorting, and filtering. Group recipes by `mealType` and sort by `lastCooked` to see what you have not cooked in a while. You are only changing how the data is presented — the notes themselves stay untouched.

# Map View: Travel Planning

Before using Obsidian for travel, planning a trip and reviewing it afterward meant scattered notes across different apps. The Map View in Bases changes that by giving you a spatial overview of trips, places, and locations — all connected and visible on an interactive map.

> [!file|float-r] Downloads
> * [Travel Planner Vault](https://kspr.me/ltr)

There are two ways to use maps:

- **Overview map** — shows all trips at a glance
- **Contextual map** — shows only the locations related to one specific trip

## Frontmatter for Maps

The key properties for map markers are:

- `location` — latitude and longitude coordinates
- `icon` — a [Lucide icon](https://lucide.dev/) name for the marker
- `color` — the marker color

These three properties control how Bases places and styles markers on the map.

## Building an Overview Map

Create a new view and filter it to notes in your travel folder. Start with a table to verify the data looks right, then right-click the view name and change the layout to "maps".

You can zoom, pan, and center the map to the region that makes sense for you. Right-click and hold to tilt and rotate the view. Once you are happy with it, right-click the map and select "set default center point" and "set default zoom" so it always opens this way.

Next, configure the markers. Right-click the view name, open the "Markers" section, and assign each property:

- **Location** → your `location` property
- **Marker icon** → your `icon` property
- **Marker color** → your `color` property

If the map shows too many items, add a filter — for example, notes containing a tag like `Travel/Trip` — to show only trips on the overview map.

## Building a Contextual Map

A contextual map shows only the locations linked from a specific trip note. Duplicate the overview map view, rename it, and change the filter to:

```
this.file.hasLink(file)
```

Now, whenever you open a trip note that embeds this Base, the map automatically updates to show only the locations linked from that note — cities, landmarks, restaurants, museums.

## Map Backgrounds

You can customize the map background by right-clicking the view, expanding the "Background" section, and pasting a style URL. Three options are available on the [Obsidian map view documentation](https://help.obsidian.md/bases/views/map):

Light background:
```
https://tiles.openfreemap.org/styles/positron
```

Standard background:
```
https://tiles.openfreemap.org/styles/liberty
```

Dark background:
```
https://tiles.openfreemap.org/styles/dark
```

Each view can have its own background, so you can match the style to the content.

The big takeaway: maps are just another view on top of structured data. Once your notes have consistent location properties, you can reuse this approach far beyond travel — site visits, research locations, real estate, events, or anything tied to geography.

# Working with Dates

Dates can feel tricky in Bases, but they are straightforward once you know a few go-to formulas.

## Today's Date

The `today()` function returns the current date. The format depends on your system settings.

For a consistent `YYYY-MM-DD` format, add `toString()`:

```
today().toString()
```

For a custom format, use `format()`. This example extracts just the year and month:

```
today().format("YYYY-MM")
```

## Extracting a Date from a Filename

If you work with daily notes named `YYYY-MM-DD` (or `YYYY-MM-DD Some Title`), you can extract a real date by taking the first ten characters of the filename:

```
date(file.name.slice(0,10))
```

If the filename matches the pattern, you get a valid date. If not, Bases returns nothing.

This unlocks views like "this day in history" — notes from previous years that share the same month and day. Filter for files where the filename contains the current note's date formatted as `MM-DD`:

```
file.name.contains(date(this.file.name).format("MM-DD").toString())
```

Optionally exclude the current file:

```
file.basename != this.file.basename
```

## Using a Dedicated Date Property

For notes without a date in their filename, you have two options: the file system's created timestamp, or a dedicated frontmatter property like `created`. A frontmatter property is the better choice — sync tools and backups can change file system timestamps.

If you do not have a `created` property, you can substitute the system property "created time" in any of the formulas below.

## Relative Date Views

Here are the formulas for common date-based filters. Each one is a formula property — set its filter to "true" to activate the view.

**Notes created today:**

```
today().format("YYYY-MM-DD") == note["created"]
```

**Notes created yesterday:**

```
(today() - "1 d").format("YYYY-MM-DD") == note["created"]
```

**Notes created on the same day as the current note:**

```
this.created.format("YYYY-MM-DD") == note["created"]
```

**Notes created this week:**

```
today().format("Yw") == date(note["created"]).format("Yw")
```

**Notes created last week:**

```
(today() - "1 w").format("Yw") == date(note["created"]).format("Yw")
```

**Notes created this month:**

```
today().format("YYYY-MM") == note["created"].format("YYYY-MM")
```

**Notes created last month:**

```
(today()- "1 M").format("YYYY-MM") == note["created"].format("YYYY-MM")
```

**Notes created this year:**

```
today().format("YYYY") == note["created"].format("YYYY")
```

**Notes created last year:**

```
(today()- "1 y").format("YYYY") == note["created"].format("YYYY")
```

All of these snippets — and more — are available on the [wiki](https://kspr.me/wiki).

# Birthday Tracker

Birthdays, deadlines, anniversaries — whatever the date, it is easy to let them slip. Here is how to build a tracker that counts down the days and auto-calculates ages.

The same method works for contract renewals, event countdowns, or any recurring date.

## Setup

Create a new view and filter it to notes with a tag like `person` where the `birthday` property is not empty.

## Days Until Next Birthday

Add a formula property called `fRemainingDays`. This formula converts today's date and the person's birthday into numbers, calculates the difference, and returns the result in days:

```
((number(
  date(today().format("YYYY") + "-" + birthday.format("MM-DD")) +
  if(date(today().format("YYYY") + "-" + birthday.format("MM-DD")) < today(), "1y", "0y")
) - number(today())) / 86400000).round()
```

It looks dense, but the logic is: take the birthday's month and day, set it to the current year, check if it already passed (if so, add a year), then subtract today's date and convert milliseconds to days.

Sort the results by `fRemainingDays` to get a clean overview of upcoming birthdays.

## Calculating Age

Add another formula property called `fAge`:

```
if(birthday.format("MM-DD") <= today().format("MM-DD"),
today() - birthday, today() - (birthday + duration("1 year")))
```

This checks whether the birthday has already occurred this year and returns the correct current age.

## Beyond Birthdays

You are not limited to birthdays or durations in years. The same approach lets you:

- Count days until a deadline
- Track contract renewals
- Calculate how long something has existed
- Show how much time is left until an important event

# What's Next

This was the visual side of Bases: recipe cards, travel maps, date formulas, and a birthday tracker. In [[Obsidian Bases Made Simple - Advanced Tips|Part 3]], you will learn how to turn numeric ratings into visual stars, use the first image in a note as a card cover, build dynamic Maps of Content, and pick up a collection of quick tips and answers to common questions.

If you missed the fundamentals, [[Obsidian Bases Made Simple - Getting Started|Part 1]] covers enabling the plugin, understanding view types, and building progress bars.
