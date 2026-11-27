# RCM Pulse Weekly
## Revenue Cycle Management Intelligence for Medical Practices

**November 27, 2026 • Volume 11, Issue 4**

---

## In This Issue

01. 35 Days: Congressional Pay-Cut Clock — AMA Presses Congress to Reverse 2.31% Medicare Physician Fee Schedule Cut Before January 1
02. FHIR PA API Final Countdown: 35 Days, Four APIs, and the Readiness Gap Payers Won't Advertise
03. ModMed Agentic RCM Enters Deployment — Waystar/Google Cloud Gemini Partnership Targets Autonomous Revenue Cycle
04. CPT 2027 Books Now Shipping — New Lactation Care Codes, ICD-10 April 2027 Codes Announced, and 340B Repository Mandate Details
05. Year-End Revenue Velocity Push — Days in AR Under 35, Clean Claim Rate 97%, and Why November 30 Is Your Last Real Billing Deadline
06. Technology Spotlight: WVU Medicine Selects Waystar AI to Consolidate 12+ RCM Vendors — CareCloud Grows via Empower Cross-Sell
07. Compliance Corner: MIPS MVP Registration Closes November 30, QPP Exception Deadline December 31, and Five January 1 Cliffs in 35 Days
08. Independent Practice Watch: Physician Ownership Falls to 42.2% as AI Adoption Widens the Gap Between Independent and Health System RCM
09. Specialty RCM Spotlight: PFS Impact by Specialty, Lactation Billing for Pediatrics, Oncology 340B Repository, and Cardiology PA Burden
10. This Week's Action Items — 8 Steps Before January 1

---

## Section 01 — Regulatory / Payment Updates

### 35 Days: Congressional Pay-Cut Clock — AMA Presses Congress to Reverse 2.31% Medicare Physician Fee Schedule Cut Before January 1

The CY 2027 Medicare Physician Fee Schedule final rule (CMS-1848-F), published November 4, 2026, is now 35 days from taking effect. The conversion factor drops 2.31% for most physicians — from $33.40 to $32.63 — and 1.83% for qualifying APM participants, from $33.57 to $32.95. The cut is deeper than the proposed 1.68% reduction because CMS moved the budget-neutrality adjustment from +0.53% (proposed) to -0.12% (final), driven by the expiration of the temporary 2.5% payment increase that applied to 2026. In its November 20 National Advocacy Update, the AMA called on Congress to intervene before the December recess to prevent the cuts from taking effect.

**Stat cards:**
- **–2.31%** — Physician fee schedule conversion factor cut taking effect January 1, 2027 (most physicians)
- **$32.63** — New Medicare conversion factor for non-APM clinicians (down from $33.40)
- **35 days** — Until CMS-1848-F, CMS-0057-F, 340B modifiers JG/TB/XX, and RTM established-patient rules all take effect
- **15%** — Maximum annual lab fee schedule payment reduction allowed through 2029 (CMS-1848-F)

### Why the Final Cut Is Deeper Than Proposed

The American Academy of Audiology's analysis of CMS-1848-F explains the mechanism: the statutory payment updates of 0.75% (qualifying APM participants) and 0.25% (other clinicians) were always insufficient to offset the expiration of the temporary 2.5% boost from 2026. But the budget-neutrality adjustment worsened between the proposed rule (July 2026) and the final rule (November 4), swinging from +0.53% to -0.12% — an additional 0.65-percentage-point drag. The net result is that the final reduction landed at 2.31%, not the proposed 1.68%.

### AMA Advocacy: Congressional Window Is Narrow

The AMA's November 20 advocacy update explicitly urges practices to contact their congressional representatives before the December recess. Congress has historically provided payment-rate relief in year-end omnibus legislation, but the window is closing. The same-day modifier 25 adjustment for 0-day global procedures — reduced from the 50% proposed cut to 20% in the final rule — remains a source of AMA concern. For practices performing same-day minor procedures with separately billable office visits, this adjustment takes effect January 1 as well.

### Lab Fee Schedule: 15% Annual Cap Through 2029

CMS finalized a provision in CMS-1848-F limiting Clinical Laboratory Fee Schedule (CLFS) payment reductions to 15% per year through 2029. This matters for practices with significant laboratory revenue — particularly primary care, internal medicine, and certain specialty practices that perform point-of-care or reference laboratory services. The 15% cap prevents the larger reductions that would otherwise result from the CLFS recalibration methodology.

> **Warning:** With five major compliance changes taking effect January 1 — the PFS conversion factor cut, the FHIR PA API mandate, 340B modifier requirements, RTM established-patient rule, and the 340B mandatory repository — practices risk missing preparation windows on multiple fronts simultaneously. Run a January 1 compliance readiness checklist across all five areas this week.

**Sources:** [CMS — CY 2027 Physician Fee Schedule Final Rule Fact Sheet (CMS-1848-F)](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-final-rule) • [AMA — Nov. 20, 2026 National Advocacy Update](https://www.ama-assn.org/health-care-advocacy/advocacy-update/nov-20-2026-national-advocacy-update) • [AHA — CMS Issues CY 2027 Physician Fee Schedule Final Rule](https://www.aha.org/news/headline/2026-11-04-cms-issues-cy-2027-physician-fee-schedule-final-rule) • [Baker Law — CMS Releases the 2027 Medicare Physician Fee Schedule Final Rule](https://www.bakerlaw.com/insights/cms-releases-the-2027-medicare-physician-fee-schedule-final-rule/) • [American Academy of Audiology — CY 2027 PFS Final Rule Overview](https://www.audiology.org/cy-2027-medicare-physician-fee-schedule-final-rule-overview-for-american-academy-of-audiology/)

---

## Section 02 — Prior Authorization / Payer Relations

### FHIR PA API Final Countdown: 35 Days, Four APIs, and the Readiness Gap Payers Won't Advertise

Exactly 35 days remain before the CMS-0057-F FHIR Prior Authorization API mandate takes effect on January 1, 2027. The rule requires Medicare Advantage organizations, Medicaid managed care plans, CHIP agencies, and federal exchange issuers to implement four production FHIR APIs: patient access, provider access, payer-to-payer exchange, and prior authorization. The critical point for practice billing teams is that the operational prior authorization rules (applying to payer processes) took effect January 1, 2026 — the January 2027 deadline is specifically for the FHIR API technical infrastructure that makes real-time PA status visible inside EHR and PM systems. Practices that have not configured their EHR vendor's FHIR PA feed are leaving a productivity gain on the table 35 days from now.

**Stat cards:**
- **35 days** — Until CMS-0057-F FHIR Prior Authorization API mandate takes effect (January 1, 2027)
- **4 APIs** — Patient access, provider access, payer-to-payer, and prior authorization FHIR APIs required
- **Dec 1** — When UHC removed PA requirements for select under-18 services (this week)
- **88%** — Aetna's share of PA volume standardized electronically (highest of major payers)

### Two-Phase Timeline: Don't Confuse Process with API

The CMS-0057-F rule operates on two separate timelines. The operational provisions — covering payer decision timelines, transparency requirements, and notification standards — generally began January 1, 2026 and are already in effect. The API development provisions — covering the FHIR endpoints that make PA data machine-readable and EHR-integrated — become mandatory January 1, 2027. Practice billing teams should not assume that because payers "already comply with PA reform" that the FHIR API layer is live. These are distinct compliance layers, and not all payers, especially smaller regional plans, have fully implemented the technical API specifications.

### Payer Policy Updates: Cigna, BCBS, and UHC

Three payer developments this week directly affect billing operations:

- **UHC pediatric PA expansion:** Effective December 1, 2026 (this week), UnitedHealthcare removed prior authorization requirements for select services for patients under age 18, with expansions to Medicaid plans in Nebraska, New Jersey, and Tennessee. Pediatric practices and family medicine groups with significant pediatric volume should update their PA requirement matrices to remove stale authorization requests.
- **Cigna E/M downcoding pause:** Cigna's downcoding policy for certain evaluation and management codes started October 1 but was temporarily paused for California HMO plans while the California Department of Managed Health Care reviews the policy. Non-California practices on Cigna PPO plans remain subject to the policy.
- **BCBS Rhode Island:** Provider Update November 2026 includes revisions to the Medicare Advantage PT/OT medical policy, now aligned with standard clinical criteria.

> **Action Required:** Contact your EHR and practice management vendor this week: (1) Confirm FHIR PA API data feeds are activated for your top 5 payers. (2) Update PA requirement matrices for pediatric services on UHC as of December 1. (3) If you are a California-based practice on Cigna HMO, confirm current E/M policy status before billing.

**Sources:** [CMS — CMS-0057-F Electronic Prior Authorization Overview](https://www.cms.gov/priorities/electronic-prior-authorization/overview) • [FHIR PA API 2027 Readiness Guide — Apiable](https://apiable.io/healthcare/healthcare-api-compliance-2027/) • [Cevi — FHIR Prior Auth APIs: January 2027 Mandate](https://cevi.ai/blog/fhir-prior-auth-api) • [UHC Provider — Prior Auth Update December 2026](https://www.uhcprovider.com/en/prior-auth-advance-notification.html) • [Aspirion — Q3 2026 Payer Policy Updates](https://www.aspirion.com/four-payer-shifts-now-in-effect-and-what-they-mean-for-your-next-appeal/)

---

## Section 03 — AI &amp; Automation Deep Dive

### ModMed Agentic RCM Enters Deployment — Waystar/Google Cloud Gemini Partnership Targets Autonomous Revenue Cycle, and 68% of Physicians Now Use AI Tools

Two significant AI RCM developments are shaping the late-2026 market. ModMed's Agentic RCM AI Platform, announced August 4, 2026, is now in deployment for ModMed RCM Services customers. The platform uses AI agents working alongside billing teams to prevent denials upstream rather than remediate them after the fact — its Claim Denial Assessment model flagged 1,341,930 out of 2,204,272 potential denials (60.88%) in internal analysis, and ModMed reports a targeted 57% reduction in time to appeal. Separately, Waystar expanded its AI innovation partnership with Google Cloud, integrating Gemini models into its autonomous revenue cycle platform, which processes over 8.5 billion healthcare payment transactions representing more than $3 trillion in gross claims annually. The industry context: a 2026 physician survey finds that 68% of physicians now use AI tools in practice, up from 38% in 2023 — with the gap between independent practices and health systems widening.

**Stat cards:**
- **68%** — Physicians using AI tools in practice (up from 38% in 2023, based on 2026 survey data)
- **60.88%** — Share of potential denials flagged by ModMed's Claim Denial Assessment AI model (internal data)
- **$3T+** — Gross claims processed annually by Waystar's AI platform (8.5B+ transactions)
- **57%** — Targeted reduction in appeal time per ModMed's internal RCM analyses

### ModMed: Agentic Prevention vs. Remediation

ModMed's platform differentiation rests on a simple argument: point solutions that manage denials after they occur are addressing a problem that already cost you money. Agentic prevention runs claim risk scoring and documentation gap analysis before submission. The platform integrates natively with ModMed Practice Management for real-time claim syncing, and portions of the platform were showcased at MOMENTUM (ModMed's annual customer conference, October 16-18, 2026 in Orlando). The company's internal claim analysis model flagging 60.88% of potential denials is a vendor-reported figure; independent performance evaluations are not yet published, but the architecture — real-time pre-submission scoring tied to payer-specific adjudication histories — reflects the direction the KLAS-ranked autonomous coding market has been moving since early 2026.

### Waystar + Google Cloud: Gemini in the Revenue Cycle

Waystar's expanded Google Cloud partnership, formalized March 2026, integrates Gemini model capabilities with Waystar's AltitudeAI agents, covering autonomous claim resolution, conversational performance intelligence, and agentic clinical documentation. The company processes transactions representing more than 60% of U.S. patients, giving its models a claims adjudication training set that smaller vendors cannot replicate. This scale advantage is precisely what Black Book's 2027 market framework highlights when it splits AI RCM into two separate emerging markets: autonomous coding (narrowly scoped, production-deployable today) and pre-bill validation AI (broader scope, still maturing).

> **Bottom Line:** The AI RCM market is bifurcating. Platforms with large claims-history datasets — Waystar, R1, and a handful of others with EHR-integrated coding engines — are delivering measurable production results on specific tasks (denial prediction, prior auth, autonomous coding). "Fully autonomous end-to-end RCM with no human in the loop" remains a marketing description rather than a production reality for most practices. Evaluate AI vendors by the specific task being automated, the size of their training data, and independently verified results rather than platform-level claims.

**Sources:** [ModMed — Agentic RCM AI Platform Press Release (August 4, 2026)](https://secure.businesswire.com/news/home/20260804997960/en/ModMed-Announces-Agentic-RCM-AI-Platform-to-Help-Specialty-Medical-Practices-Slash-the-RCM-Tax) • [Waystar — AI Innovation with Google Cloud](https://waystarholdings.gcs-web.com/news-releases/news-release-details/waystar-advances-ai-innovation-google-cloud-accelerate) • [Medikode — ModMed's Agentic RCM Launch Signals Where AI Coding Is Headed](https://medikode.ai/post/modmed-agentic-rcm-coding-denials/) • [MGMA — Revenue Cycle AI Inflection Point (HLTH Podcast)](https://www.mgma.com/podcasts/revenue-cycle-ai-inflection-point-rob-ware-denial-prevention) • [Fierce Healthcare — Waystar Touts Bigger Health System Wins and Growing AI Pipeline](https://www.fiercehealthcare.com/finance/waystar-touts-expansion-across-client-base-ai-capabilities-q3-2026)

---

## Section 04 — Coding Updates

### CPT 2027 Books Now Shipping — New Lactation Care Codes for Pediatric Practices, ICD-10 April 2027 Codes Announced, and 340B Repository Mandatory Reporting Confirmed

AAPC reports the CPT 2027 Procedural Coding Expert was released in November 2026, with the HCPCS Level II code book following in December. Two coding updates from this month's AAPC knowledge center require immediate action by specific practice types. First, new CPT codes 98963 and 98964 provide a billing pathway for lactation care in pediatric practices — a service category that previously had no clean CPT mechanism. Second, CMS's ICD-10 coordination process announces new codes effective April 1 in November of the preceding year; practices should monitor CMS's ICD-10-CM/PCS fall 2026 materials for the April 2027 additions as they are published this month. Additionally, CMS-1848-F finalized mandatory 340B Part D drug price reporting beginning in 2027, with the first mandatory submission delayed to September 30, 2027.

**Stat cards:**
- **98963 / 98964** — New CPT codes for lactation counseling (first 30 min / additional 15 min) — pediatric billing
- **Apr 1, 2027** — Effective date for new ICD-10-CM codes being announced by CMS this month
- **Sep 30, 2027** — First mandatory 340B Part D repository submission deadline (CMS-1848-F)
- **Nov 30** — MIPS MVP performance year registration closes at 8 PM ET

### New Lactation Care CPT Codes: 98963 and 98964

The two new codes — CPT 98963 for the first 30 minutes of lactation counseling and 98964 for each additional 15 minutes — give pediatric practices a reimbursement pathway for lactation services that have historically been billed inconsistently, bundled inappropriately, or not billed at all. AAPC flags this as a significant correction for pediatric billing in practices where lactation support is provided by clinical staff during well-child visits or standalone consultations. CDM and fee schedule updates to include these codes should be completed before January 1.

### ICD-10-CM: April 2027 Additions Coming This Month

CMS publishes new ICD-10-CM codes taking effect April 1 through its fall update release, typically in November of the prior year. The public comment deadline for October 2027 codes closed November 13, 2026 — meaning the next ICD-10 coding update window is now being finalized at CMS. Practices should monitor CMS's fall 2026 ICD-10-PCS update materials and the AAPC knowledge center for the April 1, 2027 additions, particularly in specialties with active code-category expansion (orthopedics, oncology, neurology).

### MIPS MVP Registration: November 30 Deadline

MIPS Value Pathways (MVP) registration for the 2026 performance year closes November 30, 2026 at 8 PM ET. If your practice intends to participate in the MIPS track for 2026 — which determines your 2028 Medicare payment adjustment — registration must be completed before this deadline. After November 30, the window closes until the 2027 performance year registration opens.

> **Action Required:** Confirm CPT 98963 and 98964 are in your CDM if your practice provides lactation support. Register for 2026 MIPS MVPs by November 30 at 8 PM ET at qpp.cms.gov. Flag the April 1, 2027 ICD-10-CM update on your 2027 coding calendar.

**Sources:** [AAPC — Lactation Care CPT 98963/98964 for Pediatric Practices](https://www.aapc.com/blog/) • [CMS — Fall 2026 ICD-10-PCS Update Materials](https://www.cms.gov/files/document/fall-2026-icd-10-pcs-update-materials.pdf) • [AAPC/AHIMA — 2027 CPT and ICD-10-CM Updates Webinar (November 3, 2026)](https://integritycoding.com/learning-resource-store/ols/products/aapc-and-ahima-approved-2027-cpt-and-icd-10-cm-updates-with-2-ceus-tuesday-november-3-2026-12-noon-est) • [CMS — CY 2027 PFS Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-final-rule) • [MSMS — CMS Announces Key 2026 MIPS and QPP Deadlines](https://www.msms.org/news/cms-announces-key-2026-mips-and-qpp-deadlines-physicians)

---

## Section 05 — Revenue Velocity / KPIs

### Year-End Revenue Velocity Push — Days in AR Under 35, Clean Claim Rate 97%, and Why November 30 Is Your Last Real Billing Deadline

The last week of November is the critical inflection point for year-end revenue velocity. Claims submitted by November 30 will typically adjudicate before December 31; claims submitted in December increasingly spill into 2027 AR. For practices managing cash flow through the holiday slowdown, the next two weeks represent the most actionable window to scrub outstanding claims, work aged AR, and push denial follow-up before billing teams go into holiday staffing mode. Industry benchmarks for 2026 place the best-in-class Days in AR target below 24 days, with an industry average of 25-35 days and anything over 40 days flagged for immediate action. Clean claim rates above 97% are best-in-class; the 92-96% range is average; below 90% signals systemic billing problems.

**Stat cards:**
- **&lt;24 days** — Best-in-class Days in AR (2026 benchmark); industry average 25-35 days
- **97%+** — Best-in-class clean claim rate; 92-96% = average; &lt;90% = at risk
- **27%** — Average cost-to-collect reduction reported by AI-driven RCM early adopters (industry data)
- **$3.20** — Average ROI per $1 invested in revenue cycle automation (Microsoft-IDC research, 2026)

### KPI Benchmarks: Where Your Practice Should Land by December 31

| KPI | Best-in-Class | Industry Average | Needs Work |
|---|---|---|---|
| Days in AR | &lt;24 days | 25-35 days | &gt;40 days |
| Clean Claim Rate (first pass) | &gt;97% | 92-96% | &lt;90% |
| Net Collection Rate | &gt;97% | 94-97% | &lt;90% |
| Denial Rate (initial) | &lt;5% | 8-12% | &gt;15% |
| Cost-to-Collect | &lt;3% | 4-6% | &gt;8% |

### Year-End Automation Priority: Front-End First

RCM automation research consistently places front-end automation — eligibility verification, PA pre-screening, and claim scrubbing — as delivering the fastest ROI because preventing errors early avoids costly rework. Back-end automation (denial follow-up, payment posting) delivers larger absolute dollar recovery but longer payback windows. For year-end, the front-end priority means: run eligibility checks on all December appointments before visit day, pre-screen high-dollar procedures for PA requirements before scheduling, and ensure claim scrubbing rules are updated for January 1 coding and payment changes.

> **Bottom Line:** 58% of healthcare practices have adopted or plan to adopt AI and automation in revenue cycle operations in 2026 (HFMA survey). Early adopters report a 27% decrease in cost-to-collect and a 6% increase in net patient revenue. If your practice is still manually processing more than 40% of denial follow-up, the gap to best-in-class is widening with each quarter.

**Sources:** [HFMA — Predict, Prevent, Perform: AI Evolution of Denials Management (April 2026)](https://www.hfma.org/technology/ai/predict-prevent-perform-the-ai-evolution-of-denials-management/) • [RCM Axis — Days in AR Benchmark 2026](https://rcmaxis.com/blog/reduce-days-in-ar/) • [Revenue Synergy — 2026 RCM Benchmarks](https://www.revenuesynergy.com/blog/2026-rcm-benchmarks.html) • [MDRevenue — Medical Billing Automation ROI in 2026](https://mdrevenuegroup.com/blog/medical-billing-and-collection-automation-roi) • [AHA — 3 Ways AI Can Improve Revenue Cycle Management](https://www.aha.org/aha-center-health-innovation-market-scan/2024-06-04-3-ways-ai-can-improve-revenue-cycle-management)

---

## Section 06 — Technology Spotlight

### WVU Medicine Selects Waystar AI to Consolidate 12+ RCM Vendors, CareCloud Grows via Empower Cross-Sell, and Waystar Processes $3T+ in Annual Claims

Two significant platform deals and a major AI partnership defined this week's technology landscape. WVU Medicine selected Waystar's AI platform on November 19, 2026, with an initial scope of consolidating more than a dozen revenue cycle vendors onto the platform. CareCloud reported new RCM contracts on November 18 through its Empower division — the healthcare compliance and advisory firm it acquired in May 2026 — representing the fourth quarter's fifth announced RCM relationship through the cross-selling strategy. And Waystar's Google Cloud Gemini integration positions the company's AltitudeAI agent suite as the AI infrastructure for health systems seeking to reduce vendor sprawl while maintaining automation depth.

**Stat cards:**
- **12+** — RCM vendors WVU Medicine is consolidating onto Waystar's AI platform
- **8.5B** — Annual healthcare payment transactions processed through Waystar's platform
- **5** — New RCM contracts CareCloud secured in Q4 2026 through the Empower cross-sell
- **70%+** — Practices planning to consolidate RCM vendors by 2027 (IDC/R1-sponsored, 2026)

### WVU Medicine / Waystar: Vendor Consolidation as AI Strategy

The WVU Medicine selection illustrates the dominant procurement narrative in RCM technology for 2026-2027: vendor consolidation. The pattern is not just about reducing per-vendor fees — it is about eliminating the data fragmentation that prevents AI agents from learning payer-specific adjudication patterns across the full revenue cycle. When a health system runs 12 separate vendors, claim submission data, denial analytics, and payer response patterns exist in separate silos that no AI model can traverse. A unified platform gives the AI training data the breadth it needs to predict denials, score claims by risk, and route exceptions efficiently. For independent practices evaluating RCM technology, the consolidation argument is the same at smaller scale: a single platform with integrated EHR, PM, and billing AI outperforms three best-of-breed solutions that do not share data.

### KLAS 2027 Framework: AI Coding Market Bifurcation

Black Book's 2027 market framework splits what has been marketed broadly as "AI RCM" into two distinct markets: (1) autonomous coding — narrowly scoped, production-deployable today, with KLAS giving CodaMetrix its Best in KLAS award in February 2026; and (2) pre-bill validation AI — broader scope, covering claim risk scoring, documentation gap detection, and payer-behavior prediction, still maturing. IKS Health's audit-ready autonomous coding engine, launched April 2026, targets 95% coding accuracy on structured documentation. The key question for practices evaluating these tools is not "does this vendor use AI" but "which specific task is being automated, what is the training data, and what are the independently verified results."

> **Key Insight:** The RCM technology market is consolidating fast. KLAS, Black Book, and IDC all show 70%+ of practices planning to reduce vendor count by 2027. The AI RCM leaders — Waystar, R1, ModMed for specialty practices, CodaMetrix for autonomous coding — are winning large deals not on features alone but on scale: the more transaction data their AI touches, the better its denial predictions. Practices that remain on fragmented point solutions will find themselves at a structural disadvantage as payer policies become more complex.

**Sources:** [RevCycleAI — WVU Medicine Selects Waystar AI Platform (November 19, 2026)](https://revcycleai.com/deals-and-raises/) • [Investing.com — CareCloud Secures New RCM Deals via Cross-Selling Strategy](https://www.investing.com/news/company-news/carecloud-secures-new-rcm-deals-through-crossselling-strategy-93CH-5036048) • [Waystar — AI Innovation with Google Cloud](https://waystarholdings.gcs-web.com/news-releases/news-release-details/waystar-advances-ai-innovation-google-cloud-accelerate) • [Fierce Healthcare — Waystar Q3 2026 AI Pipeline Growth](https://www.fiercehealthcare.com/finance/waystar-touts-expansion-across-client-base-ai-capabilities-q3-2026) • [IKS Health — Audit-Ready Autonomous Coding Launch (April 2026)](https://businesswire.com/news/home/20260407192519/en/IKS-Health-Announces-Launch-of-Audit-Ready-Autonomous-Coding-Capabilities)

---

## Section 07 — Compliance Corner

### Five January 1 Cliffs in 35 Days: MIPS MVP Registration Closes Today-Plus-Three, QPP Exceptions Close December 31, and the Full 2027 Compliance Calendar

November 27, 2026 marks the final stretch before five simultaneous compliance changes take effect January 1, 2027. This week adds two QPP/MIPS deadlines to an already dense calendar. MIPS MVP registration for the 2026 performance year closes November 30, 2026 at 8 PM ET. QPP exception applications — covering MIPS hardship, CAHPS for MIPS, Extreme and Uncontrollable Circumstances (EUC), and the Promoting Interoperability hardship — remain open through December 31, 2026 at 8 PM ET. The 2026 MIPS data submission window opens January 2, 2027 and runs through March 31, 2027.

**Stat cards:**
- **Nov 30** — MIPS MVP registration closes at 8 PM ET (3 days)
- **Dec 31** — QPP exception applications close at 8 PM ET
- **Jan 2, 2027** — 2026 MIPS data submission window opens (through March 31, 2027)
- **CY 2030** — Last performance year before traditional MIPS is sunset (CMS finalized in 2027 PFS)

### The Five January 1 Compliance Cliffs

| Change | Effective Date | Action Required |
|---|---|---|
| FHIR PA API Mandate (CMS-0057-F) | January 1, 2027 | Confirm FHIR PA feeds active with top 5 payers |
| PFS Conversion Factor Cut (-2.31%) | January 1, 2027 | Model revenue impact by CPT/specialty |
| 340B Billing Modifiers JG/TB/XX | January 1, 2027 | Configure billing system modifier mapping |
| RTM Established Patient + Initiating Visit | January 1, 2027 | Audit RTM panels; document initiating visits |
| 340B Part D Mandatory Repository | 2027 (first submission Sep 30) | Confirm compliance pathway with 340B administrator |

### MIPS Sunset: 2030 Is the Last Traditional Year

CMS finalized in the 2027 PFS final rule that traditional MIPS reporting will be sunset after the CY 2030 performance period. This does not mean an immediate change — MIPS continues through 2030 — but it signals that practices should be actively evaluating Advanced APM participation pathways or MVP tracks that will replace traditional MIPS after 2030. The transition timeline gives practices approximately four performance years to build experience with alternative payment models.

> **Action Required:** Complete MIPS MVP registration at qpp.cms.gov by November 30 at 8 PM ET. Submit QPP exception applications by December 31 at 8 PM ET if applicable. Confirm 340B billing modifier configuration is complete and test with a pilot claim before December 31. Verify FHIR PA API activation with your EHR vendor.

**Sources:** [MSMS — CMS Announces Key 2026 MIPS and QPP Deadlines](https://www.msms.org/news/cms-announces-key-2026-mips-and-qpp-deadlines-physicians) • [AUA — AQUA QPP Deadlines (October 2026)](https://www.auanet.org/research-and-data/aua-quality-(aqua)-registry/aqua-news-flash/aqua-news-flash-oct-2026-nycu) • [AASM — 2026 QPP Deadline Reminders](https://aasm.org/deadline-reminders-for-the-cms-quality-payment-program/) • [AASM — 2027 QPP Final Rule Fact Sheet](https://aasm.org/wp-content/uploads/2026/11/2027-qpp-final-rule-fact-sheet-1.pdf) • [CMS — CY 2027 PFS Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-final-rule)

---

## Section 08 — Independent Practice Watch

### Physician Ownership Falls to 42.2% as AI Adoption Widens the Gap Between Independent and Health System RCM — AMA Pushes Congress on Pay Cut That Hits Independents Hardest

Physician ownership of practices has declined to approximately 42.2% in 2026, with IPA (Independent Physician Association) formation surging as independent physicians seek negotiating leverage without full consolidation. The AMA's November 20 advocacy push for congressional action on the 2.31% Medicare fee schedule cut carries particular urgency for independent practices: unlike health systems that absorb payment reductions through cross-subsidization, independent practices feel the full impact on operating margins that are already under pressure from rising administrative costs and staffing challenges. The 2.31% cut would effectively reduce net Medicare revenue by approximately $7,000-$18,000 per year for a full-time physician depending on specialty and Medicare volume.

**Stat cards:**
- **42.2%** — Approximate physician ownership rate in 2026 (IPA formation surging as alternative to consolidation)
- **68%** — Physicians using AI tools in practice (independent practices adoption lags health systems)
- **H.R. 1** — 6-month Medicaid eligibility redeterminations starting Q3 2026 increase administrative burden for independent practices
- **$7K–$18K** — Estimated annual revenue reduction per physician from 2.31% Medicare fee schedule cut

### Where Independent Practices Stand vs. Health Systems on RCM Technology

The 2026 AI and RCM technology adoption gap between independent practices and health systems is widening. HIMSS 2026 coverage noted that agentic AI moved from demo to deployment primarily in large health systems and RCM management companies — independent practices are adopting individual tools (ambient AI scribes, eligibility verification, some coding assistance) but lack the unified data infrastructure that makes payer-behavior AI models effective. 76% of independent practices report incomplete visibility into their revenue leakage (Veradigm 2026 survey). The key challenge: independent practices cannot afford the data integration projects that make enterprise AI effective, but they also cannot afford the revenue leakage that results from manual RCM.

### Where You Should Be: Independent Practice Benchmarks for Q4 2026

| KPI | Independent Practice Target | Typical Gap vs. Health System |
|---|---|---|
| Days in AR | &lt;35 days | Health systems average &lt;28 |
| Clean Claim Rate | &ge;95% | Health systems average &ge;97% |
| Net Collection Rate | &ge;96% | Health systems average &ge;98% |
| Denial Rate (initial) | &lt;8% | Health systems average &lt;5% |
| Cost-to-Collect | &lt;5% | Health systems average &lt;3% |
| AI-Assisted Claims | &gt;50% | Health systems 75%+ |

> **Key Insight:** For independent practices, the most cost-effective AI RCM entry point in Q4 2026 is eligibility and PA automation — not autonomous coding. Eligibility failures remain the #1 preventable denial root cause, and electronic PA submission (now required by major payers under the January 1 FHIR mandate) reduces authorization costs by an estimated 50-70% compared to phone-based PA. Solve front-end automation before mid-cycle automation.

**Sources:** [AMA — Nov. 20, 2026 National Advocacy Update](https://www.ama-assn.org/health-care-advocacy/advocacy-update/nov-20-2026-national-advocacy-update) • [RevelesMD — Driving Medical Practice Revenue Growth in 2026](https://www.revelemd.com/blog/driving-medical-practice-revenue-growth-in-2026-18-technology-and-strategies-to-strengthen-your-practice) • [HIMSS 2026 — Agentic AI Moved from Demo to Deployment](https://www.revelemd.com/blog/why-himss-2026-mattered-for-medical-practices) • [Physician's Practice — MIPS Reporting Updates 2026](https://www.physicianspractice.com/view/cms-updates-mips-reporting-deadlines-what-practices-need-to-know-now) • [Medlink Analytics — Independent Practice Challenges 2026](https://medlinkanalytics.com/blog/starting-a-private-practice/)

---

## Section 09 — Specialty RCM Spotlight

### PFS Impact by Specialty, Lactation Billing for Pediatrics, Oncology 340B Repository, and Cardiology Prior-Auth Burden

This week's specialty updates focus on the differentiated impact of the 2.31% Medicare payment cut by specialty, new CPT billing opportunities for pediatric practices, and the specific 340B repository and drug-pricing changes affecting oncology. Each specialty faces a distinct combination of payment-level changes and coding updates taking effect January 1.

| Specialty | Key Update | Action |
|---|---|---|
| **Primary Care** | 2.31% CF cut hits high-volume E/M practices; new RTM established-patient rule Jan 1; CPT 98963/98964 lactation billing opportunity | Model E/M revenue impact; audit RTM panels; add lactation codes to fee schedule |
| **Cardiology** | Interventional cardiology estimated -4% to -8% PFS impact; highest prior-auth burden of any specialty on cardiac imaging; FHIR PA API critical for cath lab PA workflows | Run PA API readiness check; model interventional procedure revenue impact |
| **Orthopedics** | More granular fracture classification in ICD-10-CM updates (April 2027); year-end ASC case velocity push before December 31; modifier 25 same-day procedure rule impacts same-day E/M billing | Complete ICD-10 fracture code audit; push ASC case scheduling before December 25 |
| **Oncology** | 340B mandatory Part D drug price repository begins 2027 (first submission Sep 30, 2027); Part B drug negotiation framework expanded; highest Days in AR of any specialty per 2026 benchmarks | Confirm 340B repository compliance plan; model Part B drug revenue under negotiated prices |
| **Mental Health** | New RTM CPT codes for behavioral monitoring active as of Q4 2026; established-patient rule adds initiating visit documentation requirement Jan 1 | Audit behavioral RTM panels; document initiating visits before January 1 |
| **Radiology** | Site-neutral imaging payment concerns from 2027 PFS rule; CMS issued RFI on further alignment (not finalized); AI-assisted radiology CPT codes continue to evolve | Monitor CMS site-neutral rulemaking; confirm AI CPT code availability in billing system |
| **Gastroenterology** | BCBS Rhode Island PA/PT policy update in November Provider Update may affect GI procedures; year-end colonoscopy push before deductible resets | Verify GI PA requirements across payers for January 2027; push colonoscopy scheduling now |

### Cardiology: The Prior-Auth Burden Quantified

Of the major specialties, cardiology consistently ranks highest for prior authorization administrative burden — driven primarily by advanced cardiac imaging (stress echocardiography, PET MPI, cardiac CT) and interventional procedures (catheterization, stenting). With FHIR PA APIs taking effect January 1, the operational question for cardiology billing teams is: will payer FHIR endpoints cover cardiac imaging authorization codes, or will cardiac PAs remain on legacy EDI-278 or phone channels? The readiness gap noted in independent analysis suggests that smaller regional MA plans, which may hold significant cardiac volume in certain markets, may not have full FHIR API coverage on January 1.

**Sources:** [HealthQuestBilling — Medicare PFS Changes 2026: Cardiology, Orthopedics, Radiology](https://www.healthquestbilling.com/medicare-pfs-changes-2026/) • [AAPC — Lactation Care CPT 98963/98964 for Pediatric Practices](https://www.aapc.com/blog/) • [CMS — CY 2027 PFS Final Rule: 340B Repository Mandate](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-final-rule) • [Revenue Synergy — 2026 Medical Billing Benchmarks by Specialty](https://www.revenuesynergy.com/resources/2026-benchmark-report.html) • [American Academy of Audiology — CY 2027 PFS Final Rule Overview](https://www.audiology.org/cy-2027-medicare-physician-fee-schedule-final-rule-overview-for-american-academy-of-audiology/)

---

## Section 10 — This Week's Action Items

### 8 Steps Before January 1

1. **Register for MIPS MVP by November 30 at 8 PM ET** — qpp.cms.gov registration closes in three days. Missing this window means the 2026 performance year defaults to traditional MIPS track without MVP election for your practice.

2. **Model the 2.31% physician fee schedule revenue impact** — Pull your top 25 CPT codes by Medicare volume and multiply by the new conversion factor ($32.63 for non-APM, $32.95 for APM). Quantify the annual revenue delta. This number is what you bring to your congressional representative's office if you plan to request legislative relief.

3. **Complete FHIR PA API vendor check (35 days)** — Call your EHR and PM vendor, confirm FHIR PA data feeds are activated for your top 5 payers by name, and document the confirmation. If not activated, escalate to your implementation contact.

4. **Configure 340B billing modifiers JG/TB/XX** — If your practice administers 340B-acquired drugs, your billing system must map JG (subject to reduction), TB (exempt from reduction at ASP+6%), and XX (non-340B drugs) correctly before January 1. Test with a pilot claim before December 31.

5. **Add CPT 98963 and 98964 to your fee schedule if applicable** — Pediatric and family medicine practices providing lactation support should add both codes to the CDM now, verify payer coverage policies, and train billing staff before January 1.

6. **Submit QPP exception applications by December 31** — If your practice qualifies for a MIPS hardship, EUC, or Promoting Interoperability exception, the submission window is open through December 31 at 8 PM ET at qpp.cms.gov.

7. **Audit RTM/RPM patient panels for established-patient documentation** — RTM services are limited to established patients beginning January 1. Any new patients added to RPM or RTM after January 1 require a documented initiating visit (in-person or telehealth) before billing can begin. Patients enrolled before January 1 are grandfathered.

8. **Year-end AR push: submit all billable claims by November 30** — Claims submitted this week adjudicate before December 31. Work aged AR buckets (90+ days), refile any unworked denials, and ensure your billing team's holiday coverage plan preserves December claim submission capacity.

---

## Big Stat

**35 Days**

Five simultaneous compliance deadlines take effect on January 1, 2027: the FHIR Prior Authorization API mandate (CMS-0057-F), the 2.31% Medicare physician fee schedule conversion factor cut, 340B billing modifier requirements (JG/TB/XX), the Remote Therapeutic Monitoring established-patient and initiating-visit rule, and the beginning of the 340B mandatory Part D drug price repository. No single January 1 since the ACA implementation has carried this density of simultaneous operational changes for physician practice billing teams. The window to prepare is 35 days.

*Source: CMS — CY 2027 Physician Fee Schedule Final Rule (CMS-1848-F) • CMS — CMS-0057-F Interoperability and Prior Authorization Final Rule • CMS — CY 2027 OPPS/ASC Final Rule (340B Modifiers) • AMA — Nov. 20, 2026 National Advocacy Update*
