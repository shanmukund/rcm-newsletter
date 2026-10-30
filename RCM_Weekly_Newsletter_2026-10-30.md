# RCM Pulse Weekly
## Revenue Cycle Management Intelligence for Medical Practices

**October 30, 2026 • Volume 10, Issue 5**

---

## In This Issue

01. CY 2027 Physician Fee Schedule Final Rule Is Imminent — Open Enrollment Week 2 Reveals Fewer MA Choices, a Higher Part D Cap, and CMS Marketplace Verification Overhaul
02. FHIR Prior Authorization APIs Are 63 Days from Mandate — Aetna Exits Two States, and Part D Cap Hike Puts Specialty Prescribing in the Crosshairs
03. Marvix AI Partners for Specialty Documentation, UiPath Launches Agentic RCM Suite — But Only 15% of Providers Have Fully Integrated AI
04. Q4 HCPCS Update: New J-Codes Effective October 1, Cardiology Loses Six PCI Add-On Codes, and AI-Assisted Imaging Gets Its Own CPT Category
05. 2026 Benchmark Update: Sub-40 Days in A/R, 95%+ Clean Claim Rate, and Cost-to-Collect Under 3% Define Top Performers
06. Waystar Explores $5.2B Sale Amid AI Disruption Pressure — Gemini Launches AI RCM Advisory — 142 HCIT Deals Closed in H1 2026
07. FTC to Health Systems: CMS Price Transparency Compliance Is Not a Safe Harbor — CMS-9882-F Insurer Rule Adds Attestation and Actual Dollar Amounts
08. Independent Practice Watch: Overhead Under 65%, Net Collections Above 95%, and the 3% Cost-to-Collect Ceiling Define Financially Healthy Independent Practices
09. Specialty RCM Spotlight: Primary Care Eyes CCM Revenue from New ICD-10 Codes, Cardiology PCI Code Deletions Live, Radiology Gets 4 AI Imaging Category I Codes
10. This Week's Action Items

---

## Section 01 — Regulatory / Payment Updates

### CY 2027 Physician Fee Schedule Final Rule Is Imminent — Open Enrollment Week 2 Reveals Fewer MA Choices, a Higher Part D Cap, and CMS Marketplace Verification Overhaul

As Medicare open enrollment enters its second week (October 15–December 7), practices are navigating three simultaneous headwinds: an imminent CY 2027 Physician Fee Schedule final rule (historically released in late October or early November), a shrinking Medicare Advantage plan menu with just 35 options per beneficiary on average (down from 39 in 2026), and a CMS proposal to end automatic ACA marketplace subsidy renewals starting in 2028.

**Stat cards:**
- **~Nov 2026** — Expected CY 2027 PFS final rule release (final rules have dropped Oct 31 and Nov 1 in prior years)
- **35** — Average MA plan options per beneficiary in 2027, down from 39 in 2026 (KFF/ABC News)
- **$2,400** — Part D out-of-pocket cap for 2027, rising from $2,100 in 2026
- **193 counties** — Where Medicare Advantage beneficiaries will have NO prescription drug coverage in 2027

### CY 2027 PFS: Final Rule Expected Any Day

The proposed CY 2027 Physician Fee Schedule (CMS-1848-P) was released July 14, 2026, with the comment period closing September 14. Based on prior-year timing, the final rule (CMS-1848-F) is expected within days. Key proposed changes that practices should model against:

- **Conversion factor:** Proposed at $32.8409 for non-qualifying APM participants (down 1.68% from $33.4009 in 2026); qualifying APM participants proposed at $33.1693 (down ~1.19%). The decrease reflects expiration of the 2.5% congressional increase provided for 2026.
- **E/M visits with procedures:** CMS proposes reducing payment when a separately identifiable office/outpatient E/M visit is furnished on the same day as a 0-, 10-, or 90-day global procedure — directly affecting surgical and procedural specialties.
- **Targeted medical review:** The $3,000 threshold is proposed unchanged through CY 2027.
- **RTM/RPM staffing:** CMS proposes paying for remote therapeutic and patient monitoring only when clinical staff are employed by the physician or practice — a significant change for practices using third-party monitoring vendors.

| Proposed CF | 2026 CF | Proposed Change | Specialty Impact |
|---|---|---|---|
| $32.8409 (non-APM) | $33.4009 | -$0.56 (-1.68%) | All fee-for-service practices |
| $33.1693 (APM-QP) | $33.5675 | -$0.40 (-1.19%) | APM qualifying participants |

> **Action Required:** Pull your top 20 CPT codes by volume and run a conversion factor sensitivity analysis against $32.84 now — the final rule could publish within 72 hours. A 1.68% decline on $5M in annual Medicare revenue is $84,000 in lost reimbursement per year.

### MA Open Enrollment: Week 2 Developments

With the first week of Medicare open enrollment complete, the contours of the 2027 MA landscape are clear. The average beneficiary faces 35 plans compared to 39 last year. More critically, 193 counties — up from 123 in 2026 — will have no Medicare Advantage plan that includes prescription drug coverage. Practices in these markets should proactively advise affected patients so they can secure standalone Part D coverage before December 7.

CMS separately proposed on October 23, 2026 (CMS-9892-P) requiring ACA marketplace pre-enrollment verification before advance premium tax credits are paid, starting with 2028 plans. This would end automatic subsidy renewals and require annual reconfirmation — increasing administrative burden on practices that assist patients with insurance navigation.

**Sources:** [CMS — CY 2027 Medicare Physician Fee Schedule Proposed Rule](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-proposed-rule) • [Federal Register — CMS-1848-P](https://www.federalregister.gov/documents/2026/07/16/2026-14327/medicare-and-medicaid-programs-cy-2027-payment-policies-under-the-physician-fee-schedule-and-other) • [PBS NewsHour — Medicare Open Enrollment 2027 Changes](https://www.pbs.org/newshour/health/medicare-open-enrollment-starts-now-these-changes-will-arrive-in-2027) • [ABC News — Medicare Plans Open Enrollment](https://abcnews.com/Health/medicare-plans-open-enrollment-begins/story?id=137374397)

---

## Section 02 — Prior Authorization / Payer Relations

### FHIR Prior Authorization APIs Are 63 Days from Mandate — Aetna Exits Two States, and Part D Cap Hike Puts Specialty Prescribing in the Crosshairs

Three PA-related developments converge this week: the CMS-0057-F electronic prior authorization FHIR API mandate is now 63 days from its January 1, 2027 deadline; Aetna has reduced its Medicare Advantage footprint to 41 states for 2027 (from 43), with implications for authorization workflows in affected markets; and the Part D out-of-pocket cap increase from $2,100 to $2,400 will shift prescribing economics for specialty practices beginning January 1.

**Stat cards:**
- **63 days** — Until CMS-0057-F FHIR PA API mandate takes effect (January 1, 2027)
- **11%** — Reduction in prior authorization requests among CMS pledge signatories since June 2025
- **41 states** — Aetna's 2027 MA coverage footprint, down from 43 in 2026
- **7 calendar days** — Maximum standard PA decision time under January 2026 operational rules now in effect

### FHIR PA API: 63 Days and Counting

Under CMS-0057-F, impacted payers — including Medicare Advantage organizations, Medicaid managed care plans, CHIP agencies, and exchange issuers — must have Prior Authorization APIs built on the FHIR standard (Da Vinci Prior Authorization Support Implementation Guide) operational by January 1, 2027. The operational rules enacted January 1, 2026 — 72-hour maximum for expedited requests, 7-day maximum for standard requests, and standardized denial reason codes — have been in effect for 10 months. The API layer is the next step.

For practices, the opportunity is workflow integration: once payer FHIR PA APIs are live, EHR-embedded PA tools can auto-initiate requests and receive real-time status, reducing phone-based PA follow-up. The challenge is that not every EHR vendor has integrated the Da Vinci APIs, and payer readiness varies. Now is the time to confirm your EHR vendor's readiness and identify which payers are issuing FHIR sandbox access.

Separately, CMS proposed in April 2026 (Federal Register notice 2026-07205) extending the FHIR framework to cover drug prior authorization by October 2027. This remains a proposal.

### Aetna's 2027 Footprint Reduction

Aetna confirmed it will offer Medicare Advantage in 41 states for 2027, compared to 43 states in 2026. Practices in the two exiting markets will see affected patients needing to select new plans during open enrollment. Billing teams should run a payer mix analysis now to identify how many active Aetna MA patients are in markets where Aetna is exiting — these patients need re-verification before January 1.

> **Key Insight:** The Part D cap increasing from $2,100 to $2,400 will affect patient out-of-pocket costs on high-cost specialty drugs. Practices with oncology, rheumatology, or neurology patient panels should expect more cost-sharing conversations at the point of care and more prior authorization appeals for lower-cost alternatives starting in January.

**Sources:** [CMS-0057-F — Federal Register Rule Text](https://www.federalregister.gov/documents/2026/04/14/2026-07205/medicare-and-medicaid-programs-patient-protection-and-affordable-care-act-interoperability-standards) • [eFax — FHIR-First Mandate 2026](https://www.efax.com/blog/fhir-prior-authorization-mandate-2026-trends) • [SmartMatch — 2027 Medicare Advantage Plans](https://smartmatch.com/blog/medicare-advantage/2027-medicare-advantage-plans/) • [AARP — Medicare Open Enrollment Plan Changes](https://www.aarp.org/medicare/medicare-open-enrollment-plan-changes/)

---

## Section 03 — AI & Automation Deep Dive

### Marvix AI Partners for Specialty Documentation, UiPath Launches Agentic RCM Suite — But Only 15% of Providers Have Fully Integrated AI

Two product announcements this week bracket the state of AI in RCM: on October 29, Marvix AI announced a partnership with Unlimited Systems to link clinical documentation AI with billing and coding workflows for specialty practices. On October 1, UiPath launched an agentic AI suite targeting medical records review, denial management, and prior authorization. Both reflect a market truth that Experian Health's latest data makes explicit — 63% of providers have introduced AI in some capacity, but only 15% have fully integrated it into standard RCM operations.

**Stat cards:**
- **63%** — Providers with AI in some capacity (Experian Health, 2026)
- **15%** — Providers who have fully integrated AI into standard RCM operations (Experian Health)
- **142** — RCM and healthcare IT transactions in H1 2026 (Greenberg, via RevCycleAI)
- **Oct 29** — Marvix AI + Unlimited Systems specialty documentation + billing AI partnership

### The Documentation-to-Billing AI Gap for Specialty Practices

The Marvix AI / Unlimited Systems announcement addresses a persistent gap in specialty practices: clinical documentation AI that captures the encounter richly but fails to connect that rich content to the downstream billing and coding workflow. The partnership links Marvix's ambient documentation technology to Unlimited Systems' billing and coding infrastructure, with the goal of reducing documentation-to-claim cycle time while improving code specificity for high-acuity specialty encounters.

This matters because specialty practices — cardiology, orthopedics, oncology — have documentation requirements that differ dramatically from primary care. A cardiology encounter generating an echo interpretation, an E/M visit, and a device check may require three distinct coding pathways. Ambient AI that captures the clinical narrative needs to understand that granularity to generate accurate charge suggestions rather than a generic E/M.

### UiPath's Agentic AI Suite: Automation at the Orchestration Layer

UiPath's October 1 launch targets three RCM bottlenecks: medical records review, denial management, and prior authorization. Unlike earlier RPA-based tools that execute discrete rules-based tasks, agentic AI platforms orchestrate multi-step workflows — receiving a denial, retrieving the relevant medical records, drafting an appeal letter, and routing to a human reviewer — without requiring step-by-step human intervention. For practices with denial management workflows still heavily dependent on human review queues, agentic orchestration could reduce the time-to-appeal cycle from days to hours.

| AI Implementation Tier | Share of Providers | What It Looks Like |
|---|---|---|
| No AI in RCM | 37% | Manual eligibility, paper-based denials |
| Partial AI adoption | 48% | AI in one or two workflows (e.g., eligibility bots) |
| Full AI integration | 15% | AI across eligibility, coding, denial, appeals, posting |

> **Bottom Line:** The gap between 63% (some AI) and 15% (fully integrated) represents the ROI opportunity in front of most practices. The question is not whether to adopt AI in RCM — the market has answered that — but how to move from isolated pilots to workflow-wide deployment without adding integration complexity.

**Sources:** [GlobeNewswire — Marvix AI + Unlimited Systems Partnership (Oct 29, 2026)](https://www.globenewswire.com/news-release/2026/10/29/3391164/0/en/marvix-ai-partners-with-unlimited-systems-to-bring-smarter-clinical-documentation-ai-to-specialty-practices.html) • [RevCycleAI — UiPath Agentic AI Suite](https://revcycleai.com/) • [Experian Health — AI in Healthcare RCM 2026](https://www.experian.com/blogs/healthcare/rcm-and-ai/) • [GlobeNewswire — MedVirtual Human+AI (Oct 30, 2026)](https://globenewswire.com/news-release/2026/10/30/3392479/0/en/human-expertise-meets-ai-medvirtual-s-approach-to-the-future-of-healthcare-administration.html)

---

## Section 04 — Coding Updates

### Q4 HCPCS Update: New J-Codes Effective October 1, Cardiology Loses Six PCI Add-On Codes, and AI-Assisted Imaging Gets Its Own CPT Category

The October 2026 coding landscape has three active layers: the HCPCS Level II quarterly update (effective October 1), which introduced new J-codes for injectable drugs; CPT deletions in cardiology that eliminate six PCI add-on codes; and four new CPT Category I codes for AI-assisted imaging that formalize reimbursement for AI diagnostic tools in radiology — a first in CPT code history.

**Stat cards:**
- **Oct 1** — Effective date for Q4 2026 HCPCS Level II quarterly update (new J-codes and DME codes)
- **6** — PCI add-on CPT codes deleted in the 2026 set: 92921, 92925, 92929, 92934, 92938, 92944
- **4** — New AI-assisted imaging CPT Category I codes (lung nodule, stroke, fracture detection; MIPS pathway)
- **5 weeks** — Time since FY 2027 ICD-10-CM codes went live across all outpatient encounters (October 1)

### HCPCS Q4 Update: Injectable J-Codes and DME Changes

CMS published the October 2026 alpha-numeric HCPCS file with an updated September 23, 2026 effective date for implementation on October 1. The update includes new J-codes for recently approved injectable drugs — practices administering biologic agents, oncology infusibles, or specialty injectables should audit their charge description master against the new file. The CGS Medicare DME MAC published an October 2026 code table confirming all changes apply to dates of service on or after October 1, 2026.

Billing teams should cross-reference their current claim templates against the updated file. Using a deleted J-code past its effective-date cutoff generates an automatic rejection; using a legacy code that maps to a newly split J-code may result in either underpayment or denial.

### Cardiology: Six PCI Add-On Code Deletions

Six percutaneous coronary intervention add-on codes — 92921, 92925, 92929, 92934, 92938, and 92944 — were deleted from the CPT 2026 code set. Cardiology practices that have not yet updated their charge description masters to remove these codes and replace them with current-cycle bundling logic should do so immediately. Claims submitted with deleted codes generate CARC 4/RARC N519 adjustments and add unnecessary follow-up to the billing queue.

### AI-Assisted Imaging: Category I CPT Codes Mark a Historic First

The 2026 CPT code set introduced the first Category I CPT codes for AI-assisted imaging diagnostics, covering lung nodule detection, stroke detection, fracture identification, and a new Diagnostic Radiology MIPS Value Pathway. The Category I designation (versus Category III) means payer coverage policies must evolve from experimental to coverage-determination level. Practices and freestanding imaging centers should verify payer coverage policies for each new code before billing — Medicare coverage is not automatic on new Category I codes until CMS publishes the relevant LCD or NCD.

> **Key Insight:** The AI imaging codes are the most significant structural change to CPT in the imaging segment since the introduction of Category III codes for emerging technologies. Radiology groups that bill global components and professional components separately should confirm their modifier workflow applies correctly to the new codes.

**Sources:** [AAPC — CMS Finalizes October 2026 HCPCS Level II Changes](https://www.aapc.com/blog/94356-cms-finalizes-october-2026-hcpcs-level-ii-changes/) • [CMS — HCPCS Quarterly Update](https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update) • [Medwave — 2026 CPT Code Updates (AI Imaging)](https://medwave.io/2026/01/new-2026-cpt-coding-updates/) • [Care RCM — 2026 Cardiology CPT Code Changes](https://carercm.us/blog/2026-cardiology-cpt-code-changes-guide/)

---

## Section 05 — Revenue Velocity / KPIs

### 2026 Benchmark Update: Sub-40 Days in A/R, 95%+ Clean Claim Rate, and Cost-to-Collect Under 3% Define Top Performers

The 2026 RCM benchmark consensus across multiple industry sources shows a tightening definition of what a high-performing practice looks like. The targets are not theoretical — the gap between median-performing and top-quartile practices on these KPIs maps directly to revenue velocity and cash flow. Practices above the warning thresholds should treat these benchmarks as operational action items, not report cards.

**Stat cards:**
- **<40 days** — Days in A/R target for top-performing practices (warning: >50 days)
- **≥95%** — Clean claim rate target (industry average still running at 88–91%)
- **<5%** — Denial rate target (national average: 8–12%, concerning: >15%)
- **<3%** — Cost-to-collect ratio at best-in-class practices (warning: >4%)

### Benchmark Table: Where You Should Be vs. Where Most Practices Are

| KPI | Best-in-Class Target | Industry Average | Warning Threshold |
|---|---|---|---|
| Days in A/R | &lt;35 days | 38–45 days | &gt;50 days |
| Clean Claim Rate | &ge;97% | 88–91% | &lt;85% |
| Denial Rate | &lt;5% | 8–12% | &gt;15% |
| Net Collection Rate | &ge;97% | 90–93% | &lt;85% |
| Cost to Collect | &lt;3% | 3–6% | &gt;8% |
| First-Pass Resolution Rate | &ge;90% | 75–80% | &lt;65% |

### RPA and Automation's Role in Benchmark Performance

A Becker's Healthcare survey cited across multiple sources found that 51% of health systems have adopted RPA in at least one revenue cycle function. The "big three" automation starting points that consistently appear in implementation guides are eligibility verification, claim status inquiries, and payment posting — together, these three functions represent the highest-volume, most rules-based workflows in the revenue cycle.

Practices that have automated eligibility verification report claim rejection rates from eligibility errors dropping by 40–60%. Payment posting automation reduces the 3–5-day lag between payment receipt and A/R credit that plagues practices using manual ERA management.

The most important shift in 2026 RCM automation strategy is the move from reactive denial processing to preventive denial analytics — identifying patterns before submission rather than after rejection. Pre-submission scrubbing tools that flag modifier errors, bundling conflicts, and medical necessity mismatches before the claim leaves the PM system are now table stakes for practices exceeding $3M in annual Medicare billing.

> **Action Required:** Run your denial reason code distribution today. If any single denial reason code (CARC) accounts for more than 25% of your denial volume, that is an automation target — it means the same fixable error is occurring repeatedly. The root cause is almost always a missing step in your charge entry or eligibility workflow, not a payer dispute.

**Sources:** [AMS Solutions — Medical Billing Benchmark Report 2026](https://ams-solutions.com/medical-billing-benchmark-report-2026/) • [Revenue Synergy — 2026 RCM Benchmarks](https://www.revenuesynergy.com/blog/2026-rcm-benchmarks.html) • [Certify Health — 10 RCM Best Practices 2026](https://www.certifyhealth.com/blog/10-healthcare-revenue-cycle-management-best-practices-for-2026/) • [Medical Billers and Coders — RPA in Revenue Cycle Management](https://www.medicalbillersandcoders.com/blog/rpa-revenue-cycle-management/)

---

## Section 06 — Technology Spotlight

### Waystar Explores $5.2B Sale Amid AI Disruption Pressure — Gemini Launches AI RCM Advisory — 142 HCIT Deals Closed in H1 2026

The RCM technology market this week is defined by two forces: consolidation at the top (Waystar exploring a potential sale at a $5.2B valuation, two years after its 2024 IPO) and continued product proliferation at the mid-market (Gemini's AI RCM advisory launch, Raintree's autonomous agents for rehab therapy). Together they reflect a market where AI disruption pressure is real enough to make the largest independent RCM platform reconsider its public-company path.

**Stat cards:**
- **$5.2B** — Waystar's reported potential sale valuation (Reuters, September 2026)
- **$1.294B** — Waystar's upper 2026 revenue guidance bound (surpassed $1B for the first time in 2025)
- **Oct 8** — Gemini AI RCM Advisory launch, targeting high-cost specialties
- **142** — RCM and HCIT transactions closed in first half of 2026 (Greenberg)

### Waystar: From Public Company to Private-Equity Target?

Reuters reported in September 2026 that Waystar — the largest independent healthcare payments company — is considering a sale that could take it private, with Swedish investment firm EQT (roughly 13% shareholder) potentially involved. Waystar hired Evercore as financial advisor. The context is significant: Morgan Stanley flagged that software companies like Waystar are vulnerable to AI-led disruption, a concern that has kept Waystar's stock under pressure since its 2024 IPO.

Waystar's fundamentals remain strong. The company surpassed $1B in annual revenue in 2025 and guides to $1.274B–$1.294B for 2026. Its board authorized a $200M share repurchase in May 2026. The Iodine Software acquisition ($1.25B, July 2025) added autonomous clinical coding to its denial prevention platform, putting it in direct competition with AKASA and CodaMetrix. The sale exploration is less about operating weakness and more about whether the AI transition is best navigated as a private company.

For practices that use Waystar for clearinghouse, eligibility, or denial management, ownership change creates no operational change in the short term — but it is a signal to ensure contract terms are documented and any multi-year price locks are in writing.

### Gemini AI RCM Advisory and Mid-Market AI Strategy

Gemini's October 8 launch of an AI RCM advisory offering uses real claims data and prior authorization outcomes from high-cost specialties to inform AI vendor selection and program feasibility. This is a category that did not exist 18 months ago — external RCM advisory firms using claims intelligence to guide AI strategy rather than just best practices. It signals that the market complexity around AI vendor selection is high enough to warrant a dedicated advisory layer.

For mid-sized practices evaluating AI vendors, the advisory approach is a cost-effective alternative to running multiple pilots in parallel. A practice with 10 physicians should not be running four simultaneous AI vendor evaluations. External advisory with specialty-level benchmarking narrows the field before the pilot phase.

**Sources:** [HealthExec — Waystar $5.2B Sale Exploration](https://healthexec.com/topics/healthcare-management/mergers-and-acquisitions/52b-healthcare-rcm-giant-waystar-seeking-buyer-report-reveals) • [Waystar Q2 2026 Results](https://www.waystar.com/news/waystar-reports-second-quarter-2026-results/) • [RevCycleAI — Gemini AI RCM Advisory](https://revcycleai.com/blog/) • [RevCycleAI — Deal Tracker H1 2026](https://revcycleai.com/deals-and-raises/)

---

## Section 07 — Compliance Corner

### FTC to Health Systems: CMS Price Transparency Compliance Is Not a Safe Harbor — CMS-9882-F Insurer Rule Adds Attestation and Actual Dollar Amounts

Two developments from the first week of October have extended the price transparency compliance mandate in different directions: CMS finalized CMS-9882-F on October 5, tightening transparency requirements for insurers; and FTC Chairman Andrew Ferguson sent warning letters to 24 of the nation's largest health systems, stating explicitly that meeting CMS transparency requirements does not create a safe harbor from FTC Act liability.

**Stat cards:**
- **Oct 5** — CMS-9882-F Transparency in Coverage rule finalized (Departments of HHS, Labor, Treasury)
- **24** — Health systems receiving FTC warning letters on price transparency
- **Dec 31** — MIPS virtual group election period deadline (election window open now through December 31)
- **Jan 1, 2027** — FHIR Prior Authorization API compliance deadline for impacted payers

### CMS-9882-F: What Changes for Insurers (and How It Affects Practices)

CMS-9882-F requires health insurers and employer health plans to:
- Publish in-network prices as actual dollar amounts (not percentage ranges or ghost rates)
- Provide personalized cost estimates by phone on request
- Add a "Price Transparency" footer link on plan websites
- Submit attestations confirming compliance with the rule

For physician practices, the practical impact is indirect but meaningful: as insurer price transparency data becomes more usable, practices gain better insight into what their competitors are negotiating. Machine-readable files from multiple payers can reveal whether a practice is systematically underpaid relative to peers — a signal to bring to contract renegotiations.

Hospitals face a parallel rule under the Hospital Price Transparency Rule (separate from CMS-9882-F), which now requires publishing actual dollar amounts for allowed charges at the 10th, 90th, and median percentiles, along with National Provider Identifiers in their machine-readable files.

### FTC Warning: Compliance with CMS Is a Floor, Not a Ceiling

The FTC letters make clear that the regulator views healthcare pricing opacity as an unfair trade practice issue, independent of CMS's administrative requirements. A practice that publishes its shoppable services pricing and meets all CMS requirements could still face FTC scrutiny if its pricing behavior otherwise restricts competition or misleads consumers. Healthcare legal teams should brief their compliance officers on this distinction before year-end.

> **Key Insight:** The December 31 MIPS virtual group election window is currently open. If your practice is considering joining or forming a virtual group for the 2027 MIPS reporting year, the election must be submitted to CMS through the QPP portal by December 31, 2026. Missing this window locks you out of the virtual group option for the entire 2027 performance year.

**Sources:** [King & Spalding — FTC Price Transparency Warning](https://www.kslaw.com/insights/articles/ftc-warns-healthcare-systems-that-cms-price-transparency-compliance-is-no-safe-harbor-under-the-ftc) • [McGuireWoods — FTC to Healthcare Providers Alert](https://www.mcguirewoods.com/client-resources/alerts/2026/10/ftc-to-healthcare-providers-cms-price-transparency-compliance-is-not-safe-harbor/) • [Healthcare Finance News — CMS Overhauls Insurer Price Transparency Rules](https://www.healthcarefinancenews.com/news/cms-overhauls-insurer-price-transparency-rules) • [CMS — CY 2027 PFS Proposed Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-proposed-rule)

---

## Section 08 — Independent Practice Watch

### Overhead Under 65%, Net Collections Above 95%, and the 3% Cost-to-Collect Ceiling Define Financially Healthy Independent Practices — and Where You Should Be

Independent practices face structural headwinds that health systems do not: no volume discounts on supplies, no shared revenue cycle teams, no payer leverage in contract negotiations. Against those constraints, the 2026 benchmark consensus provides a practical "where you should be" framework. The gap between a practice at 68% overhead and one at 61% overhead is not just aesthetic — on $3M in revenue, it is $210,000 in annual earnings.

**Stat cards:**
- **<65%** — Target overhead ratio for independent practices (concerning above 70%)
- **≥97%** — Net collection rate target for primary care independent practices
- **<3%** — Cost-to-collect ratio defining financially efficient independent practices
- **~51%** — Health systems (not just independents) with RPA deployed in revenue cycle (Becker's)

### Where You Should Be: 2026 Independent Practice Benchmark Targets

| KPI | Best-in-Class | Healthy Range | Warning |
|---|---|---|---|
| Overhead ratio | &lt;55% | 55–65% | &gt;70% |
| Days in A/R | &lt;35 | 35–42 | &gt;50 |
| Net collection rate | &ge;98% | 95–97% | &lt;85% |
| Denial rate | &lt;5% | 5–8% | &gt;12% |
| Cost to collect | &lt;2.5% | 2.5–4% | &gt;6% |
| First-pass resolution | &ge;92% | 85–92% | &lt;75% |

### The Overhead Ratio as an Action Signal

Practice overhead typically ranges from 45% to 75% of total revenue across specialties, with significant variation by setting. A solo primary care practice in a high-lease market will structurally run higher overhead than a three-physician dermatology practice with owned real estate. What the benchmarks measure is controllable overhead — staffing ratios, billing costs, supply management, and administrative outsourcing decisions.

For independent practices with overhead above 65%, the highest-return interventions in 2026 are: (1) switching from per-claim to percentage-of-collections billing service pricing if you are currently paying per-claim, (2) automating eligibility verification to reduce front-desk staff time on phone-based eligibility calls, and (3) running a mid-year payer contract audit against your actual reimbursement — practices find 3–7% systematic underpayment in at least one major payer contract about 40% of the time when they audit.

> **Where You Should Be:** If your overhead ratio is above 70%, your net collection rate is below 90%, or your Days in A/R exceed 50, you have a revenue cycle problem that is worth the cost of a focused RCM audit. At $3M annual revenue, a 5% improvement in net collection rate adds $150,000 in recovered revenue — typically far exceeding the cost of an external assessment.

**Sources:** [BlueFish Medical — RCM for Independent Practices](https://bluefishmedical.com/revenue-cycle-management-independent-practices/) • [DocVA — Medical Practice Overhead Benchmarks 2026](https://docva.com/medical-practice-overhead-benchmarks-in-2026/) • [AMS Solutions — Medical Billing Benchmark Report 2026](https://ams-solutions.com/medical-billing-benchmark-report-2026/) • [Certify Health — RCM Best Practices 2026](https://www.certifyhealth.com/blog/10-healthcare-revenue-cycle-management-best-practices-for-2026/)

---

## Section 09 — Specialty RCM Spotlight

### Primary Care Eyes CCM Revenue from New ICD-10 Codes, Cardiology PCI Code Deletions Live, Radiology Gets 4 AI Imaging Category I Codes

| Specialty | Key Update This Week | Billing/Coding Implication |
|---|---|---|
| Primary Care | FY 2027 ICD-10-CM adds chronic conditions relevant to CCM and complex care management billing | Audit G0511 chronic care management claims; ensure ICD-10 specificity for CCM eligibility criteria |
| Cardiology | PCI add-on codes 92921, 92925, 92929, 92934, 92938, 92944 deleted; PA burden on cardiac imaging remains highest of any specialty | Remove deleted codes from CDM; verify bundling logic with current-year addons |
| Orthopedics | Joint injection and arthroscopy code changes effective with 2026 CPT; modifier 25/57 scrutiny for same-day E/M + procedure claims | Run pre-bill audit on all same-day E/M + injection/surgery claims |
| Oncology | 3 new CPT codes for mechanical scalp cooling; genomic biomarker lab code CDM updates required | Add scalp cooling codes; audit genomic panel charge capture against updated CDM |
| Radiology | 4 new AI-assisted imaging Category I CPT codes (lung nodule, stroke, fracture, MIPS pathway) | Verify payer LCDs before billing; confirm Modifier 26/TC split applies to AI codes |
| Gastroenterology | CMS 2026 rule changes affect procedure coding and PA requirements; colonoscopy and EGD prior auth complexity increasing | Review current payer PA lists for GI endoscopy; confirm UHC advance notification removal applies to your plan type |
| Mental Health | Telehealth flexibilities continue under current congressional authorization; Modifier GT/95 compliance critical | Audit behavioral health telehealth claims for correct modifier use; check payer-specific telehealth policies for 2027 |
| Neurology | Limited specialty-specific coding updates this week; neurostimulation PA requirements remain complex; AR days for neurology run among the highest in outpatient | Prioritize prior auth tracking for neurostimulation and neuromodulation procedures |

### Primary Care: G0511 and CCM Billing Opportunity

The FY 2027 ICD-10-CM set, now five weeks in effect, added chronic condition codes that improve specificity for chronic care management (CCM) eligible patients — particularly for cardiovascular risk factors, chronic respiratory conditions, and behavioral health comorbidities. Primary care practices that bill G0511 (Rural Health Clinic CCM) or 99490/99491/99439 should confirm their EHR problem lists are using the highest-specificity 2027 code for each condition. Undercoded diagnoses can make a patient appear not to meet the two-chronic-condition threshold for CCM billing, leaving $62–$133 per month per qualifying patient on the table.

### Cardiology: Cardiac Imaging Authorization Remains the Highest-Burden Category

2026 benchmark data consistently shows cardiology running higher A/R days than the all-specialty median. The primary driver is the prior authorization burden on cardiac imaging — echocardiography, nuclear stress testing, cardiac CT, and cardiac MRI collectively account for the highest number of PA-required services among ambulatory specialties. With the FHIR PA API mandate 63 days out, cardiology practices should be among the first to test their EHR's PA status integration as payer FHIR endpoints come online.

**Sources:** [Medical Billers and Coders — FY 2027 ICD-10-CM Primary Care Updates](https://www.medicalbillersandcoders.com/blog/fy-2027-icd-10-cm-updates-for-primary-care/) • [Care RCM — 2026 Cardiology CPT Code Changes](https://carercm.us/blog/2026-cardiology-cpt-code-changes-guide/) • [Medwave — AI-Assisted Imaging CPT Codes](https://medwave.io/2026/01/new-2026-cpt-coding-updates/) • [RCM Workshop — CMS 2026 Gastroenterology Policies](https://rcmworkshop.com/insights/how-cms-2026-policies-affect-gastroenterology-coding-and-prior-authorization/) • [Revele — Primary Care RCM Benchmarks 2026](https://www.revelemd.com/blog/primary-care-rcm-benchmarks-2026-the-kpis-and-regulatory-shifts-defining-top-performing-practices)

---

## Section 10 — This Week's Action Items

### October 30 Action Checklist — Tied to This Issue's Content

1. **Model 2027 revenue against the $32.84 conversion factor.** The CY 2027 PFS final rule is expected within days. Run a sensitivity analysis on your top 20 CPT codes now so you can assess impact within 24 hours of publication.

2. **Confirm FHIR PA API readiness — 63 days remain.** Contact your EHR vendor and primary payers to verify both are on track for January 1, 2027 FHIR PA API availability. If either is behind, begin planning manual PA workflow fallbacks for Q1.

3. **Run a Medicare patient eligibility sweep for open enrollment.** Patients enrolled in exiting Aetna MA plans or discontinued UHC/Humana plans need re-verification before January 1. Pull your MA payer mix and flag patients in affected markets.

4. **Update October HCPCS quarterly codes.** Verify new J-codes effective October 1 are in your CDM. Use deleted codes past the effective date and your claims auto-reject.

5. **Cardiology practices: remove deleted PCI add-on codes from your CDM.** Codes 92921, 92925, 92929, 92934, 92938, and 92944 are gone. Leaving them active generates CARC 4/N519 adjustments.

6. **Radiology: add the 4 new AI imaging Category I codes and check payer LCDs.** Do not bill new Category I AI imaging codes without first confirming coverage — Medicare coverage requires an LCD or NCD; most commercial payers have not yet issued policies.

7. **File your 2027 MIPS virtual group election by December 31.** If you are evaluating virtual group participation for the 2027 performance year, the QPP portal election window closes December 31, 2026. Missing it means traditional MIPS or nothing.

8. **Audit your denial CARC distribution.** If any single denial reason code accounts for more than 25% of volume, it is an automation target. Root-cause the top CARC this week and assign a process owner to fix the upstream gap.

---

## Big Stat

**193 counties** — The number of U.S. counties where Medicare Advantage beneficiaries will have NO prescription drug coverage option available in 2027, up from 123 counties in 2026. For practices in these markets, patient plan transition counseling is not optional — it is a revenue-protective service. Patients who land without drug coverage in January face plan instability that disrupts prior authorizations, formulary management, and claims workflow throughout Q1.

*Source: KFF analysis via ABC News, October 2026 Medicare open enrollment reporting*
