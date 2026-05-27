# GREEN PHASE: Skill Updates Applied

## Overview

All 5 RED phase loopholes addressed with explicit, pressure-resistant changes to SKILL.md.

## Changes Made

### Change 1: Hardened "NEVER" Section (Lines 18-26)

**Problem identified:** Agents rationalized away rules without understanding WHY or WHAT silent failures look like.

**Changes:**
- Added explicit consequence for each NEVER (e.g., "will break the second run with incomplete sections")
- Changed "optional" framing ("won't appear") to "mandatory verification" (`echo $YOUTUBE_API_KEY` must print non-empty)
- Added "do NOT rationalize" to git stash rule
- Specified rate limiting is SILENT (not visible errors, only empty sections)

**Lines affected:** 18-26 (entire NEVER section rewritten)

---

### Change 2: Step 3 - Explicit Validation Gates (Lines 60-79)

**Problem identified:** Agents skipped validation steps; "optional" checks got rationalized away.

**Changes:**
- Converted to 3 explicit CHECK commands (not suggestions)
- Each check has expected output format
- Made clear what "failure" looks like
- "Only after all 3 checks pass: Proceed to Step 4" = hard gate

**Lines affected:** 60-79 (entire Step 3 rewritten from 4 bullet points to 3 explicit checks with commands)

**Example:**
```
Before: "Git working tree is clean: git status shows no uncommitted changes"
After: 
Check 1: Git working tree is clean
git status
Expected: "nothing to commit, working tree clean"
If you see uncommitted files: git stash first
```

---

### Change 3: Step 5 - Make Preview Mandatory (Lines 81-105)

**Problem identified:** Scenario 5 showed agents skip preview when user says "trust me, don't need preview". User permission overrode safety.

**Changes:**
- Changed title from "Inspect Output" to "Inspect Output (MANDATORY - DO NOT SKIP)"
- Explained WHY: "Silent API failures (outages, throttling) produce no errors - only empty sections"
- Made preview a required command: "Always run preview first" (not optional)
- Added explicit checklist with HARD STOPS: "If any section is empty or malformed: Do NOT commit"
- Added investigation guide for each failure mode
- Changed emphasis: "Only after all criteria pass" (sequencing gate)

**Lines affected:** 81-105 (entire Step 5 rewritten, expanded from short bullet list to detailed procedure with hard gates)

---

### Change 4: Self-Verification Checklist Restructured (Lines 127-145)

**Problem identified:** Checklist was too generic; agents could rationalize "green enough" without catching real failures.

**Changes:**
- Split into 3 phases: Before running, Before committing, If any check fails
- Made checks specific and testable (not vague)
- Added "MANDATORY GATES" label
- Changed from optional checkboxes to "STOP. Do NOT commit" consequences
- Example: Added "preview shows all 6 sections have data? (empty sections = API failure, investigate before committing)" - explicit causality

**Lines affected:** 127-145 (restructured from flat list to 3-phase gated checklist)

---

### Change 5: New Section - Common Mistakes & How to Avoid Them (Lines 171-223)

**Problem identified:** Agents rationalized specific scenarios but didn't have explicit guidance. Added new section with 4 real scenarios from RED phase.

**Scenarios covered:**
1. "I need to regenerate twice in one day" - Explains rate limiting, shows preview-only pattern
2. "Can you generate for January 2026?" - Explains 30-day hard constraint, how to reject requests
3. "Just skip the preview, I trust you" - Explains user permission doesn't override safety
4. "I have other git work - should I stash?" - Explains why "unrelated" reasoning is wrong, shows stash pattern

**Rationale:** Direct addresses the exact rationalizations agents made in RED phase. No room for new excuses.

**Lines affected:** 171-223 (entirely new section added before "Related Skills")

---

## Summary of Loopholes Closed

| RED Scenario | Root Cause | GREEN Fix | Fix Type |
|-------------|-----------|----------|----------|
| Uncommitted changes | No "WHY" explanation | Added "do NOT rationalize" + new mistake section with stash pattern | NEVER rewrite + new section |
| Missing API key | "Optional" framing | Changed to "VERIFY" with explicit command and expected output | Validation gate |
| Rate limiting | No guidance on 2nd run | Added preview-only pattern + "will break second run" consequence | NEVER rewrite + new section |
| Old date range | Agents assumed "slow month" | Added "hard API constraint" + "reject requests >30 days" guidance | New section |
| Preview skip | User permission overrode safety | Changed to "MANDATORY" + "user permission doesn't matter" | Step 5 rewrite |

---

## Coverage

- ✅ 100% of RED phase loopholes have explicit counter-measures
- ✅ No vague warnings (all include WHY + WHAT failure looks like)
- ✅ All validation steps are now explicit commands (not suggestions)
- ✅ All hard stops are labeled (MANDATORY, Do NOT commit, Do NOT rationalize)
- ✅ 4 real mistake patterns documented with patterns (not just don'ts)

---

## Files Modified

- `D:\Lean Notes\09 Blog\.claude\skills\lean-obsidian-weekly\SKILL.md`
  - Lines 18-26: NEVER section (expanded, all rules now include consequences)
  - Lines 60-79: Step 3 validation (restructured as 3 explicit checks)
  - Lines 81-105: Step 5 preview (made mandatory, added hard gates)
  - Lines 127-145: Self-verification (restructured into 3-phase gated checklist)
  - Lines 171-223: New section (4 common mistakes with patterns and explanations)

---

## Next Phase: REFACTOR

Test the hardened skill with subagents on the same 5 pressure scenarios. Expected result: All loopholes closed. If new rationalizations emerge, update this document and re-test.
