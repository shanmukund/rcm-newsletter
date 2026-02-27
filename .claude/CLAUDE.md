# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Weekly newsletter ("RCM Pulse Weekly") on Revenue Cycle Management for medical practices. Each issue is researched from public domain sources, written in Markdown, then rendered as a self-contained HTML file using a custom minimalist template.

## How to Generate a New Issue

Ask Claude to "generate the next weekly newsletter" — the full process is defined in the rules files. In short:

1. **Research** — Web search across 10 RCM topic areas (CMS, AAPC, payers, AI, coding, etc.)
2. **Draft Markdown** — `RCM_Weekly_Newsletter_YYYY-MM-DD.md`
3. **Generate HTML** — `RCM_Weekly_Newsletter_YYYY-MM-DD.html` using the design template
4. **Self-audit** — Run the quality checklist before delivering

## File Structure

```
RCM_Weekly_Newsletter_YYYY-MM-DD.md    # Content (Markdown)
RCM_Weekly_Newsletter_YYYY-MM-DD.html  # Published version (self-contained HTML)
```

Date uses the Monday of the newsletter week. Volume increments yearly (Volume 1 = 2026), issue increments weekly.

## Rules (Detailed Specifications)

All rules live in `.claude/rules/` and are loaded automatically:

- **`content-strategy.md`** — Topic scope (RCM for medical practices), required source categories (CMS.gov, AAPC, HFMA, payer portals, industry pubs), three emphasis pillars (workflow automation, AI adoption, revenue velocity technology), 8-section content structure, Big Stat closing element
- **`design-template.md`** — Layout (720px single-column), typography (Playfair Display + Inter), full color palette with CSS custom properties, all visual components (stat cards, callout boxes, tables, tech stack diagram, vendor tags, checklist, hero block), 600px mobile breakpoint
- **`quality-control.md`** — Content and design verification checklists, dual-format output requirement, CSS specificity rules, error handling
- **`workflow.md`** — 5-step generation process, 10 research areas, file naming conventions, volume/issue tracking, template reuse rules

## Key Design Constraints

- HTML files are fully self-contained: no images, no JavaScript, no dependencies beyond Google Fonts
- CSS uses `:root` custom properties exclusively — no hardcoded colors
- Base CSS selectors must appear before modifier selectors (specificity ordering)
- Every section needs: section number, headline, at least one statistic, cited sources
- Three callout types: blue (insight), amber (warning), green (action required)
