# Quality Control Rules

## Self-Audit Checklist

After generating every newsletter issue, run this checklist before delivering to the user:

### Content Verification
- [ ] All 8 sections present with section numbers, headlines, and sources
- [ ] Every section includes at least one data point or statistic
- [ ] All three emphasis pillars represented (workflow automation, AI, technology/velocity)
- [ ] Sources cited are from the required source categories (government, AAPC, payers, industry pubs)
- [ ] All statistics and figures match the research data -- no hallucinated numbers
- [ ] Action items in Section 8 directly tie back to content covered in the issue
- [ ] Big Stat closing block is present with a compelling, sourced figure

### Design Verification
- [ ] CSS custom properties used consistently (no hardcoded colors)
- [ ] CSS specificity ordering is correct (base rules before modifier rules)
- [ ] All callout types render correctly (check .callout-label color cascade)
- [ ] Stat cards use semantic colors (danger for negative, success for positive)
- [ ] KPI table has green targets and amber warnings
- [ ] Mobile breakpoint styles present and logical
- [ ] All links have `target="_blank"` for external sources
- [ ] HTML validates (proper nesting, closed tags, escaped entities like &amp; &mdash; &ndash;)

### Formatting Standards
- [ ] Use HTML entities for special characters (&mdash; not --, &ndash; for ranges, &amp; for ampersands)
- [ ] No raw markdown in the HTML file
- [ ] Consistent heading hierarchy (h2 for sections, h3 for subsections)
- [ ] No orphaned sections without sources

## Output Formats

Generate two files per issue:
1. **Markdown version** (`RCM_Weekly_Newsletter_YYYY-MM-DD.md`) — for quick reading and editing
2. **HTML version** (`RCM_Weekly_Newsletter_YYYY-MM-DD.html`) — for publishing with full template styling

Both files must contain identical content. The HTML version adds the visual design layer.

## CSS Standards

- Use CSS custom properties (`:root` variables) for all colors, radii, shadows, and max-width
- Order CSS rules: reset > layout > header > TOC > sections > components > footer > responsive
- Base selectors before modifier selectors (e.g., `.callout .callout-label` before `.callout.warning .callout-label`)
- Mobile-first is not required (desktop-first with 600px breakpoint is the established pattern)
- No `!important` declarations
- No vendor prefixes except `-webkit-font-smoothing`

## Error Handling

- If research returns insufficient data for a section, note the gap and fill with the most recent available data rather than omitting the section
- If a source URL appears broken or redirects, still include it but flag it in the sources label
- If CSS specificity conflicts are found during audit, fix them before delivering
