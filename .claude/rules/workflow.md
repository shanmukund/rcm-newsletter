# Workflow Rules

## Newsletter Generation Process

### Step 1: Research (Web Search)
Search broadly across all source categories for the latest RCM developments. Cover these 10 research areas:

1. CMS/Medicare/Medicaid regulatory changes
2. AAPC coding updates (ICD-10, CPT, HCPCS)
3. AI and automation trends in medical billing and RCM
4. Payer policy changes from major insurers (UHC, Cigna, Aetna, Humana, BCBS)
5. Prior authorization reform updates
6. Revenue cycle technology trends (AI denial management, automated coding, RPA)
7. Workflow automation best practices
8. Revenue velocity improvement strategies
9. Healthcare IT news related to billing/RCM
10. CMS interoperability and price transparency rule updates
11. Independent medical practice trends — financial pressures, consolidation vs. independence data, RCM benchmarks for solo/small-group practices, and technology adoption gaps vs. health systems
12. Specialty-specific RCM news — billing, coding, reimbursement, and payer policy updates for Primary Care, Cardiology, Orthopedics, Oncology, Radiology, Neurology, Mental Health, and Gastroenterology

### Step 2: Content Assembly
- Map research findings to the 10-section structure defined in content-strategy.md
- Ensure all three emphasis pillars are represented across sections
- Extract key statistics for stat cards and tables
- Draft callout boxes for the most actionable or urgent insights
- Compose the Big Stat closing block

### Step 3: Markdown Draft
- Generate the Markdown version first for content review
- Use the established heading structure and formatting conventions

### Step 4: HTML Generation
- Apply the full design template from design-template.md
- Use the established HTML structure as the base (header, TOC, sections, big stat, footer)
- Populate with content from the Markdown draft

### Step 5: Self-Audit
- Run the complete quality-control.md checklist
- Fix any issues found before delivering
- Report audit results to the user

## File Naming Convention

```
RCM_Weekly_Newsletter_YYYY-MM-DD.md
RCM_Weekly_Newsletter_YYYY-MM-DD.html
```

Date is the Monday of the newsletter week (or the nearest weekday if generated mid-week).

## File Location

All newsletter files are stored in the project root:
```
c:/Users/shanm/OneDrive/Desktop/RCM newsletter blog/
```

## Volume and Issue Tracking

- **Volume = month number** (e.g., February = Volume 2, March = Volume 3)
- **Issue = week of month** calculated as ceil(day / 7) (e.g., March 9 = Issue 2, March 16 = Issue 3)
- Track in the header meta: "Volume X, Issue Y"
- Next issue date noted in the footer

## Template Reuse

When generating a new issue:
1. Read the most recent HTML file to use as the structural template
2. Replace all content with new research
3. Update date, volume/issue number, and next issue date
4. Do NOT copy-paste old content -- every issue must be freshly researched
