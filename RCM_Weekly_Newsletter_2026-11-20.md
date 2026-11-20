# RCM Pulse Weekly
## Revenue Cycle Management Intelligence for Medical Practices

**November 20, 2026 • Volume 11, Issue 3**

---

## In This Issue

01. CRUSH Anti-Fraud Rule Targets $90 Billion in Medicare Savings — CMS-6098-P Released November 16 with 30-Day Enrollment Reporting and MA Cross-Enrollment Requirements
02. 42 Days to FHIR PA API Mandate — One Year of Payer PA Commitments: Cigna Standardizes 70%, Aetna Hits 88%, Only 36% of Providers Believe Payers Deliver
03. Agentic AI in RCM: What's Actually Running in Production — AGS Health Deploys Denial Agent, QWay Analysis Separates Signal From Noise
04. CPT 2027 Final Countdown: AAPC Webinar in 5 Days, CDM Audit Window Closing, and Q3 2026 HCPCS Drug Decisions Posted
05. Kodiak H1 2026 Data: Initial Denials Down to 10.63% but Final Commercial Denials Up 9.1% — MGMA Reports 48% of Revenue Leaks Come From Denials
06. Technology Spotlight: VisiQuate Acquires Artiva HCx — KLAS #1 Analytics Platform Adds Execution Layer; Children's Mercy Outsources 473 RCM Roles
07. Compliance Corner: CRUSH Comment Deadline January 19, 340B Billing Modifiers JG/TB/XX Due January 1, and RPM/RTM Initiating Visit Rule Takes Effect
08. Independent Practice Watch: 30% of H1 2026 Healthcare Bankruptcies Are Physician Practices — Congressional Pay Reform Advances as Only Structural Relief
09. Specialty RCM Spotlight: 340B Oncology Impact, Cardiology Pay Reform Push, Primary Care RPM/RTM Rule, Orthopedics Year-End ASC Velocity
10. This Week's Action Items

---

## Section 01 — Regulatory / Payment Updates

### CRUSH Anti-Fraud Rule Targets $90 Billion in Medicare Savings — CMS-6098-P Released November 16 With 30-Day Enrollment Reporting and MA Cross-Enrollment Requirements

CMS released the Comprehensive Regulations to Uncover Suspicious Healthcare (CRUSH) proposed rule (CMS-6098-P) on November 16, 2026, targeting an estimated $90 billion in taxpayer savings through the most significant overhaul of Medicare and Medicaid enrollment oversight in a generation. The rule would impose a universal 30-day deadline for all provider enrollment changes, require providers billing Medicare Advantage to also enroll in Original Medicare, expand CMS's authority to deny or revoke enrollment based on fraud risk assessments, and mandate MA organizations to submit fraud referrals. Comment period closes January 19, 2027.

**Stat cards:**
- **$90B** — CMS estimated taxpayer savings from the CRUSH proposed rule (CMS-6098-P)
- **30 days** — Proposed universal deadline for all Medicare enrollment change reporting
- **ASP−28%** — New 340B drug payment rate in CY 2027 OPPS (down from ASP+6%)
- **Jan 19, 2027** — Comment deadline for CRUSH proposed rule; CMS moratoria extended through Nov 2026

### CRUSH Rule: Key Provisions for Physician Practices

The CRUSH proposed rule (CMS-6098-P) affects physician practices across four operational dimensions:

- **Enrollment reporting:** A unified 30-day deadline would replace the current split between 30- and 90-day reporting windows for different types of enrollment changes. If finalized, the effective date would be two years post-publication — but practices should begin auditing their enrollment change tracking processes now.
- **MA cross-enrollment:** Providers billing Medicare Advantage plans would be required to also enroll in Original Medicare. For independent practices billing primarily through commercial MA contracts, this represents a new compliance requirement. Many already have dual enrollment; those that don't should assess the administrative pathway.
- **Fraud risk revocation:** CMS would gain authority to deny or revoke Medicare enrollment when it determines a party poses an undue fraud, waste, or abuse risk — a standard that is broader than current grounds for revocation. Practices with unusual billing patterns should ensure documentation systems can withstand this level of scrutiny.
- **Extended moratoria:** CMS extended the home health and hospice moratoria on November 13, 2026. The moratorium on certain DMEPOS suppliers ended August 27, 2026.

### 340B: ASP Minus 28% Takes Effect January 1

The CY 2027 OPPS/ASC final rule (Federal Register: November 6, 2026) finalizes 340B-acquired drug reimbursement at ASP minus 28% — a reduction from the current ASP plus 6%. The proposed cut had been deeper (ASP minus 33.4%), and the final rule offsets the drug payment reduction with a 7.50% increase to the OPPS conversion factor for non-drug services. CMS estimates the drug payment policy will reduce OPPS drug payments by approximately $4.65 billion in 2027.

Billing teams must configure three new modifiers by January 1:
- **JG** — 340B-acquired drugs subject to the payment reduction
- **TB** — 340B-acquired drugs exempt from the reduction (continuing at ASP+6%)
- **XX** — All non-340B drugs

> **Warning:** The JG/TB/XX modifier transition is a hard-deadline billing change. Practices and hospital outpatient departments that submit 340B drug claims without the correct modifier after January 1 will receive incorrect payment and face retroactive adjustment exposure. Begin billing system configuration now.

**Sources:** [CMS — CRUSH Proposed Rule Press Release (CMS-6098-P)](https://www.cms.gov/newsroom/press-releases/cms-crush-proposed-rule-aims-reap-nearly-90-billion-taxpayers-savings-targeting-fraud-across) • [AHA — CMS Issues Proposed CRUSH Rule](https://www.aha.org/news/headline/2026-11-17-cms-issues-proposed-rule-crush-initiative-addressing-fraud) • [Foley Hoag — CRUSH Proposed Rule Analysis](https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/november/cms-crush-proposed-rule-builds-on-new-exclusion-and-enrollment-authorities-raising-the-stakes-for/) • [Federal Register — CY 2027 OPPS/ASC Final Rule](https://www.federalregister.gov/documents/2026/11/06/2026-22739/medicare-program-hospital-outpatient-prospective-payment) • [Advis — CY 2027 OPPS 340B Payment Cuts](https://advis.com/340b/cy-2027-opps-340b-payment-cuts/) • [Conventional Law — CMS Final OPPS 340B Reduction](https://conventuslaw.com/report/us-cms-final-opps-rule-will-reduce-reimbursement-for-340b-drugs/) • [Holland & Knight — Sweeping CY 2027 OPPS/ASC Final Rule](https://www.hklaw.com/en/insights/publications/2026/11/cms-issues-sweeping-cy-2027-hospital-opps-asc-final-rule)

---

## Section 02 — Prior Authorization / Payer Relations

### 42 Days to FHIR PA API Mandate — One Year of Payer PA Commitments: Cigna Standardizes 70%, Aetna Leads at 88%, but Only 36% of Providers Believe Payers Reliably Deliver

The CMS-0057-F FHIR Prior Authorization API mandate is now 42 days from enforcement. This week also marks the one-year progress point for the AHIP and BCBSA industry-wide PA commitment. Cigna has standardized approximately 70% of its prior authorization volume; Aetna reports 88% and leads all major payers; Humana has eliminated one-third of outpatient prior authorizations; UHC removed requirements for 231 procedures in December 2025 and committed to cutting 30% more by year-end 2026. But an Aetna-run provider survey found that only 36% of providers believe payers reliably follow through on their commitments — a credibility gap that underscores why the federal mandate matters.

**Stat cards:**
- **42 days** — Until CMS-0057-F FHIR PA API mandate takes effect (January 1, 2027)
- **88%** — Aetna's share of PA volume standardized electronically (highest of major payers)
- **36%** — Providers who believe payers reliably deliver on PA reform commitments (Aetna provider survey)
- **95%** — Humana's target: deciding 95% of complete electronic PA requests within one business day

### One Year of PA Commitments: Progress and Gaps

The 2025 AHIP-BCBSA voluntary commitment created a framework for payers to standardize electronic PA submissions and process at least 80% of electronic approvals in real time by 2027. The major-payer self-reported progress one year in:

- **Aetna:** 88% of PA volume standardized; first large payer to integrate medical and pharmacy decisions into single condition-specific reviews.
- **Cigna:** Standardized more than 70% of PA volume; reduced total medical PA volume by approximately 15%.
- **Humana:** Eliminated about one-third of outpatient prior authorizations, including colonoscopies and certain imaging; committed to 95% one-business-day decision rate on complete electronic requests.
- **UHC:** Dropped 231 procedures from PA requirements in December 2025; committed to eliminating 30% more by end of 2026; December 1 expansion removes PA for select under-18 services.

The critical qualifier: these figures are self-reported. The 36% provider trust figure suggests the operational experience on the ground differs substantially from the announced commitments. The FHIR PA API mandate is a structural enforcement mechanism that makes real-time PA data availability verifiable — which is precisely why the January 1 deadline matters beyond compliance.

### RPM/RTM: New Patient Requirements Effective January 1

Buried in the CY 2027 PFS final rule but equally important for PA-adjacent workflows: Remote Therapeutic Monitoring (RTM) is now limited to established patients starting January 1, 2027. This matches the existing established-patient requirement for RPM. Additionally, billing for a new RPM or RTM patient requires a face-to-face initiating visit (in-person or telehealth) that includes a discussion of remote monitoring before billing can begin. Patients already enrolled before January 1 are grandfathered in.

> **Action Required:** Contact your EHR vendor this week and confirm: (1) Is FHIR PA API integration active for your top 5 payers? (2) Have you verified your 278 prior authorization transactions are routing through FHIR endpoints rather than legacy EDI? (3) Are RTM patient panels documented as established patients with initiating visits on file? All three take weeks to fix — 42 days is not a comfortable runway.

**Sources:** [Becker's Payer Issues — PA Commitments One Year In](https://www.beckerspayer.com/policy-updates/insurers-prior-authorization-commitments-1-year-in/) • [Fierce Healthcare — Payer PA Standardization Progress](https://www.fiercehealthcare.com/payers/unitedhealthcare-aetna-tout-progress-standardize-prior-authorization-part-industry-wide) • [DistilINFO — Prior Authorization Reform 2026](https://distilinfo.com/2026/05/07/prior-authorization-reform-key-updates-for-2026/) • [Nixon Peabody — CMS Finalizes 2027 RPM/RTM Changes](https://www.nixonpeabody.com/insights/alerts/2026/11/09/cms-finalizes-2027-medicare-rpm-rtm-changes-direct-employee-rule-delayed-to-2029) • [Health Recovery Solutions — 2027 RPM RTM Final Rule](https://www.healthrecoverysolutions.com/blog/2027-rpm-rtm-final-rule-hrs) • [CMS — Electronic Prior Authorization Overview](https://www.cms.gov/priorities/electronic-prior-authorization/overview)

---

## Section 03 — AI & Automation Deep Dive

### Agentic AI in RCM: What's Actually Running in Production — AGS Health Deploys Denial Agent, QWay Analysis Separates Signal From Noise, and William Blair Calls AI Adoption a Market Inflection

The revenue cycle AI market in late 2026 has an increasingly clear fault line: a small set of vendors deploying narrowly scoped, production-grade agentic AI on specific RCM tasks versus a much larger set marketing fully autonomous "agentic RCM" that is not yet running at scale. AGS Health deployed agentic workflow solutions in mid-October 2026 targeting denial management. A QWay Healthcare independent analysis finds that agentic AI is delivering solid, production-grade results in prior authorization, mid-cycle coding, and denial analytics — but that fully autonomous, end-to-end RCM with no human in the loop is "still mostly marketing." William Blair's new research report identifies AI RCM adoption as a market inflection point.

**Stat cards:**
- **15%** — Share of providers with fully integrated AI across standard RCM operations (Experian Health, 2026)
- **48%** — Revenue cycle leaks attributed to denials and appeals (MGMA Stat poll, Jan 2026)
- **Mid-Oct 2026** — When AGS Health deployed agentic workflow solutions for denial management
- **3–6 months** — Typical full RCM automation deployment timeline for a multi-specialty practice

### What Agentic AI Is Actually Doing in RCM Today

The honest picture from independent sources:

**Working at scale in production:**
- Pre-submission denial prevention: AI agents checking claims before submission against payer-specific edits, flagging denial risk before the claim is filed
- Prior authorization intake: agents validating coverage requirements and documentation against payer rules at point of order
- Mid-cycle coding: AI-assisted coding review with human exception handling for complex encounters
- Denial analytics: root-cause analysis and denial pattern identification across payer populations

**Still emerging:**
- Fully autonomous appeals generation without human review
- End-to-end agentic billing with no human in any workflow step
- Cross-payer policy intelligence that adapts in real time to LCD changes

The strategic shift is from post-denial recovery (wait for the denial, work the appeal) to pre-submission prevention (catch the denial risk before the claim is submitted). Innovaccer's analysis frames this as the central value of autonomous agents: intervention shifts from 90-day recovery queues to real-time prevention. AGS Health's mid-October deployment targets this exact model.

### William Blair on AI Adoption as Market Inflection

A William Blair research report on AI in the revenue cycle management marketplace identifies the current period as a market inflection — the point at which AI RCM transitions from early-adopter experiment to mainstream deployment expectation. The report's framing aligns with Waystar's Q3 subscription revenue surge (reported last week) and the accelerating pace of RCM AI M&A. For practices in vendor evaluation mode, this means the window for first-mover advantage on AI RCM is narrowing: practices that move now build workflow competency before payer complexity increases further in 2027.

> **Bottom Line:** The 15% AI integration rate across standard RCM operations is the most important benchmark to internalize. It means 85% of practices are still running legacy workflows on tasks where AI-assisted alternatives are commercially available. For denial prevention, eligibility verification, and prior authorization, the technology gap is not theoretical — it is producing measurable Days in AR differences between practices that have adopted and those that haven't.

**Sources:** [QWay Healthcare — Agentic AI in Revenue Cycle: What's Real in 2026](https://qwayhealthcare.ai/insights/agentic-ai-healthcare-revenue-cycle-whats-actually-real-in-2026/) • [Healthcare IT Today — Agentic AI and RCM Future](https://www.healthcareittoday.com/2026/04/02/how-agentic-ai-is-reshaping-the-future-of-revenue-cycle-management-and-the-work-behind-it/) • [William Blair — Growing Importance of AI in RCM](https://www.williamblair.com/-/media/downloads/eqr/2026/williamblair_the-growing-importance-of-ai-in-the-revenue-cycle-management.pdf) • [Innovaccer — Denial Management Solutions 2026](https://innovaccer.ai/blogs/denial-management-solutions-for-revenue-cycle-teams-2026) • [Experian Health — State of Claims 2026](https://www.experian.com/blogs/healthcare/state-of-claims-2026-why-denials-remain-an-uphill-climb/) • [Onixnet — Agentic AI in RCM 2026 Paradigm Shift](https://www.onixnet.com/blog/the-2026-paradigm-shift-agentic-ai-in-healthcare-revenue-cycle-management/)

---

## Section 04 — Coding Updates

### CPT 2027 Final Countdown: AAPC Webinar in 5 Days, CDM Audit Window Closing, and Q3 2026 HCPCS Drug Decisions Posted

The CPT 2027 preparation window is closing. AAPC's CPT 2027 Coding Updates webinar is scheduled for November 25 — five days from today. This is the most important CPT 2027 planning resource available, and registration should be complete now. CMS has posted its final determinations for the Third Quarter 2026 HCPCS Level II drug and biological coding applications, adding new drug codes that take effect January 1. And the 340B billing modifier transition (JG/TB/XX) adds a parallel CDM update requirement that must be completed before December 31.

**Stat cards:**
- **Nov 25** — AAPC CPT 2027 Coding Updates webinar (5 days away)
- **Jan 1, 2027** — Effective date for CPT 2027 code set, 340B modifiers, E/M complexity modifier, and RPM/RTM rule changes
- **Q3 2026** — CMS posted final HCPCS Level II drug coding decisions for quarterly cycle
- **418** — Total CPT code changes in CPT 2026 (288 new, 46 revised, 84 deleted) — expect similar scale for 2027

### CDM Audit: Four Action Areas Before January 1

For billing teams running CPT 2027 preparation in parallel with 340B modifier compliance, the four CDM audit priorities for the remaining six weeks of 2026 are:

1. **CPT deletions and replacements:** Identify any CPT 2026 codes in your CDM scheduled for deletion in CPT 2027. Claims submitted after January 1 with deleted codes will reject at the clearinghouse level. AAPC's November 25 webinar will provide the definitive deletions list.
2. **340B modifier assignment:** Map all outpatient drug NDCs in your CDM to their 340B status (JG-eligible, TB-eligible, or XX). This requires coordination between pharmacy, billing, and IT — start now.
3. **E/M complexity modifier documentation:** The new CMS E/M complexity modifier takes effect January 1. Update your charge entry rules to flag eligible encounters and ensure documentation templates support the longitudinal care requirement.
4. **Q3 2026 HCPCS drug code additions:** Verify that any new drug codes from the Q3 2026 CMS determination are in your CDM if applicable to your specialty. Oncology, rheumatology, and infusion centers are most likely affected.

### JW/JZ Modifier Compliance: Year-End Drug Wastage Audit

CMS's JW/JZ modifier policy for discarded single-dose drugs and biologicals is frequently underaudited. The JW modifier reports discarded amounts from a single-use vial that are billed for reimbursement; JZ confirms no drug was discarded. With the transition to JG/TB/XX for 340B drugs, billing teams should conduct a year-end audit to ensure JW/JZ compliance is not disrupted by the modifier transition workflow.

> **Action Required:** Register for the AAPC November 25 CPT 2027 webinar today if not already done. Run a CDM audit this week that covers all four action areas above. For practices with 340B programs, assign a specific team member to own the JG/TB/XX modifier mapping — this cannot be a last-week-of-December project.

**Sources:** [AAPC — CPT 2027 Coding Updates Webinar](https://www.aapc.com/codes/coding-newsletters/articles) • [CMS — Q3 2026 HCPCS Drug and Biological Coding Decisions](https://www.cms.gov/files/document/2026-hcpcs-application-summary-quarter-3-2026-drugs-biologicals.pdf) • [CMS — JW and JZ Modifier Policy](https://www.cms.gov/files/document/jw-modifier-and-jz-modifier-policy-hcpcs-codes.pdf) • [Advis — 340B Billing Modifiers](https://advis.com/340b/cy-2027-opps-340b-payment-cuts/) • [AMA — CPT Code Information](https://www.ama-assn.org/amaone/cpt-current-procedural-terminology) • [CMS — ICD-10 Coordination and Maintenance](https://www.cms.gov/medicare/coding-billing/icd-10-codes)

---

## Section 05 — Revenue Velocity / KPIs

### Kodiak H1 2026 Data: Initial Denials Down to 10.63% but Final Commercial Denials Up 9.1% — MGMA Reports 48% of Revenue Cycle Leaks Come From Denials

New Kodiak Solutions data covering 375,000 physicians in H1 2026 reveals a bifurcated denial market: initial claim denial rates fell to 10.63% (down from 12.00% in H1 2025), suggesting payer-side investments in eligibility verification and electronic claims processing are having some effect. But final commercial denial rates increased 9.1% year over year — a signal that payers are denying less initially but increasing post-payment recovery activity. The TriZetto analysis of 630 million claims found an average denial rate of 14.6%, nearly three times the 5% industry benchmark. MGMA's January 2026 Stat poll found that 48% of revenue cycle revenue leaks come from denials and appeals.

**Stat cards:**
- **10.63%** — H1 2026 initial claim denial rate (down from 12.00% in H1 2025, Kodiak / 375,000 physicians)
- **9.1%** — Increase in final commercial denial rate H1 2026 vs. H1 2025 (Kodiak)
- **14.6%** — Average denial rate across 630 million claims (TriZetto — nearly 3× the 5% benchmark)
- **48%** — Revenue cycle leaks from denials and appeals (MGMA Stat poll, January 2026)

### The Bifurcated Denial Market: What It Means

The divergence between lower initial denial rates and higher final denial rates describes a specific payer strategy: pay first, claw back later. Post-payment recovery activity — medical necessity reviews, coordination of benefits audits, and clinical documentation requests initiated after payment — is becoming a larger share of payer-to-provider financial friction. This is harder for practices to track than upfront denials because it doesn't appear in the same AR metrics.

For year-end revenue velocity, the practical implications are:

- **Track post-payment recoveries separately.** If your practice cannot distinguish post-payment claw-backs from initial denials in your reporting, you're likely underestimating the true cost of payer disputes.
- **Build a Q4 priority queue.** With six weeks left in 2026, work all claims 60+ days outstanding by payer bucket. Claims with commercial payers where the final denial rate is rising deserve priority attention — these are increasingly likely to result in final non-payment if unworked before year-end.
- **Patient deductible opportunity.** Patients who have met their 2026 out-of-pocket maximums represent your highest-probability Q4 collection opportunity. Run a list from your PM system this week.

### KPI Benchmarks: The Six-Week Sprint Targets

| Metric | H1 2026 Actual (Kodiak) | Industry Target | Best-in-Class |
|--------|------------------------|-----------------|---------------|
| Initial denial rate | 10.63% | <5% | <3% |
| Final denial rate (commercial) | Rising 9.1% YoY | <3% | <2% |
| Clean claim rate | ~88% (industry avg) | ≥95% | ≥98% |
| Days in AR | 35–50 days | <38 days | <30 days |
| Net collection rate | 90–94% | ≥96% | ≥98% |

> **Action Required:** Pull your November 1 AR aging report and sort by payer. Identify all commercial payer claims 60+ days outstanding. Create a priority work queue: (1) all claims >$500 that are 60–90 days, (2) all claims with known high-volume commercial payers that have increased post-payment recovery activity. Set a goal to clear 25% of this queue before the Thanksgiving holiday slowdown.

**Sources:** [Kodiak Solutions — H1 2026 Denial Data](https://www.kodiaksolutions.com/) • [TriZetto — A Clean Claim Isn't a Fully Paid Claim](https://www.trizettoprovider.com/resource-library/a-clean-claim-isnt-a-fully-paid-claim) • [MGMA — Your Best Biller Can't Fix Your Denial Rate Alone](https://www.mgma.com/sponsored-solutions/your-best-biller-cant-fix-your-denial-rate-alone) • [Experian Health — State of Claims 2026](https://www.experian.com/content/dam/noindex/na/us/healthcare/state-of-claims-2026.pdf) • [Fierce Healthcare — Insurers Deny Less But Claw Back More](https://www.fiercehealthcare.com/finance/despite-better-cash-flow-providers-missed-out-more-revenue-2025-due-increased-payer-denials) • [Physicians Practice — Denial Rates Are Rising](https://www.physicianspractice.com/view/denial-rates-are-rising-here-s-how-to-fight-back)

---

## Section 06 — Technology Spotlight

### Technology Spotlight: VisiQuate Acquires Artiva HCx — KLAS #1 Analytics Platform Adds Execution Layer; Children's Mercy Outsources 473 RCM Roles in Accelerating Health System Trend

The revenue cycle technology market this week is defined by consolidation between analytics intelligence and workflow execution. VisiQuate — KLAS #1 in RCM analytics with a 92/100 performance score — acquired Artiva HCx from Finvi (closing October 20, announced November 4), adding an insurance follow-up, denial management, and collections workflow platform to its intelligence foundation. Children's Mercy announced the outsourcing of 473 revenue cycle roles in the latest signal that health systems are industrializing RCM operations rather than staffing them internally.

**Stat cards:**
- **92/100** — VisiQuate KLAS performance score for RCM analytics (Black Book #1 2026)
- **473** — Revenue cycle roles outsourced by Children's Mercy (November 2026)
- **142** — RCM and HCIT transactions closed in H1 2026 (RevCycleAI deal tracker)
- **Oct 20** — VisiQuate / Artiva HCx deal close date (announced November 4)

### VisiQuate + Artiva HCx: Analytics Meets Execution

The strategic rationale is explicit in VisiQuate's announcement: connect analytics with execution. The combined platform pairs VisiQuate's data ontology and revenue intelligence with Artiva HCx's workflow routing for insurance follow-up, denial management, and collections — covering the full cycle from insight generation to work execution. VisiQuate earned KLAS's #1 position in both RCM analytics and CFO command center categories in Black Book's 2026 rankings, bringing an external validation score of 92/100.

For practices and health systems that use separate analytics and workflow tools, this acquisition represents a market signal: the category boundary between RCM intelligence and RCM execution is dissolving. Single-platform buyers will increasingly be choosing combined analytics-execution solutions rather than best-of-breed point tools.

Finvi — the seller — is a New Mountain Capital portfolio company with a 50-year legacy in accounts receivable management. The divestiture of Artiva HCx allows Finvi to focus on its core third-party collections market while VisiQuate deepens its healthcare RCM footprint.

### Health System RCM Outsourcing: Children's Mercy and the Trend

Children's Mercy's outsourcing of 473 revenue cycle roles continues a pattern visible across health systems in 2026. The same week, Grady Health System and Ensemble Health Partners announced a new RCM partnership — Ensemble managing revenue cycle operations for a major safety-net system. RevCycleAI's deal tracker shows 142 RCM and HCIT transactions in H1 2026, pace for the highest annual volume since 2022. For independent practices evaluating their own build-vs.-buy-vs.-outsource decisions, the health system outsourcing trend provides a useful reference: even organizations with 400+ dedicated RCM staff are concluding that outsourced specialist platforms outperform in-house operations on key metrics.

> **Key Insight:** Mark Cuban's warning on RCM AI, surfaced in Becker's this week, reflects the right skepticism: not all AI RCM claims are real, vendor performance metrics are self-reported, and a 92-point KLAS score is more reliable than a startup's pitch deck. For practices evaluating vendors, independent KLAS validation is the most reliable third-party benchmark available. If a vendor cannot point to a KLAS score or Black Book ranking, ask why.

**Sources:** [Healthcare IT Today — VisiQuate Acquires Artiva HCx](https://www.healthcareittoday.com/2026/11/12/visiquate-acquires-artiva-hcx-leantaas-brings-ambient-intelligence-to-iqueue/) • [CityBiz — VisiQuate Adds Artiva HCx Workflow Technology](https://www.citybiz.co/article/929181/visiquate-adds-artiva-hcx-workflow-technology-to-its-revenue-cycle-intelligence-platform/) • [CityBiz — Finvi Sells Artiva HCx Business to VisiQuate](https://www.citybiz.co/?p=929337) • [Becker's Hospital Review — Revenue Cycle Archives](https://www.beckershospitalreview.com/newsletter-category/becker-s-revenue-cycle-e-weekly/) • [RevCycleAI — Deals and Raises 2026](https://revcycleai.com/deals-and-raises/) • [HL Houlihan Lokey — Advises Finvi](https://hl.com/about-us/transactions/finvi-visiquate-nmc-akkr/)

---

## Section 07 — Compliance Corner

### Compliance Corner: CRUSH Comment Deadline January 19, 340B Billing Modifiers Due January 1, RPM/RTM Initiating Visit Rule Takes Effect, and Three December 31 Deadlines

Four compliance timelines require immediate attention: the CRUSH proposed rule (CMS-6098-P) comment window closing January 19, 2027; the 340B billing modifier transition (JG/TB/XX) with a hard January 1 implementation deadline; the RPM/RTM established-patient and initiating-visit requirements effective January 1, 2027; and three December 31 deadlines that arrive in 41 days.

**Stat cards:**
- **Jan 19, 2027** — Comment deadline for CRUSH proposed rule (CMS-6098-P)
- **Jan 1, 2027** — 340B billing modifiers JG/TB/XX, RPM/RTM new patient rules, CPT 2027 all take effect
- **2029** — When CMS direct employee staffing rule for RPM takes effect (delayed; third-party contracting OK through Dec 31, 2028)
- **Dec 31** — Three simultaneous deadlines: Medicare participation, MIPS virtual group election, year-end RPM patient panel review

### CRUSH Rule: What to Read and What to Comment On

The comment period for CRUSH runs through January 19, 2027. The provisions with the broadest practical impact on physician practices:

- **30-day enrollment reporting:** If finalized, this would require practices to notify CMS of any ownership change, practice location change, group practice affiliation change, or other enrollment modification within 30 days. Many practices currently operate on the 90-day window and have informal processes that wouldn't meet a 30-day standard. Practices with high turnover, multi-site operations, or frequent physician group changes should comment specifically on operational feasibility.
- **MA cross-enrollment:** Independent practices that bill exclusively through Medicare Advantage contracts may not be enrolled in Original Medicare. This provision, if finalized, would require that enrollment. Comments should address the administrative burden and timeline feasibility for practices in this situation.

### 340B Billing Modifiers: A Hard Deadline

The JG/TB/XX modifier transition is unusual in healthcare compliance because it has no grace period. Claims submitted after January 1 with 340B drugs and no modifier — or with the wrong modifier — will be processed incorrectly. For hospital outpatient billing teams, this is a TPA/split-billing workflow change. For independent practices using 340B pricing through a contract pharmacy or infusion center arrangement, verify with your pharmacy team that the modifier mapping is correct before the first January claim.

### RPM/RTM New Requirements: Established Patient and Initiating Visit

Effective January 1, 2027:
- RTM is limited to established patients (matching RPM's existing requirement). A patient is established if the billing practitioner, or a practitioner in the same group practice, has provided professional services within the past three years.
- New RPM or RTM patients require a face-to-face initiating visit (in-person or telehealth) that includes a discussion of remote monitoring before billing can begin.
- Patients already enrolled in RPM or RTM before January 1, 2027, are grandfathered — no initiating visit required retroactively.
- The direct employee staffing rule was finalized but delayed to January 1, 2029. Third-party contracted RPM/RTM vendors remain compliant through December 31, 2028.

> **Action Required:** Complete all four compliance actions before December 31: (1) configure JG/TB/XX modifiers in billing systems; (2) file Medicare participation decision for CY 2027; (3) submit MIPS virtual group election at qpp.cms.gov if applicable; (4) audit RPM/RTM patient panel for established-patient status and initiating visit documentation.

**Sources:** [CMS — CRUSH Proposed Rule (CMS-6098-P)](https://www.cms.gov/newsroom/press-releases/cms-crush-proposed-rule-aims-reap-nearly-90-billion-taxpayers-savings-targeting-fraud-across) • [Nixon Peabody — CMS Finalizes RPM/RTM Changes](https://www.nixonpeabody.com/insights/alerts/2026/11/09/cms-finalizes-2027-medicare-rpm-rtm-changes-direct-employee-rule-delayed-to-2029) • [Medical Billers and Coders — CY 2027 RPM RTM Billing Changes](https://www.medicalbillersandcoders.com/blog/cy-2027-rpm-rtm-billing-changes/) • [Advis — 340B Modifier Guidance](https://advis.com/340b/cy-2027-opps-340b-payment-cuts/) • [CMS — QPP Portal](https://qpp.cms.gov) • [Lathrop GPM — CRUSH Proposed Rule Analysis](https://www.lathropgpm.com/insights/someones-got-a-crush-on-you-cms-proposed-rule-would-make-substantial-changes-to-fraud-and-abuse-enforcement/)

---

## Section 08 — Independent Practice Watch

### Physician Practice Bankruptcies Surge to 30% of H1 2026 Healthcare Filings — Congressional Pay Reform Advances as Only Structural Relief

Clinics and physician groups accounted for nearly 30% of healthcare bankruptcy filings in the first half of 2026 and are on pace for the highest annual total since 2019 (Medical Economics). The Veradigm 2026 survey found that 94% of independent practices have been approached about acquisition or consolidation in the past two years — a figure that reveals the structural financial pressure creating those conversations. CMS projects 2.7% practice cost growth in 2026 while the CY 2027 physician fee schedule cut removes $23,600 per $1 million in annual Medicare revenue. The only near-term structural relief in view is congressional: an AMA-led coalition of 62 organizations is pushing to include physician payment reform in any year-end legislative package.

**Stat cards:**
- **~30%** — Share of H1 2026 healthcare bankruptcies from clinics and physician groups (Medical Economics)
- **94%** — Independent practices approached about acquisition or consolidation in past 2 years (Veradigm 2026)
- **2.7%** — CMS projected physician practice cost growth in 2026 (while revenue faces cuts)
- **62** — Organizations in the AMA-led coalition urging Congress to pass physician payment reform

### Congressional Pay Reform: What's on the Table

The year-end legislative package is the likeliest vehicle for any 2026 physician payment action. The AMA-led coalition of 62 organizations is advocating for two specific actions:

- **1-year extension of the 2.5% temporary payment boost:** The 2026 temporary increase expires December 31. Without a congressional extension, the 2027 conversion factor drops to $32.6286 for non-APM participants (a 2.36% cut). An extension would hold the effective rate at $33.4009.
- **Provider Reimbursement Stability Act (H.R. 8163):** This would give CMS more flexibility to adjust physician payment while capping year-to-year rate volatility. It's a structural change rather than a one-year patch. The Data-Driven Performance Payment System Act would replace MIPS with a more stable framework — estimated at $12,800 per physician annually in MIPS administrative cost savings.

The CRUSH proposed rule adds a new cost dimension for independent practices: if MA cross-enrollment is finalized, practices billing primarily through MA contracts will face a new administrative enrollment requirement. This provision merits a comment, specifically on implementation timeline and operational burden.

### Where You Should Be: Independent Practice Q4 Benchmarks

| KPI | H1 2026 Actual | Independent Practice Target | Action if Below Target |
|-----|---------------|----------------------------|----------------------|
| Initial denial rate | 10.63% (national avg) | <7% | Audit top 5 denial codes; fix root causes |
| Net collection rate | 90–94% | ≥96% | Identify payer buckets with lowest net collection |
| Days in AR | 35–50 (avg) | <38 days | Work 60+ day claims before year-end |
| Revenue visibility | 24% complete (Veradigm) | ≥80% | Build 4 tracking reports: charge lag, claim response, denial root cause, write-off rate |
| Practice cost growth | 2.7% CMS projection | Offset with revenue automation | Identify one manual process to automate before Q1 2027 |

> **Where You Should Be:** If your practice is in the 94% that have been approached about acquisition, the financial metrics that determine your leverage in that conversation — net collection rate, Days in AR, clean claim rate — are also the metrics that determine whether you stay independent. A practice generating $2M annually with a 96% net collection rate and 35 Days in AR is a fundamentally different acquisition conversation than one at 90% and 48 days. The difference is roughly $120,000 in annual recovered revenue. That gap is achievable in one year with focused RCM improvement.

**Sources:** [Medical Economics — Why Physician Group Bankruptcies Are Rising](https://www.medicaleconomics.com/view/why-are-claims-being-denied-in-2026-services-not-covered-now-tops-the-list) • [Veradigm — State of the Independent Practice in 2026](https://veradigm.com/img/resource-veradigm-state-of-independent-practice-2026-wp.pdf) • [AMA — National Advocacy Update November 13, 2026](https://www.ama-assn.org/health-care-advocacy/advocacy-update/nov-13-2026-national-advocacy-update) • [Healthcare Dive — Doc Pay, Price Transparency on Congress Healthcare Agenda](https://www.healthcaredive.com/news/doctor-pay-price-transparency-congress-healthcare-agenda-bills-legislation/825457/) • [STAT News — Patients First Act](https://www.statnews.com/2026/09/24/patients-first-act-congress-moves-on-doctor-pay-medicare-reform/) • [Colliers — Healthcare Services Q3 2026](https://www.colliers.com/en/research/nrep-ushc-us-healthcare-services-research-report-q3-2026)

---

## Section 09 — Specialty RCM Spotlight

### Specialty RCM Spotlight: 340B Oncology Impact, Cardiology Congressional Pay Push, Primary Care RPM/RTM Initiating Visit, Orthopedics Year-End ASC Velocity

| Specialty | Key Development | Action |
|-----------|----------------|--------|
| **Primary Care** | RTM now limited to established patients effective Jan 1; new RTM patients require face-to-face initiating visit; E/M complexity modifier documentation should cover 65–75% of established patient panel | Audit RTM patient panels for established-patient status; document initiating visits for any new RPM/RTM enrollments; build E/M modifier documentation templates for qualifying chronic-condition encounters |
| **Cardiology** | 340B drug billing transition: JG modifier for infusion drugs subject to reduction effective Jan 1; Congressional E/M modifier reform could add 45–60% boost to longitudinal CHF/arrhythmia management encounters if passed | Update 340B infusion billing workflows for JG/TB/XX by Dec 31; model E/M modifier revenue impact for high-volume longitudinal cardiology patients; submit comments to AMA coalition |
| **Orthopedics** | Year-end ASC case velocity: patients who've met 2026 out-of-pocket maximums are ideal Q4 surgical candidates before deductibles reset Jan 1; expanded ASC-eligible procedures from CY 2027 OPPS | Contact high-deductible patients who've met OOP max for elective joint/spine cases; verify updated ASC-eligible procedure list from OPPS final rule is in CDM |
| **Oncology** | 340B impact is largest in oncology: $4.65B total OPPS drug payment reduction; JG modifier implementation required for affected drugs; drug price negotiation framework may further shift Part B drug economics in 2027 | Complete 340B billing system update for JG/TB/XX modifiers by Dec 31; review Part B drug acquisition cost strategy against ASP minus 28% economics; assess impact of drug negotiation framework on infusion drug revenue |
| **Radiology** | AI imaging CPT codes payer LCDs still developing; Q3 2026 HCPCS updates include imaging-related drug and contrast codes; year-end is final chance to audit AI imaging code billings and ensure LCD coverage exists | Verify payer LCD status before billing Category I AI imaging codes for 2026; review Q3 drug coding decisions for radiopharmaceuticals; conduct Q4 audit of modifier 26/TC splits |
| **Mental Health** | RTM new established-patient and initiating-visit rules affect behavioral health remote monitoring; direct employee rule delayed to 2029 preserves third-party contracting flexibility; CoCM codes G0568–G0570 billing established | Audit behavioral health RTM patient panels for established-patient status; document initiating visits for new remote monitoring patients; confirm CoCM billing workflows are live |
| **Neurology** | RPM for chronic neurological conditions (MS, epilepsy, Parkinson's) now requires established-patient relationship and face-to-face initiating visit effective Jan 1; EEG coding updates from 2026 set | Build initiating visit documentation templates for RPM patient onboarding; confirm established-patient status for all current remote monitoring patients; verify EEG billing codes against 2026 CPT set |
| **Gastroenterology** | Q4 2026 is last reporting period for colonoscopy follow-up interval quality measure in ASQRP (removed starting 2027); year-end deductible opportunity for colonoscopy scheduling | File final Q4 colonoscopy follow-up interval measure data; accelerate scheduling for patients who've met 2026 deductibles; retire quality reporting workflow after Dec 31 |

**Sources:** [Medical Billers and Coders — CY 2027 RPM RTM Billing Changes](https://www.medicalbillersandcoders.com/blog/cy-2027-rpm-rtm-billing-changes/) • [Advis — 340B OPPS Payment Cuts](https://advis.com/340b/cy-2027-opps-340b-payment-cuts/) • [ACC — CMS Final 2027 PFS and OPPS Rules](https://www.acc.org/Latest-in-Cardiology/Articles/2026/11/05/14/15/CMS-Releases-Final-2027-Medicare-Physician-Fee-Schedule-and-Hospital-OPPS-Rules) • [AnnexMed — Radiology CPT Updates 2026](https://annexmed.com/radiology-cpt-code-updates-2026) • [MedSoler RCM — Mental Health CPT Codes 2026](https://medsolercm.com/blog/mental-health-cpt-codes) • [Becker's ASC — OPPS 2027 Final Rule](https://www.beckersasc.com/asc-news/what-cms-final-opps-2027-rule-means-for-asc-leaders-more-cases-less-pay/) • [Sprypt — Clean Claim Rate vs. Denial Rate by Specialty](https://www.sprypt.com/blog/clean-claim-rate-vs-denial-rate-by-specialty)

---

## Section 10 — This Week's Action Items

### This Week's Action Items — 8 Steps Before November 27

1. **Configure 340B billing modifiers by December 31.** Assign a team owner for the JG/TB/XX modifier mapping in your billing system today. This is a hard January 1 deadline with no grace period. Claims with 340B drugs submitted after January 1 without the correct modifier will be paid at the wrong rate.

2. **Read and assess CRUSH proposed rule (CMS-6098-P).** Review the CMS press release and law firm analyses. Assess: (a) Do you bill Medicare Advantage without Original Medicare enrollment? (b) Can your practice meet 30-day enrollment change reporting? Submit comments through regulations.gov before January 19, 2027.

3. **Register for AAPC CPT 2027 webinar — 5 days.** The November 25 AAPC webinar is the essential CPT 2027 preparation resource. Begin CDM audit this week for codes expected to change in January.

4. **Audit RPM/RTM patient panel before January 1.** Identify all patients currently in remote monitoring programs. For each: (a) confirm established-patient status (professional services within 3 years), (b) document initiating visit on file. New patients after January 1 need a face-to-face initiating visit before billing starts.

5. **Year-end denial sprint.** Pull November AR by commercial payer, sort by denial age. Build a priority work queue: all claims over $500 at 60–90 days. Work the queue before Thanksgiving — holiday-week volume drops create a natural catch-up window.

6. **Patient deductible opportunity — this week.** Identify patients who have met their 2026 out-of-pocket maximums in your PM system. Contact them proactively about elective procedures and outstanding balances before deductibles reset January 1. This is your highest-probability Q4 collection and scheduling opportunity.

7. **Advocate for physician pay reform.** The AMA coalition's window for year-end legislative action closes before Christmas. Contact your specialty society or state medical association to add your voice to the congressional push. If the 2.5% temporary boost is not extended, model your January 1 revenue impact now.

8. **December 31 triple-check.** Set three calendar reminders for December 31: (a) CY 2027 Medicare participation decision submission, (b) MIPS virtual group election at qpp.cms.gov, (c) RPM/RTM patient panel review for established-patient documentation. All three have no extensions.

**Sources:** [CMS — CRUSH Proposed Rule](https://www.cms.gov/newsroom/press-releases/cms-crush-proposed-rule-aims-reap-nearly-90-billion-taxpayers-savings-targeting-fraud-across) • [AAPC — CPT 2027 Webinar](https://www.aapc.com/codes/coding-newsletters/articles) • [AMA — National Advocacy Update November 2026](https://www.ama-assn.org/health-care-advocacy/advocacy-update/nov-13-2026-national-advocacy-update) • [CMS — QPP Portal](https://qpp.cms.gov) • [Medical Billers and Coders — RPM RTM 2027 Changes](https://www.medicalbillersandcoders.com/blog/cy-2027-rpm-rtm-billing-changes/) • [Advis — 340B Modifier Guidance](https://advis.com/340b/cy-2027-opps-340b-payment-cuts/)

---

## Big Stat

**$90 Billion**

CMS's projected taxpayer savings from the CRUSH proposed rule (CMS-6098-P), released November 16, 2026 — representing the most aggressive fraud enforcement framework proposed in Medicare history. The rule would impose universal 30-day enrollment reporting, require MA-billing providers to enroll in Original Medicare, and give CMS direct authority to revoke enrollment based on fraud risk assessments. For the 94% of independent practices approached about consolidation, the CRUSH rule adds another compliance layer to the financial calculus of staying independent. Comment deadline: January 19, 2027.

*Source: CMS Press Release — CRUSH Proposed Rule (CMS-6098-P), November 16, 2026 • Veradigm State of the Independent Practice in 2026*

---

*Next issue: November 27, 2026*

*RCM Pulse Weekly aggregates publicly available information from government sources, professional associations, and industry publications. It does not constitute legal, compliance, or billing advice. Verify all regulatory and coding information against official CMS publications before implementation.*
