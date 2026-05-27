---
aliases:
  - Sync Obsidian Settings
  - Obsidian Settings Sync Guide
author:
  - Sascha D. Kasper
source: https://www.reddit.com/r/ObsidianMD/comments/1g9hxsu/syncing_settings_and_plugins_between_devices/
description: How to keep your Obsidian settings, plugins, hotkeys, and themes consistent across devices using a primary-secondary approach with Obsidian Sync. No .obsidian folder conflicts, no third-party tools.
cover: zAttachments/How to Sync Obsidian Settings and Plugins Between Devices-1.webp
date: 2026-03-31
draft: true
categories:
  - obsidian
  - sync
cssclasses:
tags:
  - obsidian
  - sync
created: 2026-03-31T00:00
updated: 2026-04-01T09:48:39+03:00
---

Obsidian Sync keeps your notes in sync, but your settings — plugins, hotkeys, themes, appearance — need a different approach. This guide shows how to use a primary-secondary device strategy to sync the `.obsidian` folder without conflicts, using only Obsidian Sync.
# In a Nutshell

> [!important|float-r] Related
> * [[Bulletproof Your Notes - Best Obsidian Sync and Backup Picks|Obsidian Sync & Backup Guide]]

Obsidian Sync handles your notes, but getting **settings and plugins** consistent across devices is a different problem. There is no built-in one-way sync for the `.obsidian` folder - but you can fake it.

The trick is sequencing. You pick one device as your **primary**, let it upload its settings first, then have every other device pull from it. The result: identical plugins, hotkeys, themes, and appearance settings everywhere - without conflicts.
# How It Works
You designate one device as the single source of truth for settings. Secondary devices never push their own configuration - they only receive.

Obsidian Sync does not have a "one-way" toggle. But if you control **which device uploads first**, secondary devices will always pull the primary's settings instead of overwriting them with their own.
# Step-by-Step Guide

## Step 1: Reset All Devices
On EVERY device:
1. Open Obsidian
2. Disable **Settings Sync** completely
3. Close Obsidian

This gives you a clean starting point with no conflicting settings in the cloud.
## Step 2: Configure Your Primary Device
On your primary device (the one where you do most of your configuration):
1. Open Obsidian
2. Set up your settings exactly how you want them - plugins, hotkeys, themes, appearance, everything
3. Enable **Settings Sync**
4. Wait for the upload to finish completely

> [!warning|float-r] Order Matters
> Do NOT touch your other devices until the primary has finished uploading. If a secondary device enables sync before the primary is done, it may push its own settings to the cloud and overwrite your work.
## Step 3: Connect Secondary Devices
On each secondary device (other laptops, phone, tablet):
1. Make sure Obsidian is closed
2. Delete the `.obsidian` folder from your vault - this removes all local settings
3. Open Obsidian
4. Enable **Settings Sync**
5. The device downloads the primary's settings automatically
## Step 4: Keep It Consistent
From now on:
- Only change settings on your **primary device**
- If a secondary device accidentally changes something, repeat Step 3 for that device
- Keep Settings Sync enabled on all devices
# FAQ

> [!question]- Does this work with Obsidian Sync only, or also with third-party sync tools?
> This method is designed for **Obsidian Sync** specifically. If you use Syncthing, Git, or cloud storage for vault sync, settings sync works differently - and you may run into conflicts with the `.obsidian` folder. See [[Bulletproof Your Notes - Best Obsidian Sync and Backup Picks|the full sync and backup guide]] for alternatives.

> [!question]- What happens if I install a plugin on a secondary device?
> It depends on your Settings Sync configuration. If plugin sync is enabled, the new plugin may upload to the cloud and appear on your primary device. To keep things clean, install plugins only on your primary device.

> [!question]- Do I lose my notes when I delete the .obsidian folder?
> No. The `.obsidian` folder contains settings, plugins, themes, and appearance configuration - not your notes. Your notes stay exactly where they are.
# Infographic
![[How to Sync Obsidian Settings and Plugins Between Devices.webp]]