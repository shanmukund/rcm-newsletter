# Design Template Rules

## Layout

- Single-column layout, max-width 720px, centered
- 24px horizontal padding on desktop, 16px on mobile
- 48px vertical padding between sections (36px on mobile)
- Sections separated by 1px border (#E8E8EE)
- No sidebar, no multi-column body layout

## Typography

- **Headings:** Playfair Display (serif), 700 weight
  - H1 (newsletter title): 2rem / 1.6rem mobile
  - H2 (section titles): 1.55rem / 1.3rem mobile
  - H3 (subsection titles): 1rem, Inter font, 600 weight
- **Body:** Inter (sans-serif), 400 weight, 0.95rem, line-height 1.7
- **Labels/Meta:** Inter, 0.7-0.8rem, uppercase, letter-spacing 0.08-0.12em, 600 weight
- **Sources:** Inter, 0.8rem
- Load fonts from Google Fonts with preconnect

## Color Palette

```
--color-bg: #FAFAFA          (page background)
--color-surface: #FFFFFF      (card/component backgrounds)
--color-text: #1A1A2E         (primary text, headings, strong)
--color-text-secondary: #4A4A68 (body paragraphs, list items)
--color-text-muted: #8888A0   (labels, meta, sources)
--color-accent: #0F5FE0       (links, section numbers, default callout)
--color-accent-light: #E8F0FE (default callout background, vendor tags)
--color-accent-dark: #0A4ABF  (hover states, gradient start)
--color-border: #E8E8EE       (all borders and dividers)
--color-highlight: #FFF8E1    (warning callout background)
--color-highlight-border: #F5C518 (warning callout border)
--color-success: #0D9F6E      (action callout, positive KPIs)
--color-success-light: #E6F9F1 (action callout background)
--color-danger: #DC3545       (negative stats, danger indicators)
--color-kpi-green: #0D9F6E    (KPI target values)
--color-kpi-amber: #D97706    (KPI warning values)
```

Use colors semantically -- green for targets/positive actions, amber for warnings, red for negative/danger stats. Blue is the primary brand accent only.

## Visual Components

### Stat Cards
- Grid layout: `repeat(auto-fit, minmax(180px, 1fr))`
- White background, 1px border, 10px border-radius, 20px padding
- Value in Playfair Display 1.8rem (1.5rem mobile), colored by meaning
- Label in 0.78rem muted text below

### Callout Boxes
Three types, all with 3px left border and rounded right corners:
- **Default (insight):** Blue border + light blue background
- **Warning:** Amber border + light yellow background
- **Action:** Green border + light green background
- Each has an uppercase label ("Bottom Line", "Action Required", "Key Insight", etc.)

### Tables
- Wrapped in overflow container with border-radius and border
- Uppercase headers, 0.78rem, with 2px bottom border
- Row borders 1px, last row no border
- KPI tables use green for targets, amber for warnings

### Tech Stack Diagram
- Stacked horizontal bars, each with a colored label (left) and description (right)
- Darkest shade at top (Generative AI), medium (AI/ML), lightest (RPA)

### Vendor Tags
- Pill-shaped badges: 20px border-radius, light blue background, dark blue text
- Grouped under uppercase category labels

### Checklist (Action Items)
- Custom checkbox squares (20px, 2px blue border, 4px radius)
- Items separated by 1px borders
- Bold action title + description text

### Big Stat Hero Block
- Full-width within wrapper, 16px border-radius
- Blue gradient background (135deg, dark to light blue)
- White text, Playfair Display 3rem number (2.2rem mobile)
- Description text at 0.95rem, 0.9 opacity, max-width 520px centered

## Mobile Responsive (600px breakpoint)

- Reduce wrapper padding to 16px
- Scale down heading sizes
- Stat card grid collapses to 2 columns
- Stack layer labels shrink to 100px
- Header meta stacks vertically
- Big stat number reduces to 2.2rem

## Self-Contained

- No external dependencies beyond Google Fonts
- No images -- all visual elements are CSS-only
- No JavaScript
- Single HTML file output
