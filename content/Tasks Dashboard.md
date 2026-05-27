---
aliases:
  - obsidian/tweaks/tasks-dashboard
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/Tasks-Dashboard
description: Build a multi-column tasks dashboard in Obsidian that groups tasks by overdue, today, this week, and upcoming.
cover:
date: 2024-11-25
draft: false
categories:
  - obsidian
  - CSS
cssclasses:
tags:
  - obsidian
  - css
created: 2024-11-25T10:54
updated: 2026-01-09T11:58
---


# Setup
To make it work and look as I show it here, you will need the "MCL Multi Column.css" and the "Tasks" community plugin.
# Result
You get a compact tasks dashboard, grouping tasks in four categories:
- Overdue
- Due today
- Due this week
- Due after this week
Adapt the queries to modify the grouping blocks.
![[Pasted image 20241125161828.webp|Four-column tasks dashboard with Overdue, Today, This Week, and Upcoming sections]]
# Code
```text
> [!multi-column]
> > [!important] Overdue by Due Date
> > ```tasks
> > path includes Task View for Homepage
> > not done
> > due before today
> > sort by due date
> > hide edit button
> > hide backlink
> > short mode
> > ```
> 
> > [!warning] Today by Prio
> > ```tasks
> > path includes Task View for Homepage
> > not done
> > due today
> > sort by priority
> > hide due date
> > hide edit button
> > hide backlink
> > short mode
> > ```
> 
> > [!todo] This Week by Due Date
> > ```tasks
> > path includes Task View for Homepage
> > not done
> > due after today
> > due this week
> > sort by due date, priority
> > hide task count
> > hide edit button
> > hide backlink
> > short mode
> > ```
> 
> > [!seealso] Upcoming by Due Date
> > ```tasks
> > path includes Task View for Homepage
> > not done
> > due after this week
> > sort by due date
> > hide task count
> > hide edit button
> > hide backlink
> > short mode
> > ```
```

# Source
on the Obsidian forum, posted by user "SenRVA".  
