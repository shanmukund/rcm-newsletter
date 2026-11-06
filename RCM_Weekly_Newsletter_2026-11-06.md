# RCM Pulse Weekly
## Revenue Cycle Management Intelligence for Medical Practices

**November 6, 2026 • Volume 11, Issue 1**

---

## In This Issue

01. CY 2027 Physician Fee Schedule Final Rule Drops — 2.31% Conversion Factor Cut, E/M Complexity Add-On Replaced, and MIPS Traditional Track Confirmed to Sunset in 2031
02. 56 Days to FHIR PA API Mandate — Humana and athenahealth Expand ePA to 180,000 Clinicians, UHC Drops Pediatric Imaging Prior Auth, and Cigna E/M Downcoding Goes Live
03. Waystar Q3 2026: 21% Revenue Growth as AI Bookings Surge — Raintree Debuts Agentic RCM Tools Targeting 91% Touch-Time Reduction at TherapyCon '26
04. ICD-10 Public Comment Window Closes November 13 — CPT 2027 Preparation Season Begins as AAPC Sets Coding Update Webinar for November 25
05. CY 2027 E/M Modifier Upgrade: 16% Pay Boost for All Physicians, 32% for ACO Participants — Modeling the Revenue Impact Before January 1
06. CY 2027 OPPS/ASC Final Rule Released November 4 — 2.3% Hospital Outpatient Rate Increase, 2% ASC Payment Rise, Colonoscopy Quality Measure Removed
07. MIPS Traditional Track Sunsets 2031 — Not 2028 as Proposed — ACO Part B Cost Sharing Waiver and Virtual Group Election Window Closes December 31
08. Independent Practice Watch: AMA Data Shows 42.2% of Physicians in Private Practice — Down from 60.1% in 2012, with Physician Pay Off 33% Inflation-Adjusted Since 2001
09. Specialty RCM Spotlight: Primary Care E/M Gains, Cardiology MA Plan Disruption, ASC Orthopedics Wins New Cases, Oncology J-Code Audit Season
10. This Week's Action Items

---

## Section 01 — Regulatory / Payment Updates

### CY 2027 Physician Fee Schedule Final Rule Drops — 2.31% Conversion Factor Cut, E/M Complexity Add-On Replaced, and MIPS Traditional Track Confirmed to Sunset in 2031

CMS released the CY 2027 Physician Fee Schedule Final Rule (CMS-1848-F) on November 4, 2026, with an effective date of January 1, 2027. The rule delivers the most consequential structural changes to physician payment in several years — a deeper-than-proposed conversion factor cut, a sweeping overhaul of the E/M complexity payment mechanism, and a confirmed end date for traditional MIPS.

**Stat cards:**
- **$32.6286** — Non-APM conversion factor for CY 2027 (down from $33.4009, a 2.36% decrease)
- **$32.9548** — QPM/APM qualifying participant conversion factor (down 1.86% from 2026)
- **16%** — E/M base payment increase for all physicians under the new complexity modifier
- **32%** — E/M payment increase for ACO participants replacing G2211 add-on code
- **2031** — Year traditional MIPS reporting option ends (changed from proposed 2028)

### Conversion Factor: Deeper Than Proposed

The final non-APM conversion factor lands at $32.6286 — a 2.36% decrease from the 2026 factor of $33.4009. This is marginally deeper than the proposed reduction, with the gap explained by the budget-neutrality adjustment shifting from a small positive to –0.12% in the final rule. The cut is primarily driven by the expiration of the 2.5% temporary congressional payment increase enacted for 2026 under Public Law 119-21.

For APM qualifying participants, the factor is $32.9548, a 1.86% decrease. The difference between the two tracks represents a 1% advantage for practices participating in qualifying alternative payment models.

| Conversion Factor | CY 2027 | CY 2026 | Change |
|---|---|---|---|
| Non-APM participants | $32.6286 | $33.4009 | -2.36% |
| APM qualifying participants | $32.9548 | $33.5675 | -1.86% |
| Budget-neutrality adjustment | -0.12% | +0.08% | -0.20 pp |

### E/M Complexity Add-On Replaced by Modifier

The most significant structural change in the final rule is the elimination of HCPCS code G2211 and its replacement with a modifier that affects all office/outpatient E/M base codes. Under the new framework:

- **All physicians** receive a 16% increase to the base E/M payment when they append the new complexity modifier, reflecting a practice that serves as the continuing, longitudinal source of care for a patient's serious illness or complex chronic condition.
- **ACO participants** receive a 32% increase to the base E/M code when the modifier is applied, recognizing the longitudinal care coordination burden in accountable care models.

The practical effect: for a primary care practice that appropriately appends this modifier to 70% of its established-patient office visits, the net E/M revenue impact partially offsets the conversion factor reduction. Specialties that see patients primarily for discrete, non-longitudinal services will see less benefit.

### OPPS/ASC Final Rule: 2.3% Rate Increase for Outpatient Services

Also released November 4, the CY 2027 OPPS/ASC final rule (CMS-1850-F) gives hospital outpatient departments a 2.3% payment rate increase (down from the proposed 2.4%), reflecting a 3.2% market basket update minus a 0.9% productivity adjustment. CMS projects aggregate Medicare ASC payments will rise 2%. CMS also removed the colonoscopy follow-up interval measure from the ASC Quality Reporting Program starting with the 2027 reporting period.

> **Action Required:** Run your top 50 Medicare CPT codes by volume against $32.6286 today. A 2.36% cut on $4M in annual Medicare revenue equals $94,400 in lost annual reimbursement. Assess which E/M encounters qualify for the new complexity modifier — legitimate application could recover $60,000–$150,000 depending on your payer mix and visit volume.

**Sources:** [CMS — CY 2027 Physician Fee Schedule Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-final-rule) • [AHA — CMS Issues CY 2027 PFS Final Rule](https://www.aha.org/news/headline/2026-11-04-cms-issues-cy-2027-physician-fee-schedule-final-rule) • [ACC — CMS Releases Final 2027 Medicare PFS and Hospital OPPS Rules](https://www.acc.org/Latest-in-Cardiology/Articles/2026/11/05/14/15/CMS-Releases-Final-2027-Medicare-Physician-Fee-Schedule-and-Hospital-OPPS-Rules) • [Becker's ASC — What CMS' Final OPPS 2027 Rule Means for ASC Leaders](https://www.beckersasc.com/asc-news/what-cms-final-opps-2027-rule-means-for-asc-leaders-more-cases-less-pay/)

---

## Section 02 — Prior Authorization / Payer Relations

### 56 Days to FHIR PA API Mandate — Humana and athenahealth Expand ePA to 180,000 Clinicians, UHC Drops Pediatric Imaging Prior Auth, and Cigna E/M Downcoding Goes Live

Three payer developments converged this week that together represent the most significant operational shift in prior authorization and payer policy since the January 2026 operational rules took effect. The CMS-0057-F FHIR PA API mandate is now 56 days from enforcement. Humana and athenahealth expanded their FHIR-based electronic prior authorization collaboration to over 180,000 clinicians. UnitedHealthcare is following through on its May 2026 pledge to eliminate PA requirements for pediatric imaging. And Cigna's E/M code complexity review policy launched October 1, reshaping claims review for higher-acuity visits.

**Stat cards:**
- **56 days** — Until CMS-0057-F FHIR PA API mandate takes effect (January 1, 2027)
- **180,000+** — Clinicians in athenahealth's network now covered by expanded Humana ePA integration
- **~2/3** — Fraction of UHC pediatric prior authorization requirements being eliminated across pediatric imaging
- **97%+** — Cigna's estimate of providers NOT affected by its new E/M complexity review policy (Oct 1, 2026)

### FHIR PA API: 56 Days and Practice Readiness

CMS-0057-F requires Medicare Advantage organizations, Medicaid managed care plans, CHIP agencies, and exchange issuers to have Prior Authorization APIs built on FHIR standards operational by January 1, 2027. For practices, this creates the technical foundation for real-time PA status updates embedded in EHR workflows.

The question heading into the final weeks is payer readiness versus EHR readiness. The American Medical Association is on record urging CMS to maintain the January 1 deadline. Some payers, including Humana through its athenahealth expansion, are using the deadline as an accelerant for FHIR integration. Others are behind.

The Humana-athenahealth expansion is particularly notable for independent practices: athenahealth's client base skews toward small to mid-size physician practices, meaning the ePA coverage improvement is reaching practices that historically have relied on phone-based PA follow-up. The integration uses FHIR-based standards for coverage requirements discovery, documentation templates, and prior authorization support.

### UHC Pediatric Imaging PA Removal

UnitedHealthcare is following through on its commitment to eliminate roughly two-thirds of pediatric prior authorization requirements, including pediatric imaging. For pediatric practices and pediatric-specialist practices, this represents a meaningful reduction in authorization queue volume and turnaround time. Practices should confirm the specific CPT code list affected and update their authorization workflows to avoid unnecessary PA requests that waste staff time.

### Cigna E/M Downcoding Policy Goes Live

Cigna's new policy — which launched October 1, 2026, and allows the insurer to adjust higher-level E/M codes for visits that do not meet complexity standards — is now operational across all commercial and exchange plans except California HMO (paused for state regulatory review). Cigna estimates that over 97% of providers billing these codes will not be impacted, suggesting the policy is targeted at a small population of outlier billing patterns.

> **Key Insight:** The Cigna E/M downcoding policy coincides with the CMS E/M complexity modifier change effective January 1, 2027. Practices should ensure their documentation supports the highest E/M level billed *before* appending the new CMS complexity modifier — a well-documented E/M 99215 that also appropriately appends the modifier is doubly protected; a poorly documented 99215 that gets downcoded by Cigna and also fails to meet modifier criteria represents a double revenue loss.

**Sources:** [Healthcare Finance News — Humana and athenahealth Expand Electronic Prior Authorization](https://healthcarefinancenews.com/news/humana-and-athenahealth-expand-electronic-prior-authorization) • [Becker's Payer Issues — Payer Reimbursement Policies Making Headlines](https://www.beckerspayer.com/policy-updates/payer-reimbursement-policies-making-headlines-6-updates/) • [Aspirion — Q3 2026 Payer Policy Updates](https://www.aspirion.com/four-payer-shifts-now-in-effect-and-what-they-mean-for-your-next-appeal/) • [AMA — CMS Prior Authorization Deadline](https://www.ama-assn.org/practice-management/medicare-medicaid/what-expect-2026-medicare-physician-fee-schedule)

---

## Section 03 — AI & Automation Deep Dive

### Waystar Q3 2026: 21% Revenue Growth as AI Bookings Surge — Raintree Debuts Agentic RCM Tools Targeting 91% Touch-Time Reduction at TherapyCon '26

Two stories dominate the AI/automation RCM landscape this week. Waystar reported Q3 2026 revenue of $325.6 million — up 21% year over year — with management attributing growth to leveraging AI and agentic capabilities to reshape the revenue cycle. Year-to-date bookings grew 25%, reflecting accelerating demand for AI-powered RCM. Simultaneously, Raintree Systems debuted a suite of agentic RCM tools at TherapyCon '26, targeting an ambitious 91% reduction in touch time for eligibility verification and autonomous billing in rehab therapy settings.

**Stat cards:**
- **$325.6M** — Waystar Q3 2026 revenue, up 21% year over year (reported November 2, 2026)
- **+25%** — Waystar year-to-date bookings growth, driven by AI product adoption
- **91%** — Touch-time reduction target for Raintree's new AI eligibility specialist agent (Lucy) for rehab therapy
- **15%** — Share of providers with fully integrated AI across standard RCM operations (Experian Health, 2026)

### Waystar: Subscription Revenue Surges as AI Reshapes Pricing

Waystar's Q3 2026 results revealed an important structural shift: subscription revenue grew 34% year over year to $180.7 million, while volume-based revenue grew 8% to $142.9 million. This divergence is consistent with a shift toward outcome-based and subscription AI pricing models, where practices pay for AI workflow capabilities rather than per-transaction fees. Adjusted EBITDA margin held at 43%.

The company lowered its full-year revenue guidance to $1.277–$1.287 billion (from $1.274–$1.294 billion), citing slower conversion of bookings into recognized revenue from large client implementations. Shares fell 7.4% in after-hours trading despite the top-line beat, as investors focused on Q4 margin pressure. The Iodine Software acquisition (closed July 2025) contributed to the subscription revenue surge, adding autonomous clinical coding to Waystar's denial prevention platform.

| Waystar Q3 2026 | Q3 2026 | YoY Change |
|---|---|---|
| Total revenue | $325.6M | +21% |
| Subscription revenue | $180.7M | +34% |
| Volume-based revenue | $142.9M | +8% |
| Adj. EBITDA margin | 43% | Maintained |
| YTD bookings growth | +25% | — |

### Raintree and the Agentic RCM Moment

Raintree's TherapyCon '26 debut reflects a broader market shift: agentic AI is moving from claims scrubbing and denial routing into autonomous front-end and billing functions. Raintree's AI eligibility specialist "Lucy" targets a 91% reduction in touch time for eligibility verification — a task that currently consumes 15–25 minutes of staff time per patient in many rehab therapy settings. Its autonomous billing agent handles charge capture, claim prep, and resubmission without human review for clean-claim pathways.

The pattern emerging across vendors — Raintree, Cosentus (Zeus platform), and Waystar/Iodine — is a horizontal stack covering documentation, coding, eligibility, claims, and denials with minimal handoffs. The practice of tomorrow does not "do RCM" with a team of billers; it configures AI agents and reviews exceptions. The gap between that future and the 15% of practices that have fully integrated AI today is both the market opportunity and the operational challenge.

> **Bottom Line:** Waystar's 21% revenue growth in a revenue cycle market experiencing consolidation pressure is a signal that well-capitalized AI platforms are pulling ahead. For practices still evaluating AI RCM vendors, Waystar's growing subscription base and Iodine integration make it a tier-1 option for mid-size and larger practices. For smaller practices, Raintree and athenahealth's expanding ePA capabilities offer more accessible entry points.

**Sources:** [Waystar — Third Quarter 2026 Results](https://www.waystar.com/news/waystar-reports-third-quarter-2026-results/) • [GuruFocus — Waystar Q3 2026 Earnings Call Highlights](https://www.gurufocus.com/news/9164069/waystar-holding-corp-way-q3-2026-earnings-call-highlights-revenue-jumps-21-as-ai-bookings-surge) • [Experian Health — AI in Healthcare RCM 2026](https://www.experian.com/blogs/healthcare/rcm-and-ai/) • [RevCycleAI — RCM Intelligence](https://revcycleai.com/)

---

## Section 04 — Coding Updates

### ICD-10 Public Comment Window Closes November 13 — CPT 2027 Preparation Season Begins as AAPC Sets Coding Update Webinar for November 25

November is the transition month between the current code set and the next annual cycle. Two deadlines frame the coding work this week: CMS's public comment period for proposed FY 2027 ICD-10 code revisions closes November 13, 2026 — after which CMS will process feedback for October 1, 2027 implementation. And AAPC has announced its CPT 2027 Coding Updates webinar for November 25, hosted by AAPC President Raemarie Jimenez, marking the start of CPT 2027 preparation season for coding and billing teams.

**Stat cards:**
- **Nov 13** — CMS public comment deadline for proposed FY 2027 ICD-10 codes (October 1, 2027 implementation)
- **Nov 25** — AAPC CPT 2027 Coding Updates webinar (hosted by AAPC President Raemarie Jimenez)
- **418** — Total CPT changes in the current CPT 2026 code set (288 new, 46 revised, 84 deleted)
- **487** — New ICD-10-CM diagnosis codes added in the FY 2026/2027 update (now 5 weeks in effect)

### ICD-10 Public Comment: What's at Stake for October 2027

CMS's ICD-10 Coordination and Maintenance Committee process is well underway for the October 1, 2027 implementation cycle. The November 13 public comment deadline gives practices, specialty societies, and professional associations the last opportunity to submit input on proposed new codes, revisions, and deletions. Comments that identify gaps in clinical specificity — particularly for newly approved therapies, emerging diagnoses, or coding ambiguities that consistently generate CARC 97 (payer does not recognize claim) or CARC 50 (medical necessity) denials — have the highest impact.

Specialties with active lobbying around code specificity include oncology (genomic biomarker codes), neurology (neurostimulation and neuromodulation), and behavioral health (new DSM-related diagnostic categories). Billing managers who have encountered claim patterns suggesting ICD-10 specificity gaps should work with their specialty societies to submit comments before the November 13 cutoff.

### CPT 2027 Preparation: What to Expect

CPT 2027 code set preparation typically begins in November, with the AMA releasing the new code set for preview. Coding teams should begin:

1. **Tracking announced deletions and additions** through AAPC's webinar and specialty society alerts — particularly in high-volume service lines.
2. **Auditing charge description masters** for codes scheduled for deletion, to prevent claims with invalid codes from reaching January submissions.
3. **Updating encoder tools** — most PM/EHR vendors push CPT 2027 updates in December, but billing teams that use standalone encoder software must verify vendor timelines.
4. **Revisiting modifier workflows** — the CY 2027 PFS E/M complexity modifier is a CPT-adjacent change that takes effect January 1, requiring documentation standards and charge entry rule updates.

> **Key Insight:** The November 13 ICD-10 public comment deadline also matters for practices managing coding for emerging technologies. The 2026 CPT set introduced four AI-assisted imaging Category I codes — the first of their kind. If a practice's AI imaging tools generate encounter types that do not yet have adequate ICD-10 diagnosis code specificity to support medical necessity, now is the time to flag that gap to CMS through the public comment channel.

**Sources:** [CMS — ICD-10 Coordination and Maintenance Committee](https://www.cms.gov/medicare/coding-billing/icd-10-codes) • [AAPC — CPT 2027 Coding Updates Webinar](https://www.aapc.com/codes/coding-newsletters/articles) • [CMS — Fall 2026 ICD-10-PCS Update Materials](https://www.cms.gov/files/document/fall-2026-icd-10-pcs-update-materials.pdf) • [AAPC — CMS Releases FY 2026 ICD-10-CM Update](https://www.aapc.com/blog/92808-cms-releases-fy-2026-icd-10-cm-update/)

---

## Section 05 — Revenue Velocity / KPIs

### CY 2027 E/M Modifier Upgrade: 16% Pay Boost for All Physicians, 32% for ACO Participants — Modeling the Revenue Impact Before January 1

The E/M complexity modifier in the CY 2027 PFS final rule is not just a payment change — it is a documentation discipline opportunity. Practices that proactively build documentation workflows to support the modifier will begin January 1 with a revenue tailwind that partially offsets the 2.36% conversion factor cut. Practices that apply it incorrectly or inconsistently will face payer audits and recoupment exposure. The revenue velocity question is: what does appropriate application of the modifier realistically look like for your practice?

**Stat cards:**
- **16%** — E/M base payment increase when complexity modifier is appended (all physicians)
- **32%** — E/M base payment increase for ACO participants with complexity modifier
- **~70%** — Estimated share of established primary care visits that may qualify for the complexity modifier (AMA guidance)
- **$0** — Additional revenue from the modifier if documentation does not support complex chronic condition or serious illness management

### Complexity Modifier Application: The Revenue Math

A primary care practice billing 99214 (established patient, moderate complexity) at the current 2026 conversion factor generates approximately $112 per visit in Medicare reimbursement. Under CY 2027 with the 2.36% conversion factor reduction, that falls to roughly $109. With the complexity modifier appropriately appended, the same 99214 becomes approximately $127. For a practice billing 3,000 established patient visits per year with 65% Medicare, appropriate modifier application on qualifying visits could add $70,000–$120,000 in annual revenue.

The critical qualifier is "appropriately." The modifier applies when the physician serves as the continuing, longitudinal source of care for a patient's serious illness or complex chronic condition. It does not apply to consultations, one-time visits, or acute-condition-only encounters. CMS has indicated it will monitor utilization and may audit practices with outlier modifier rates.

| Practice Type | Likely Modifier-Eligible Visit % | Net Revenue Impact vs. 2026 |
|---|---|---|
| Primary care (high chronic condition panel) | 65–75% | +3–8% on E/M revenue |
| Cardiology (longitudinal CHF/arrhythmia mgmt) | 45–60% | +1–4% on E/M revenue |
| Oncology (active treatment longitudinal care) | 55–70% | +2–5% on E/M revenue |
| Surgical specialty (discrete procedures) | 10–20% | -1 to -2% net (CF cut dominates) |
| Urgent care / episodic visits | <5% | -2 to -3% net (CF cut dominates) |

### RPA and Clean Claim Rate: The Revenue Velocity Foundation

The E/M modifier opportunity only materializes if claims get out cleanly and paid on first submission. Practices with clean claim rates below 90% are leaving modifier revenue on the table due to rejections and resubmissions that delay payment by 15–45 days. The 2026 industry consensus targets — 95%+ clean claim rate, <40 days in A/R — remain the operational baseline that makes the payment policy gains real.

Automation of eligibility verification and pre-authorization status checking reduces the front-end errors (eligibility mismatches, missing authorizations) that account for 30–40% of first-submission rejections at practices that have not automated these functions.

> **Action Required:** Model your 2027 E/M revenue before January 1. Use your actual 2026 E/M code distribution, apply $32.6286 to get the base impact, then estimate what percentage of your established patient visits qualify for the complexity modifier. The difference between that estimate and your current 2026 revenue tells you how much documentation work you need to do before year-end.

**Sources:** [CMS — CY 2027 Physician Fee Schedule Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-final-rule) • [AHA — CY 2027 PFS Final Rule Summary](https://www.aha.org/news/headline/2026-11-04-cms-issues-cy-2027-physician-fee-schedule-final-rule) • [AMS Solutions — Medical Billing Benchmark Report 2026](https://ams-solutions.com/medical-billing-benchmark-report-2026/) • [Chief Healthcare Executive — CMS Final 2027 PFS](https://www.chiefhealthcareexecutive.com/view/cms-final-2027-physician-fee-schedule-cuts-pay-and-reworks-aco-incentives)

---

## Section 06 — Technology Spotlight

### CY 2027 OPPS/ASC Final Rule Released November 4 — 2.3% Hospital Outpatient Rate Increase, 2% ASC Payment Rise, Colonoscopy Quality Measure Removed

The simultaneous release of the CY 2027 OPPS/ASC and PFS final rules on November 4 creates a compressed transition window for billing and coding teams. For practices with hospital outpatient departments or affiliated ASCs, the OPPS/ASC changes are equally significant — particularly the 2% aggregate ASC payment increase and the removal of the colonoscopy follow-up interval measure from quality reporting.

**Stat cards:**
- **2.3%** — OPPS payment rate increase in CY 2027 (3.2% market basket – 0.9% productivity adjustment)
- **2%** — CMS projected aggregate Medicare ASC payment increase in CY 2027
- **Nov 9** — Date CY 2027 OPPS/ASC final rule publishes in the Federal Register (on display since Nov 4)
- **142** — RCM and HCIT transactions closed in H1 2026 (RevCycleAI deal tracker)

### OPPS/ASC Final Rule: What Changes January 1

For hospital outpatient billing teams and practice-affiliated ASCs, four specific changes warrant immediate attention:

1. **Colonoscopy quality measure removal:** CMS removed the colonoscopy follow-up interval measure from the ASC Quality Reporting Program starting with the 2027 reporting period. Gastroenterology ASCs and hospital outpatient endoscopy programs can retire quality reporting workflows for this specific measure.

2. **340B drug payment:** The final rule retains the 340B-acquired drug payment at a discounted rate from average sales price. Hospital billing teams operating 340B programs should verify no changes to their existing payment calculations.

3. **Inpatient-only service removals:** CMS continues removing services from the inpatient-only list, expanding the range of procedures eligible for HOPD and ASC settings. Orthopedic and spine ASCs benefit most from this ongoing expansion.

4. **Cost exemption codes:** CMS clarified that an inadvertent proposed change to the ASC addendum will not take effect, so codes including 63650, 63685, and 64590 keep their existing exemption. Spine neurostimulation billing teams should confirm this in their charge description masters.

### Technology Market: RCM M&A and AI Investment Signals

The 142 RCM and HCIT transactions closed in H1 2026 represent a market still consolidating around AI-enabled platforms. Waystar's strong Q3 subscription revenue growth (up 34%) signals that practices are shifting from per-transaction to subscription AI relationships. The practical implication for practices evaluating RCM technology: multi-year subscription contracts with AI vendors provide more cost predictability than per-claim models in a high-volume denial environment.

> **Key Insight:** For practices affiliated with ASCs considering whether to migrate additional procedures from hospital outpatient to ASC settings — where ASC reimbursement is typically 50–60% of OPPS rates — the 2% ASC aggregate payment increase is a marginal improvement. The more significant driver is payer-mix modeling: procedures that have higher commercial than Medicare volume will often be more financially efficient in an ASC setting regardless of the 2% Medicare adjustment.

**Sources:** [ACC — CMS Releases Final 2027 Medicare PFS and Hospital OPPS Rules](https://www.acc.org/Latest-in-Cardiology/Articles/2026/11/05/14/15/CMS-Releases-Final-2027-Medicare-Physician-Fee-Schedule-and-Hospital-OPPS-Rules) • [Becker's ASC — What CMS' Final OPPS 2027 Rule Means for ASC Leaders](https://www.beckersasc.com/asc-news/what-cms-final-opps-2027-rule-means-for-asc-leaders-more-cases-less-pay/) • [Waystar — Third Quarter 2026 Results](https://www.waystar.com/news/waystar-reports-third-quarter-2026-results/) • [RevCycleAI — Deal Tracker](https://revcycleai.com/deals-and-raises/)

---

## Section 07 — Compliance Corner

### MIPS Traditional Track Sunsets 2031 — Not 2028 as Proposed — ACO Part B Cost Sharing Waiver Launches April 2027, and Virtual Group Election Closes December 31

Three compliance deadlines and transitions from the CY 2027 PFS final rule require immediate attention from quality reporting teams. First, CMS confirmed the traditional MIPS reporting option will sunset after the 2030 performance period (measured in 2031), not after 2028 as proposed — giving practices three additional years to transition to MIPS Value Pathways or APM participation. Second, ACOs approved by CMS may reduce or eliminate Part B cost sharing starting April 1, 2027. Third, the MIPS virtual group election window for the 2027 performance year closes December 31, 2026.

**Stat cards:**
- **2031** — Year traditional MIPS reporting ends (changed from proposed 2028; two additional years for transition)
- **April 1, 2027** — Effective date for ACO Part B cost sharing waiver authority
- **December 31** — MIPS virtual group election deadline for 2027 performance year
- **50% → 75%** — Prior savings adjustment scaling factor increase in CY 2027 ACO rules

### MIPS Sunset: 2028 vs. 2031 — What Changed

The proposed rule would have ended traditional MIPS after the 2028 performance period. The final rule extends that to after the 2030 performance period. This three-year extension matters significantly for independent practices that have not yet completed the transition to MIPS Value Pathways (MVPs) — it removes the urgency of a forced MVP migration by 2029 and allows two additional years to select the right pathway. Practices currently meeting MIPS thresholds under traditional reporting should verify they are tracking against the Merit-based Incentive Payment System's 2027 performance thresholds and avoid the exceptional performance bonus opportunity cutoff.

### ACO Changes: Benchmarking and Cost Sharing

The prior savings adjustment scaling factor rising from 50% to 75% is the most significant ACO benchmarking change in the final rule. This change addresses the "ratchet effect" — the mechanism by which an ACO's benchmark falls after it generates savings, making it progressively harder to earn bonuses in subsequent years. By raising the scaling factor, CMS reduces the speed at which prior savings reduce future benchmarks, making ACO participation more financially sustainable for high-performing practices.

The April 1, 2027, Part B cost sharing waiver authority allows ACO-approved practices to reduce or eliminate patient cost sharing for certain services — a tool that could meaningfully improve care adherence for price-sensitive patient populations and reduce revenue leakage from uncollected cost-sharing balances.

> **Action Required:** If your practice is considering virtual group participation for the 2027 MIPS performance year, the election window closes December 31, 2026. Missing this window locks you out of the virtual group option for the entire year. Submit through the QPP portal at qpp.cms.gov before the deadline.

**Sources:** [CMS — CY 2027 PFS Final Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-final-rule) • [Chief Healthcare Executive — CMS Final 2027 PFS Cuts Pay and Reworks ACO Incentives](https://www.chiefhealthcareexecutive.com/view/cms-final-2027-physician-fee-schedule-cuts-pay-and-reworks-aco-incentives) • [MedAxiom — CMS Releases 2027 Medicare Physician Fee Schedule Final Rule](https://www.medaxiom.com/news/2026/11/04/news/cms-releases-2027-medicare-physician-fee-schedule-final-rule/) • [AHA — CMS Issues CY 2027 PFS Final Rule](https://www.aha.org/news/headline/2026-11-04-cms-issues-cy-2027-physician-fee-schedule-final-rule)

---

## Section 08 — Independent Practice Watch

### AMA Data Shows 42.2% of Physicians in Private Practice — Down from 60.1% in 2012, with Physician Pay Off 33% Inflation-Adjusted Since 2001 — and What the CY 2027 PFS Cut Means for Independent Practice Economics

The same week CMS finalized a 2.36% physician fee schedule cut, the AMA's most recent Physician Practice Benchmark Survey data puts the independent practice landscape in stark financial relief: just 42.2% of U.S. physicians are in wholly physician-owned practices in 2024, down from 60.1% in 2012. Medicare physician pay has fallen 33% in inflation-adjusted terms since 2001. The 2027 conversion factor cut is not an isolated event — it is the latest increment in a 25-year erosion that is restructuring the ownership composition of American medicine.

**Stat cards:**
- **42.2%** — Share of U.S. physicians in wholly physician-owned practices in 2024 (AMA, down from 60.1% in 2012)
- **34.5%** — Share in hospital-owned practices (up from 23.4% in 2012)
- **–33%** — Inflation-adjusted Medicare physician pay decline from 2001 to 2025 (AMA)
- **14%** — Average price increase for physician services after hospital acquisition (Bipartisan Policy Center study)

### Where You Should Be: Independent Practice Benchmarks in a 2.36% Cut Environment

The CY 2027 conversion factor cut amplifies the financial pressure on independent practices that have not built operational efficiency into their revenue cycles. For every $1M in annual Medicare revenue, the 2.36% cut represents $23,600 in lost annual reimbursement. For a primary care practice generating $1.5M in Medicare and Medicare Advantage revenue annually, the net impact before E/M modifier recovery is approximately $35,400.

The countermeasures available to independent practices are the same ones that separate top-quartile performers from median performers:

| Metric | Best-in-Class Target | Median Independent Practice | Warning Threshold |
|---|---|---|---|
| Overhead ratio | <55% | 61–68% | >70% |
| Net collection rate | ≥98% | 91–94% | <85% |
| Days in A/R | <35 | 38–48 | >55 |
| Denial rate | <5% | 8–12% | >15% |
| Cost to collect | <2.5% | 3.5–5% | >7% |

### Independence, Acquisition Pressure, and Technology Adoption Gaps

The AMA survey found that the top three reasons physicians report leaving independent practice are: difficulty negotiating payer rates, the cost of managing payer administrative and regulatory requirements, and limited access to costly resources. All three are directly addressable through RCM technology and economies of scale — but those economies require capital investment that many independent practices cannot finance.

The practical bridge: independent practices that adopt AI-assisted eligibility verification, automated PA tracking, and denial management tools narrow the technology gap with health system-employed practices without requiring the capital structure of a large system. The first-mover advantage in AI RCM adoption is shifting toward practices that move now, before the cost-to-collect gap becomes a tipping point for the acquisition conversation.

> **Where You Should Be:** If your practice has overhead above 68%, net collection rate below 91%, or Days in A/R above 48 — AND your most recent payer contract renegotiation was more than 24 months ago — you have both a revenue cycle problem and a payer strategy problem. At $2M annual revenue, closing a 5% gap in net collection rate adds $100,000 in annual recovered revenue. Closing a 2-point overhead gap adds another $40,000 in retained earnings. That $140,000 funds one year of a comprehensive AI RCM platform and still delivers a net positive.

**Sources:** [AMA — Smaller Share of Doctors in Private Practice Than Ever Before](https://www.ama-assn.org/practice-management/private-practices/smaller-share-doctors-private-practice-ever) • [Medical Economics — AMA Physician Private Practice Unraveling](https://www.medicaleconomics.com/view/ama-physician-private-practice-unraveling-due-to-low-payment-high-costs-administrative-burdens) • [Bipartisan Policy Center — Health Care Provider Consolidation](https://bipartisanpolicy.org/issue-brief/health-care-provider-consolidation/) • [AMS Solutions — Medical Billing Benchmark Report 2026](https://ams-solutions.com/medical-billing-benchmark-report-2026/)

---

## Section 09 — Specialty RCM Spotlight

### Primary Care E/M Gains, Cardiology MA Plan Disruption, ASC Orthopedics Wins New Cases, Oncology J-Code Audit Season, and ASC Gastroenterology Loses One Quality Measure

| Specialty | Key Update This Week | Billing/Coding Implication |
|---|---|---|
| Primary Care | CY 2027 E/M complexity modifier provides 16-32% base E/M payment boost; ICD-10 comment deadline Nov 13 | Identify qualifying longitudinal chronic condition patients; build documentation templates for modifier support |
| Cardiology | UHC dropping ~13% of MA plans in 18 states (~390K members), Humana footprint shrinking to 80% of counties; MA exit affecting ~600K Humana patients | Run MA patient panel re-verification immediately; model revenue impact of payer mix shift before Jan 1 |
| Orthopedics | CMS continues removing services from inpatient-only list, expanding ASC-eligible procedures; E/M complexity modifier applies to chronic joint condition management | Review updated ASC-eligible procedure list; model case migration from HOPD to ASC for high-volume procedures |
| Oncology | J-code CDM audit season: Q4 HCPCS update new J-codes now in effect 5 weeks; E/M modifier applicable to active treatment management | Complete Q4 J-code CDM audit; identify longitudinal oncology patients qualifying for E/M modifier |
| Radiology | AI-assisted imaging Category I CPT codes (lung nodule, stroke, fracture, MIPS pathway) in first year of billing; payer LCDs still developing | Confirm payer LCDs before billing new AI imaging codes; monitor coverage policy updates through December |
| Gastroenterology | ASC colonoscopy follow-up interval quality measure removed from ASQRP starting 2027 reporting period | Retire quality reporting workflow for colonoscopy follow-up measure; reallocate reporting resources |
| Mental Health | Telehealth flexibilities continue; Modifier GT/95 compliance critical; CY 2027 PFS E/M modifier applies to complex behavioral health longitudinal care | Audit behavioral health telehealth modifier use; identify SPMI patients qualifying for E/M complexity modifier |
| Neurology | CY 2027 PFS complexity modifier particularly valuable for neurology's high-burden chronic disease population (MS, epilepsy, Parkinson's); spinal cord stimulator exemption codes confirmed | Build E/M complexity documentation protocols for high-volume chronic disease neuro encounters; verify 63650/63685/64590 exemption status |

### Primary Care: Complexity Modifier Economics in Detail

For primary care practices with a predominantly Medicare and Medicare Advantage panel of patients with chronic conditions, the CY 2027 E/M complexity modifier is the most significant reimbursement opportunity in the past five years. A primary care physician billing 3,500 established-patient visits annually with 65% Medicare and 60% of those visits qualifying as longitudinal chronic condition management could see $80,000–$140,000 in additional annual Medicare revenue from the modifier — more than offsetting the conversion factor cut.

### Cardiology: MA Plan Exit Revenue Risk

The MA plan exits by UHC (13% of plans, 18 states, ~390,000 members) and Humana (footprint shrinking from 85% to 80% of U.S. counties, ~600,000 members) create an immediate revenue risk for cardiology practices with high MA patient volumes. MA plans typically pay at 95–115% of Medicare rates; patients who transition to traditional Medicare face deductible and coinsurance exposure that can reduce collection rates and increase bad debt. Run a payer mix analysis by zip code to identify the magnitude of MA disruption in your market before January 1.

**Sources:** [ACC — CMS Releases Final 2027 PFS and OPPS Rules](https://www.acc.org/Latest-in-Cardiology/Articles/2026/11/05/14/15/CMS-Releases-Final-2027-Medicare-Physician-Fee-Schedule-and-Hospital-OPPS-Rules) • [Fortune — UnitedHealthcare and Humana Ending MA Plans](https://fortune.com/2026/10/20/unitedhealthcare-humana-ending-medicare-advantage-plans-for-nearly-1-million-people-open-enrollment/) • [Revele — Primary Care RCM Benchmarks 2026](https://www.revelemd.com/blog/primary-care-rcm-benchmarks-2026-the-kpis-and-regulatory-shifts-defining-top-performing-practices) • [Becker's ASC — OPPS 2027 Final Rule](https://www.beckersasc.com/asc-news/what-cms-final-opps-2027-rule-means-for-asc-leaders-more-cases-less-pay/)

---

## Section 10 — This Week's Action Items

### November 6 Action Checklist — Tied to This Issue's Content

1. **Model your CY 2027 revenue impact immediately.** Use your 2026 E/M code distribution, apply $32.6286 (non-APM) or $32.9548 (APM-qualifying), then estimate qualifying complexity modifier visits. Know your net 2027 impact before year-end budgeting is finalized.

2. **Build E/M complexity modifier documentation templates.** The modifier requires that the physician serves as the continuing, longitudinal source of care for a serious illness or complex chronic condition. This is a documentation standard, not just a billing code change — your clinical team needs templates or EHR smart text before January 1.

3. **Confirm FHIR PA API readiness — 56 days remain.** Contact your EHR vendor and top 3 payers to verify both are ready for January 1. If your EHR is not integrated, identify which payers have FHIR sandbox access available and begin testing.

4. **Run a Medicare Advantage patient payer-mix analysis by county.** UHC is exiting MA plans in 18 states (~390K members) and Humana's footprint is shrinking to 80% of counties (~600K members). Identify affected patients in your panel before they miss open enrollment re-selection.

5. **Register for the AAPC CPT 2027 Coding Updates webinar (November 25).** Begin CPT 2027 preparation — audit your CDM for codes expected to change and confirm your PM/EHR vendor's update timeline for the January 1 code set.

6. **Submit ICD-10 public comments by November 13.** If your practice has encountered recurring denials or claims ambiguity tied to insufficient ICD-10 code specificity in your specialty, the November 13 deadline is your opportunity to influence the FY 2027 code set.

7. **File your 2027 MIPS virtual group election by December 31.** The traditional MIPS option now sunsets in 2031 (not 2028), but virtual group elections still require annual QPP portal filing — missing the December 31 window locks you out for all of 2027.

8. **Update the CDM to remove the Cigna E/M downcoding risk.** Audit your top 10 E/M codes for documentation completeness against Cigna's new complexity review criteria. Any encounter with a 99215 or 99214 that cannot be supported by documentation level should be remediated before the claim is submitted.

---

## Big Stat

**2.36%** — The CY 2027 physician conversion factor cut for non-APM participants, the deepest reduction since 2022. On $5M in annual Medicare revenue, that is $118,000 in lost annual reimbursement. When layered on top of the 33% inflation-adjusted physician pay decline since 2001 documented by the AMA, the 2027 rule is not a one-year budget adjustment — it is the continuation of a structural reimbursement contraction that is accelerating physician practice consolidation and threatening the financial independence of physician-owned practices.

*Source: CMS CY 2027 Physician Fee Schedule Final Rule (CMS-1848-F), released November 4, 2026 • American Medical Association Physician Practice Benchmark Survey*

---

*Next issue: November 13, 2026*
