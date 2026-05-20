# RCM Pulse Weekly — Newsletter Generation Procedure

This file is the **source of truth** for the weekly newsletter generation.

- **Recurring cowork routine** (`trig_011MyvQ9AcDW2LQyHJNFTUxw`, Fri+Sat 9 AM Phoenix) reads this file and executes it. To change how the newsletter is generated, edit this file and commit — no need to update the routine config.
- For **off-cycle backfills**, see the "Manual / backfill override" section at the bottom.

---

## EXECUTE — start here if you are the agent

You are generating an issue of the **RCM Pulse Weekly** newsletter for the GitHub repo `shanmukund/rcm-newsletter`. The repo is checked out at your working directory.

**Read `.claude/rules/*.md` FIRST.** Those files contain the authoritative content-strategy, design-template, quality-control, and workflow rules — follow them exactly. This file orchestrates the run; the rules files define the substance.

### STEP 1 — Compute the newsletter date

```bash
TODAY_WD=$(date -u +%u)                                  # 1=Mon ... 7=Sun

if [ "$TODAY_WD" = "5" ]; then
  # Friday — newsletter is dated today
  NEWSLETTER_DATE=$(date -u +%Y-%m-%d)
  RUN_MODE="primary"
elif [ "$TODAY_WD" = "6" ]; then
  # Saturday — backup retry for yesterday's Friday
  NEWSLETTER_DATE=$(date -u -d "yesterday" +%Y-%m-%d)
  RUN_MODE="backup"
elif [ -n "$NEWSLETTER_DATE_OVERRIDE" ]; then
  # Manual / backfill override — see "Manual run" section
  NEWSLETTER_DATE="$NEWSLETTER_DATE_OVERRIDE"
  RUN_MODE="backfill"
else
  echo "ERROR: routine fired on a day other than Fri/Sat with no NEWSLETTER_DATE_OVERRIDE set." >&2
  exit 1
fi

MONTH=$(date -u -d "$NEWSLETTER_DATE" +%-m)
DAY=$(date -u -d "$NEWSLETTER_DATE" +%-d)
ISSUE=$(( (DAY - 1) / 7 + 1 ))
MD_FILE="RCM_Weekly_Newsletter_${NEWSLETTER_DATE}.md"
HTML_FILE="RCM_Weekly_Newsletter_${NEWSLETTER_DATE}.html"
NEXT_FRIDAY=$(date -u -d "$NEWSLETTER_DATE + 7 days" +"%B %-d, %Y")

echo "Mode=$RUN_MODE  Date=$NEWSLETTER_DATE  Volume=$MONTH  Issue=$ISSUE"
```

### STEP 2 — Idempotency check

If `$HTML_FILE` already exists in the repo root, the issue was already published. Print **"Already exists, exiting (mode=$RUN_MODE)"** and `exit 0`. Do not regenerate.

This is what makes Saturday a true backup: if Friday's run succeeded, Saturday sees the file and exits cleanly.

### STEP 3 — Research

Use **WebSearch** across all 12 research areas in `.claude/rules/workflow.md`:

1. CMS / Medicare / Medicaid regulatory changes
2. AAPC coding updates (ICD-10, CPT, HCPCS)
3. AI and automation trends in medical billing and RCM
4. Payer policy changes (UHC, Cigna, Aetna, Humana, BCBS)
5. Prior authorization reform
6. RCM technology trends (AI denial mgmt, autonomous coding, RPA)
7. Workflow automation best practices
8. Revenue velocity improvement strategies
9. Healthcare IT news on billing / RCM
10. CMS interoperability and price transparency rule updates
11. Independent medical practice trends (financial pressure, consolidation, RCM benchmarks)
12. Specialty-specific RCM news for Primary Care, Cardiology, Orthopedics, Oncology, Radiology, Neurology, Mental Health, Gastroenterology

Scope to news from approximately the week ending on `$NEWSLETTER_DATE`.

**Do not duplicate headlines from previous issues.** Read the most recent 2–3 `RCM_Weekly_Newsletter_*.md` files first and pick fresh angles or newer developments.

### STEP 4 — Write the markdown

Write `$MD_FILE` per `.claude/rules/content-strategy.md`:

- All **10 sections** with section numbers, headlines, and cited sources on every section
- At least one data point / statistic per section
- All three emphasis pillars represented (workflow automation, AI adoption, revenue velocity tech)
- Independent Practice Watch (§8) must include a "Where You Should Be" benchmark
- Specialty RCM Spotlight (§9) must cover at minimum Primary Care, Cardiology, Orthopedics, Oncology
- **Big Stat** closing block
- Header shows the formatted date and `Volume $MONTH, Issue $ISSUE`

### STEP 5 — Pick the structural template

Find the most recent existing `RCM_Weekly_Newsletter_*.html` (sort filenames descending, exclude `$HTML_FILE`). Use that file as your structural template — **same CSS verbatim, same canvas + bubble-animation `<script>` verbatim**, same layout. Apply the full design from `.claude/rules/design-template.md`.

### STEP 6 — Write the HTML

Write `$HTML_FILE`. Populate header, TOC, all 10 sections, Big Stat block, footer. Footer must say `Next issue: $NEXT_FRIDAY`. Use HTML entities (`&mdash;`, `&ndash;`, `&amp;`) — no raw `--` or `&` in text content.

### STEP 7 — Update index.html

- Add a new `<div class="newsletter-item">` block as the **first** entry inside `.newsletter-list` (right after `<h2 class="section-title">Latest Issues</h2>`)
- Anchor text must be a **descriptive 2–3-story title** naming the actual top stories — NOT just "RCM Pulse Weekly"
- Include `<span class="newsletter-date">` (formatted date) and `<span class="newsletter-volume">Volume $MONTH, Issue $ISSUE</span>`
- Include a bullet-separated topics summary in `.newsletter-topics`
- Find the existing `<div class="stat-number">N</div>` immediately followed by `<div class="stat-label">Issues</div>` and **increment N by 1**

### STEP 8 — Self-audit

Run the full checklist in `.claude/rules/quality-control.md` (content + design + formatting). Fix anything that fails before proceeding.

### STEP 9 — Verify before committing

This is the most important step — previous automation pipelines silently no-op'd because nothing checked file output. **All four checks below MUST pass:**

```bash
test -f "$MD_FILE" && [ "$(stat -c %s "$MD_FILE")" -ge 8000 ] \
  || { echo "VERIFICATION FAILED: $MD_FILE missing or under 8KB"; exit 1; }

test -f "$HTML_FILE" && [ "$(stat -c %s "$HTML_FILE")" -ge 30000 ] \
  || { echo "VERIFICATION FAILED: $HTML_FILE missing or under 30KB"; exit 1; }

git diff --quiet index.html && { echo "VERIFICATION FAILED: index.html not modified"; exit 1; } || true

for id in regulatory prior-auth ai-automation coding revenue-velocity \
          tech-spotlight compliance independent-practice specialty action-items; do
  grep -q "id=\"$id\"" "$HTML_FILE" \
    || { echo "VERIFICATION FAILED: missing section #$id"; exit 1; }
done

echo "Verification passed."
```

If any check fails, exit 1. **Do not commit a broken issue.**

### STEP 10 — Commit

Commit **only these three files** — no logs, no drafts, no other changes:

```bash
git add "$MD_FILE" "$HTML_FILE" index.html
COMMIT_MSG="Add newsletter for $NEWSLETTER_DATE (Volume $MONTH, Issue $ISSUE)"
if [ "$RUN_MODE" = "backup" ]; then COMMIT_MSG="$COMMIT_MSG — Saturday backup"; fi
if [ "$RUN_MODE" = "backfill" ]; then COMMIT_MSG="$COMMIT_MSG — backfill"; fi
git commit -m "$COMMIT_MSG"
```

### STEP 11 — Push

```bash
git pull --rebase origin main
git push origin main
```

### STEP 12 — Final summary

Print:
- The 10 section headlines you produced
- Commit hash: `git rev-parse HEAD`
- The full `git push` output
- Live URL: `https://shanmukund.github.io/rcm-newsletter/$HTML_FILE`

---

## Hard rules — DO NOT

- Skip the research step or reuse content from previous issues
- Commit if any verification check fails — exit 1 instead so the failure is visible
- Commit files other than the three listed (no `.log` files, drafts, or anything else)
- Use `--no-verify`, `--force`, or any flag that bypasses checks
- Recalculate `NEWSLETTER_DATE` from anything other than the bash logic in Step 1

---

## Manual / backfill override

When you need to generate an off-cycle issue (missed Friday, mid-week catch-up):

1. Compute the target Friday's date in `YYYY-MM-DD` form.
2. Start a Claude Cowork session attached to `shanmukund/rcm-newsletter`.
3. Send the agent this message:

> Set `NEWSLETTER_DATE_OVERRIDE=2026-MM-DD` then read `NEWSLETTER_PROMPT.md` from the repo root and execute it.

The Step 1 bash logic picks up the override and proceeds with `RUN_MODE=backfill`. Everything else (research, generation, verification, commit) is identical to a scheduled run.
