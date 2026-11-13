# RCM Pulse Weekly
## Revenue Cycle Management Intelligence for Medical Practices

**November 13, 2026 • Volume 11, Issue 2**

---

## In This Issue

01. CMS Proposes CARE Rule Eliminating 3.26 Million Annual Staff Hours — $320M in Administrative Savings Targeted Across Medicare and Medicaid Providers
02. 49 Days to FHIR PA API Mandate — UHC Removes PA for Under-18 Services Effective December 1, Humana Cuts 600,000 MA Members for 2027, and 62% of Patients Facing PA Delays Give Up on Care
03. R1 Launches Six Connected AI Solutions on Phare OS, Reaching $275 Billion in Net Patient Revenue — Sagility Acquires Chirok Health for Clinical Documentation and Coding
04. ICD-10 Public Comment Deadline Closed Today — CPT 2027 PLA Codes Updated, AAPC November 25 Webinar, and New Remote Therapeutic Monitoring Codes for Mental Health
05. RCM Market on Path to $132 Billion by 2031 — Benchmarking Days in AR, Clean Claims, and Denial Rates Against HFMA Targets Before Year-End
06. Technology Spotlight: R1 Phare Denials Module, CareCloud Wound Care Expansion, Peppermint $4.7M Seed Round, and 70% of Providers Planning RCM Vendor Consolidation
07. Compliance Corner: TiC Final Rule Eliminates Ghost Rates, CMS Prescription Drug File Schema Begins This Month, and December 31 Medicare Participation Deadline
08. Independent Practice Watch: 76% of Independent Practices Lack Full Visibility Into Revenue Leakage — Veradigm 2026 Survey Reveals the Blindspot Threatening Practice Survival
09. Specialty RCM Spotlight: Primary Care RTM Codes, Cardiology MA Network Losses, Orthopedics Modifier Scrutiny, Oncology AR Days, Radiology AI Codes, Mental Health Rate Update, Neurology RVU Changes
10. This Week's Action Items

---

## Section 01 — Regulatory / Payment Updates

### CMS Proposes CARE Rule Eliminating 3.26 Million Annual Staff Hours — $320M in Administrative Savings Targeted Across Medicare and Medicaid Providers

CMS published proposed rule CMS-3484-P — "Cutting Administrative Requirements for Excellence in Patient Care" (CARE) — in the Federal Register on November 10, 2026. The proposal is the most sweeping deregulatory action on Medicare and Medicaid provider Conditions of Participation in years, targeting duplicative requirements, outdated COVID-era mandates, and administrative overhead that CMS estimates consumes over 3.26 million annual staff hours across provider types.

**Stat cards:**
- **3.26M hours** — Annual staff time reduction estimated from the CARE proposed rule
- **$320M** — CMS projected cost savings if the CARE rule is finalized as proposed
- **21 provider types** — Covered in CMS's comprehensive CoP review under this rule
- **December 31** — Deadline for CY 2027 Medicare participation decision (separate from CARE)

### CARE Rule: What It Proposes

The rule covers all 21 Medicare and Medicaid provider and supplier types. Key categories of change include:

- **COVID-era requirements removed:** CMS proposes to end the COVID-19 vaccine offer and documentation requirements for long-term care residents, which were kept post-pandemic as ongoing conditions of participation.
- **Training duplication cut:** CMS argues that EMTALA requirements, existing discharge planning CoP requirements, and accrediting organization standards already ensure staff competency in transfer processes — removing redundant annual training mandates.
- **Hospital operational flexibility:** CAH distance rule clarifications and birth tissue patient-rights standards are updated. CMS also proposes to ease administrative requirements where existing accreditation standards already achieve the same patient safety outcome.
- **Hospice updates:** Hospice providers will see adjustments to conditions intended to reduce documentation burden without affecting care quality.

This is a proposed rule, not a final rule, so practices should comment during the comment period but not adjust workflows until finalization. The comment deadline was not specified in available sources — check the Federal Register entry (2026-22812) for the exact date.

### Drug Pricing: Permanent Negotiation Framework Finalized

The CMS MLN Connects newsletter dated November 12, 2026 notes that a final rule was issued creating a permanent framework for Medicare drug price negotiation, following the initial negotiation rounds conducted under the Inflation Reduction Act. This framework is expected to expand the number of drugs subject to negotiated pricing beyond the first cycles, with direct implications for practices that administer Part B drugs — primarily oncology, rheumatology, and infusion centers.

> **Key Insight:** The CARE proposed rule would reduce administrative burden without altering reimbursement. For billing managers, the most practical immediate benefit would be the removal of redundant training documentation requirements. However, CoP changes do not translate to streamlined payer workflows — billing automation and PA efficiency remain unchanged by this rule.

**Sources:** [CMS — CARE Proposed Rule Fact Sheet (CMS-3484-P)](https://www.cms.gov/newsroom/fact-sheets/medicare-medicaid-programs-cutting-administrative-requirements-excellence-patient-care-care-cms-3484) • [Federal Register — CMS-3484-P](https://www.federalregister.gov/documents/2026/11/10/2026-22812/medicare-medicaid-programs-cutting-administrative-requirements-for-excellence-in-patient-care) • [AHA News — CMS Proposes Rule to Reduce Administrative Burden](https://www.aha.org/news/headline/2026-11-05-cms-proposes-rule-reduce-administrative-burden-hospitals-other-providers) • [CMS MLN Connects — November 12, 2026](https://www.cms.gov/training-education/medicare-learning-network/newsletter/mln-connects-newsletter-november-12-2026) • [HFMA — CMS Proposal to Cut Administrative Requirements](https://www.hfma.org/legal-and-regulatory-compliance/cms-proposal-cut-administrative-requirements/)

---

## Section 02 — Prior Authorization / Payer Relations

### 49 Days to FHIR PA API Mandate — UHC Removes PA for Under-18 Services Effective December 1, Humana Cuts 600,000 MA Members for 2027, and 62% of Patients Facing PA Delays Give Up on Care

With exactly 49 days remaining until the CMS-0057-F FHIR Prior Authorization API mandate takes effect on January 1, 2027, three converging payer developments this week underscore both the operational urgency and the human cost of a broken prior authorization system. UnitedHealthcare will begin removing PA requirements for select services for patients under age 18 on December 1, expanding Medicaid reductions to Nebraska, New Jersey, and Tennessee. And a Penguin AI survey released November 12 found that 62% of patients facing PA delays or denials have given up on care entirely.

**Stat cards:**
- **49 days** — Until the CMS-0057-F FHIR PA API mandate takes effect (January 1, 2027)
- **62%** — Patients facing PA delays/denials who have given up on care (Penguin AI, Nov 2026)
- **600,000** — MA members affected by Humana's 2027 plan exits
- **Dec 1** — When UHC begins removing PA for select under-18 services

### FHIR PA API Readiness: 49 Days

The CMS-0057-F mandate requires Medicare Advantage organizations, Medicaid managed care plans, CHIP agencies, and exchange issuers to implement FHIR-based Prior Authorization APIs by January 1, 2027. Practices benefit from this through EHR-embedded PA status updates and coverage requirements discovery that eliminate fax and phone workflows. The readiness question is on the payer side — but practices should confirm their EHR vendor and PM system have activated the FHIR PA data feeds before the deadline.

A Healthcare Business Today analysis notes that electronic prior authorization under CMS-0057-F is a mandate on payers, but practices still need to configure the receiving end: 270/271 eligibility, 278 prior authorization request transactions, and integration with the FHIR endpoints being stood up by their primary payers.

### UHC Under-18 PA Removal Expands

Beginning December 1, 2026, UnitedHealthcare will remove prior authorization requirements for select services for patients under age 18. This follows its earlier commitment to eliminate approximately two-thirds of pediatric PA requirements, including imaging. The expansion now includes Medicaid plans in Nebraska, New Jersey, and Tennessee. Pediatric practices and family medicine practices with high pediatric volume should proactively update their PA requirement matrices to remove stale authorization requests that waste staff time.

### Medicare Advantage 2027: Humana Exits, Network Narrowing Accelerates

Humana's 2027 Medicare Advantage plan reductions affect approximately 600,000 current members. UnitedHealthcare, Aetna, and Centene are also cutting plan footprints, though the national plan count dips only slightly (5,553 in 2026 to roughly 5,532 in 2027). The more significant shift is network narrowing — a doctor in-network in 2026 may not be in 2027, and insurers are systematically shifting from PPOs to HMOs to tighten utilization management. CMS finalized a 2.48% average payment rate increase for MA plans in 2027, translating to $13+ billion in additional payments — but that additional funding is being applied to narrower benefit designs and tighter networks rather than broader access.

> **Warning:** If your practice has significant Medicare Advantage volume, check your 2027 contract status with Humana, UHC, and Aetna networks now. Practices that discover mid-January that they were dropped from a narrowed network will face billing disruption, claims rejections, and patient confusion during one of the highest-volume claim months of the year.

**Sources:** [CMS — Electronic Prior Authorization](https://www.cms.gov/priorities/electronic-prior-authorization/overview) • [Healthcare Business Today — Electronic Prior Authorization: Preparing for 2027](https://www.healthcarebusinesstoday.com/electronic-prior-authorization-2027-readiness/) • [UHC Provider — Prior Auth Update December 2026](https://www.uhcprovider.com/en/prior-auth-advance-notification.html) • [Penguin AI Survey — 62% of PA Patients Give Up on Care (Nov 12, 2026)](https://www.prnewswire.com/news-releases/six-in-10-patients-and-caregivers-facing-prior-authorization-delays-or-denials-have-given-up-on-care-penguin-ai-survey-finds-302937233.html) • [Oliver Wyman — Medicare Advantage 2027 Market](https://www.oliverwyman.com/our-expertise/perspectives/health/2026/nov/medicare-advantage-market-2027-plan-exits-snp-growth.html) • [STAT News — Medicare Advantage 2027 Higher Deductibles](https://www.statnews.com/2026/10/01/medicare-advantage-plans-have-higher-deductibles-fewer-benefits-in-2027/)

---

## Section 03 — AI & Automation Deep Dive

### R1 Launches Six Connected AI Solutions on Phare OS, Reaching $275 Billion in Net Patient Revenue — Sagility Acquires Chirok Health for Clinical Documentation and Coding

This week's most significant AI development in revenue cycle was R1's November 12 announcement expanding its Phare OS revenue operating system with six connected AI solutions, bringing the total net patient revenue on the platform to over $275 billion. The expansion marks R1's move from a point-solution AI vendor to an integrated revenue intelligence platform that shares clinical, financial, and payer data across the full revenue cycle. Separately, Sagility agreed to acquire Chirok Health, a clinical documentation and medical coding firm, in a move that will strengthen Sagility's AI-driven RCM and risk adjustment capabilities.

**Stat cards:**
- **$275B** — Net patient revenue on R1 Phare OS after the Nov 12 expansion
- **$95B** — NPR added to Phare OS in just the past six months from new module adopters
- **6** — Connected AI solutions now live or in early access on Phare OS
- **68.7%** — Healthcare organizations running 6+ RCM vendors/platforms (IDC, R1-sponsored)

### R1 Phare OS: Six-Module Expansion

The November 12 announcement details four commercially available modules and two in early access:

**Commercially available:**
- **Phare Auth** — Prior authorization AI covering coverage requirements discovery and documentation
- **Phare Audit** — Automated clinical documentation audit before submission
- **Phare UM** — Utilization management AI for inpatient and observation-status decisions
- **Phare Denials** — NEW: denial management module that reconstructs the payer's original determination logic to build appeals with payer-specific supporting evidence

**Early access (broader availability in 2027):**
- **Phare CDI** — Clinical documentation improvement AI
- **Phare Recovery** — Underpayment recovery and secondary billing automation

R1 says health systems representing approximately $95 billion in NPR have adopted individual modules in the past six months. The strategic argument underlying the platform is that 68.7% of healthcare organizations run six or more separate RCM vendors, creating data fragmentation that prevents the intelligence developed in one workflow (e.g., denial root-cause analysis) from improving another (e.g., prior authorization submissions).

### Sagility Acquires Chirok Health

Sagility agreed to acquire Chirok Health, a clinical documentation and medical coding firm, to strengthen its revenue cycle and risk adjustment services. The Health IT Answers November 12 roundup notes the transaction is expected to deepen Sagility's AI-assisted coding capabilities, particularly in hierarchical condition category (HCC) risk adjustment coding that is critical for Medicare Advantage revenue integrity.

> **Bottom Line:** The R1 Phare Denials module is the AI development most immediately relevant to billing managers — the idea that an AI system can reconstruct the same payer logic used to generate a denial, then build a targeted appeal using that logic, is a qualitative shift from pattern-matching appeal letter generation. Organizations already on Phare OS should activate the Denials module during the remaining weeks of Q4 to build baseline performance data before January's high-volume claim season.

**Sources:** [GlobeNewswire — R1 Takes Aim at Healthcare's Fragmented Revenue Cycle (Nov 12, 2026)](https://www.globenewswire.com/news-release/2026/11/12/3401540/0/en/r1-takes-aim-at-healthcare-s-fragmented-revenue-cycle-with-six-connected-ai-solutions.html) • [Fierce Healthcare — R1 New AI Solutions Weekly Rundown](https://www.fiercehealthcare.com/health-tech/weekly-rundown-openevidence-launches-free-access-intelligence-tools-clinicians-r1) • [Health IT Answers — Financial Edition November 12, 2026](https://healthitanswers.net/health-it-business-news-financial-edition-november-12-2026) • [Experian Health — AI in Healthcare RCM 2026](https://www.experian.com/blogs/healthcare/revenue-cycle-management-and-ai/) • [AHA — 3 Ways AI Can Improve Revenue Cycle Management](https://www.aha.org/aha-center-health-innovation-market-scan/2024-06-04-3-ways-ai-can-improve-revenue-cycle-management)

---

## Section 04 — Coding Updates

### ICD-10 Public Comment Deadline Closed Today — CPT 2027 PLA Codes Updated, AAPC November 25 Webinar, and New Remote Therapeutic Monitoring Codes for Mental Health

Today, November 13, 2026, marks the close of the public comment window for proposed ICD-10-CM and ICD-10-PCS changes presented at the September 15–16, 2026 ICD-10 Coordination and Maintenance Committee meeting. Any approved codes from this comment cycle would take effect October 1, 2027. Organizations that have not yet submitted comments on proposed diagnostic codes affecting their patient population have no further opportunity to influence this cycle. Separately, the AMA has updated its approved Proprietary Laboratory Analysis (PLA) code list effective October 1, with CPT 2027 preparation materials from AAPC available through the November 25 coding webinar.

**Stat cards:**
- **Oct 1, 2027** — Effective date for ICD-10 codes from this comment cycle
- **Nov 25** — AAPC CPT 2026 coding update webinar
- **418 total** — CPT code set changes in 2026 (288 new, 46 revised, 84 deleted)
- **Oct 1** — When AMA updated the CPT 2027 PLA code list

### ICD-10 Public Comment Cycle Closes

Today's deadline closes the November 2026 comment window for the September 2026 ICD-10 C&M meeting. CMS will post its decisions on proposed diagnosis and procedure code additions and revisions in coming months, with new ICD-10-PCS codes for the following April 1 cycle to be announced separately. Practice billing teams should track CMS's ICD-10 C&M meeting schedule and monitor for code additions affecting their primary service lines before the October 1, 2027 effective date.

### CPT 2027 PLA Codes: October 1 Update

The AMA updated its approved PLA code list on October 1, 2026, with new proprietary laboratory analysis codes for CPT 2027. These codes cover laboratory tests with specific trade names from specific labs, and practices ordering or reporting these tests need to verify their charge description masters reflect the current approved PLA code set. AAPC noted that the AMA's expanded use of PLA codes continues to increase — practices with laboratory billing should audit CDM entries against the October 1 approved list.

### Remote Therapeutic Monitoring: New Codes Operational

Mental health and behavioral health practices should ensure their CDMs and billing workflows reflect the 2026 RTM code set. New remote therapeutic monitoring codes include:
- **98985** and **99470** — New codes for remote therapeutic monitoring of therapeutic response and adherence
- **G0568–G0570** — Collaborative Care Model (CoCM) codes for behavioral health integration in primary care settings

Radiology practices should also note that four new Category I CPT codes for AI-assisted imaging interpretation were added in the 2026 set, with NCCI edit guidance applicable to modifier 26/TC splits when billing AI-assisted reads alongside traditional interpretations. ACR advised radiology practices to review the Q3 2026 edit files effective July 1.

> **Action Required:** Run a CDM audit this week against the October 1, 2027 proposed ICD-10 changes from the September C&M meeting. Practices with mental health, remote monitoring, or behavioral health integration services should also verify 98985, 99470, and CoCM codes G0568–G0570 are in CDM and mapped correctly to your PM system.

**Sources:** [CMS — Fall 2026 ICD-10-PCS Update Materials](https://www.cms.gov/files/document/fall-2026-icd-10-pcs-update-materials.pdf) • [AAPC — Coding Newsletters & Articles](https://www.aapc.com/codes/coding-newsletters/articles) • [AAPC — 2026 CPT Coding Books](https://www.aapc.com/medical-coding-books/icd-10-cm-book/) • [AMA — CPT 2026 PLA Code Update](https://www.aapc.com/blog/93398-ama-releases-cpt-2026/) • [AnnexMed — Radiology CPT Code Updates 2026](https://annexmed.com/radiology-cpt-code-updates-2026) • [MedSoler RCM — Mental Health CPT Codes 2026](https://medsolercm.com/blog/mental-health-cpt-codes)

---

## Section 05 — Revenue Velocity / KPIs

### RCM Market on Path to $132 Billion by 2031 — Benchmarking Days in AR, Clean Claims, and Denial Rates Against HFMA Targets Before Year-End

A MarketsandMarkets report released November 11, 2026 projects the global revenue cycle management market to reach $132.06 billion by 2031 at a compound annual growth rate of 12.4%, driven by the shift to AI-driven platforms and payer complexity that exceeds the capacity of legacy rule-based systems. The market growth number is a backdrop to the more immediate operational question for most practices: where do your Q4 KPIs stand against the benchmarks that determine whether you're keeping pace or falling behind? With six weeks left in 2026, this is the time to identify gaps before they carry into January.

**Stat cards:**
- **$132.06B** — Global RCM market projected by 2031 at 12.4% CAGR (MarketsandMarkets, Nov 2026)
- **<30 days** — Best-in-class Days in AR target (industry standard: 35–50 days)
- **≥95%** — Clean claim rate minimum target (best-in-class ≥98%)
- **<5%** — Denial rate target (national average: 8–12%)

### Days in AR: Benchmarking the Final Six Weeks of 2026

Days in AR remains the single most closely watched RCM KPI because it integrates charge lag, claim submission timing, payer adjudication speed, and AR follow-up efficiency into one number. The 2026 benchmarks show:

| Metric | Industry Average | Target | Best-in-Class |
|---|---|---|---|
| Days in AR | 35–50 days | <38 days | <30 days |
| Clean Claim Rate | 88–96% | ≥95% | ≥98% |
| Denial Rate | 8–12% | <5% | <3% |
| Net Collection Rate | 90–95% | ≥96% | ≥97% |
| Cost to Collect | 5–10% | <4% | <3% |

The linkage between clean claim rate and Days in AR is well-documented: every 1 percentage point improvement in first-pass clean claim rate reduces Days in AR by approximately 0.5–1 day, because corrected claims cycle back through the submission and adjudication queue, adding 2–4 weeks to revenue realization.

### Q4 Revenue Velocity Checklist

For the final six weeks of 2026, the highest-impact operational focus areas are:

1. **Charge lag review:** Identify services rendered in October/November that have not yet been coded and submitted. Every day of charge lag = one additional day in AR.
2. **Payer aging clean-up:** Pull AR by payer bucket. Claims 90+ days outstanding are unlikely to self-resolve — work them or write them off.
3. **Year-end patient balance strategies:** Patient payments represent approximately one-third of physician revenue in 2026. High-deductible plan patients who have met their out-of-pocket maximum for the year are more likely to pay balances now than in January.

> **Action Required:** Set an AR floor rule: any claim over $200 that is 60+ days with no payer response gets worked. Claims under $60 at 90+ days should be evaluated against cost-to-collect — pursuing a $45 balance that takes 2 hours of staff time is a loss. Automate small-balance write-offs to protect staff capacity for high-value AR work.

**Sources:** [GlobeNewswire — RCM Market to Reach $132.06 Billion by 2031 (Nov 11, 2026)](https://www.globenewswire.com/news-release/2026/11/11/3400815/0/en/revenue-cycle-management-market-to-worth-usd-132-06-billion-by-2031-at-a-cagr-of-12-4-marketsandmarkets.html) • [DataRovers — Revenue Cycle Management KPIs 2026](https://datarovers.com/revenue-cycle-management-kpis/) • [RCM Axis — Days in AR Benchmark 2026](https://rcmaxis.com/blog/reduce-days-in-ar/) • [HFMA MAP Keys — RCM Benchmark Framework](https://www.hfma.org/) • [Qualigenix — 12 Medical Billing KPIs to Track in 2026](https://qualigenix.com/medical-billing-kpis-practice-managers-2026/)

---

## Section 06 — Technology Spotlight

### Technology Spotlight: R1 Phare Denials Module, CareCloud Wound Care Expansion, Peppermint $4.7M Seed Round, and 70% of Providers Planning RCM Vendor Consolidation

The November 11–12 period brought a cluster of RCM technology news that together signal a consolidating market: larger platforms adding integrated AI capabilities, niche players raising capital to serve underserved billing verticals, and provider organizations planning to reduce the number of vendors they work with.

**Stat cards:**
- **70%+** — Provider organizations planning to reduce reliance on third-party RCM vendors (FinThrive survey)
- **$4.7M** — Peppermint seed round for clinical research billing automation (Nov 2026)
- **$132.06B** — Projected 2031 global RCM market size
- **6** — Phare OS AI modules now on R1's platform (4 live, 2 early access)

### CareCloud Wound Care Expansion

CareCloud announced new wound care specialty clients, a preferred-vendor selection by Vantage Health Collective, and a new bi-directional EHR interface that enables practices to use CareCloud's RCM services without replacing their existing EHR. This is a meaningful development for independent wound care practices that have historically been underserved by enterprise RCM platforms. The integration allows charge capture, claim submission, and denial management to run through CareCloud while clinical documentation remains in the existing EHR. CareCloud also reported multimillion-dollar payer client audit wins in its Q4 press release.

### Peppermint: $4.7M for Clinical Research Billing

Clinical research billing remains one of the most complex and underautomated RCM verticals — with separate payer logic for investigator-initiated vs. industry-sponsored trials, coverage analysis requirements, and consent-coding dependencies. Peppermint's $4.7 million seed round for clinical research billing automation addresses a gap in an $80B+ clinical research market that most mainstream RCM platforms do not cover. For academic medical centers and large group practices with active research portfolios, this is a vendor worth tracking.

### RCM Vendor Consolidation Trend

FinThrive research cited in the MarketsandMarkets November 11 report finds that more than 70% of provider organizations expect to reduce their reliance on third-party RCM vendors, consolidating toward integrated platforms. Black Book's 2026 hospital RCM rankings named Waystar as the top-rated vendor for agentic AI RCM, with Epic, TruBridge, and XIFIN leading other categories.

> **Bottom Line:** The vendor consolidation trend is a signal, not a recommendation. Consolidating to fewer RCM platforms makes sense if the unified platform delivers better data flow between modules — but consolidating to a single vendor that underperforms in one specialty vertical (e.g., oncology J-code billing, behavioral health RTM coding) can cost more in revenue leakage than the administrative efficiency gained. Evaluate performance by specialty, not platform brand.

**Sources:** [GlobeNewswire — CareCloud Wound Care Expansion (Nov 11, 2026)](https://www.globenewswire.com/news-release/2026/11/11/3400657/16541/en/carecloud-accelerates-wound-care-expansion-with-new-clients-ehr-integration-and-multimillion-dollar-payer-client-audit-wins.html) • [Health IT Answers — Financial Edition November 12, 2026](https://healthitanswers.net/health-it-business-news-financial-edition-november-12-2026) • [GlobeNewswire — RCM Market $132.06 Billion by 2031](https://www.globenewswire.com/news-release/2026/11/11/3400815/0/en/revenue-cycle-management-market-to-worth-usd-132-06-billion-by-2031-at-a-cagr-of-12-4-marketsandmarkets.html) • [R1 RCM — Phare OS Revenue Operating System](https://www.r1rcm.com/newsroom/r1-launches-phare-healthcare-s-first-revenue-operating-system) • [Becker's Hospital Review — R1 Launches Revenue Operating System](https://www.beckershospitalreview.com/finance/r1-rcm-launches-revenue-operating-system/)

---

## Section 07 — Compliance Corner

### Compliance Corner: TiC Final Rule Eliminates Ghost Rates, CMS Prescription Drug File Schema Due This Month, and December 31 Medicare Participation Deadline

Three distinct compliance timelines converge in November 2026: the Transparency in Coverage final rule restructuring payer machine-readable files and eliminating ghost rates, CMS beginning development of the first standardized Prescription Drug File schema this month, and the approaching December 31 deadline for CY 2027 Medicare participation decisions.

**Stat cards:**
- **Dec 31** — CY 2027 Medicare participation decision deadline
- **Nov 2026** — When CMS begins developing the Prescription Drug File schema (finalize ~May 2027)
- **Oct 5, 2026** — Date TiC final rule was finalized by HHS, Labor, and Treasury
- **49 days** — Until FHIR PA API mandate takes effect

### Transparency in Coverage: Ghost Rates and File Restructuring

The HHS, Labor, and Treasury departments finalized updates to the federal Transparency in Coverage (TiC) requirements in a rule published around October 5, 2026. Two changes most directly affect practices:

**Ghost rate removal:** Payers must remove rates for services a provider is unlikely to be paid for given their specialty. These "ghost rates" — reimbursement values showing payment rates for services a practice never performs — have made the machine-readable files difficult for price comparison tools to use, and created confusion in market rate analyses. Removal requires payers to tighten the mapping between provider NPIs and service categories.

**Rate file restructuring:** Payers move from one machine-readable file per plan to one file per provider network. This change reduces file redundancy but requires practices using price comparison tools or reference-based pricing analytics to adjust their data ingestion pipelines.

**Prescription Drug File schema:** CMS indicated in MLN Connects (November 12) that it will begin developing the initial schema for the Prescription Drug File this month, with finalization expected around May 2027. This will eventually require payers to publish machine-readable drug pricing data in a standardized format.

### December 31 Participation Decision Deadline

Practices must submit their CY 2027 Medicare participation decisions (opt into assignment, opt out, or remain with current status) by December 31, 2026. CMS notes this date in the November 12 MLN Connects newsletter. The participation status determines whether the practice receives the full approved Medicare rate or only 95% of that rate for unassigned claims. For practices with significant Medicare volume, the participation decision should be reviewed annually as conversion factor changes affect the financial calculus.

> **Action Required:** Verify your FHIR PA API readiness with your EHR/PM vendor this week — with 49 days to the mandate, any technical gaps need to be identified now, not in December. Also confirm your CY 2027 Medicare participation decision before December 31, and review payer TiC machine-readable file access if you use rate transparency tools.

**Sources:** [CMS — MLN Connects November 12, 2026](https://www.cms.gov/training-education/medicare-learning-network/newsletter/mln-connects-newsletter-november-12-2026) • [CMS — Electronic Prior Authorization Overview](https://www.cms.gov/priorities/electronic-prior-authorization/overview) • [Fierce Healthcare — CMS Finalizes TiC Updates](https://www.fiercehealthcare.com/regulatory/cms-finalizes-updates-price-transparency-regulations-aim-improve-usability) • [Becker's Payer Issues — CMS Finalizes Price Transparency Overhaul](https://www.beckerspayer.com/policy-updates/cms-finalizes-price-transparency-overhaul-for-payers-6-things-to-know/) • [SlicedHealth — Price Transparency Compliance Checklist 2026](https://slicedhealth.com/price-transparency-compliance-checklist-what-cms-actually-requires-in-2026/) • [Alston & Bird — Health Care Week in Review November 6, 2026](https://www.alston.com/en/insights/publications/2026/11/health-care-week-in-review-november-6-2026)

---

## Section 08 — Independent Practice Watch

### 76% of Independent Practices Lack Full Visibility Into Revenue Leakage — Veradigm 2026 Survey Reveals the Blindspot Threatening Practice Survival

A 2026 Veradigm survey of 360 independent practice leaders — the most granular look at independent practice financial health published this year — found that only 24% of independent physician practices report high or complete visibility into where they're losing revenue. That means 76% of independent practices are operating with partial or no visibility into their revenue leakage. Combined with the finding that 54% of respondents said financial pressure increased over the prior 12 months, the data paints a picture of practices working harder, billing more carefully, and still losing money they can't see or account for.

**Stat cards:**
- **24%** — Independent practices with high or complete visibility into revenue leakage (Veradigm 2026)
- **54%** — Independent practices reporting increased financial pressure in the prior 12 months
- **~40%** — Share of physicians in private practice (down steadily from 60%+ in 2012)
- **~33%** — Share of physician revenue from patient payments in 2026 (Ventra Health estimate)

### Where Revenue Leakage Hides

For independent practices, the specific areas where revenue most commonly leaks without detection include:

- **Undercoded visits:** Without a documentation improvement program, practices may systematically underbill on complex visit types. A practice billing 70% 99213 and 30% 99214 on established patients when the patient acuity justifies a higher ratio is leaving 8–15% of E/M revenue on the table.
- **Missing charges:** Procedures performed in the office and not separately captured in the charge entry process — suture removals, joint injections, wound care — represent charges that simply never enter the billing pipeline.
- **Secondary payer leakage:** Medicare + supplemental, workers' compensation, and auto liability coordination-of-benefits errors can leave substantial secondary payer balances uncollected.
- **Eligibility gaps:** Practices without automated pre-visit eligibility checks are more likely to submit claims for coverage that lapsed or changed without notice.

### Where You Should Be: Independent Practice Benchmarks

| KPI | National Average | Independent Practice Target | High-Performer Threshold |
|---|---|---|---|
| Days in AR | 35–50 days | ≤38 days | ≤30 days |
| Clean Claim Rate | 88–94% | ≥95% | ≥97% |
| Net Collection Rate | 90–94% | ≥96% | ≥98% |
| Denial Rate | 8–12% | ≤5% | ≤3% |
| Cost to Collect | 5–10% | ≤4% | ≤3% |
| Revenue Leakage Visibility | 24% complete | 80%+ complete visibility | Real-time dashboards |

The revenue leakage visibility metric is the most undertracked. Practices should implement monthly reporting on: (1) charge lag by provider and service type, (2) claim submission-to-first-response time by payer, (3) denial root cause analysis by denial code, and (4) write-off rates by denial type. If you cannot produce these four reports today, that is your Week 1 benchmark improvement project.

> **Bottom Line:** A 76% revenue blindspot rate across independent practices is not an anomaly — it reflects the structural reality that most independent practices were built to deliver care, not to manage a revenue intelligence function. The difference between practices that survive the next five years and those that consolidate or close will increasingly be their capacity to instrument and monitor their own revenue cycle in real time.

**Sources:** [Veradigm — State of the Independent Practice in 2026](https://veradigm.com/img/resource-veradigm-state-of-independent-practice-2026-wp.pdf) • [Ventra Health — 2026 RCM Trend Report](https://ventrahealth.com/2026-rcm-trend-report/) • [Becker's ASC — Where Have All the Independent Physicians Gone?](https://www.beckersasc.com/asc-transactions-and-valuation-issues/where-have-all-the-independent-physicians-gone-2/) • [Health Prime — Revenue Resiliency for Physician Groups in 2026](https://www.hpiinc.com/resources/prime-blogs/revenue-resiliency-in-2026-how-strong-rcm-strategy-can-help-physician-groups-survive/) • [Encoda — Why PM's RCM Isn't Enough in 2026](https://encoda.com/practice-management-system-rcm-holding-back-practice/)

---

## Section 09 — Specialty RCM Spotlight

### Specialty RCM Spotlight: Primary Care RTM Codes, Cardiology MA Network Losses, Orthopedics Modifier Scrutiny, Oncology AR Days, Radiology AI Codes, Mental Health Rate Update, Neurology RVU Changes

| Specialty | Key Development | Action |
|---|---|---|
| **Primary Care** | New RTM codes 98985 and 99470 for remote therapeutic monitoring now billable; CoCM codes G0568–G0570 for behavioral health integration in primary care settings | Audit CDM for RTM code additions; confirm documentation requirements for CoCM billing |
| **Cardiology** | MA 2027 network reductions: Humana, UHC, Aetna all narrowing; cardiology median AR 39.4 days, 12.7% denial rate from cardiac imaging prior auth | Verify 2027 MA contract status this week; accelerate PA submissions for cardiac imaging on Humana/Aetna plans now |
| **Orthopedics** | Modifier 25 and 57 scrutiny remains elevated from BCBS and commercial payers; ASC orthopedic case volume growing under CY 2027 OPPS ASC-qualified procedure list additions | Document separately billed E/M before surgical procedures with Modifier 25/57; verify ASC procedure eligibility list updated |
| **Oncology** | Longest AR days of major specialties, driven by drug prior authorization, J-code administration, and Part B drug billing complexity; drug price negotiation framework finalized this week | Review J-code charge capture and administration fee billing; monitor drug pricing negotiation framework updates for Part B drugs |
| **Radiology** | Four new Category I CPT codes for AI-assisted imaging interpretation in 2026 set; ACR Q3 edit files in effect July 1; neurointerventional embolization codes 61624/61626 revised | Verify NCCI edit guidance for modifier 26/TC splits on AI-assisted reads; update procedure codes for CPT 61624 and 61626 |
| **Mental Health** | 2026 Medicare rate update: +3.26% to +3.85% rate increase; new RTM codes 98985/99470; CoCM G0568–G0570 for behavioral integration | Confirm rate table updated in PM system; activate RTM codes in CDM if not already live |
| **Neurology** | 2026 RVU update includes −2.5% efficiency adjustment to work RVUs for non-time-based services; EEG coding revisions effective January 2026; Category III code additions for extended EEG monitoring | Audit EEG billing codes against 2026 CPT set; adjust fee schedules for updated work RVUs |
| **Gastroenterology** | OPPS colonoscopy quality measure removed from ASC Quality Reporting Program for 2027 (from CY 2027 OPPS/ASC final rule) | Update quality reporting workflows; no longer submit colonoscopy follow-up interval measure for 2027 ASC reporting |

**Sources:** [Revenue Synergy — 2026 Medical Billing Benchmarks by Specialty](https://www.revenuesynergy.com/resources/2026-benchmark-report.html) • [Neolytix — Neurology Billing & Coding Guide 2026](https://neolytix.com/billing-coding-guides/neurology-medical-billing-coding-guide/) • [AnnexMed — Radiology CPT Code Updates 2026](https://annexmed.com/radiology-cpt-code-updates-2026) • [MedSoler RCM — Mental Health CPT Codes 2026](https://medsolercm.com/blog/mental-health-cpt-codes) • [QuestNS — Mental Health CPT Codes for 2026](https://questns.com/mental-health-cpt-codes-for-2026-modifiers/) • [Oliver Wyman — Medicare Advantage 2027 Market](https://www.oliverwyman.com/our-expertise/perspectives/health/2026/nov/medicare-advantage-market-2027-plan-exits-snp-growth.html) • [Sirius Solutions — 2026 Medicare RVU Changes: Neurology](https://www.siriussolutionsglobal.com/post/2026-medicare-rvu-changes-neurology)

---

## Section 10 — This Week's Action Items

### This Week's Action Items — 7 Steps Before November 20

1. **ICD-10 comment cycle noted.** The November 13 public comment deadline closed today. Mark your calendar for the next C&M meeting cycle and monitor CMS for decisions on this cycle's proposed codes — these will affect CDM coding for October 1, 2027.

2. **FHIR PA API readiness check.** With 49 days until the January 1, 2027 mandate, contact your EHR/PM vendor today and ask specifically: (a) Has the FHIR PA API integration been activated for your contracted payers? (b) Is your 278 prior authorization request transaction routing through the new FHIR endpoints or still using legacy EDI?

3. **Verify 2027 MA network status.** If your practice has Medicare Advantage patients from Humana, UHC, or Aetna, check your contract status now against the 2027 networks. Practices dropped from narrowed networks face January billing disruption. Use the Medicare Plan Finder to check if your physicians appear in-network on the 2027 plans.

4. **December 31 Medicare participation deadline.** Set a calendar reminder today. CY 2027 Medicare participation decisions must be submitted by December 31. Confirm with your practice administrator that the decision has been reviewed and submitted.

5. **CMS CARE rule — read and assess.** Review the CMS-3484-P proposed rule summary and CMS fact sheet for provisions affecting your practice type. While the savings are primarily for facilities and long-term care, physician practices should track the comment period deadline and assess whether any administrative burden reductions apply.

6. **CDM audit for RTM and CoCM codes.** Confirm that remote therapeutic monitoring codes (98985, 99470) and CoCM codes (G0568–G0570) are active in your CDM if applicable. For radiology practices, verify the four AI-assisted imaging Category I codes are in CDM with correct modifier guidance.

7. **Q4 revenue velocity sprint.** Pull your November 1 AR aging report now. Identify: (a) claims 60+ days outstanding by payer, (b) charge lag greater than 5 days, (c) patient balances from patients who have met their 2026 out-of-pocket maximum. These are your highest-probability Q4 collection opportunities.

**Sources:** [CMS — MLN Connects November 12, 2026](https://www.cms.gov/training-education/medicare-learning-network/newsletter/mln-connects-newsletter-november-12-2026) • [CMS — Medicare Plan Finder](https://www.medicare.gov/plan-compare/) • [Healthcare Business Today — Electronic Prior Authorization 2027 Readiness](https://www.healthcarebusinesstoday.com/electronic-prior-authorization-2027-readiness/) • [CMS — CARE Proposed Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/medicare-medicaid-programs-cutting-administrative-requirements-excellence-patient-care-care-cms-3484)

---

## Big Stat

**62%**

Six in ten patients facing a prior authorization delay, denial, or medication restriction say they have given up on care entirely — a figure that reflects not just patient harm but practice revenue that disappears without a trace. The claim is never filed. The denial is never appealed. The patient simply stops coming. As the FHIR PA API mandate approaches in 49 days, the case for investing in prior authorization automation is not bureaucratic compliance — it is protecting the clinical and financial integrity of every referral your practice makes.

*Source: Penguin AI Survey, November 12, 2026 (sample n=500 U.S. adults). CMS-0057-F FHIR PA API mandate effective January 1, 2027.*

---

*Next issue: November 20, 2026*

*RCM Pulse Weekly aggregates publicly available information from government sources, professional associations, and industry publications. It does not constitute legal, compliance, or billing advice. Verify all regulatory and coding information against official CMS publications before implementation.*
