---
description: Lean Obsidian Terminal embeds a real terminal directly inside your Obsidian workspace. No external windows, no workarounds.
date: 2026-03-31
substackStatus: published
tags:
  - obsidian
  - plugins
created: 2026-03-31T12:00
updated: 2026-03-31T13:11
substackId: 192711826
substackUrl: https://skasper.substack.com/publish/post/192711826
---

# A Real Terminal Inside Obsidian

You know that moment when you are deep in your notes and need to run a quick git command? You switch to your terminal. You lose your place. You switch back. Repeat that fifty times a day.

I got tired of it, so I built something.

**Lean Obsidian Terminal** embeds a real terminal directly inside your Obsidian workspace. Not a JavaScript emulator. Not an external window that pops up somewhere behind your browser. Your actual system shell - PowerShell, Bash, Zsh - running right next to your notes.

## What Makes It Different

Other terminal plugins for Obsidian either open external windows (defeating the purpose) or use workarounds that break across platforms. The core problem is that Obsidian's Electron environment makes running native terminal processes tricky - most plugins give up.

Lean Obsidian Terminal runs a real PTY (pseudoterminal) in-process. Your shell runs *inside* Obsidian, not alongside it. Everything you can run in a standalone terminal works here - `git rebase -i`, `npm install` with progress bars, Python scripts with input prompts.

## The Highlights

**Multiple tabs** - open as many terminal sessions as you need. Name them, close them, switch between them.

**Split panes** - run your build in one pane while tailing logs in another. All inside a single Obsidian window.

**ANSI color output** - syntax highlighting, colored diffs, status indicators. All rendered correctly through xterm.js.

**Customizable** - themes (Obsidian Dark, Obsidian Light, Monokai, Solarized), fonts, cursor settings, scrollback history, and even sound notifications when a long-running command finishes in a background tab.

## Getting Started

Two minutes. Three steps.

1. **Install via BRAT** - add the plugin repo URL ([kspr.me/lot](https://kspr.me/lot))
2. **Download binaries** - open Settings > Terminal > Binary Management, click Download. It detects your platform automatically. Every download is verified with a SHA256 checksum.
3. **Open a terminal** - click the ribbon icon or use the command palette. Done.

No npm install. No build tools. No command line gymnastics to get it running.

## Who Is This For

If you are a developer, scripter, or power user who lives in Obsidian - this removes a constant source of friction. Run git commands while writing commit notes. Execute vault maintenance scripts while looking at the notes they modify. Work through tutorials with code and notes side by side.

If you only use Obsidian for writing and never touch a terminal - you can safely skip this one. It is a power user tool and it knows it.

## Try It

The plugin is free, open source, and works on Windows, macOS, and Linux. Desktop only - mobile does not support pseudoterminal processes.

**Install it:** [kspr.me/lot](https://kspr.me/lot)
**Watch the walkthrough:** [kspr.me/lotvid](https://kspr.me/lotvid)
**Questions?** Join the [Discord](https://discord.gg/sbMg6PP2vq)

Best - Sascha
