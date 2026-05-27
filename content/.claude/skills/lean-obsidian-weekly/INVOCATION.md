# Direct Script Invocation

For automated or scripted workflows, invoke `run_newsletter.py` directly instead of using the skill.

## Location

```
D:\Lean Notes\09 Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py
```

## Quick Commands

### Preview existing cache

```bash
cd D:\GitProjects\lean-obsidian-weekly
python "D:\Lean Notes\09 Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py" --mode preview
```

### Full pipeline (fetch + generate + commit)

```bash
cd D:\GitProjects\lean-obsidian-weekly
export YOUTUBE_API_KEY="AIzaSyAX6oXwIFKwAMZ9oyBZ4uZc7m-d3jruzuU"
python "D:\Lean Notes\09 Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py" --mode full
```

### Full pipeline with custom dates

```bash
cd D:\GitProjects\lean-obsidian-weekly
python "D:\Lean Notes\09 Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py" \
  --mode full \
  --start-date 2026-05-01 \
  --end-date 2026-05-07
```

### Full pipeline without committing

```bash
cd D:\GitProjects\lean-obsidian-weekly
python "D:\Lean Notes\09 Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py" \
  --mode full \
  --skip-commit
```

### Preview with custom output name

```bash
cd D:\GitProjects\lean-obsidian-weekly
python "D:\Lean Notes\09 Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py" \
  --mode preview \
  --output "Test Newsletter.md"
```

## Usage in Bash/PowerShell Scripts

```bash
#!/bin/bash
cd D:\GitProjects\lean-obsidian-weekly
export YOUTUBE_API_KEY="..." # set from CI/CD secret
python "D:\Lean Notes\09 Blog\.claude\skills\lean-obsidian-weekly\scripts\run_newsletter.py" \
  --mode full

# Check exit code
if [ $? -eq 0 ]; then
  echo "Newsletter generated successfully"
  # Trigger Substack publish
else
  echo "Newsletter generation failed"
  exit 1
fi
```

## Exit Codes

- `0` — Success (no errors)
- `1` — Failure (errors encountered, see log)

## Typical Workflow in CI/CD

1. **Scheduled Tuesday 6 AM:**
   ```bash
   python run_newsletter.py --mode full
   ```

2. **If full pipeline succeeds:**
   - Cache is committed and pushed
   - Output file is saved to `D:\Lean Notes\09 Blog\Substack\`
   - Next step: post to Substack via `/substack-publish`

3. **If full pipeline fails:**
   - Error logged and printed
   - No git operations performed
   - Investigate errors before retry

## Script Reference

For full argument documentation, see: `scripts/README.md`

For CLI command reference, see: `references/cli-commands.md`
