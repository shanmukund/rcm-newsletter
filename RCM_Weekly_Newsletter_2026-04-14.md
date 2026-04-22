# RCM Pulse Weekly — April 14, 2026
## Volume 4, Issue 2 | Revenue Cycle Management Intelligence for Medical Practices

---

## In This Issue

1. CMS Drops Drug PA Interoperability Rule; H.R. 1 Puts Medicaid Eligibility on a New Clock
2. The MA Denial Crisis Deepens: 56% Jump in PA Denials, 80.7% Overturned on Appeal
3. Ambient AI Delivers Measurable Revenue Lift: 11% wRVU Gain, 14% More HCCs Documented
4. New CPT Codes in Play: AI-Enhanced Cardiac CT Billable, RPM Splits, GI and Neurology Updates
5. The MA Denial Tax: $47 Per Claim — How Rework Costs Are Eroding Revenue Velocity
6. Technology Spotlight: IKS Health Eyes $600M TruBridge Acquisition; FHIR Countdown at 8.5 Months
7. Compliance Corner: HIPAA Now Requires MFA; CMS Audits Expand to All 550 MA Contracts
8. Independent Practice Watch: Physician Ownership Falls to 42.2% — IPA Formation Surges
9. Specialty RCM Spotlight: Primary Care, Cardiology, Orthopedics, Oncology, Neurology, Mental Health, Gastroenterology
10. This Week's Action Items

---

## Section 01 — Regulatory/Payment Updates
### CMS Drops Drug PA Interoperability Rule; H.R. 1 Puts Medicaid Eligibility on a New Clock

The week of April 14 brought two seismic regulatory developments that every practice billing Medicaid or dealing with drug prior authorization must now track closely.

**CMS-0062-P: Drug Prior Authorization Proposed Rule (April 14, 2026)**

CMS released the "2026 CMS Interoperability Standards and Prior Authorization for Drugs Proposed Rule" (CMS-0062-P) on April 14 — the most significant new rulemaking of the week. This rule extends the CMS-0057-F framework specifically to drug prior authorization, requiring impacted payers (Medicare Advantage, Medicaid, CHIP, and QHP issuers on the FFE) to support electronic prior authorization for drugs via updated FHIR-based APIs beginning **October 1, 2027**.

Key proposed decision timelines:
- Medicaid/CHIP: standard PA decisions within **7 days**, expedited within **72 hours**
- QHP issuers on the FFE: standard within **72 hours**, expedited within **24 hours**
- Payers must publicly report drug PA metrics beginning **2028** (based on 2027 data)

Public comment period closes **June 15, 2026**. Practices and RCM vendors should submit comments on workflow implementation challenges now.

**H.R. 1 — Medicaid Work Requirements Now Law**

The "One Big Beautiful Bill Act" is signed into law, restructuring Medicaid with direct implications for practice eligibility workflows:
- States must implement **community engagement (work) requirements** — 80 hours/month — for Medicaid expansion adults by **December 31, 2026**
- States must conduct **eligibility redeterminations every 6 months** (replacing annual renewals)
- HHS implementation guidance to states due **June 1, 2026**; state enrollee outreach between **June 30 – August 31, 2026**
- An estimated **11.8 million Americans** could lose Medicaid coverage over 10 years; **4.8 million** from work requirements alone
- Federal Medicaid spending cut by **$344 billion** over 10 years

**CY 2026 Dual Conversion Factors: Site-of-Service Rebalancing in Effect**

The 2026 PFS conversion factors remain live: **$33.5675 for APM-qualifying physicians** and **$33.4009 for all others**. The structural shift: facility-based payments fell approximately **7%** while independent office-based service payments rose approximately **4%** — a deliberate CMS site-of-service rebalancing that rewards care delivered in independent physician offices rather than hospital outpatient settings.

**Key Insight:** The H.R. 1 eligibility changes will trigger a wave of Medicaid coverage churn starting Q3 2026. Practices serving Medicaid populations must upgrade eligibility verification to real-time, automated daily checks — a manual verification workflow will fail to keep pace with six-month redetermination cycles.

**Sources:** CMS CMS-0062-P Fact Sheet | HMA — H.R. 1 Signed Into Law | CMS CY 2026 PFS Final Rule | Revele Spring 2026 Key Developments | Center for Children and Families — Work Requirements

---

## Section 02 — Prior Authorization / Payer Relations
### The MA Denial Crisis Deepens: 56% Jump in PA Denials, 80.7% Overturned on Appeal

Despite voluntary reform commitments from more than 50 health plans, the Medicare Advantage prior authorization crisis is worsening. The data from the first quarter of 2026 tells a troubling story.

**MA Denial Metrics (Q1 2026):**
- MA plans now deny approximately **17% of submitted claims** — more than double traditional Medicare's ~8% denial rate
- MA prior authorization denials jumped **56%** in the most recent reporting period
- **80.7% of appealed MA PA denials are ultimately overturned** (KFF analysis) — meaning initial denials are statistically likely to be wrong, but practices absorb the full cost of the appeals process
- Administrative rework per MA claim: **$47**
- Denial volumes driven by a nearly **fivefold increase** in Request for Information (RFI) and medical necessity denials

**Voluntary Reform: Mixed Results**

The 50+ health plans that committed to PA reforms effective January 1, 2026 have delivered mixed results:
- UHC dropped PA for **231 procedures** including nuclear medicine, OB ultrasounds, and ECGs
- Cigna eliminated PA for ~**100 services** and added real-time PA status tools
- Aetna bundled medical procedure + pharmaceutical PA into a **single submission** workflow
- All plans honor existing authorizations for **90 days** when a patient switches insurers

Yet despite these commitments, MA PA denial rates are up 56% — signaling meaningful implementation gaps between policy announcements and operational execution at the plan level.

**CMS Expands MA Audits to All 550 Contracts**

CMS announced expansion of its MA audit program from ~60 plans per year to all **550 eligible MA contracts annually**, with a backlog of 2018–2024 audits being completed. Practices should expect increased scrutiny on risk adjustment documentation and claim accuracy as CMS intensifies plan-level enforcement.

**Warning:** Practices accepting Medicare Advantage must treat denial management as a permanent, dedicated workflow — not an occasional task. At $47 per rework event and an 80.7% appeal reversal rate, every appealed denial is statistically likely to be collected, but only if your practice has the capacity to pursue it.

**Sources:** Saving Advice — MA PA Denials Jumped 56% | Health Affairs — MA Denies 17% of Claims | KFF MA PA Analysis | UASI Solutions — CMS Audit Expansion | Becker's Payer — 7 PA Updates 2026 | CMS CMS-0062-P Fact Sheet

---

## Section 03 — AI & Automation Deep Dive
### Ambient AI Delivers Measurable Revenue Lift: 11% wRVU Gain, 14% More HCCs Documented

The debate over ambient AI scribes moved definitively into evidence territory this week. A landmark study published April 1, 2026 covering **1,800 clinicians across five academic medical centers** (2023–2025) quantified the effect of ambient AI documentation tools on physician time and clinical output.

**Key Findings from the Multi-Site Study:**
- Ambient AI scribe users saved **16 minutes of documentation time** and **13 fewer minutes in the medical record** per 8-hour shift
- Results varied by product: Nabla users showed a **9.5% decrease in time-in-note** vs. control; DAX Copilot showed no significant change (-1.7%)
- Riverside Health (Virginia): deployed ambient AI across its network and reported an **11% rise in physician wRVUs** and **14% increase in documented HCC diagnoses per encounter**
- A 2024 Texas Oncology study found ambient scribes increased documented diagnoses from **3.0 to 4.1 per encounter** — directly improving coding completeness and downstream reimbursement

**Agentic AI Crosses the Mainstream Threshold**

Per the 2026 Guidehouse/HFMA RCM Trends survey:
- **78% of healthcare executives** are using automation and AI to accelerate manual revenue cycle processes
- **53% of healthcare organizations** have adopted agentic AI or multi-agent workflows (up dramatically from pilot stage in 2024)

Early adopters of AI-powered RCM report: denial rate reductions of **30–50%**, prior authorization times dropping from days to hours, clean claim rate improvements of **15–30%**, and Days in A/R declining **20–35%**.

**Autonomous Coding Adoption Accelerates**

- Over **30% of U.S. healthcare organizations** are adopting or actively considering fully autonomous coding
- AI-driven coding systems reduce coding time by **40%** and increase accuracy to **95%+**
- The global AI in RCM market was **$20.63 billion in 2024** and is projected to reach **$70.12 billion by 2030** (CAGR of **24.16%**)
- 60% of RCM leaders cite finding ICD-11-ready certified coders as their primary staffing hurdle — driving autonomous coding adoption to address a growing **45-day average backlog** in unbilled charts for manual-only operations

**AI Technology Stack for RCM (2026)**

| Layer | Tools | RCM Application |
|-------|-------|-----------------|
| Generative AI | LLMs, ambient scribes (Nabla, DAX, Abridge, Nuance) | Clinical note-to-code generation, denial appeal drafting, PA letter automation |
| AI / ML | Autonomous coding (CodaMetrix, AKASA), denial risk scoring | Predictive A/R analytics, contract underpayment detection |
| RPA | Eligibility bots, claim status scrapers, ERA posting | Portal data extraction, patient statement generation |

**Bottom Line:** The ambient AI revenue lift is no longer theoretical. An 11% wRVU increase and 14% more HCCs documented per encounter translate directly into billing revenue. For a physician billing $400,000/year in Medicare RVUs, an 11% lift represents $44,000 in additional annual revenue — before any improvement in coding accuracy.

**Sources:** STAT News — Large AI Scribe Study (April 1, 2026) | AHA — 6 Health Systems Enhancing Care with Ambient AI (April 14, 2026) | Guidehouse/HFMA 2026 RCM Trends Report | Revele Spring 2026 | Grand View Research — AI in RCM Market | HIT Consultant — Ambient AI ROI and Autonomous Coding

---

## Section 04 — Coding Updates
### New CPT Codes in Play: AI-Enhanced Cardiac CT Billable, RPM Splits, GI and Neurology Updates

While the April 1 ICD-10-CM instructional note updates were covered in last week's issue, several January 1 CPT code changes are now showing up in real-world billing workflows and deserve immediate attention. The **2026 CPT code set includes 418 total changes** (288 new codes, 84 deletions, 46 revisions) — the largest overhaul in recent memory.

**CPT 75577 — AI-Enhanced Cardiac CT (Now Billable)**

New permanent Category I code **75577** covers AI-enhanced CT coronary angiography plaque quantification. This converts AI-assisted cardiac imaging analysis from an overhead cost into a direct revenue-generating service. Cardiology and radiology practices using AI-assisted coronary CT tools must immediately map their workflow to this code.

**RPM/RTM Code Split — 2-15 Days vs. 16-30 Days**

New 2026 CPT codes now cover **2–15 days** of remote patient monitoring transmitted data. Existing codes (99454 for RPM; 98976–98978 for RTM) now apply exclusively to **16–30 days** of data. Practices billing RPM or RTM must update their billing logic: patients with data transmissions under 16 days now require the new short-cycle codes or claims will be miscoded.

**GI: Endoscopic Sleeve Gastroplasty and Anorectal Physiology**

- New permanent CPT code for **endoscopic sleeve gastroplasty** (bariatric endoscopy) — converts a previously unlisted procedure to a directly billable code
- Two new codes modernizing **anorectal physiology testing** — GI practices performing these studies should audit billing against new code descriptors

**Neurology: Continuous EEG Monitoring and AI EEG Analysis**

- New Category III codes **X461T–X466T** for continuous EEG monitoring across multiple session durations
- **X504T** for AI-supported algorithmic EEG waveform analysis — emerging technology billing pathway for academic and tertiary neurology centers

**Warning:** Practices that have not audited their superbills and billing software configurations against the full 2026 CPT update are at risk of submitting claims under deleted or revised codes. A claim submitted under a deleted CPT code will be rejected by payers. Conduct a full audit against your top 30 procedure codes before end of April.

**Sources:** IMO Health — 2026 CPT Code Set 7 Key Updates | ASGE — New CPT Codes for GI 2026 | CMS CY 2026 PFS Final Rule | Medisys — Cardiology Billing Guidelines 2026 | MedCare MSO — Neurology Medical Billing and Compliance Guide 2026

---

## Section 05 — Revenue Velocity / KPIs
### The MA Denial Tax: $47 Per Claim — How Rework Costs Are Eroding Revenue Velocity

The Medicare Advantage denial burden is now a quantifiable line item eroding practice revenue. With **$47 in administrative cost per reworked MA claim** and denial rates exceeding 17%, the math reveals a hidden revenue drain that dwarfs most other billing inefficiencies.

**The Denial Rework Cost Model**

| Scenario | Detail | Annual Cost |
|----------|--------|-------------|
| Practice with 1,000 MA claims/month | 17% denial rate = 170 denials/month | 170 × $47 = $7,990/month = **$95,880/year** in rework cost |
| 80.7% of those are ultimately paid on appeal | But each requires ~2 hrs of staff time | 137 claims × 2 hrs × $25/hr = **$82,200/year** in labor |

**2026 RCM Performance Benchmarks**

| KPI | Industry Average | Best Practice Target | High-Risk Threshold |
|-----|-----------------|---------------------|---------------------|
| Denial Rate | 6–13% | < 5% | > 15% |
| Days in A/R | 33–42 days | < 30 days | > 50 days |
| Clean Claim Rate | ~85% | 95–98%+ | < 80% |
| Net Collection Rate | ~92% | > 95% | < 90% |
| First-Pass Acceptance Rate | ~80% | > 85% | < 75% |

**Revenue Velocity Improvement Strategies for Q2 2026**

1. **Implement real-time eligibility at scheduling** — Automated checks before the appointment catch coverage gaps that create MA denial clusters at the point of care
2. **Build a dedicated MA denial management workflow** — At 80.7% appeal reversal rate, every denied MA claim has a statistically strong expected value; the bottleneck is bandwidth
3. **Segment A/R by payer type** — Separate MA from commercial from traditional Medicare to isolate which bucket is driving your aging profile
4. **Switch to daily statement cycles** — Practices running daily patient statements vs. monthly billing cycles report 15–20% faster patient collections
5. **Use ERA data plus MRF data for contract benchmarking** — New price transparency data lets you identify payers paying below the Medicare median allowed amount

**Bottom Line:** A practice with $5M in annual charges, a 12% denial rate, and 45 days in A/R could recover $300,000–$500,000 annually by hitting industry best-practice targets. The ROI on denial management automation and real-time eligibility is rarely negative.

**Sources:** Health Affairs — MA Denies 17% of Claims | Saving Advice — MA PA Denials 56% | HFMA — 7 KPIs Providers Should Track | Plutus Health — RCM KPI Guide 2026 | NCDSINC — RCM Benchmarks 2026

---

## Section 06 — Technology Spotlight
### IKS Health Eyes $600M TruBridge Acquisition; FHIR API Countdown at 8.5 Months

**Acquisition of the Week: IKS Health / TruBridge**

India-based health IT and RCM firm IKS Health (Inventurus Knowledge Solutions, backed by the Jhunjhunwala family) is nearing a deal to acquire Nasdaq-listed **TruBridge for approximately $600 million**, financed by a $675M debt facility from Citi, Deutsche Bank, and JP Morgan (reported April 13, 2026). This is IKS's largest acquisition to date, targeting community hospitals and rural/mid-size providers — a segment chronically underserved by enterprise RCM platforms. TruBridge serves approximately **700 community hospitals** primarily in the Southeast and rural Midwest. The deal signals continued consolidation in the outsourced RCM market, valued at **$85.2 billion globally in 2025**.

**FHIR API Implementation: 8.5 Months Remaining**

With the CMS-0057-F Prior Authorization FHIR API compliance deadline at **January 1, 2027**, practices now have fewer than 9 months to ensure their EHR/PM systems are configured to use FHIR-based PA workflows. Epic, Cerner, eClinicalWorks, and Athenahealth all support FHIR R4 access. The new CMS-0062-P rule extends FHIR requirements to drug PA by October 2027 — making FHIR integration a two-phase compliance project.

**Vendor Landscape — April 2026**

| Category | Key Vendors |
|----------|-------------|
| Ambient AI Scribes | Nabla, DAX Copilot (Nuance), Abridge, Suki |
| Autonomous Coding | CodaMetrix, AKASA, Cosentus, FinThrive |
| Eligibility & Patient Access | Experian Health, Waystar, Athelas, Quadax |
| Denial Management & Appeals | Aspirion, R1 RCM, Omega Healthcare, FinThrive |
| RCM Outsourcing | IKS Health, TruBridge (pending acquisition), Omega Healthcare |

**Key Insight:** The IKS/TruBridge deal, if completed, creates a new global RCM powerhouse targeting the underserved community hospital and independent practice segment. Practices currently using TruBridge for outsourced billing should request clarity on service continuity, pricing, and roadmap commitments before the deal closes.

**Sources:** BusinessToday — IKS Health/TruBridge $600M | Firely — CMS-0057-F Decoded | Healthcare IT News KLAS 2026 | Grand View Research — RCM Market | KLAS — Waystar Ratings

---

## Section 07 — Compliance Corner
### HIPAA Now Requires MFA; CMS Audits Expand to All 550 MA Contracts

Three compliance priorities converge in Q2 2026 that practices cannot defer.

**1. HIPAA Security Rule 2026 — MFA, Encryption, and 72-Hour Breach Notification**

The 2026 HIPAA Security Rule update introduced mandatory security controls that take effect this year:
- **Multi-factor authentication (MFA)** is now required for all PHI access — including EHR logins, billing software, and clearinghouse portals
- **Encryption** of electronic PHI at rest and in transit is now required (no longer "addressable")
- **72-hour breach notification** to HHS is mandatory (down from 60 days for smaller breaches)
- **Annual technical risk assessments** are required, replacing the previous "periodic" standard

OCR HIPAA fines averaged **$6.6 million total** in 2025 penalties and are rising. Practices that have not implemented MFA across all clinical and billing systems are out of compliance now.

**2. CMS MA Audit Expansion — All 550 Contracts Under Annual Review**

CMS is auditing all **550 eligible MA contracts annually** (up from ~60/year). CMS is clearing a backlog of audits from 2018–2024. This increases MA payer scrutiny on risk adjustment documentation, PA practices, and claim accuracy — and creates downstream compliance pressure for practices submitting claims to MA plans.

**3. H.R. 1 Medicaid Eligibility Churn — Real-Time Verification Is Now Mandatory**

With H.R. 1 requiring **6-month eligibility redeterminations** for Medicaid expansion adults starting Q3–Q4 2026, practices serving Medicaid populations face a coverage verification challenge unlike anything since the post-COVID unwinding. Manual eligibility checks at check-in will not be sufficient. Real-time automated eligibility verification before every encounter is the only sustainable approach.

**Action Required:** Assign a HIPAA Security Rule compliance owner before May 1. Audit all PHI access points (EHR, clearinghouse, billing software, email) for MFA compliance. Contact your IT vendor to confirm encryption status. Then run eligibility automation RFPs for any system still relying on manual Medicaid verification.

**Sources:** Medcurity — 2026 HIPAA Security Rule | CBIZ — 5 HIPAA Security Rule Changes 2026 | UASI Solutions — CMS Audit Expansion | HMA — H.R. 1 Signed Into Law | Center for Children and Families — Work Requirements

---

## Section 08 — Independent Practice Watch
### Physician Ownership Falls to 42.2% — IPA Formation Surges as the Defense Strategy

The latest AMA data confirms the long-running consolidation trend accelerated through 2024:
- Just **42.2% of physicians** worked in private practices in 2024 (down from **60.1% in 2012**)
- **34.5%** worked in hospital-owned settings; **6.5%** reported private-equity ownership
- The 2026 budget environment — flat-to-declining Medicare rates, H.R. 1 Medicaid cuts, rising operational costs — is expected to intensify consolidation pressure further

**The IPA Formation Surge**

Thousands of primary care practices facing financial distress are joining **Independent Physician Associations (IPAs)** to increase negotiating leverage with payers, access value-based care contracts, and maintain independence. NPR (February 2026) reported this as a direct response to Medicaid cuts and commercial rate pressure. Bain & Company's Global Healthcare Private Equity Report 2026 notes the industry has shifted "from raw consolidation to an era where operational excellence is the only way to win."

**The LEAD APM Opportunity — Request for Applications Open Spring 2026**

The new voluntary LEAD APM model offers independent primary care practices a sustainable alternative to selling or merging:
- **10-year performance period** — no ratchet effect
- Professional Risk Option caps downside at **50%**
- APM conversion factor of **$33.57** for qualifying participants (vs. $33.40 for non-APM practices)
- RFA is open now — practices should evaluate whether LEAD APM participation makes sense before the enrollment window closes

**Where You Should Be: Q2 2026 Benchmarks for Independent Practices**

| Metric | Where Most Practices Are | Where You Should Be | Priority |
|--------|--------------------------|---------------------|----------|
| Denial Rate | 10–15% | < 7% | HIGH |
| Days in A/R | 40–55 days | < 35 days | HIGH |
| Clean Claim Rate | 78–84% | > 92% | HIGH |
| PA Time per Week | 14–18 hours | < 8 hours (with automation) | MEDIUM |
| Patient Collection Rate | 55–65% | > 75% | MEDIUM |
| AI Tool Adoption | < 20% of workflows | 50%+ of routine workflows | MEDIUM |
| Telehealth Billing | Ad hoc or incomplete | Permanent workflows in place | HIGH |

**Key Insight:** 68% of physicians now use AI tools in practice (up from 38% in 2023). Independent practices that have not adopted AI-assisted documentation, coding, or eligibility verification are no longer early adopters who missed a trend — they are operationally behind. The gap between AI-adopting and non-adopting practices is widening every quarter.

**Sources:** Medical Economics — Will Independent Practices Thrive or Die Off in 2026? | NPR — Primary Care Forming IPAs | AMA Private Practice Data 2024 | Revele Spring 2026 | Doctors Management — 2026 Private Practice Playbook | Wink CHSB — 2026 Medicare Payment Changes

---

## Section 09 — Specialty RCM Spotlight
### Primary Care, Cardiology, Orthopedics, Oncology, Neurology, Mental Health, Gastroenterology

| Specialty | Key Update | Financial Impact | Recommended Action |
|-----------|-----------|------------------|--------------------|
| **Primary Care** | APCM add-on codes allow APCM + BHI/CoCM billing in same month; LEAD APM RFA open; E/M codes exempt from 2.5% efficiency adjustment | Neutral to positive; CCM/TCM and APCM billing generate protected revenue | Enroll eligible patients in APCM; evaluate LEAD APM participation; expand CCM/TCM billing |
| **Cardiology** | CPT 75577 (AI-enhanced CT CA plaque quantification) now billable; 0992T/0993T for cardiac risk assessment; ASM model — CMS releases **preliminary July 2026** participant list (based on 2024 data) for mandatory ASM enrollment | Revenue opportunity from AI-enhanced CT codes; 8,600 cardiologists face mandatory ASM with ±9–12% payment adjustments | Map AI cardiac CT workflows to 75577 now; determine ASM eligibility from CMS July list; model ASM financial impact |
| **Orthopedics** | TEAM model (mandatory bundled payment 30-day episode post-discharge) now active; ASM targets orthopedic surgery + spine/pain; 2.5% efficiency cut on all surgical codes | Direct bottom-line impact; TEAM bundled episodes add shared-savings/risk complexity | Audit TEAM model episode definitions; build episode cost management workflows; accelerate modifier and documentation specificity |
| **Oncology** | GLOBE/GUARD drug pricing models reduce ASP reimbursement for select drugs (ibrutinib cut **38%**); 37% of oncologists face Medicare cuts of 10–20%; radiation therapy codes (77402/77407/77412) converted to Levels 1/2/3; IMRT codes 77385/77386 deleted | Significant per-drug revenue compression; IMRT code deletion creates billing risk | Update drug administration billing to new ASP rates immediately; remap IMRT codes to new three-level framework; identify commercial contracts with ASP floors |
| **Neurology** | Claim denial rates average **18%** — highest of any specialty reviewed; X461T–X466T continuous EEG monitoring codes available; X504T AI EEG analysis; NCCI edit scrutiny on EMG/EEG bundling intensifying | Denial rate 3× industry average represents significant recoverable revenue | Build neurology-specific denial work queue; audit EMG/EEG billing against NCCI edits; evaluate continuous EEG monitoring code adoption |
| **Mental Health** | Telehealth extended through **December 31, 2027** (CAA 2026); home-based telehealth at non-facility rates; audio-only parity maintained; new 2026 CPT codes for **remote behavioral monitoring** (2–15-day cycles); MHPAEA parity audits intensifying | Multi-year telehealth billing stability; remote monitoring new revenue stream; parity audit risk | Establish permanent tele-mental health billing workflows; activate remote behavioral monitoring codes; prepare for MHPAEA comparative analysis documentation requests |
| **Gastroenterology** | New permanent CPT code for **endoscopic sleeve gastroplasty**; two new anorectal physiology codes; 2.5% efficiency cut on endoscopy; office-based GI services receive payment increase vs. ASC/hospital-based cuts | Office-based GI practices advantaged vs. hospital-based settings; bariatric endoscopy new billing opportunity | Evaluate moving appropriate procedures to office setting; add endoscopic sleeve gastroplasty code to superbill; update modifier workflows (XE/XS/XP/XU vs. 59 by payer) |

**Action Required:** Oncology practices must act immediately on ibrutinib and select drug reimbursement reductions under the GLOBE/GUARD models. If you are billing ASP-based drug administration codes for affected drugs without updated pricing, you are either over- or under-billing — both are compliance risks.

**Sources:** CMS ASM Model | Revele Spring 2026 | Medisys Cardiology Billing 2026 | RCM Workshop — Oncology Billing 2026 | Human Medical Billing — GLOBE & GUARD | Ventra Health — Radiology 2026 | MedCare MSO — Neurology Guide 2026 | ADSC — Psychiatry and Behavioral Health 2026 | ASGE — New CPT Codes for GI 2026 | AGA — CMS Finalizes 2026 Payment Policies

---

## Section 10 — This Week's Action Items

1. **Submit comments on CMS-0062-P before June 15** — The drug PA interoperability proposed rule will directly shape how your practice handles pharmaceutical prior authorization for Medicare Advantage and Medicaid plans. If your practice faces high drug PA volume (oncology, rheumatology, neurology), submit a comment documenting the administrative burden. CMS is listening — this rule is still in proposed form.

2. **Build a dedicated MA denial management workflow this week** — At 80.7% appeal reversal rate, MA denials have a statistically positive expected value. Every practice with more than 200 MA claims per month should have a named denial follow-up owner, a denial aging dashboard, and an appeal template library. If you don't, assign it today.

3. **Audit all CPT code changes against your superbills and billing software** — With 418 CPT code changes in effect since January 1, practices that have not verified their top 30 procedure codes against the 2026 CPT update are filing claims with material risk. Start with RPM/RTM code split, CPT 75577 (cardiology), oncology radiation therapy codes, and GI endoscopy codes.

4. **Implement MFA across all PHI access points before May 31** — The 2026 HIPAA Security Rule update makes MFA mandatory. Audit every system that accesses patient data: EHR login, clearinghouse portal, billing software, patient portal, and email with PHI. Non-compliance with MFA is no longer a gray area.

5. **Evaluate LEAD APM enrollment before the RFA window closes** — If your practice is independent and primarily primary care, the LEAD APM model offers a 10-year contract with APM conversion factor access ($33.57 vs. $33.40) and no ratchet effect. The RFA is open now. Schedule a LEAD APM evaluation meeting with your practice administrator this week.

6. **Upgrade Medicaid eligibility verification to real-time automation now** — With H.R. 1 mandating 6-month eligibility redeterminations starting Q3 2026, your current annual or check-in-based verification workflow will fail. Contact your clearinghouse or PM vendor about real-time automated eligibility for all Medicaid patients before July.

7. **Oncology and cardiology: update drug administration billing for GLOBE/GUARD pricing** — Ibrutinib reimbursement is cut 38% under the new CMS drug pricing models. Any oncology or hematology practice billing affected drugs must update unit pricing in their billing system immediately. Check with your specialty pharmacy partner for a full list of GLOBE/GUARD-affected drugs.

**Sources:** CMS CMS-0062-P | KFF MA PA Analysis | IMO Health 2026 CPT | CBIZ HIPAA 2026 | CMS LEAD APM | HMA H.R. 1 | Human Medical Billing GLOBE & GUARD

---

## Big Stat

**80.7%**

The share of Medicare Advantage prior authorization denials that are ultimately reversed on appeal — meaning 4 out of every 5 MA PA denials are statistically likely to be wrong. With practices absorbing $47 in rework cost per claim, the MA prior authorization system is generating hundreds of millions of dollars in unnecessary administrative waste annually. CMS-0062-P signals regulators have had enough.

*Source: KFF Analysis of Medicare Advantage Prior Authorization Outcomes | April 2026*

---

*RCM Pulse Weekly — Volume 4, Issue 2 — April 14, 2026*
*Next Issue: April 21, 2026*
*Revenue Cycle Management Intelligence for Medical Practices*
*All information sourced from public domain sources including CMS.gov, AAPC, HFMA, AHA, payer portals, and industry publications. Not legal or compliance advice. Consult qualified billing compliance counsel for specific guidance.*
