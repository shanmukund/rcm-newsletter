# RCM Pulse Weekly

**Revenue Cycle Management Intelligence for Medical Practices**

Volume 3, Issue 4 | March 23, 2026

---

## In This Issue

1. [CMS Finalizes Electronic Claims Attachments Rule — $782M in Annual Savings, Fax Machines on Notice](#section-01)
2. [March 31 PA Metrics Deadline Looms as Payers Publicly Report Denial Data for the First Time](#section-02)
3. [HIMSS26 Unleashes Agentic AI Arms Race — Waystar, Epic, and FinThrive Ship Autonomous RCM Agents](#section-03)
4. [36 New HCPCS Codes Drop April 1 — Plus Critical ICD-10 Excludes 1 Enforcement at UHC](#section-04)
5. [Days in A/R Benchmarks Tighten as Denial Rates Hit 11.8% and $262B in Claims Go Unpaid](#section-05)
6. [CodaMetrix Wins Inaugural KLAS Autonomous Coding Title; Adonis Raises $40M for AI-Driven RCM](#section-06)
7. [Hospital Price Transparency v3.0 Enforcement Begins April 1 — Up to $2M/Year in Penalties](#section-07)
8. [Independent Practice Renaissance Meets Margin Compression — Where You Should Be](#section-08)
9. [Specialty RCM Spotlight: Primary Care, Cardiology, Orthopedics, Oncology, and More](#section-09)
10. [This Week's Action Items](#section-10)

---

## Section 01
## CMS Finalizes Electronic Claims Attachments Rule — $782M in Annual Savings, Fax Machines on Notice

On **March 20, 2026**, CMS finalized a landmark rule phasing out fax machines and postal mail for healthcare claims documentation, adopting national electronic standards for claims attachments. The rule projects **$781.98 million in annual savings** for the healthcare industry and applies to all HIPAA-covered entities — health plans, clearinghouses, and providers conducting electronic transactions.

**Key Details:**

- **Effective date:** May 26, 2026
- **Compliance deadline:** May 26, 2028 (24-month implementation window)
- Adopts standards for electronic signatures for secure, authenticated transmission
- Eliminates the need for paper-based and fax-based documentation exchange for claims processing

| Metric | Value |
|---|---|
| Projected annual savings | $781.98 million |
| Effective date | May 26, 2026 |
| Compliance deadline | May 26, 2028 |
| Applies to | All HIPAA-covered entities |

Simultaneously, the **OPPS Drug Acquisition Cost Survey (ODACS)** deadline was extended from March 31 to **April 7, 2026**. Hospitals that received OPPS payments for outpatient drugs between July 2024 and June 2025 must complete this survey.

The **MedPAC March 2026 Report** (released March 12) recommended a net physician payment reduction of **1.2%–1.7%** for FY 2027 after the temporary 2.5% statutory bump expires at the end of 2026. MedPAC also recommended **-7% cuts** for home health and inpatient rehabilitation, and **-4% for skilled nursing facilities**.

> **⚠ Warning:** The current 2.5% statutory payment bump expires December 31, 2026. MedPAC's FY 2027 recommendations signal a net payment reduction for physicians unless Congress acts. Practices should model 2027 scenarios now — not after the cliff arrives.

**Sources:** [CMS Press Release (March 20, 2026)](https://www.cms.gov/newsroom/press-releases/cms-rule-phases-out-fax-machines-snail-mail-save-taxpayers-781-98-million-year) · [Becker's Payer](https://www.beckerspayer.com/policy-updates/the-1980s-called-cms-to-phase-out-fax-mail/) · [MedPAC March 2026 Report](https://www.medpac.gov/document/march-2026-report-to-the-congress-medicare-payment-policy/) · [HFMA](https://www.hfma.org/finance-and-business-strategy/cms-claims-attachments-rule-electronic-standards/) · [National Law Review — ODACS Extension](https://natlawreview.com/article/2026-opps-drug-acquisition-cost-survey-response-deadline-extended)

---

## Section 02
## March 31 PA Metrics Deadline Looms as Payers Publicly Report Denial Data for the First Time

The **March 31, 2026** deadline under CMS's Interoperability and Prior Authorization Final Rule (CMS-0057-F) marks a watershed moment: for the first time, impacted payers must **publicly report prior authorization metrics** for Calendar Year 2025 on their websites. This includes approval/denial percentages, appeal overturn rates, average decision turnaround times, and requests for additional information — broken down by contract, state, or plan level.

| Metric Required | Detail |
|---|---|
| % of PA requests approved/denied | By plan/contract level |
| % approved after appeal | Overturn transparency |
| Average decision turnaround | Submission to decision |
| Additional info requests | Frequency of payer follow-up |

**What This Means for Practices:**

- **Benchmark your payers:** For the first time, you can compare PA approval rates, denial rates, and turnaround times across every payer you contract with — using their own reported data
- **Denial reason specificity:** Since January 1, 2026, payers must provide a **specific reason for every PA denial** regardless of submission method — generic "not medically necessary" rejections are no longer compliant
- **FHIR API mandate on horizon:** By January 1, 2027, payers must have live FHIR-based Prior Authorization APIs, Patient Access APIs, Provider Access APIs, and Payer-to-Payer APIs

The **CAQH Index** estimates electronic prior authorization standards save **14 minutes per authorization** and **$515 million annually** in industry-wide administrative costs.

Meanwhile, payer PA reform commitments continue evolving. **Aetna** now provides preauthorization bundles for musculoskeletal conditions (X-rays, knee surgeries, medications) and cancer imaging (MRI/CT bundles). **BCBS** is targeting **80% near-real-time electronic PA responses** by 2027.

> **✅ Action Required:** After March 31, pull each payer's published PA metrics and compare against your own internal PA tracking data. Any significant discrepancies between your denial experience and their reported rates should trigger a payer meeting or formal dispute.

**Sources:** [CMS-0057-F Official Page](https://www.cms.gov/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f) · [CMS Interoperability Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) · [Firely CMS-0057-F Decoded](https://fire.ly/blog/cms-0057-f-decoded-must-have-apis-vs-nice-to-have-igs-for-2026-2027/) · [Healthcare Dive — Aetna PA Reform](https://www.healthcaredive.com/news/aetna-updates-on-prior-authorization-reform/807134/) · [BCBS PA Commitments](https://www.bcbs.com/news-and-insights/article/simplifying-prior-authorization)

---

## Section 03
## HIMSS26 Unleashes Agentic AI Arms Race — Waystar, Epic, and FinThrive Ship Autonomous RCM Agents

HIMSS26 (March 9–12, Las Vegas) marked the moment agentic AI shifted from concept to commercially deployed product across the revenue cycle. Multiple major vendors shipped autonomous AI agents capable of end-to-end claim processing, denial prevention, and appeal generation — with measurable production results.

| Vendor | Key Announcement | Production Result |
|---|---|---|
| Waystar | Google Cloud partnership; AltitudeAI expansion | $15B in prevented denials; 90% faster appeals; ~99% clean claim rate |
| Epic | Agent Factory (no-code AI agent builder) | 85%+ of customers actively using Epic AI; 42% faster PA submission; 20%+ coding denial reduction |
| FinThrive | 50+ AI use cases across Fusion architecture | 1.1% underpayment recovery (~$1M/3 months); 2.5% denial rate reduction |
| XiFin | Empower AI RCM Ecosystem | Agentic workflows for correspondence, OOP estimates, denial prioritization, appeal creation |
| athenahealth | MCP Server + athenaConnect interoperability | Natural language AI access to patient data for 170,000 providers (20% of U.S. population) |

**Waystar earned the #1 overall ranking** in Black Book's Q1 2026 Agentic and Generative AI RCM Benchmark — scoring 9.75/10 across 18 KPIs in a survey of 49 vendors and 750+ senior healthcare leaders.

**The Three-Layer AI Stack in RCM (2026):**

- **Generative AI:** Autonomous coding, appeal letter generation, prior auth clinical criteria drafting, EOB interpretation
- **AI/ML:** Denial prediction, eligibility risk scoring, charge capture gap detection, underpayment identification
- **RPA:** Batch eligibility verification, payment posting, remittance reconciliation, claim status checks

**Adoption Data:**

- **63%** of providers have introduced AI in some capacity; only **15%** have fully integrated AI into standard RCM operations
- **Over 80%** of healthcare executives expect both agentic AI and generative AI to deliver moderate-to-significant value in 2026
- **50%** cite data privacy/security as the biggest barrier to AI adoption; **41%** say it's difficult to trust AI results fully
- **Mayo Clinic** cut ~30 FTE positions over two years and saved $700,000 in vendor costs through AI bots in the revenue cycle
- **Ambient AI documentation** adopted by 62% of Epic hospitals; clinicians spend 20% less time on EHR documentation per appointment

> **💡 Key Insight:** The "battle of the bots" is now real — payers use AI to drive more denials while providers deploy AI to fight back. Practices without AI-powered denial prevention are bringing a knife to a gunfight. The ROI is no longer theoretical: Waystar's $15 billion in prevented denials and Epic's 42% PA time reduction are production numbers, not pilot projections.

**Sources:** [TechTarget — HIMSS26 Agentic AI](https://www.techtarget.com/revcyclemanagement/news/366639962/Agentic-AI-powers-revenue-cycle-technology-news-at-HIMSS26) · [Experian Health — RCM and AI](https://www.experian.com/blogs/healthcare/revenue-cycle-management-and-ai/) · [Deloitte 2026 US Health Care Outlook](https://www.deloitte.com/us/en/insights/industry/health-care/agentic-ai-health-care-operating-model-change.html) · [Healthcare IT News — Epic AI](https://www.healthcareitnews.com/news/himss26-epic-highlight-no-code-agent-factory-and-other-ai-advances) · [HFMA — Battle of the Bots](https://www.hfma.org/revenue-cycle/denials-management/health-systems-start-to-fight-back-against-ai-powered-robots-driving-denial-rates-higher/)

---

## Section 04
## 36 New HCPCS Codes Drop April 1 — Plus Critical ICD-10 Excludes 1 Enforcement at UHC

The **April 1, 2026 HCPCS Level II quarterly update** brings **36 new codes**, primarily for injectable drugs, biologics, and skin substitute products. Medicare Administrative Contractors have until **April 6** to implement changes. Simultaneously, UnitedHealthcare's aggressive coding enforcement actions are reshaping claim submission requirements across specialties.

**HCPCS April 1 Highlights:**

- **36 new HCPCS Level II codes** effective April 1
- Code **J0174** short descriptor revised
- **J1572** (Flebogamma injection) reinstated retroactively to January 1, 2026
- New code **Q0238** for TYENNE (tocilizumab-aazg) for COVID-19 treatment

**UnitedHealthcare Enforcement Actions (March–April 2026):**

- **March 1:** UHC began enforcing ICD-10 **"Excludes 1" rules** on outpatient claims — mutually exclusive diagnosis code combinations will trigger edits or denials
- **April 1:** Automated pre-payment policy enforcement for **laboratory services** in office, hospital outpatient, and independent lab settings
- **April 1:** Professional/technical component policy update — radiology review (not full interpretation) reimbursement now considered included in the E/M service
- **February 1:** Enhanced **anatomical modifier requirements** aligned with CMS laterality/anatomical modifier rules

**FY 2026 ICD-10-CM Recap (effective October 1, 2025):**

- **487 new diagnosis codes**, 38 revisions, 28 deletions
- BMI codes now require an associated reportable diagnosis (e.g., obesity)
- New code **E11.A** for Type 2 DM without complications in remission
- Updated COVID-19 code pairing requirements for respiratory manifestations

**CPT 2026 (effective January 1, 2026):**

- **11,525 total CPT codes** in the 2026 code set
- New vascular procedure codes **37254–37299** replace outdated 37220–37235
- Three new **APCM add-on G-codes** (G0556, G0557, G0558) for Advanced Primary Care Management
- New vaccine codes for RSV, COVID-19, Influenza, and Chikungunya

> **⚠ Warning:** UHC's Excludes 1 enforcement is a denial trap for practices that haven't updated their code validation logic. Run a retroactive audit of all UHC claims submitted since March 1 to identify and correct any mutually exclusive diagnosis code pairings before they become uncollectible.

**Sources:** [AAPC — HCPCS Level II April 2026](https://www.aapc.com/blog/93980-hcpcs-level-ii-code-changes-go-into-effect-april-1/) · [AAPC — UHC 2026 Policies](https://www.aapc.com/blog/93893-keep-up-with-2026-unitedhealthcare-policies-that-affect-reimbursement/) · [AAPC — FY 2026 ICD-10-CM Guidelines](https://www.aapc.com/blog/92967-coding-update-fy-2026-icd-10-cm-official-guidelines-released/) · [CMS CY 2026 PFS Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-medicare-physician-fee-schedule-final-rule-cms-1832-f)

---

## Section 05
## Days in A/R Benchmarks Tighten as Denial Rates Hit 11.8% and $262B in Claims Go Unpaid

The RCM performance gap between top performers and the median continues to widen. Initial denial rates hit **11.8% in 2024** (up from 10.2%), with **$262 billion** in claims denied annually out of $3 trillion submitted. The most alarming statistic: **65% of denied claims are never resubmitted** — representing massive, preventable revenue leakage.

| KPI | Target (Top Performers) | Industry Median | Danger Zone |
|---|---|---|---|
| Days in A/R | <30 days | 33–42 days | >55 days |
| Clean Claims Rate | >98% | 90–95% | <85% |
| Initial Denial Rate | <5% | 6–13% | >15% |
| Net Collection Rate | >96% | 90–95% | <88% |
| First-Pass Resolution | >90% | 70–85% | <65% |

**Denial Breakdown:**

- **41% of providers** now face denial rates of at least 10%
- **73% of providers** say denials are increasing (vs. 42% in 2022)
- Medicare Advantage initial denial rate averages **15.7%**
- Commercial payer initial denial rates estimated at **13.9%**
- **77% of denials** stem from paperwork or plan design issues — not clinical judgment
- Hospitals spend **$19.7 billion industry-wide** overturning denied claims
- Specialty clinics using AI report denial recovery rates up to **75%**, reclaiming over **$1 million per physician**

**Revenue Velocity Market Data:**

- U.S. Medical Billing Outsourcing Market projected to more than double to **$17.7 billion by 2033**
- Patient Access/Front-end RCM Solutions growing by **$1.65 billion during 2026–2030**
- RCM staff turnover rates average **~20%**; hospitals lose up to **$125,000 per open RCM position** annually

> **💡 Key Insight:** With 65% of denied claims never resubmitted, the single highest-ROI revenue cycle investment is not faster coding or better charge capture — it's systematic denial follow-up. Every denied claim that goes unworked is cash left on the table. Build an automated denial worklist with aging alerts before investing in anything else.

**Sources:** [Aptarro — US Healthcare Denial Statistics 2026](https://www.aptarro.com/insights/us-healthcare-denial-rates-reimbursement-statistics) · [Experian Health — Claim Denial Statistics](https://www.experian.com/blogs/healthcare/healthcare-claim-denials-statistics-state-of-claims-report/) · [GlobeNewswire — Billing Outsourcing Market](https://www.globenewswire.com/news-release/2026/03/23/3260657/28124/en/U-S-Medical-Billing-Outsourcing-Market-Report-2026-Industry-to-More-Than-Double-by-2033-Reaching-USD-17-7-Billion.html) · [NCDS — RCM Benchmarks 2026](https://www.ncdsinc.com/rcm-benchmarks-for-2026-what-good-performance-looks-like-now/)

---

## Section 06
## CodaMetrix Wins Inaugural KLAS Autonomous Coding Title; Adonis Raises $40M for AI-Driven RCM

The RCM technology landscape saw two landmark developments this week: **CodaMetrix** earned the inaugural **Best in KLAS for Autonomous Medical Coding**, and AI-driven RCM startup **Adonis** closed a **$40 million Series C** to scale autonomous claim resolution.

**CodaMetrix — Best in KLAS 2026 (Autonomous Medical Coding):**

- First-ever KLAS award in this category, signaling market maturity for autonomous coding
- Reduces coding costs by **50%+**
- Cuts manual coding volume by **70%+**
- Lowers coding-related denials by up to **60%**
- Cleveland Clinic deployed AKASA's generative AI tools for medical coding across all U.S. locations — a production-scale validation of autonomous coding

**Adonis — $40M Series C (March 25, 2026):**

- Led by Quadrille Capital; total funding now exceeds **$95 million** since 2022 founding
- Achieved **4x revenue growth** in 2025; net retention above **130%**
- Platform deploys Intelligence and AI Agent products that monitor, detect RCM issues, recommend actions, and autonomously progress claims to resolution
- Customer: **Mount Sinai Health System**

**Procode AI — Exits Stealth (March 2, 2026):**

- $4M funding; acquired The Auctus Group (leading U.S. medical biller for plastic surgeons)
- Coding Copilot enables coders to code **90% faster** with greater accuracy

**2026 KLAS RCM Rankings — Other Notable Winners:**

- **R1 RCM:** Best in KLAS for Extended Business Office (Small), Government Reimbursement Services, and Underpayment Recovery — 7th consecutive year, 18 total awards
- **Waystar:** #1 in Black Book's Q1 2026 Agentic and Generative AI RCM Benchmark (9.75/10 composite, 49 vendors surveyed)

**Vendor Tags:**

- *Autonomous Coding:* CodaMetrix, AKASA, Procode AI, Epic Penny
- *AI-Driven RCM Platforms:* Adonis, Waystar, FinThrive, XiFin
- *Extended Business Office:* R1 RCM
- *Ambient Documentation:* DAX Copilot, Abridge, ThinkAndor

**RPA Market Growth:**

- Global healthcare RPA market: **$1.4B (2022)** projected to **$14.18B by 2032** (CAGR 26.1%)
- Agentic bots now adapt to payer portal layout changes without developer rewrites

> **✅ Action Required:** If your practice still relies on 100% manual coding, the KLAS validation of autonomous coding is your signal to evaluate. CodaMetrix, AKASA, and Epic Penny each serve different practice sizes — request demos with your actual claim volume and specialty mix to compare accuracy rates and ROI projections.

**Sources:** [CodaMetrix — Best in KLAS PR](https://www.prnewswire.com/news-releases/codametrix-named-no-1-in-inaugural-best-in-klas-title-for-autonomous-medical-coding-302678539.html) · [Adonis — $40M Series C](https://www.prnewswire.com/news-releases/adonis-raises-40m-series-c-to-equip-healthcare-providers-with-aidriven-revenue-cycle-operations-302722199.html) · [R1 — Best in KLAS 2026](https://www.globenewswire.com/news-release/2026/02/04/3232043/0/en/R1-Awarded-Best-in-KLAS-Across-Multiple-RCM-Categories-for-2026.html) · [HIT Consultant — Procode AI](https://hitconsultant.net/2026/03/02/procode-ai-4m-funding-acquires-auctus-group-rcm-medical-billing/)

---

## Section 07
## Hospital Price Transparency v3.0 Enforcement Begins April 1 — Up to $2M/Year in Penalties

**April 1, 2026** marks the enforcement start date for CMS's updated Hospital Price Transparency requirements under the v3.0 schema. Hospitals face penalties of up to **$2,007,500 per year** for non-compliance — and the new requirements are significantly more detailed than previous versions.

**New v3.0 Requirements:**

- Replace estimated allowed amount with **median allowed amount**
- Add **10th and 90th percentile** allowed amounts for each service
- **Type 2 NPI** required in general data elements
- New **Attestation Statement** (replacing Affirmation Statement) with Attester name

**Penalty Structure:**

| Hospital Size | Daily Penalty | Annual Maximum |
|---|---|---|
| Minimum | $300/day | $109,500/year |
| Maximum | $5,500/day | $2,007,500/year |
| Calculation | $10/bed/day | Based on licensed bed count |

A **35% CMP reduction** is available if the hospital waives ALJ hearing rights (does not apply to MRF posting failures).

**Compliance & Deadlines Tracker (March–May 2026):**

| Deadline | Action Item |
|---|---|
| March 31, 2026 | Payers: Publish CY 2025 prior auth metrics (CMS-0057-F) |
| March 31, 2026 | MSSP ACOs: Submit PY 2025 quality data |
| April 1, 2026 | Hospital Price Transparency enforcement begins (v3.0) |
| April 1, 2026 | OPPS new codes effective (COVID-19 mAbs, lab analysis, skin substitutes) |
| April 7, 2026 | ODACS drug acquisition cost survey due (extended) |
| May 1–July 31, 2026 | Clinical Lab private payor rate/volume reporting window |
| May 12–15, 2026 | Updated CMS forms (ABN, Important Message, Detailed Notice) must be in use |
| May 26, 2026 | Electronic claims attachments rule effective |

**Medicaid Impact — "One Big Beautiful Bill":**

State Medicaid budgets projected to decline by **$664–665 billion** (2025–2034). An estimated **5.3 million people** could lose coverage from new work requirements. Nebraska implementing early (May 1, 2026); federal implementation guidance due June 1, 2026, with mandatory state outreach June 30–August 31, 2026, and full work requirement implementation by January 1, 2027.

> **⚠ Warning:** Practices with hospital-based outpatient departments should confirm their MRF files have been updated to v3.0 schema before April 1. The penalty structure is now aggressive enough to make non-compliance a material financial risk — $10/bed/day adds up quickly for mid-size and large facilities.

**Sources:** [CMS Price Transparency Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/cy-2026-opps-ambulatory-surgical-center-final-rule-hospital-price-transparency-policy-changes) · [HFMA — Price Transparency](https://www.hfma.org/price-transparency/cmss-latest-transparency-rule-aims-to-make-price-estimates-more-exact/) · [Stateline — $665B Medicaid Impact](https://stateline.org/2026/03/04/state-medicaid-budgets-will-decline-by-665-billion-under-new-federal-law-report-finds/) · [MLN Connects March 26, 2026](https://www.cms.gov/training-education/medicare-learning-network/newsletter/mln-connects-newsletter-march-26-2026)

---

## Section 08
## Independent Practice Renaissance Meets Margin Compression — Where You Should Be

Independent practices are at a crossroads. While **47% of physicians** have consolidated with hospital systems (up from <30% in 2012), a counter-movement is gaining momentum: **micro-practices, direct primary care (DPC) models, and tech-enabled MSOs** are enabling physicians to maintain independence while competing on RCM efficiency.

**Consolidation by the Numbers:**

- **42.2%** of physicians worked in private practice in 2024, down from **60.1% in 2012**
- Hospital/corporate ownership of practices jumped from **39% to 59%** between 2019–2023
- **6.5%** of physicians in PE-owned practices in 2024 (up from 4.5% in 2022); PE exceeds **30%** in gastro, derm, and ophthalmology
- Hospital-physician consolidation reached **66% in the Midwest** and **58% in rural areas**
- On **March 5, 2026**, DOJ/FTC/HHS jointly launched a cross-government inquiry into PE in healthcare

**The Independent Practice Renaissance:**

- IPAs (Independent Physician Associations) forming at accelerating pace — primary care doctors are uniting for market power against payers
- DPC membership models growing; HSA eligibility for DPC memberships removing barriers in 2026
- Tech-enabled MSOs reducing administrative burden without sacrificing ownership
- AAMC projects a deficit of **86,000 primary care doctors by 2036** — independent practices in underserved areas hold strategic value

**Where You Should Be — Independent Practice RCM Benchmarks:**

| KPI | Where You Should Be | Industry Median | Action If Below Target |
|---|---|---|---|
| Days in A/R | <35 days | 33–42 days | Implement automated claim status checks and denial worklists |
| Net Collection Rate | >96% | 90–95% | Audit underpayments; automate secondary billing |
| Denial Rate | <8% | 6–13% | Deploy AI-powered claim scrubbing; address top 3 denial codes |
| Clean Claims Rate | >97% | 90–95% | Add front-end eligibility verification automation |
| First-Pass Resolution | >85% | 70–85% | Review coding accuracy and modifier compliance |
| AR >120 Days | <10% | 15–25% | Escalate aged claims to dedicated follow-up team |

**Biggest Revenue Cycle Leaks for Independent Practices:**

- Denials/appeals: **48%** of revenue leakage
- Front-end issues (eligibility, registration errors): **23%**
- Billing/collections gaps: **14%**
- Coding errors: **13%**

> **💡 Key Insight:** Independent practices face a technology adoption gap that directly impacts their denial rates. Payer AI review systems now evaluate authorization requests before human reviewers — practices without matching technology face systematically higher denial rates. The most impactful first investment isn't autonomous coding; it's automated real-time eligibility verification and claim scrubbing.

**Sources:** [PAI-Avalere Physician Employment Trends 2019–2023](https://www.physiciansadvocacyinstitute.org/PAI-Research/PAI-Avalere-Study-on-Physician-Employment-Practice-Ownership-Trends-2019-2023) · [Becker's — Physician Consolidation Stats](https://www.beckersasc.com/asc-transactions-and-valuation-issues/50-stats-behind-the-physician-consolidation-wave/) · [NPR — Primary Care Doctors Unite (March 2026)](https://www.npr.org/2026/03/10/nx-s1-5707306/under-financial-strain-primary-care-doctors-unite) · [Doctors Management — 2026 Private Practice Playbook](https://www.doctorsmanagement.com/blog/the-2026-private-practice-playbook-how-independent-groups-are-surviving-margin-compression/) · [NCDS — RCM Benchmarks 2026](https://www.ncdsinc.com/rcm-benchmarks-for-2026-what-good-performance-looks-like-now/)

---

## Section 09
## Specialty RCM Spotlight: Primary Care, Cardiology, Orthopedics, Oncology, and More

| Specialty | Key Update | Data Point | Action |
|---|---|---|---|
| **Primary Care** | New APCM add-on G-codes (G0556, G0557, G0558) for behavioral health integration; E/M codes exempt from 2.5% efficiency adjustment | CF up to +3.77% for APM participants | Update fee schedules; begin billing APCM codes for qualifying patients |
| **Cardiology** | New complex PCI category replaces 92928 for bifurcation/multi-vessel lesions; 2.5% efficiency adjustment hits procedural wRVUs | Overall reimbursement ~+1% vs. 2025; 418 CPT changes | Update operative note templates for new PCI codes; model procedural volume impact |
| **Orthopedics** | Joint arthroplasty documentation requirements tightened; site-of-service a direct reimbursement driver | Denial rates above 20% in some settings; 285 procedures removed from IPO list | Update operative note templates to prevent downcoding; review ASC-eligible procedures |
| **Oncology** | IRA Maximum Fair Prices slashing drug reimbursement: ibrutinib -38%, pomalidomide -60%, palbociclib -50% | Facility settings ~-11% reimbursement; community ~+6% | Model drug margin impact per protocol; shift eligible infusions to community settings |
| **Radiology** | Screening mammography RVU reduced 1.82%; screening tomosynthesis reduced 2.55% | Overall -2% for diagnostic radiology; permanent remote imaging supervision finalized | Renegotiate global imaging contracts; leverage remote supervision for staffing |
| **Neurology** | G35 (multiple sclerosis) deleted — replaced by phenotype/activity-specific codes | Overall +1% payment increase; new Category III codes for continuous EEG/AI-supported EEG | Update MS diagnosis workflows immediately; explore AI-assisted diagnostic coding |
| **Mental Health** | Permanent telehealth parity; audio-only permanently allowed; LMFTs/LMHCs billing at 75% of psychologist rate | Home = originating site (POS 10, non-facility rates); 6-month in-person visit requirement | Update POS codes for home-based telehealth; set in-person visit scheduling triggers |
| **Gastroenterology** | New CPT 43889 for Endoscopic Sleeve Gastroplasty (replacing C9784); tighter LCD requirements | PE involvement exceeds 30% in GI; efficiency adjustment hits endoscopy wRVUs | Adopt new gastroplasty code; review LCD compliance for screening vs. diagnostic colonoscopy |

**Cross-Specialty Alert — GLOBE Model (October 1, 2026):**

The CMS **Generics Leveraging Outsized Biologic Expenditures (GLOBE)** model starts October 1, 2026 for Part B physician-administered drugs, ending the traditional ASP + 6% formula. Practices administering biologics and biosimilars should model the financial impact before the transition — community oncology and rheumatology practices will feel this most acutely.

> **💡 Key Insight:** The oncology reimbursement overhaul is the biggest specialty-specific disruption this year. With IRA-driven drug price cuts of 38%–60% on key agents and an 11% facility reimbursement reduction, oncology practices that haven't modeled per-protocol margins risk discovering revenue shortfalls after the fact. Community oncology settings gain a 6% lift — making site-of-service optimization a strategic imperative.

**Sources:** [ASCO — 2026 Medicare Reimbursement Changes](https://www.asco.org/news-initiatives/policy-news-analysis/significant-Medicare-physician-reimbursement-methodology-changes-finalized-2026) · [ACC — 2026 Medicare PFS Dive](https://www.acc.org/Latest-in-Cardiology/Articles/2025/11/06/12/51/Dive-Into-the-2026-Medicare-Physician-Fee-Schedule-Final-Rule) · [Neolytix — Neurology Billing 2026](https://neolytix.com/billing-coding-guides/neurology-medical-billing-coding-guide/) · [Behave Health — Mental Health Reimbursement 2026](https://behavehealth.com/mental-health-reimbursement) · [ACG — 2026 Payment Shifts](https://gi.org/2026/02/27/2026-payment-shifts/)

---

## Section 10
## This Week's Action Items

1. **Audit UHC claims for Excludes 1 violations.** UHC's March 1 enforcement of ICD-10 Excludes 1 rules means any claim with mutually exclusive diagnosis code combinations is being denied. Run a retroactive report on all UHC outpatient claims since March 1 and correct any flagged pairings before timely filing deadlines expire.

2. **Prepare to pull payer PA metrics after March 31.** CMS-0057-F requires impacted payers to publicly report CY 2025 prior authorization approval rates, denial rates, and turnaround times by March 31. Bookmark your top 5 payer websites and assign a team member to pull and compare these metrics against your internal PA tracking data within the first week of April.

3. **Verify HCPCS code updates effective April 1.** Load the 36 new HCPCS Level II codes into your billing system before April 1. Pay special attention to reinstated code J1572 (Flebogamma) and new code Q0238 (TYENNE). Confirm your MACs have implemented changes by April 6.

4. **Model 2027 physician payment scenarios.** The 2.5% statutory payment bump expires December 31, 2026, and MedPAC's FY 2027 recommendations signal a 1.2%–1.7% net reduction. Run financial projections on your top 20 procedure codes by payer mix under 2027 conversion factor scenarios to prepare for potential revenue compression.

5. **Evaluate autonomous coding solutions.** CodaMetrix's Best in KLAS validation and AKASA's Cleveland Clinic deployment signal that autonomous coding is production-ready. Request demos from CodaMetrix, AKASA, and Epic Penny using your actual claim volume, specialty mix, and denial patterns to assess fit and ROI.

6. **Update MS diagnosis workflows for ICD-10 G35 deletion.** The deletion of ICD-10 code G35 (multiple sclerosis) requires practices treating MS patients to use the new phenotype- and activity-specific replacement codes. Update your diagnosis workflow templates and train clinical staff before claims start denying for invalid codes.

---

## Big Stat

# $782M

**Annual savings projected from CMS's electronic claims attachments rule — finalizing the end of fax machines and postal mail for claims documentation. The compliance deadline is May 26, 2028, but the practices that move first will capture efficiency gains two years ahead of the laggards.**

*Source: CMS Final Rule, March 20, 2026*

---

*RCM Pulse Weekly is published every Monday. Next issue: March 30, 2026.*

*Content sourced from CMS.gov, Federal Register, AAPC, HFMA, AHA, AHIP, Becker's Healthcare, RevCycleIntelligence, Healthcare IT News, Healthcare Dive, MedPAC, MACPAC, KLAS Research, GlobeNewswire, and vendor publications. All statistics and regulatory references are from public domain sources as of March 27, 2026.*
