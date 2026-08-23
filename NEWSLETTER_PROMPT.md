# RCM Pulse Weekly — Newsletter Generation Procedure

This file is the **source of truth** for the weekly newsletter generation.

- **The GitHub Actions workflow** `.github/workflows/weekly-newsletter.yml` (Fri + Sat 9 AM Phoenix) reads this file and executes it. To change how the newsletter is generated, edit this file and commit — no need to touch the workflow.
- The workflow **computes the dates and performs the push itself**. When it invokes you it hands you the date, volume, and issue number; you skip Step 1 and stop after Step 10.
- For **off-cycle backfills**, see the "Manual / backfill override" section at the bottom.
- The claude.ai routine `trig_011MyvQ9AcDW2LQyHJNFTUxw` was the generator from 2026-05-19 until **2026-08-22, when it was disabled**. Do not re-enable it without reading the outage note in the watchdog section below.

---

## EXECUTE — start here if you are the agent

You are generating an issue of the **RCM Pulse Weekly** newsletter for the GitHub repo `shanmukund/rcm-newsletter`. The repo is checked out at your working directory.

**Read `.claude/rules/*.md` FIRST.** Those files contain the authoritative content-strategy, design-template, quality-control, and workflow rules — follow them exactly. This file orchestrates the run; the rules files define the substance.

### STEP 1 — Compute the newsletter date

**If your prompt already gave you the newsletter date, volume, and issue number, skip this step entirely and use those values.** The GitHub Actions workflow computes them before it starts you, and a backfill run targets a date that is not today — recalculating from `date` would silently overwrite it with the wrong week.

Only when no date was supplied:

```bash
TODAY_WD=$(date -u +%u)                                  # 1=Mon ... 7=Sun

if [ "$TODAY_WD" = "5" ]; then
  # Friday — newsletter is dated today
  NEWSLETTER_DATE=$(date -u +%Y-%m-%d)
  RUN_MODE="primary"
elif [ "$TODAY_WD" = "6" ]; then
  # Saturday — backup retry for yesterday's Friday. Never a Saturday-dated issue.
  NEWSLETTER_DATE=$(date -u -d "yesterday" +%Y-%m-%d)
  RUN_MODE="backup"
elif [ -n "$NEWSLETTER_DATE_OVERRIDE" ]; then
  # Manual / backfill override — see "Manual run" section
  NEWSLETTER_DATE="$NEWSLETTER_DATE_OVERRIDE"
  RUN_MODE="backfill"
else
  echo "ERROR: fired on a day other than Fri/Sat with no NEWSLETTER_DATE_OVERRIDE set." >&2
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

Every derived value — `MONTH`, `DAY`, `ISSUE`, `NEXT_FRIDAY`, the formatted header date — must come from `$NEWSLETTER_DATE`, never from "today". Deriving the issue number from today's date while writing a backfill is how the 2026-08-07 and 2026-08-14 issues both shipped stamped "Issue 4".

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
- On a **backfill**, insert in date order rather than at the top, so the list stays reverse-chronological

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

The GitHub Actions workflow re-runs every one of these checks itself after you finish, plus a date/volume/issue stamp check. It does not take your word for any of it. Passing them here just means the run gets that far.

### STEP 10 — Commit

Commit **only these three files** — no logs, no drafts, no other changes:

```bash
git add "$MD_FILE" "$HTML_FILE" index.html
COMMIT_MSG="Add newsletter for $NEWSLETTER_DATE (Volume $MONTH, Issue $ISSUE)"
if [ "$RUN_MODE" = "backup" ]; then COMMIT_MSG="$COMMIT_MSG — Saturday backup"; fi
if [ "$RUN_MODE" = "backfill" ]; then COMMIT_MSG="$COMMIT_MSG — backfill"; fi
git commit -m "$COMMIT_MSG"
```

**If the GitHub Actions workflow started you, STOP HERE.** The workflow performs the push and confirms it against the remote. Do not push, and do not leave anything running in the background.

### STEP 11 — Push (only when running outside the workflow)

**Read this before you push. An issue was lost here.**

On 2026-08-21 the Friday run completed a full, verified newsletter, hit a 403 on `git push`, launched the backoff retry loop **as a background task**, and ended its turn four seconds later while the loop was still on its first sleep. The sandbox went idle. Thirty-one minutes later the agent resumed, never read the background task's output, reported *"push succeeded on retry"*, and sent a mobile notification saying the issue was live. The commit had never left the sandbox. The same thing happened on 08-07 and 08-14. Three complete issues were written and thrown away.

Two rules follow from that, and they are absolute:

1. **Run the push loop in the FOREGROUND.** Never `run_in_background`, never `&`. Blocking for 31 minutes is the intended behavior.
2. **Confirm against the remote before claiming anything.** A push that returned 0 is not proof. `git ls-remote` is.

```bash
git pull --rebase origin main
PUSH_OK=""
for wait in 0 30 60 120 240 480 960; do
  [ "$wait" -gt 0 ] && sleep "$wait"
  if git push origin main; then PUSH_OK=1; break; fi
  echo "Push failed; retrying after the next backoff interval..."
  git pull --rebase origin main || true
done
[ -n "$PUSH_OK" ] || { echo "PUSH FAILED after ~31 minutes — real auth/permission problem, not transient"; exit 1; }

# Do not skip this. The push exit code is not evidence.
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git ls-remote origin refs/heads/main | cut -f1)
[ "$LOCAL" = "$REMOTE" ] \
  || { echo "PUSH LIED: origin/main is $REMOTE, expected $LOCAL"; exit 1; }
echo "Confirmed on origin/main: $REMOTE"
```

A repeated 403 across separate runs is **not** a transient blip — it means the credential is no longer authorized. Stop retrying and say so plainly rather than reporting success.

### STEP 12 — Final summary

Print:
- The 10 section headlines you produced
- Commit hash: `git rev-parse HEAD`
- The `git ls-remote origin refs/heads/main` output proving the commit is on the remote
- Live URL: `https://www.vaqyaweekly.com/$HTML_FILE`

State only what you verified. If the push did not confirm, say the issue was **not** published and exit non-zero — a false success report costs a week, because the watchdog gets contradicted by your own notification.

---

## Hard rules — DO NOT

- Skip the research step or reuse content from previous issues
- Recalculate `NEWSLETTER_DATE`, the volume, or the issue number from today's date when a target date was supplied
- Commit if any verification check fails — exit 1 instead so the failure is visible
- Commit files other than the three listed (no `.log` files, drafts, or anything else)
- Use `--force` or any flag that bypasses checks or rewrites published history
- Background the push, or end a turn with a background task still running
- Report a push, a publication, or a check as successful without having verified it in that same turn

---

## Watchdog / verification layer

Friday publication is the commitment. The Saturday 9 AM run is **failure recovery, not a publication day** — it regenerates *Friday's* issue and no-ops if Friday landed. A Friday miss is a P1.

| Layer | What | When | Alerts |
|---|---|---|---|
| 1. Generator | GitHub Action `.github/workflows/weekly-newsletter.yml` runs this file, then verifies the output and pushes it itself | Fri + Sat 9 AM Phoenix | Opens an `automation`/`urgent` issue on failure, and fails the run |
| 2. Cloud watchdog | GitHub Action `.github/workflows/verify-newsletter.yml` — checks the expected `RCM_Weekly_Newsletter_<friday>.html` is committed AND returns HTTP 200 on www.vaqyaweekly.com | Fri 1 PM + Sat 10 AM Phoenix | Opens/updates a `missed-publication` issue **and** fails the run — two email paths |

Both layers run entirely in GitHub's cloud on the auto-issued `GITHUB_TOKEN`, independent of any local machine, any claude.ai routine, and any stored credential.

**Credentials (hard rule — no expiring or manually-rotated tokens in unattended automation):** everything uses the workflow's auto-issued `GITHUB_TOKEN` — minted fresh per run, scoped to this repo, never expires, nothing to rotate. **Do not reintroduce a personal access token.** The 2026-08 outage was a PAT stored in a claude.ai trigger config that stopped being authorized after 2026-07-31; three Fridays failed silently because nothing checked whether the push had actually landed. If you find yourself pasting a `ghp_…` token anywhere, stop — the answer is a workflow, not a token.

If a watchdog fires: open the failed Actions run, read which step failed, and re-run the generator with `newsletter_date` set to the missed Friday. Close the GitHub issue only after the live URL returns 200.

---

## Manual / backfill override

To generate an off-cycle issue (missed Friday, mid-week catch-up), **use the workflow** — it applies the same verification and push confirmation as a scheduled run:

> GitHub → Actions → **"Weekly RCM Newsletter — Auto-Generate"** → **Run workflow** → set **newsletter_date** to the target Friday (`YYYY-MM-DD`) → Run.

The workflow sets `RUN_MODE=backfill` and proceeds identically to a scheduled run. It refuses to run on a non-Friday/Saturday unless you supply that date, so it can never invent one.

To run it by hand in a local Claude Code session against this repo instead:

> Set `NEWSLETTER_DATE_OVERRIDE=2026-MM-DD` then read `NEWSLETTER_PROMPT.md` from the repo root and execute it, including Step 11.
