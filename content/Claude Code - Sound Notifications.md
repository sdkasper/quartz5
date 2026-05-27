---
aliases:
author:
  - Sascha D. Kasper
source:
description: Learn how to add sound notifications to Claude Code with hooks so you never miss when it needs your input — setup for macOS and Windows.
cover:
date: 2026-03-09
draft: false
categories:
  - obsidian
  - ai
cssclasses:
tags:
  - Claude-Code
  - ai
created: 2026-03-09T00:00
updated: 2026-03-12T13:30:20+02:00
---
# In a Nutshell

> [!important|float-r] Key Info
> * Config: `~/.claude/settings.json`
> * Command: `/hooks` in Claude Code
> * Events: `idle_prompt`, `permission_prompt`

**Claude Code** doesn't play sounds by default when it finishes a task or needs permission. If you're multitasking, you'll miss the prompt and waste time checking back. With a simple hooks configuration in your `settings.json`, you can make Claude Code play a sound whenever it's waiting for you.

This guide gives you copy-paste configs for both macOS and Windows.

# Setting Up Sound Notifications

Add the following `hooks` block to your `settings.json`. You can open it via `/hooks` in Claude Code or edit the file directly.

**File location:**
- **macOS:** `~/.claude/settings.json`
- **Windows:** `%USERPROFILE%\.claude\settings.json`

## macOS

```json
"hooks": {
  "Notification": [
    {
      "matcher": "idle_prompt",
      "hooks": [
        {
          "type": "command",
          "command": "afplay /System/Library/Sounds/Glass.aiff"
        }
      ]
    },
    {
      "matcher": "permission_prompt",
      "hooks": [
        {
          "type": "command",
          "command": "afplay /System/Library/Sounds/Ping.aiff"
        }
      ]
    }
  ]
}
```

To use a custom sound, replace the path with any `.aiff`, `.wav`, or `.mp3` file:

```
"command": "afplay /path/to/your/sound.mp3"
```

Browse available system sounds in `/System/Library/Sounds/` — you'll find options like Glass, Ping, Hero, Purr, and Pop.

## Windows

```json
"hooks": {
  "Notification": [
    {
      "matcher": "idle_prompt",
      "hooks": [
        {
          "type": "command",
          "command": "powershell -Command \"(New-Object System.Media.SoundPlayer 'C:\\Windows\\Media\\Ring10.wav').PlaySync()\""
        }
      ]
    },
    {
      "matcher": "permission_prompt",
      "hooks": [
        {
          "type": "command",
          "command": "powershell -Command \"(New-Object System.Media.SoundPlayer 'C:\\Windows\\Media\\Ring10.wav').PlaySync()\""
        }
      ]
    }
  ]
}
```

To use a custom sound, replace the path with any `.wav` file:

```
"command": "powershell -Command \"(New-Object System.Media.SoundPlayer 'C:\\path\\to\\your\\sound.wav').PlaySync()\""
```

Browse available system sounds in `C:\Windows\Media\` — try `Ring10.wav`, `chimes.wav`, or `notify.wav`.

# How to Verify

1. Restart Claude Code after editing `settings.json`.
2. Run `/hooks` and select **Notification** to confirm your hooks are registered.

If you hear the sound when Claude Code finishes a task or asks for permission, you're all set.

# FAQ

*What events can I hook into?*

The two most useful are `idle_prompt` (Claude finished and is waiting for your next input) and `permission_prompt` (Claude needs you to approve a tool call). You can use different sounds for each to distinguish them.

*Can I use different sounds for different events?*

Yes. Just set a different file path in the `command` field for each matcher. For example, use a subtle chime for `idle_prompt` and a more attention-grabbing sound for `permission_prompt`.

*Do I need to install anything extra?*

No. Both macOS (`afplay`) and Windows (`System.Media.SoundPlayer`) use built-in system tools. You just need a sound file — the OS ships with plenty.
