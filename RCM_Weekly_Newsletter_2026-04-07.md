# RCM Pulse Weekly
**Revenue Cycle Management Intelligence for Medical Practices**
April 7, 2026 | Volume 4, Issue 1

---

## In This Issue

01. Hospital Price Transparency Enforcement Is Live — What Every Practice Must Know Now
02. PA Reform Wave Continues: UHC, Cigna, Aetna Deliver on January Commitments
03. Agentic AI Is No Longer a Pilot — Autonomous Revenue Cycle Operations Go Mainstream
04. April 1 ICD-10-CM Update: Instructional Note Changes That Will Shift Your Coding
05. Closing the Gap: 2026 RCM Benchmarks and the Revenue Velocity Playbook
06. Technology Spotlight: Front-End RCM Market Hits $3.1B — KLAS Best-in-Class Winners
07. Compliance Corner: Price Transparency Fines, FHIR API Deadlines, and Audit Readiness
08. Independent Practice Watch: Margins Under Pressure — Where You Should Be in Q2
09. Specialty RCM Spotlight: Cardiology, Orthopedics, Oncology, Primary Care
10. This Week's Action Items

---

## Section 01 — Regulatory/Payment Updates

### Hospital Price Transparency Enforcement Is Live — What Every Practice Must Know Now

CMS began enforcement of its revised Hospital Price Transparency requirements on **April 1, 2026**, following a three-month compliance window granted after the November 2025 final rule. While the regulations technically apply to hospitals and outpatient facilities, the downstream billing implications directly affect physician practices — particularly those operating in hospital-affiliated or ASC settings.

Key new requirements effective April 1, 2026:
- Payer-specific negotiated charges expressed as percentages or algorithms must now be encoded as **actual dollar amounts** in machine-readable files (MRFs).
- Hospitals must report the **median allowed amount**, the 10th and 90th percentile allowed amounts, and the count of allowed amounts derived from electronic remittance advice (ERA) data.
- Hospital MRFs must include Type 2 National Provider Identifiers (NPIs) for all active codes.
- CMS is now actively fining non-compliant hospitals — fines are a reality, not a threat.

Meanwhile, the **CY 2026 Physician Fee Schedule's 3.26% aggregate rate increase** remains in effect across all specialties. The **5.06% average Medicare Advantage benchmark rate increase** was finalized for contract year 2026, and hospital outpatient departments received a **2.6% net OPPS rate increase**. Practices should confirm their contracted payer rates have been updated and aligned with the new fee schedules.

> **Key Insight:** The new price transparency MRF requirements give practice administrators unprecedented visibility into what facilities are actually collecting per procedure. Use this data to benchmark your own negotiated rates against the reported median allowed amounts — and identify contracts that are underperforming.

**Sources:** [CMS CY 2026 OPPS Price Transparency Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/cy-2026-opps-ambulatory-surgical-center-final-rule-hospital-price-transparency-policy-changes) | [CMS Hospital Price Transparency](https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency) | [CMS CY 2026 PFS Final Rule](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-medicare-physician-fee-schedule-final-rule-cms-1832-f) | [AHA CMS OPPS Final Rule](https://www.aha.org/news/headline/2025-11-21-cms-issues-cy-2026-opps-final-rule) | [SlicedHealth Price Transparency Fines](https://slicedhealth.com/post/is-your-hospital-still-non-compliant-cms-price-transparency-fines-are-now-a-reality/)

---

## Section 02 — Prior Authorization / Payer Relations

### PA Reform Wave Continues: UHC, Cigna, Aetna Deliver on January Commitments

The first wave of voluntary prior authorization reforms — announced by **50+ health plans** in partnership with HHS Secretary Kennedy and CMS Administrator Oz in June 2025 — took full effect January 1, 2026, and practices are beginning to see measurable changes in workflow. Plans covering nearly **270 million Americans** committed to reducing PA volume, improving transparency, and ensuring continuity of care during plan transitions.

Here is where the major payers stand as of April 2026:

| Payer | Action Taken | Impact |
|---|---|---|
| **UnitedHealthcare** | Dropped PA requirements for 231 procedures (nuclear medicine, OB ultrasounds, ECG) | Reduced pre-auth admin burden for cardiology, OB, diagnostic practices |
| **Aetna** | Bundled medical procedure + pharmaceutical PA into single submission | Eliminated double-submission workflows for procedure + drug combos |
| **Cigna** | Eliminated PA for ~100 services; added real-time PA status tools | Faster approvals; less phone-based follow-up |
| **All 50+ Plans** | Honor existing authorizations for 90-day transition when patient switches insurers | Protects continuity-of-care billing during mid-year transitions |

Looking ahead, the **CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F)** requires all impacted payers to implement a **Prior Authorization API** (built on HL7 FHIR Release 4.0.1) by **January 1, 2027**. This API will allow practices to submit PA requests electronically, receive real-time approvals or denial reasons, and access plan-level lists of services requiring prior authorization — all programmatically. Practices using PM/EHR systems with FHIR connectivity should begin vendor conversations now.

> **Action Required:** Audit your top 20 most-PA'd procedures against each payer's updated exception list. Remove manual authorization steps from your intake workflow for procedures now exempt — this alone can recover 2–4 hours of administrative time per day per front-desk FTE.

**Sources:** [MedCity News PA Commitment 2026](https://medcitynews.com/2025/12/prior-authorization-commitment-2026/) | [HHS Kennedy/Oz PA Pledge](https://www.hhs.gov/press-room/kennedy-oz-cms-secure-healthcare-industry-pledge-to-fix-prior-authorization-system.html) | [Modern Healthcare PA Easings](https://www.modernhealthcare.com/insurance/mh-prior-authorizations-unitedhealthcare-aetna-elevance-cigna/) | [CMS CMS-0057-F Prior Auth API](https://www.cms.gov/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f)

---

## Section 03 — AI & Automation Deep Dive

### Agentic AI Is No Longer a Pilot — Autonomous Revenue Cycle Operations Go Mainstream

The inflection point has arrived. **63% of providers** have introduced AI into RCM workflows, but only **15% have fully integrated** AI into standard operations. That gap is closing rapidly: **over 75% of U.S. health systems plan to expand AI-driven RCM automation** through 2026, with autonomous coding, denial prevention, and agentic workflow orchestration ranked as top priorities.

The shift from computer-assisted coding (CAC) to **autonomous coding** is accelerating. AI agents now deliver no-touch or zero-touch coding — translating clinical notes directly into billable codes without human intervention for routine cases. Experienced coders are being redirected to complex cases where clinical judgment is genuinely required, not routine E&M encounters.

At HIMSS 2026 (held in late March), **FinThrive** unveiled its agentic AI-powered revenue cycle platform, featuring 50+ AI and automation use cases across a unified "Fusion Architecture." The platform positions AI not as a feature but as the operating model, with agents continuously identifying risk, orchestrating next-best actions, and executing work across the revenue cycle using unified financial and payer data.

**Waystar** introduced agentic AI capabilities to its cloud-native platform in January 2026, while **AKASA** continues its partnership model with health systems including Cleveland Clinic — where AI handles high-volume, routine code selection and coders focus on complex cases.

Key outcomes from early adopters:
- Practices implementing AI-powered real-time eligibility verification have reported cutting denial rates by as much as **42%** (Experian Health case data)
- FinThrive's Denials and Underpayment Analyzer delivered a **1.1% recovery on overall underpayments**, equating to nearly $1 million in additional cash within three months, plus a **2.5% reduction in denial rates**
- McKinsey identifies agentic AI as the primary driver toward a "touchless revenue cycle" — where claims are validated, coded, scrubbed, submitted, and followed up with minimal human intervention

> **Warning:** AI accuracy and data security remain real adoption barriers. 50% of healthcare leaders cite data privacy as the top concern; 41% cite AI accuracy. Before deploying autonomous coding or agentic denial management, establish clear audit policies — the AMA's 2026 CPT code set now includes codes explicitly recognizing AI-augmented services, so your billing must reflect what was actually AI-assisted vs. clinician-performed.

**Sources:** [Experian Health AI in RCM 2026](https://www.experian.com/blogs/healthcare/rcm-and-ai/) | [FinThrive HIMSS Agentic AI](https://www.prnewswire.com/news-releases/finthrive-highlights-agentic-ai-powered-rcm-platform-at-himss-showcasing-50-ai-and-automation-use-cases-across-unified-fusion-architecture-302707502.html) | [McKinsey Agentic AI Touchless Revenue Cycle](https://www.mckinsey.com/industries/healthcare/our-insights/agentic-ai-and-the-race-to-a-touchless-revenue-cycle) | [HIT Consultant Autonomous Coding](https://hitconsultant.net/2026/04/02/ambient-ai-roi-autonomous-coding-rcm-denial-prevention/) | [TechTarget Agentic AI Revenue Cycle](https://www.techtarget.com/revcyclemanagement/feature/Agentic-AI-evolution-begins-to-pave-way-for-autonomous-revenue-cycle)

---

## Section 04 — Coding Updates

### April 1 ICD-10-CM Update: Instructional Note Changes That Will Shift Your Coding

CMS released the **April 1, 2026 ICD-10-CM update** — and while there are no new code additions, deletions, or revisions, the changes to **instructional notes** carry significant billing implications that coders and billers need to act on immediately.

The most consequential change: several **Excludes1 notes** have been converted to **Excludes2 notes** in Chapter 2 (Neoplasms), specifically under:
- **D18** — Hemangioma and lymphangioma, any site
- **D49** — Neoplasms of unspecified behavior

This distinction is critical:
- **Excludes1** = "Not coded here" — the two codes should **never** be reported together
- **Excludes2** = "Not included here" — the listed conditions are distinct and **may be reported together** when the provider documents both

In practice, this means coding pairs that were previously prohibited can now be billed together when clinically appropriate and properly documented. Practices treating patients with concurrent conditions covered by these codes should immediately review their claim edits and billing rule sets.

> **Warning:** If your billing software has hard-coded Excludes1 edits for these code pairs, those edits are now incorrect as of April 1. Claims that were previously rejected or downgraded may now be billable in full. Review your edit libraries and update them to reflect Excludes2 logic.

Additionally, the **2026 CPT code set** — effective since January 1 — made history as the **first time AI is explicitly recognized in medical coding**. New CPT codes describe services augmented by AI tools, distinct from services performed by clinicians alone. Radiology, pathology, and diagnostic practices should ensure their AI-augmented workflows are mapped to the correct CPT codes before filing claims.

**Sources:** [AAPC April 2026 ICD-10-CM Update](https://www.aapc.com/blog/93952-cms-releases-april-2026-icd-10-cm-update/) | [AGS Health April 2026 ICD-10 Changes](https://www.agshealth.com/blog/april-2026-icd-10-cm-updates-include-significant-instructional-and-sequencing-changes/) | [HIA Code ICD-10-CM April Update](https://hiacode.com/blog/icd-10-cm-code-updates-april-1) | [AAPC ICD-10 Coding Clinic Q1 2026](https://www.aapc.com/codes/latest-updates/icd10-coding-clinic-q1-2026-walk-through-april-updates-to-official-guidelines-and-codes--03172026) | [Unislink AMA 2026 CPT AI Codes](https://unislink.com/rcm-best-practices-blog/the-amas-2026-cpt-updates-what-physician-groups-need-to-know-about-ai-augmented-codes/)

---

## Section 05 — Revenue Velocity / KPIs

### Closing the Gap: 2026 RCM Benchmarks and the Revenue Velocity Playbook

The financial performance gap between top-quartile and median-performing practices is widening in 2026. With reimbursement pressure, rising administrative complexity, and payer behavior shifts, practices that have not benchmarked their RCM operations against current standards are likely leaving substantial revenue on the table.

**2026 RCM Performance Benchmarks**

| KPI | Industry Average | Best Practice Target | High-Risk Threshold |
|---|---|---|---|
| Denial Rate | 6–13% | < 5% | > 15% |
| Days in A/R | 33–42 days | < 30 days | > 50 days |
| Clean Claim Rate | ~85% | 95–98%+ | < 80% |
| Net Collection Rate | ~92% | > 95% | < 90% |
| First-Pass Acceptance Rate | ~80% | > 85% | < 75% |

Revenue velocity improvement strategies gaining traction in 2026:

1. **Zero-day denial prevention** — AI claim scrubbing against payer-specific rules before submission eliminates the most preventable denial category
2. **Real-time eligibility verification** — Automated eligibility checks at scheduling AND check-in catches coverage gaps that create downstream AR aging
3. **Daily statement cycles** — Practices running daily patient statements instead of monthly billing cycles report 15–20% faster patient collections
4. **Days in A/R segmentation** — Separate A/R by payer type (Medicare, commercial, self-pay) to identify which buckets are driving your aging
5. **Contract performance monitoring** — Use ERA data + new price transparency MRF data to identify payers paying below contract rates

> **Bottom Line:** A practice with $5M in annual charges operating at a 10% denial rate and 42 days in A/R could recover $250,000–$400,000 per year by achieving industry best-practice benchmarks. The math on investing in RCM technology is compelling.

**Sources:** [NCDS RCM Benchmarks 2026](https://www.ncdsinc.com/rcm-benchmarks-for-2026-what-good-performance-looks-like-now/) | [Plutus Health RCM KPI Guide](https://www.plutushealthinc.com/post/revenue-cycle-management-kpi) | [R1 RCM Revenue Metrics](https://www.r1rcm.com/articles/5-revenue-cycle-metrics-profitable-practices-are-measuring/) | [Impact Innovations RCM KPIs](https://www.impactinnovations.ai/blog/top-7-rcm-kpis-every-practice-should-track-revenue-cycle-management-metrics-how-to-use-them)

---

## Section 06 — Technology Spotlight

### Front-End RCM Market Hits $3.1B — KLAS Best-in-Class Winners Named

The patient access and front-end RCM technology market is experiencing accelerated growth. According to a March 2026 GlobeNewswire market report, the sector grew from **$2.8 billion in 2025 to $3.11 billion in 2026**, with projections to reach **$4.76 billion by 2030**. This expansion is driven by provider demand for AI-powered eligibility verification, digital intake automation, and real-time insurance discovery tools.

**2026 KLAS Best-in-KLAS Winners — RCM Category Highlights**

| Category | Winner | Notable |
|---|---|---|
| Patient Access | **Waystar** | Introduced agentic AI in Jan 2026; cloud-native platform |
| Revenue Cycle Contract Management | **Experian Health** | eCare NEXT: 83.4 KLAS score; deep EHR integration |
| Insurance Discovery | **FinThrive** | HIMSS 2026 showcase of 50+ AI/automation use cases |
| Government Reimbursement Services | **R1 RCM** | End-to-end platform adoption rising across IDNs |

**AI Technology Stack for Modern RCM (2026)**

| Layer | Technology | Primary Use Case |
|---|---|---|
| Generative AI | LLMs, Ambient Documentation | Clinical note to code generation, appeals drafting |
| AI / ML | Predictive Analytics, Autonomous Coding | Denial risk scoring, zero-touch coding, contract modeling |
| RPA | Bot Automation, Workflow Triggers | Eligibility pinging, claim status checks, ERA posting |

The market shift toward **platform AI vs. point solutions** is accelerating. KLAS research shows organizations that adopt integrated AI platforms — rather than standalone tools — advance to higher levels of automation maturity significantly faster.

> **Key Insight:** Practices evaluating RCM technology in 2026 should prioritize vendors with native FHIR API connectivity and demonstrated Prior Authorization API roadmaps ahead of the January 1, 2027 CMS-0057-F compliance deadline. Vendors who are late on FHIR will become a bottleneck.

**Sources:** [GlobeNewswire Patient Access RCM Market](https://www.globenewswire.com/news-release/2026/03/27/3263905/28124/en/Patient-Access-Front-end-RCM-Solutions-to-Grow-by-USD-1-65-Billion-During-2026-2030-Analysis-of-Competitive-Strategies-and-Key-Revenue-Opportunities-Globally.html) | [KLAS 2026 Best in KLAS Full List](https://hitconsultant.net/2026/02/04/2026-best-in-klas-winners-full-list-software-services/) | [Healthcare IT News KLAS 2026](https://www.healthcareitnews.com/news/best-klas-2026-sees-positive-disruption-tangible-tech-improvements) | [RevCycleAI Waystar Review](https://revcycleai.com/blog/waystar-vendor-deep-dive/)

---

## Section 07 — Compliance Corner

### Compliance Corner: Price Transparency Fines, FHIR API Deadlines, and Audit Readiness

Three compliance deadlines converge in Q2 2026, creating an unusually high-stakes period for healthcare compliance teams:

**1. Hospital Price Transparency — Enforcement Active (April 1, 2026)**
CMS delayed enforcement of its November 2025 final rule updates until April 1, 2026. As of this issue, enforcement is live. New requirements include ERA-derived median allowed amounts, percentile reporting, and elimination of algorithmic/percentage-based charge expressions. Non-compliant hospitals now face active fines. Physician practices billing through hospital facilities or operating in ASC settings should confirm their facility partners are in compliance — non-compliant facilities create billing instability.

**2. CMS-0057-F Prior Authorization FHIR API — Deadline January 1, 2027**
Impacted payers (MA organizations, Medicaid managed care, CHIP, QHP issuers) must implement a Prior Authorization API compliant with HL7 FHIR Release 4.0.1 by January 1, 2027. The API must:
- List all covered services requiring prior authorization
- Provide documentation requirements
- Support electronic PA requests and responses with real-time approval status, denial reasons, or requests for additional information

Practices have 9 months to prepare their PM/EHR systems for FHIR-based PA workflows. Start the vendor conversation now.

**3. Medicare Advantage — Reopening Inpatient Approvals Restricted**
Under the CY 2026 MA final rule, MA plans can only reopen a previously approved inpatient hospital decision for **obvious error or fraud**. Plans can no longer use post-admission information gathered after approval to reverse admission decisions. This closes a common appeals loophole that had resulted in retroactive claim denials.

> **Action Required:** Schedule a Q2 compliance audit covering: (1) price transparency MRF accuracy for facility partners, (2) PA workflow updates for newly exempted procedures, and (3) EHR/PM vendor confirmation of FHIR API roadmap for CMS-0057-F compliance.

**Sources:** [CMS CMS-0057-F Interoperability Rule](https://www.cms.gov/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f) | [CMS MA CY 2026 Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/contract-year-2026-policy-and-technical-changes-medicare-advantage-program-medicare-prescription-final) | [Stroudwater Price Transparency 2026](https://www.stroudwater.com/cmss-cy-2026-updates-to-hospital-price-transparency-and-machine-readable-file-requirements/) | [Elion Health CMS-0057-F Explained](https://elion.health/resources/cms-2026-prior-authorization-rule-explained)

---

## Section 08 — Independent Practice Watch

### Margins Under Pressure — Where You Should Be in Q2

Independent and small-group physician practices are entering Q2 2026 in a financially precarious position. According to MGMA data, only **56% of medical group leaders reported revenue growth** in 2025, while **30% reported a decline**. The margin math is stark: practices need to grow revenue by **6% or more annually** just to maintain current margins against inflation, staffing costs, and compliance overhead.

**The Independent Practice Disadvantage in RCM**

Unlike large health systems with dedicated RCM departments, independent practices typically operate with:
- Front-desk staff performing dual roles (scheduling + eligibility verification)
- No dedicated denial management team — follow-up is reactive, not proactive
- Limited data visibility — PM systems designed as transactional tools, not financial dashboards
- An average of **16 hours per week spent on prior authorizations** per practice — largely manual

**Where You Should Be: Q2 2026 Benchmarks for Independent Practices**

| Metric | Where Most Practices Are | Where You Should Be | Priority |
|---|---|---|---|
| Denial Rate | 10–15% | < 7% | HIGH |
| Days in A/R | 40–55 days | < 35 days | HIGH |
| Clean Claim Rate | 78–84% | > 92% | HIGH |
| PA Time per Week | 14–18 hours | < 8 hours (with automation) | MEDIUM |
| Patient Collection Rate | 55–65% | > 75% | MEDIUM |
| AI Tool Adoption | < 20% of workflows | 50%+ of routine workflows | MEDIUM |

The highest-ROI action available to most independent practices right now is **automated eligibility verification** — cross-checking coverage, coordination of benefits, and patient demographics at the time of scheduling, not at check-in. Practices that have implemented AI-powered eligibility at the point of scheduling report denial rates dropping by up to 42%.

> **Key Insight:** Independent practices spending 16 hours/week on manual PA represent at least 0.4 FTE of cost that could be redirected. AI-powered PA automation tools targeting your top 10 PA-heavy procedures can recapture that time within 90 days of deployment.

**Sources:** [AMA Private Practice RCM](https://www.ama-assn.org/practice-management/private-practices/keep-your-physician-private-practice-thriving-smarter-rcm) | [Health Prime Revenue Resiliency 2026](https://www.hpiinc.com/resources/prime-blogs/revenue-resiliency-in-2026-how-strong-rcm-strategy-can-help-physician-groups-survive/) | [Tebra March 2026 RCM Wrap-Up](https://www.tebra.com/theintake/getting-paid/vital-signs-march-2026) | [Privia Health RCM Trends](https://www.priviahealth.com/blog/4-trends-transforming-independent-practices-revenue-cycle-management/)

---

## Section 09 — Specialty RCM Spotlight

### Specialty RCM Spotlight: Cardiology, Orthopedics, Oncology, Primary Care

The CY 2026 Medicare Physician Fee Schedule finalized a **−2.5% efficiency adjustment** targeting surgical procedures, orthopedic surgical services, and diagnostic imaging — while protecting time-based E&M and behavioral health codes. The downstream billing impact varies significantly by specialty.

| Specialty | Key Update | Financial Impact | Action |
|---|---|---|---|
| **Primary Care** | E&M codes protected from −2.5% efficiency adjustment; care management codes (CCM, TCM) unaffected | Neutral to positive; practices with strong chronic care management billing see relative advantage | Expand CCM/TCM billing to maximize protected revenue streams |
| **Cardiology** | CPT 33340 (LAA occlusion) wRVU cut 27% (14.00 → 10.25); stress test CPT 93017 drops from $311.40 to $220.60 nationally | Significant revenue reduction per procedure for interventional and diagnostic cardiology | Model the per-case revenue impact; negotiate commercial contract floors above Medicare rates |
| **Orthopedics** | −2.5% efficiency adjustment hits all surgical codes; for a $5M Medicare-allowable surgical practice, equals $125,000 annual reduction | Direct bottom-line impact; margins already thin in high-cost surgical settings | Accelerate documentation specificity and modifier usage to capture every allowable unit of service |
| **Oncology** | Multi-phase treatment protocol billing complexity increasing; payer PA requirements for infused oncology drugs remain high | Revenue cycle lag from complex authorizations + frequent mid-cycle payer policy changes | Implement chemotherapy-specific workflow automation for PA and drug administration coding |
| **Radiology** | New AI-augmented CPT codes effective January 1 — AI-assisted reads must be coded distinctly from standard reads | Potential upside if AI-assisted interpretations are coded correctly; downside if miscoded | Map your AI diagnostic tools to the correct 2026 CPT codes immediately |
| **Mental Health / Behavioral Health** | PA overhaul specifically covering behavioral health services expected to debut in 2026 per CMS commitment | PA burden relief coming for high-PA specialties like psychiatry and addiction medicine | Monitor payer-specific PA exemption announcements for behavioral health service codes |

> **Warning:** Orthopedic and cardiology practices absorbing the −2.5% efficiency cut should not simply accept lower reimbursement. Evaluate whether commercial payer contracts have been updated — many commercial rates are indexed to Medicare, and if your contracts do not include a Medicare floor clause, you may have grounds for renegotiation.

**Sources:** [Health Quest Billing Medicare PFS 2026](https://www.healthquestbilling.com/medicare-pfs-changes-2026/) | [AAPC 2026 Medicare Reimbursement Changes](https://www.aapc.com/blog/93784-get-ready-for-2026-medicare-reimbursement-changes/) | [A2Z Billings Medicare Cuts 2026](https://a2zbillings.com/medicare-cuts-2026-complete-guide-to-physician-payment-reductions-rcm-strategy/) | [Behavioral Health Business PA Overhaul](https://bhbusiness.com/2025/06/24/prior-authorization-overhaul-to-debut-in-2026-with-broader-reform-for-behavioral-health-on-the-horizon/)

---

## Section 10 — This Week's Action Items

### April 7, 2026 — Your RCM Pulse Checklist

1. **Audit PA exemption lists now** — Pull your top 20 most-PA'd procedures and cross-reference against updated UHC, Cigna, and Aetna exemption lists. Remove manual authorization steps from your intake workflow for any newly exempted codes.

2. **Update ICD-10 edit libraries for April 1 changes** — If your billing software has hard-coded Excludes1 edits for codes under D18 or D49, those are now incorrect. Update to Excludes2 logic immediately to avoid leaving billable code combinations on the table.

3. **Confirm your payer rates reflect CY 2026 PFS** — The 3.26% PFS rate increase has been in effect since January 1. If any commercial contracts tied to Medicare rates have not been updated, contact your payer rep to confirm adjustments were applied retroactively to January 1.

4. **Begin your FHIR API vendor conversation** — The CMS-0057-F Prior Authorization API deadline is January 1, 2027 — 9 months away. Contact your EHR/PM vendor today to confirm their implementation roadmap and whether any practice-side configuration will be required.

5. **Benchmark your Q1 RCM performance** — Pull your Q1 2026 denial rate, days in A/R, clean claim rate, and net collection rate. Compare against the 2026 benchmarks in Section 05. Identify your single worst-performing metric and assign an owner.

6. **Cardiology/Orthopedics: Model the −2.5% cut impact** — Calculate the dollar impact of the efficiency adjustment on your top 10 Medicare-billed codes. Identify whether commercial payer contracts need floor-rate renegotiation.

7. **Evaluate AI-powered eligibility verification** — If your practice is verifying eligibility at check-in only, move verification to the point of scheduling. This single workflow change is the highest-ROI action available for reducing front-end denials.

---

## Big Stat

**$140 Billion**
The estimated annual waste in U.S. healthcare revenue cycle operations attributable to manual administrative processes, duplicate work, and preventable claim denials — the total addressable opportunity that agentic AI platforms are now beginning to systematically recapture.

*Sources: Moveo.AI Revenue Cycle Management Analysis | McKinsey Agentic AI Touchless Revenue Cycle*

---

*RCM Pulse Weekly | Volume 4, Issue 1 | April 7, 2026*
*Next Issue: April 14, 2026*
*All information is sourced from public domain sources. Not legal or compliance advice.*
