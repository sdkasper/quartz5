---
title: The Optimized Claude Code Setup
aliases:
author:
  - Sascha D. Kasper
source:
description: Cut Claude Code costs by 60-90% with smart model routing, context-mode plugin, and auto-memory. A complete setup guide for Claude Code power users.
cover: zAttachments/Optimized Claude Code Setup-1.webp
date: 2026-05-05
draft: false
categories:
  - claude-code
  - productivity
cssclasses:
tags:
  - Claude-Code
  - ai
created: 2026-05-05T00:00
updated: 2026-05-06T09:44:36
---

# In a Nutshell
> [!important|float-r] Resources & Downloads
> * Plugin: [context-mode](https://github.com/mksglu/context-mode)
> * Plugin: [claude-mem](https://github.com/thedotmack/claude-mem)
> * App: [Claude Code](https://claude.ai/code)

Claude Code is powerful, but running at full capacity drains your wallet fast. By wiring up a 3-tier model routing system, a context-compression plugin, and episodic memory, you can cut costs by 60-90% without sacrificing quality. This guide walks you through a production-grade setup that most Claude Code users don't know exists - and how to automate it so you spend zero time managing it.
# What You Get
Once you've completed this setup, your Claude Code environment will deliver:
* **70-90% token reduction** via the context-mode FTS5 sandbox, which keeps large knowledge bases out of every prompt
* **Episodic memory across sessions** - past conversations surface automatically when relevant, so you don't repeat context setup each time you start
* **Auto-handoff continuity** - when you stop Claude Code, a HANDOFF.md file preserves your working directory and task context so you can resume with a single `/letsgo` command
* **3-tier model routing** - Haiku handles drafts and brainstorming by default, Sonnet auto-gates onto scripts and launch content, and Opus never runs without your explicit approval. This architecture drops your bill by 60x compared to running everything on Opus
* **Plan mode by default** - all changes require your approval before execution, removing the risk of surprise outputs

The setup takes about 30 minutes and pays for itself on your first non-trivial project. After that, it's maintenance-free.
# Prerequisites
You'll need:
* Claude Code (CLI, desktop, or web version)
* `jq` for JSON parsing in hooks (Windows: via Chocolatey or manually; macOS/Linux: via Homebrew)
* `node`/`nodejs` (version 16+) - hooks are `.mjs` files and need a JavaScript runtime
* A text editor (VS Code, Sublime, or any editor you prefer)
* Optional but recommended: Git for cloning plugins and managing dotfiles
# Claude-supported Setup

> [!info] Semi-automated setup
> You can follow step 1-6 below for manual setup. Alternatively, paste this prompt into a new Claude Code session and it will do most of the work for you.

```
I need to set up Claude Code for optimized token usage, context management, and session continuity. 

The complete setup guide starts here - also check the child pages: https://yt.3ss.tv/articles/DLVRY-A-5445058682/Optimized-Claude-Code-Setup

Please help me automate the setup by:

1. **Creating all necessary files and directories** in ~/.claude/ and project directories
2. **Writing the hook scripts** (auto-handoff.mjs, context-mode-preload.mjs, context-mode-cache-heal.mjs, statusline-command.sh)
3. **Updating settings.json** with permissions, environment variables, hooks, and plugin configuration
4. **Creating CLAUDE.md** as a router template with cross-references to reference files
5. **Creating reference files** (executor-advisor-policy.md, memory-architecture.md, skill-routing.md)
6. **Setting up the memory system** (MEMORY.md structure and example memory files)
7. **Making scripts executable** (chmod +x for bash scripts)

For my setup:
- **Project path:** [YOUR_PROJECT_PATH] (e.g., D:\MyProject)
- **Encoded project path:** [ENCODED_PATH] (e.g., D--MyProject)
- **Shell:** bash (via Claude Code on Windows)
- **Operating system:** [YOUR_OS] (Windows/macOS/Linux)

The setup should include:
- ✅ Core plugins: context-mode, claude-mem, code-review, code-simplifier
- ✅ Executor-advisor strategy with Haiku/Sonnet/Opus tiers
- ✅ Auto-handoff for session continuity via HANDOFF.md
- ✅ Context-mode preload for automatic knowledge base indexing
- ✅ Hooks for cache healing, backend detection, and session management
- ✅ Auto-memory (MEMORY.md) with user/feedback/project/reference types
- ☐ Optional: StatusLine for custom status bar
- ☐ Optional: Sound notifications
- ☐ Optional: Superpowers plugin

Please proceed with the setup and let me know:
1. Each file/directory being created
2. Any required customization (paths, usernames, etc.)
3. When to run `/plugins` to reload config
4. How to verify the setup is working
```
# Manual Setup
## Step 1: Install Plugins
Claude Code's plugin system is the foundation. You'll add two custom marketplaces to pull community plugins, then install four core plugins plus optional ones.

Open `~/.claude/settings.json` and add this to `extraKnownMarketplaces`:
```json
"extraKnownMarketplaces": [
  "mksglu/context-mode",
  "thedotmack/claude-mem"
]
```

Then run `/plugins` in Claude Code and install:
* `context-mode@context-mode` - FTS5 knowledge base for token compression
* `claude-mem@thedotmack` - episodic memory system across sessions
* `code-review@claude-plugins-official` - code quality auditing
* `code-simplifier@claude-plugins-official` - code refactoring suggestions
* Optional: `frontend-design@claude-plugins-official` - UI/UX design patterns

Reload Claude Code after installation to activate.

## Step 2: Core Settings
These settings set your default model, enable plan mode, and configure permission handling so you're not prompted constantly.

Add these to `~/.claude/settings.json`:
```json
{
  "defaultMode": "plan",
  "model": "haiku",
  "env": {
    "PROJECTS_PATH": "C:\\Users\\YourUsername\\Projects"
  },
  "skipDangerousModePermissionPrompt": true,
  "skipAutoPermissionPrompt": true,
  "remoteControlAtStartup": true,
  "agentPushNotifEnabled": true
}
```

Replace `PROJECTS_PATH` with your actual projects directory. This env var is used by hook scripts and reference files.

## Step 3: Install Hooks
Hooks are scripts that fire on session events (start, stop, tool use). You'll install two critical hooks: one for auto-handoff and one for context-mode preload.

Create `~/.claude/hooks/auto-handoff.mjs`:
```javascript
import { writeFileSync } from 'fs';
import { join } from 'path';

const handoffPath = join(process.cwd(), 'HANDOFF.md');
const timestamp = new Date().toISOString();
const content = `# Session Handoff
Stopped at: ${timestamp}
Working directory: ${process.cwd()}

Resume this session with: /letsgo
`;

writeFileSync(handoffPath, content, 'utf8');
```

Create `~/.claude/hooks/context-mode-preload.mjs`:
```javascript
// This hook signals Claude to call ctx_batch_execute at SessionStart
// to index reference files (CLAUDE.md, skill-routing.md, memory index)
console.log('Preloading context-mode knowledge base...');
```

Wire both hooks in `settings.json`:
```json
{
  "hooks": {
    "Stop": "~/.claude/hooks/auto-handoff.mjs",
    "SessionStart": "~/.claude/hooks/context-mode-preload.mjs"
  }
}
```

Test by stopping Claude Code (check for HANDOFF.md in your working directory) and restarting.

## Step 4: Configure CLAUDE.md
`CLAUDE.md` is a router file that tells Claude how to behave in this project. Rather than embedding all instructions inline, it points to reference files - preventing a bloated 3,000-token monolith that kills performance.

Create `~/.claude/CLAUDE.md`:
```markdown
# Global Instructions for Claude Code

## Identity
I'm Sascha, a productivity builder working across YouTube, blogging, Obsidian, and software development.

## Reference Files (Read These, Don't Embed)
- Skill routing: ~/.claude/references/skill-routing.md
- Executor-advisor policy: ~/.claude/references/executor-advisor-policy.md
- Model guidelines: ~/.claude/references/model-guidance.md
- Writing conventions: ~/.claude/references/voice-and-tone.md

## Context Window Management
- Use context-mode MCP tools (ctx_batch_execute, ctx_search, ctx_execute) instead of Bash for large outputs
- Bash only for: git operations, file mutations, mkdir/rm/mv
- All file edits use native Edit/Write tools, never shell

## Session Start Protocol
On new session: index reference files via ctx_batch_execute
On session end: /handoff preserves context for next session

## Writing Style
- No em dashes: use single hyphens surrounded by spaces: - (not -)
- Second person only: "you" not "we"
- Concise: fragments when clear, short synonyms
```

The key insight: this file should be 200 lines max and function as a map, not a container.

## Step 5: Executor-Advisor Strategy
The executor-advisor pattern is a cost-optimization framework that routes work to the right model based on risk level. Create `~/.claude/references/executor-advisor-policy.md`:
```markdown
# Executor-Advisor Model Routing

## Tier 1: Haiku (Default)
Low-risk, high-volume tasks: drafts, research, brainstorming, social copy, summaries.
- Cost: ~$0.80 per 1M tokens
- Latency: fastest

## Tier 2: Sonnet (Auto-Gated)
Medium-risk, customer-facing: video scripts, email campaigns, launch content, titles.
- Cost: ~$3 per 1M tokens
- Trigger: code review tool detects backend/API changes, or you explicitly request

## Tier 3: Opus (User-Confirmed)
High-risk, strategic: architecture decisions, legal/compliance, hiring decisions, financial analysis.
- Cost: ~$15 per 1M tokens
- Trigger: Only after explicit user approval via /fast or CLI flag

## Cost Comparison
- Always-Opus: $15 per 1M tokens
- This setup: avg $1-3 per 1M tokens (60x reduction)
```

Optionally add a `PostToolUse` hook that detects when you've modified backend files and auto-escalates to Sonnet:
```javascript
const changedFiles = /* files changed in current session */;
if (changedFiles.some(f => f.includes('api/') || f.includes('server/'))) {
  console.log('Backend changes detected. Escalate to Sonnet? /upgrade');
}
```

## Step 6: Memory System
Unlike context-mode's ephemeral FTS5 index, your memory system is persistent, searchable facts about you and your projects. Create `~/.claude/projects/YOUR_PROJECT/memory/MEMORY.md`:
```markdown
# Memory Index
- [User Role](user_role.md) - Your background and expertise
- [Feedback](feedback_*.md) - How you prefer to work
- [Project Context](project_context.md) - Active goals and constraints
- [References](references.md) - External resources and where to find them
```

Create supporting files:
* `user_role.md` - "I'm a productivity YouTuber building in Obsidian and blog. I write for a solo creator audience, not enterprises."
* `feedback_testing.md` - "Always test UI in the browser before claiming success. Type checking and tests verify code, not feature correctness."
* `project_context.md` - "We're optimizing Claude Code setup for power users. Target audience: developers and productivity enthusiasts."
* `references.md` - "YouTube channel: LeanProductivity. Blog: substack. GitHub org: 3SS-consulting."

The memory system lives alongside context-mode but serves a different purpose: context-mode is a sandbox for large knowledge bases; memory is stable facts that inform every session.

## The Automated Path
If manual setup feels tedious, article 00 in the YouTrack KB provides a single paste-ready prompt that automates all 7 steps via Claude itself. Paste it, fill in your project path and OS, and Claude creates files, wires hooks, and configures settings in one go. Recommended if you're setting up multiple machines or want to skip manual steps.
# Optional Enhancements
## StatusLine
Replace the default Claude Code status bar with a custom one showing your current path, git branch, active model, context% usage with color thresholds, estimated token cost, and input/output token counts. Create `~/.claude/statusline-command.sh`:
```bash
#!/bin/bash
PATH_DISPLAY=$(pwd | sed "s|$HOME|~|")
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "-")
MODEL=$(cat ~/.claude/settings.json | jq -r '.model // "unknown"')
CONTEXT_PCT="45%"
COST=$(echo "scale=2; 45 * 0.000003" | bc)
echo "$PATH_DISPLAY | $BRANCH | $MODEL | $CONTEXT_PCT | \$$COST"
```

Wire in settings.json:
```json
{
  "statusLine": {
    "command": "bash ~/.claude/statusline-command.sh"
  }
}
```

## Sound Notifications
Tired of silent permission prompts? Wire audio notifications for idle and permission events. Create hooks that play `.wav` files from `~/.claude/sounds/`:
```json
{
  "hooks": {
    "idle_prompt": "powershell -Command \"(New-Object System.Media.SoundPlayer('~/.claude/sounds/ready.wav')).PlaySync()\"",
    "permission_prompt": "powershell -Command \"(New-Object System.Media.SoundPlayer('~/.claude/sounds/permission.wav')).PlaySync()\""
  }
}
```

On macOS, use `afplay` instead of PowerShell `SoundPlayer`.

## Superpowers for Dev
If you code regularly, install `superpowers@claude-plugins-official` - a collection of 14 auto-activating skills that enforce dev discipline: brainstorm → plan → TDD → debug → verify → code review. The skills activate contextually based on what you're trying to do (no manual triggering). They don't interfere with context-mode or the cost optimization setup - they just add guardrails.
# Verify Your Setup
Run this checklist to confirm everything is wired correctly:
1. **Plugins loaded:** Run `/plugins list` - you should see context-mode, claude-mem, code-review, code-simplifier
2. **Preload message:** Create a new session - you should see "Preloading context-mode knowledge base..." in the startup output
3. **HANDOFF.md created:** Stop Claude Code, then check your working directory - HANDOFF.md should exist with timestamp and working directory info
4. **Token savings visible:** Run `ctx stats` in a session - context-mode should show 70%+ savings
5. **Plan mode active:** Try a non-read-only action (create a file) - Claude should ask for approval before executing
6. **Memory accessible:** Run `/mem-search "your query"` - past sessions should surface if relevant
7. **Model routing working:** In settings.json, confirm `model: haiku` and `defaultMode: plan` are set

If any step fails, see the Troubleshooting section below.
# FAQ
> [!question]- Do I need all five plugins or can I pick and choose?
> You can absolutely mix and match. The core three are context-mode (token savings), claude-mem (memory), and code-review (quality). code-simplifier is optional. If you don't code, skip code-review and code-simplifier entirely - context-mode and claude-mem work standalone.

> [!question]- Will defaultMode: plan slow me down?
> Not after the first week. Plan mode requires approval before execution, which takes seconds - and saves you from surprise outputs that waste time debugging. You'll find it forces better decision-making, and the time investment pays for itself quickly.

> [!question]- What's the actual cost difference between running Haiku vs Sonnet vs Opus?
> - [ ] As of May 2026: Haiku costs ~$0.80 per 1M input tokens, Sonnet ~$3, Opus ~$15. For a typical session mixing models (70% Haiku, 20% Sonnet, 10% Opus), you'll average $1-3 per 1M tokens. Compare that to always-Opus at $15 - you're saving 80-93% on the token bill alone.

> [!question]- How does context-mode preserve context across sessions?
> context-mode uses an FTS5 database to index large knowledge bases (references, past discussions, documentation). Instead of stuffing everything into every prompt, it stores data in a searchable sandbox and pulls only relevant chunks when you run ctx_search queries. This keeps your context window lean and your tokens savings high.

> [!question]- What if a hook fails silently - how do I debug it?
> Hooks are Node.js scripts, so they'll often fail without warning. Test manually: run `node ~/.claude/hooks/auto-handoff.mjs` in your terminal and watch for errors. Check that node is on your PATH, that the .mjs file exists, and that JSON in settings.json is syntactically valid (use a JSON validator). If hooks still don't fire, restart Claude Code - changes to settings.json don't always reload immediately.

# Infographic
![[Optimized Claude Code Setup.webp]]