---
name: blog-update
description: Review and publish blog content changes for the LeanProductivity Quartz blog. Shows a summary of what changed, flags issues, and requires explicit approval before publishing. Use when the user says "/blog-update", "publish blog", "update blog", "push blog changes", or wants to deploy content to the live site.
---

# Blog Update Skill

Review pending content changes, present a summary for approval, then execute `publish.ps1`.

## NEVER Do

- NEVER run `publish.ps1` if non-content files are also staged — the script only commits `content/` but leaves other staged files in a confusing half-staged state. Check `git status` first and warn.
- NEVER publish without confirming the branch is `v4` — pushing to any other branch won't trigger Vercel deployment, and the script hardcodes `git push origin v4`.
- NEVER present a summary based on filenames alone — always read actual frontmatter, because titles frequently differ from filenames and renamed files appear as add+delete pairs.
- NEVER assume all `.md` changes are posts — files in `content/zAttachments/` are assets, not posts. The script includes them automatically without filtering.
- NEVER modify blog content files — this skill only reviews and publishes.
- NEVER run `publish.ps1` without showing the summary and getting explicit user approval first.

## publish.ps1 Behavior (Expert Knowledge)

Understanding these behaviors prevents surprises:

- **Staging side effect**: The script runs `git add content/` as its first action. This stages ALL content changes, including files you might not intend to publish. Your pre-publish review must happen BEFORE the script runs.
- **Draft/future filtering unstages files**: Filtered posts are removed from staging via `git reset HEAD -- $file`. After a cancelled or filtered publish, previously staged content files may be unstaged. This is expected, not an error.
- **Counts are post-filter**: The auto-generated commit message (e.g., "content: add 3 new, update 2") counts files AFTER draft/future filtering. If 5 files changed but 2 are drafts, the message says "add 3 new."
- **Attachments are never filtered**: Only `.md` files are checked for draft/future status. Images and other assets in `content/zAttachments/` always pass through.
- **`$ErrorActionPreference = "Stop"`**: Any git error halts execution immediately. If `git push` fails, the commit still exists locally — it is NOT rolled back.
- **Unparseable dates are included**: If a post's `date` field can't be parsed, the script includes it (doesn't filter it). This is intentional but worth flagging to the user.

## Step 1: Pre-Flight Checks

Run git status, diff, log, and branch check in parallel from `$PROJECTS_PATH\quartz-blog`.

**Exit early if**:
- No changes in `content/` — tell user "nothing to publish" and stop.
- Not on `v4` branch — warn and stop. Do not switch branches automatically.
- Non-content files are staged — warn the user with the specific filenames. Ask whether to proceed (publish.ps1 won't commit them, but they'll remain staged) or to unstage them first.

**Selective publishing is not supported**: The script is all-or-nothing for `content/`. If the user wants to publish only some changed files, acknowledge this limitation and suggest stashing unwanted changes first (`git stash push -m "hold back" -- content/file-to-skip.md`).

## Step 2: Analyze Changes

Read each changed `.md` file's frontmatter. Extract: `title`, `date`, `draft`, `categories`. Classify as new/updated/deleted. Separate attachments (`content/zAttachments/`). For updated posts, note whether the change is content vs frontmatter-only.

**Flag issues** (these mirror what `publish.ps1` will filter):
- `draft: true` — will be unstaged by script
- Future `date` — will be unstaged by script
- Missing `title` or `date` — will still publish but may render poorly

**For 20+ changed files**: summarize by category count instead of listing every file. Ask if user wants the full list.

## Step 3: Present Summary & Get Approval

Before presenting, consider: Is this a routine update (few modified files) or a significant publish (new posts, category changes)? Adjust detail level — routine updates need a compact summary, significant publishes deserve per-post detail.

Present a summary with: posts that will be published (title, date, new/updated, categories), posts filtered out (with reason), attachment counts, and the auto-generated commit message.

Ask: **Approve, modify commit message, or cancel?**

Wait for explicit answer. Do not proceed without one.

## Step 4: Execute

On approval, run `pwsh -File "$PROJECTS_PATH\quartz-blog\publish.ps1"` (add `-Message "..."` if user provided a custom message).

**For large or unfamiliar change sets**: Consider running with `-DryRun` first to verify the script's filtering matches your analysis, then re-run without `-DryRun` on confirmation.

## Step 5: Confirm or Recover

**On success**: Report commit hash (`git log --oneline -1`), confirm push succeeded, remind that Vercel deploys automatically. Site: https://blog.sascha-kasper.com

**On push failure** (most common error):
- Upstream has new commits → tell user to run `git pull --rebase origin v4` then re-run `/blog-update`
- Auth failure → tell user to check git credentials
- The local commit still exists — nothing is lost

**On script error**: Read the error output. The commit may or may not have been created. Run `git log --oneline -1` and `git status` to determine state, then report clearly.

## Self-Verification Checklist

Before presenting the publish summary, verify:
- [ ] Branch is confirmed as `v4`
- [ ] No non-content files are staged (or user is warned about them)
- [ ] All changed `.md` files have been read and classified (new/updated/deleted)
- [ ] Draft and future-dated posts are flagged (will be filtered by script)
- [ ] Attachments in `content/zAttachments/` are identified separately from posts
- [ ] Summary matches what `publish.ps1` will actually do (accounts for filtering)
- [ ] User has given explicit approval before execution

## Cross-References

Related skills: `/blog-post` (new posts), `/blog-book` (book reviews), `/blog-wiki` (wiki entries), `/lp-social-guru` (social promotion after update).
