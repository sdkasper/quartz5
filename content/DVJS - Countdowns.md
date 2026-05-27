---
aliases:
  - obsidian/tweaks/dvjs-countdowns
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/DVJS---Countdowns
description: Add live countdown timers to your Obsidian notes for anniversaries, holidays, or any target date using DataviewJS.
cover:
date: 2024-12-05
draft: false
categories:
  - obsidian
  - dataview
cssclasses:
tags:
  - obsidian
  - dataview
created: 2024-04-12T09:58
updated: 2026-01-09T11:58
---

# Code
Don't forget to start and end the code block with three backticks.
## Countdown to the same date every year (e.g. anniversary)
```text
dataviewjs
const now = new Date();
const ax = new Date(now.getFullYear(), 11, 12); 
if (now > ax) {
  ax.setFullYear(ax.getFullYear() + 1);
}
const diff = ax.getTime() - now.getTime();
const daysLeft = Math.ceil(diff / (1000 * 60 * 60 * 24));
dv.paragraph(`_Anniversary_ in: **${daysLeft}** days.`);
```
## Countdown to Christmas
```text
dataviewjs
const now = new Date();
const ax = new Date(now.getFullYear(), 11, 25); 
if (now > ax) {
  ax.setFullYear(ax.getFullYear() + 1);
}
const diff = ax.getTime() - now.getTime();
const daysLeft = Math.ceil(diff / (1000 * 60 * 60 * 24));
dv.paragraph(`_Christmas_ in: **${daysLeft}** days.`);
```
## Countdown to fixed date
```text
dataviewjs
const targetDate = moment("2028-12-01", "YYYY-MM-DD");
const targetLabel = "Retirement";
const currentDate = moment();

const duration = moment.duration(targetDate.diff(currentDate));
const years = Math.floor(duration.asYears());
const months = Math.floor(duration.asMonths() % 12);
const weeks = Math.floor(duration.asWeeks() % 4.35); // Approximation: 4.35 weeks in a month
const days = Math.floor(duration.asDays() % 7);

dv.paragraph(`_${targetLabel}_ in:\n**${years}** years\n**${months}** months\n**${weeks}** weeks\n**${days}** days`);
```
# Result
![[DVJS - Countdowns-20241205133948464.webp|Three countdown timers showing days to anniversary, Christmas, and years to retirement]]
