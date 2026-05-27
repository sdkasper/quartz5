---
aliases:
author:
  - Sascha D. Kasper
source: https://github.com/ichris007/Obsidian_Lifein
description: A comprehensive CSS snippet that beautifies Obsidian Bases views with alternating row colors, hover effects, animated header reveal, row numbering, checkbox centering, card title styling, and more.
cover:
date: 2026-03-20
draft: true
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - wiki
created: 2026-03-20T12:00
updated: 2026-03-20T12:00
---

# Setup
Go to `Settings`, `Appearance`, and scroll all the way down to the `CSS snippets` section. You might already have some there, or not. It does not matter for us.

Click on the folder icon. This should open the local folder containing the snippets. Create a new file and give it a name that makes sense to you. For example, `bases-beautification.css`. Make sure that the file extension is `css`. If you don't see your file extensions, click on `View`, `Show`, and `File name extensions` (in Windows Explorer).

Now open the file and copy the CSS code below into it. Save the file, go back to Obsidian and refresh the list of snippets. Enable this one, and that should do it. If it does not, you may have to restart Obsidian.

> [!tip] Some features require cssclasses
> A few of the enhancements below only activate when you add specific values to the `cssclasses` property in a note's frontmatter:
> * `hide-basebar` — hides the filter/sort bar
> * `no-toolbar` — hides the edit block toolbar
> * `bases-ordered-list` — adds row numbers to the table
# Result
This snippet is a collection of ~15 visual enhancements for Obsidian Bases views. It covers table styling (alternating row colors, hover effects, header styling), card view improvements (two-line titles, title color), UI cleanup (hidden column icons, hidden multi-select remove buttons), animated header reveal on hover, ordered list numbering, checkbox centering, and search row optimization.

![[CSS - Bases Beautification-PLACEHOLDER.webp]]
# Code
## Hide Column Header Icons
```css
/* Hide text icons in column headers */
.bases-table-header-icon {
    display: none;
}
```
## Two-Line Card Titles
```css
/* Show title on two lines */
.bases-cards-property.mod-title .bases-cards-line {
  font-size: var(--font-ui-small);
  line-height: 1.2;
  height: 2.8em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
```
## Hide Multi-Select Remove Buttons
```css
/* Bases table view - hide remove buttons until hover */
.bases-table .multi-select-pill-remove-button {
  visibility: hidden;
}

.bases-table .multi-select-pill:hover .multi-select-pill-remove-button {
  visibility: visible;
}
```
## Card Title Color
```css
/* Set card title color */
.bases-cards-property.mod-title {
  color: rgb(187, 128, 245);
}
```
## Hide Filter Bar (cssclass)
```css
/* Hide the filter bar via cssclass hide-basebar */
.hide-basebar .bases-header {
    display: none !important;
}
```
## Hide Toolbar (cssclass)
```css
/* Hide edit block toolbar via cssclass no-toolbar */
.no-toolbar {
    .query-toolbar {
        display: none;
    }
    &.mod-cm6 .cm-content > .bases-embed .edit-block-button {
        opacity: 0.3;
    }
}
```
## Alternating Row Colors
```css
/* Odd row background */
.bases-table-container .bases-tbody .bases-tr:nth-child(odd) {
    background-color: var(--color-base-00);
}

/* Even row background */
.bases-table-container .bases-tbody .bases-tr:nth-child(even) {
    background-color: var(--color-base-20);
}
```
## Row Hover Effect
```css
/* Hover background color */
.bases-table-container .bases-tbody .bases-tr:hover {
    background-color: var(--color-accent);
    transition: background-color 0.2s ease;
}
```
## Header Styling
```css
/* Table header styling */
.bases-table-container .bases-thead .bases-tr {
    background-color: var(--color-base-20) !important;
    font-weight: bold;
}
```
## Ordered List with Row Numbers (cssclass)
```css
/* Add row numbers - activate with cssclasses: bases-ordered-list */
.workspace-split.mod-sidedock.mod-right-split .workspace-tabs:not(.mod-top) .bases-view,
.bases-ordered-list,
.bases-embed[alt~="ordered-list"] {

    .query-toolbar-item:not(.mod-views) { display: none; }

    /* Hide bottom shadow */
    .bases-tbody { box-shadow: none; }

    .bases-view[data-view-type="table"] {--bases-embed-border-width: 0; overflow-x: hidden;}

    /* Hide header row */
    .bases-thead { display: none; }

    /* Row counter */
    .bases-tr { counter-increment: di-bases-pure-list-counter; }

    /* Remove table grid lines */
    .bases-tr, .bases-td { box-shadow: none; }

    /* Hide underline for links in the first column */
    .bases-td:first-of-type a {
        text-decoration: none;

        &:hover {
            text-decoration: underline;
        }
    }

    /* Prepend row number */
    .bases-td:first-of-type .bases-table-cell::before {
        content: counter(di-bases-pure-list-counter) ". ";
        color: var(--list-marker-color);
        padding-right: 1ch;
        padding-left: 1ch;
    }
}
```
## Checkbox Centering
```css
/* Center-align checkboxes */
.bases-view .bases-tbody .bases-tr > *:has(input[type="checkbox"]) {
  text-align: center !important;
}
.bases-view input[type="checkbox"] {
  display: inline-block;
  margin: 0 auto !important;
  vertical-align: middle;
}
```
## Animated Header Reveal on Hover
```css
/* 1. Container setup */
.bases-embed {
    overflow: hidden !important;
    position: relative;
    transition: height 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
}

/* 2. Header: hidden by default, revealed on hover */
.bases-embed .bases-header {
    height: 25px !important;
    min-height: 25px !important;
    max-height: 25px !important;
    padding: 0 8px !important;

    transform: translateY(-25px);
    opacity: 0;

    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    z-index: 99;

    transition:
        transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1),
        opacity 0.2s ease-out;
}

/* 3. View layer shift */
.bases-embed .bases-view,
.bases-embed .bases-embed-view {
    transform: translateY(0);
    transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    will-change: transform;
}

/* 4. Hover trigger: synchronized shift */
.bases-embed:hover .bases-header {
    transform: translateY(0);
    opacity: 1;
}

.bases-embed:hover .bases-view,
.bases-embed:hover .bases-embed-view {
    transform: translateY(25px);
}

/* 5. Bottom compensation: prevent content clipping */
.bases-embed {
    padding-bottom: 0px;
    transition: padding-bottom 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.bases-embed:hover {
    padding-bottom: 25px;
}

/* 6. Icon scaling adjustment */
.bases-embed .bases-header > div {
    height: 25px !important;
    display: flex;
    align-items: center;
    transform: scale(0.85);
    transform-origin: left center;
}
```
## Search Row Optimization
```css
/* 7. Search row container and state control */
.bases-embed .bases-search-row {
    height: 30px !important;
    min-height: 30px !important;
    padding: 0 10px !important;
    background: transparent !important;

    /* Animation synced with header */
    transform: translateY(0);
    transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    will-change: transform;

    position: relative;
    z-index: 5;
}

/* Shift down on hover to make room for header */
.bases-embed:hover .bases-search-row {
    transform: translateY(25px);
}

/* Activate flex layout only when not hidden by plugin */
.bases-embed .bases-search-row:not([style*="display: none"]) {
    display: flex !important;
    align-items: center !important;
}

/* Respect plugin's hide directive */
.bases-embed .bases-search-row[style*="display: none"] {
    display: none !important;
}

/* Search input container layout */
.bases-embed .bases-search-row .search-input-container {
    height: 24px !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    position: relative !important;
}

/* Input field typography */
.bases-embed .bases-search-row input[type="search"] {
    width: 100% !important;
    height: 100% !important;
    padding-left: 28px !important;
    padding-right: 28px !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
    line-height: normal !important;
    margin: 0 !important;
}

/* Search icon */
.bases-embed .bases-search-row .search-input-container::before {
    content: "";
    position: absolute !important;
    left: 8px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    width: 14px !important;
    height: 14px !important;
    z-index: 2;
    pointer-events: none;
}

/* Clear button */
.bases-embed .bases-search-row .search-input-clear-button {
    position: absolute !important;
    right: 8px !important;
    top: 50% !important;
    transform: translateY(calc(-50% + 1px)) !important;
    justify-content: center !important;
    align-items: center !important;
    width: 16px !important;
    height: 16px !important;
    padding: 0 !important;
    margin: 0 !important;
    line-height: 0 !important;
}

/* Clear button icon fix */
.bases-embed .bases-search-row .search-input-clear-button svg {
    display: block !important;
    margin: 0 !important;
}

/* 8. Stability fix: prevent header buttons from shifting */
.bases-embed .bases-header * {
    transform: none !important;
}

/* 9. Layout patch: prevent search row overlap with table header */
.bases-search-row {
    background-color: var(--background-primary);
    border-bottom: 1px solid var(--background-modifier-border);
}
```
# Source
- By 科叔 (ichris007): [Obsidian Lifein on GitHub](https://github.com/ichris007/Obsidian_Lifein)
