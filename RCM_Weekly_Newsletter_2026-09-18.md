# RCM Pulse Weekly
## Revenue Cycle Management Intelligence for Medical Practices

**September 18, 2026 • Volume 9, Issue 3**

---

## In This Issue

01. The Comment Window Closed Monday — Now You Plan As If It's Final: 105 Days to a 100%/50% Same-Day E/M Cut, a Three-Tier Skin Substitute Rate, and G2211 Turning Into a Modifier
02. UnitedHealthcare Deletes 1,700 Prior Authorization Codes in 13 Days — Roughly 30% of Its Book, and the Most Under-Prepared Payer Change of the Year
03. The AI Taxonomy Becomes Billable Language: 10 New AI Codes Bring CPT to 43, Appendix S Splits Assistive From Augmentative — While 59% of Organizations Still Have No AI Anywhere in the Revenue Cycle
04. Two Code Sets, Thirteen Days Apart and 105: FY 2027 ICD-10-CM Lands October 1, and CPT 2027 Publishes 453 Editorial Changes Including 80 Deletions
05. The 24-Minute Problem Has a New Number: Electronic Prior Auth Adoption Hits 40% but Only 35% Is True X12 278 — and A/R Days Rose 2.4 at the Median
06. Waystar Tops the 2026 KLAS Suites Report as a $189B Market Heads to $505B and 70% of Systems Plan to Outsource More
07. Compliance Corner: Price Transparency Enforcement Passes Its Sixth Month, Four FHIR APIs Come Due in 105 Days, and WISeR Clears Its Senate Challenge
08. Independent Practice Watch: 89% Say Staying Independent Got Harder — Against Medicare Payment Up 10% and Practice Costs Up 63% Since 2001
09. Specialty RCM Spotlight: Dermatology and ENT at −9%, Orthopedics −7%, Hem/Onc −1.5%, Cardiology +1% — and Nearly Every One of Them Gets Prior Auth Relief on October 1
10. This Week's Action Items

---

## Section 01 — Regulatory / Payment Updates

### The Comment Window Closed Monday — Now You Plan As If It's Final: 105 Days to a 100%/50% Same-Day E/M Cut, a Three-Tier Skin Substitute Rate, and G2211 Turning Into a Modifier

The comment period on the **CY 2027 Medicare Physician Fee Schedule proposed rule (CMS-1848-P)** closed at the end of **Monday, September 14, 2026**. For the last nine weeks this newsletter has been counting down to that date. That clock is now finished, and a different one has started — and it is the one that actually costs money.

| Clock | Date | Days from today |
|---|---|---|
| Comment period on CMS-1848-P | Closed September 14, 2026 | — |
| FY 2027 ICD-10-CM effective | October 1, 2026 | **13** |
| CY 2027 PFS final rule expected | Early November 2026 | ~45 |
| CPT 2027, final PFS rates, CMS-0057-F APIs all effective | January 1, 2027 | **105** |

**Stat cards:**
- **105** — Days until the CY 2027 PFS takes effect, January 1, 2027
- **50%** — Proposed payment for every same-day service after the most expensive one
- **$33.17 / $32.84** — Proposed CY 2027 conversion factors (qualifying / non-qualifying APM participants)
- **~45** — Days until the final rule is expected, in early November

The window between a proposed rule closing and a final rule publishing is the single most wasted period in the practice-management calendar. Nothing is certain, so nothing gets done — and then the final rule drops around November 1 and leaves sixty days to reconfigure charge templates, renegotiate contracts, and retrain front-desk staff over the holidays. The proposals below are not guaranteed. They are, however, the best available forecast, and every one of them can be modeled now against your own claims data at zero risk.

#### The Modifier 25 Proposal Is the One That Reprices Your Schedule

CMS calls it "accounting for overlap between stand-alone E/M visits and global periods." In operation it is simpler than that: when a separately identifiable office or outpatient E/M visit is furnished on the same day as a procedure with a 0-, 10-, or 90-day global period, **the most expensive service is paid at 100% and every other service that day is paid at 50%**.

CMS's rationale is that same-day E/M visits reported with modifier 25 frequently share physician work and practice resources with the procedure performed at the same encounter, and that the current fee schedule therefore pays twice for one set of inputs. The argument is coherent. The financial effect on a practice that routinely sees and treats in one visit is severe, and it is not evenly distributed: **dermatology, otolaryngology, podiatry, ophthalmology, orthopedics, and several primary care specialties carry the largest exposure.**

This is a modeling exercise you can complete in an afternoon. Pull twelve months of claims. Filter to lines where an office or outpatient E/M was billed with modifier 25 alongside a 0-, 10-, or 90-day global procedure. For each of those encounters, identify the higher-allowed service, and halve everything else. The resulting number is your 2027 exposure under the proposal as written, and it is the number that belongs in your budget conversation this month — not after the final rule.

#### Skin Substitutes Move to Three Flat Tiers

CMS will establish a **three-tiered, flat-rate payment system for skin substitute products based on FDA regulatory classification**. Medicare currently pays for these products as incident-to supplies at a single 2026 rate of **$127.28 per square centimeter** across all care settings, with no reimbursement for discarded amounts.

Any wound care, podiatry, vascular, or dermatology practice with a skin substitute line needs to map its current product mix to the three FDA classification tiers before contracting for 2027 inventory. A product that sits in the lowest tier under the new methodology is a fundamentally different economic proposition than it was in 2026, and purchasing commitments signed this quarter will outlive the rate that justified them.

#### G2211 Stops Being a Code and Becomes a Modifier

The complexity add-on **G2211** — the code CMS created to recognize complex, longitudinal primary care — is proposed to convert from a standalone HCPCS code into a **modifier appended to the associated E/M base code**, and from a flat payment into a **percentage add-on: 16% of the base E/M, rising to 32% for practices participating in a qualifying ACO model**.

The doubling for ACO participants is the policy signal. CMS is no longer merely paying for continuity; it is paying twice as much for continuity delivered inside an accountable care arrangement. For an independent primary care practice that has been weighing ACO participation as an administrative burden with a speculative return, the 16-point spread is now a line item that can be multiplied by the practice's own G2211-eligible visit volume.

The mechanical change matters too. A modifier behaves differently from a code in nearly every practice management system: different edits, different claim-scrubber rules, different denial patterns. A practice appending 16% or 32% of its E/M revenue to a modifier it has never used before should be testing that path against its clearinghouse well before January.

**Sources:** [CMS — CY 2027 Physician Fee Schedule Proposed Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-proposed-rule) • [Federal Register — CMS-1848-P](https://www.federalregister.gov/documents/2026/07/16/2026-14327/medicare-and-medicaid-programs-cy-2027-payment-policies-under-the-physician-fee-schedule-and-other) • [AMA — 2027 Proposed Medicare Fee Schedule: What Physicians Need to Know](https://www.ama-assn.org/practice-management/medicare-medicaid/2027-proposed-medicare-fee-schedule-what-physicians-need-know) • [Coker — CMS Proposes Major Cuts to Modifier-25 Billing for 2027](https://www.cokergroup.com/insights/cms-2027-modifier-25-payment-cuts) • [HFMA — 2027 Medicare Primary Care Payment Changes](https://www.hfma.org/payment-reimbursement-and-managed-care/2027-medicare-primary-care-payment/) • [CMS — Modernizing Payment Accuracy and Cutting Spending Waste](https://www.cms.gov/newsroom/press-releases/cms-modernizes-payment-accuracy-significantly-cuts-spending-waste) • [Health Affairs Scholar — Reforming Medicare Payment for Skin Substitutes](https://academic.oup.com/healthaffairsscholar/article/4/7/qxag164/8715896)

---

## Section 02 — Prior Authorization / Payer Relations

### UnitedHealthcare Deletes 1,700 Prior Authorization Codes in 13 Days — Roughly 30% of Its Book, and the Most Under-Prepared Payer Change of the Year

On **October 1, 2026**, UnitedHealthcare eliminates prior authorization requirements on approximately **1,700 CPT codes** — by the insurer's own accounting, **roughly 30% of its total prior authorization requirements**. The change applies across **UnitedHealthcare commercial, Medicare Advantage, Community Plan (Medicaid), Individual Exchange, and Oxford plans**.

**Stat cards:**
- **1,700** — CPT codes losing UnitedHealthcare prior authorization on October 1, 2026
- **30%** — Share of UHC's total prior authorization requirements eliminated
- **13** — Days until the change takes effect
- **5** — UnitedHealthcare plan families affected: commercial, MA, Community, Exchange, Oxford

This is the largest single prior authorization reduction any national payer has executed, and it is not a pilot. The codes span **oncology, cardiology, orthopedic and musculoskeletal procedures, genetic and laboratory testing, chiropractic care, physical, occupational and speech therapy, home health, and durable medical equipment**. Named procedures include lesion excisions, fracture treatment, joint injections, arthroscopies, colonoscopies, endoscopies, biopsies, hernia repairs, and soft tissue tumor removals.

#### The Trap: Fewer Authorizations Is Not Fewer Verifications

Here is where practices will lose money on good news.

A code leaving UnitedHealthcare's prior authorization list does not mean that code is authorization-free. It means it is authorization-free **for the specific UnitedHealthcare plan variants covered by the memo**. The same CPT code may still require authorization under a delegated behavioral or musculoskeletal vendor arrangement, under a self-funded employer plan with a carve-out, under a state Medicaid managed care requirement layered on the Community Plan, or under any other payer in your contract portfolio.

The predictable failure mode is a front-desk team that hears "UnitedHealthcare dropped prior auth on arthroscopy" and stops checking arthroscopy authorization entirely — for every payer. The denials from that arrive in November, they are administrative, and they are almost entirely unappealable.

**Action Required:** Before October 1, pull the plan-specific code lists from the UnitedHealthcare Prior Authorization and Notification Tool for each of the five plan families you participate in — the lists differ. Update your payer matrix at the **code-and-plan** level, not the code level. Retrain the front desk on the distinction. Then monitor authorization-related denials weekly through November, segmented by payer, so you can see immediately whether the change is being over-applied.

#### The Standardization Track Underneath It

The 1,700-code cut is the visible part of a broader industry commitment. **Cigna expects to standardize more than 70% of its prior authorization volume for medical services by the end of 2026.** UnitedHealthcare states it already applies standardized prior authorization criteria to more than half of its reviews. Under the industry pledge signed by UnitedHealthcare, Aetna, Cigna, and Elevance, payers committed to reducing the volume of services requiring authorization, honoring existing approvals for 90 days when patients change plans, and clearly communicating denial rationale and appeal rights — with a common payer-provider framework targeted for **January 1, 2027**.

That date is not a coincidence. It is the same day the **CMS-0057-F** Prior Authorization API requirement takes effect, with its 7-calendar-day standard and 72-hour expedited decision clocks. The voluntary pledge and the federal mandate are converging on one deadline **105 days** from today.

#### And the Countervailing Track

Not every line moves the same direction. The **WISeR model** — CMS's AI- and machine-learning-assisted prior authorization pilot — remains active across **Arizona, New Jersey, Ohio, Oklahoma, Texas, and Washington**, covering **17 outpatient services** including skin and tissue substitutes, electrical nerve stimulators, and knee arthroscopy for osteoarthritis. On **July 16, 2026**, the Senate voted **46–50** against an effort to overturn it, leaving the model on track through its scheduled end date of **December 31, 2031**.

Note the overlap: knee arthroscopy is simultaneously losing commercial prior authorization at UnitedHealthcare and carrying an AI-assisted review requirement in traditional Medicare in six states. For an orthopedic practice in Phoenix or Houston, October 1 makes the payer mix, not the procedure, the determinant of whether an authorization is needed.

**Sources:** [UHCprovider.com — October 2026 Prior Authorization Reductions](https://www.uhcprovider.com/en/resource-library/news/2026/october-prior-auth-reductions.html) • [Healthcare Dive — UnitedHealthcare Cuts Prior Authorization From 1,700 Codes](https://www.healthcaredive.com/news/unitedhealthcare-prior-authorization-codes-cut-1700/829406/) • [Fierce Healthcare — UnitedHealthcare to Nix Prior Auth on 1,700 Services Oct. 1](https://www.fiercehealthcare.com/payers/unitedhealthcare-nix-prior-auth-1700-services-oct-1) • [Becker's Hospital Review — UnitedHealthcare to Drop Prior Authorization for 1,700 Services](https://www.beckershospitalreview.com/finance/unitedhealthcare-to-drop-prior-authorization-requirements-for-1700-services/) • [Becker's Spine Review — UnitedHealthcare Drops Some Prior Auth for Cardiology, Orthopedic Services](https://www.beckersspine.com/orthopedic/unitedhealthcare-drops-some-prior-auth-requirements-for-cardiology-orthopedic-services/) • [Fierce Healthcare — Payers Tout Progress on Standardizing Prior Authorization](https://www.fiercehealthcare.com/payers/unitedhealthcare-aetna-tout-progress-standardize-prior-authorization-part-industry-wide) • [CMS — WISeR Model](https://www.cms.gov/priorities/innovation/innovation-models/wiser) • [KFF — Examining the Potential Impact of Medicare's New WISeR Model](https://www.kff.org/medicare/examining-the-potential-impact-of-medicares-new-wiser-model/)

---

## Section 03 — AI & Automation Deep Dive

### The AI Taxonomy Becomes Billable Language: 10 New AI Codes Bring CPT to 43, Appendix S Splits Assistive From Augmentative — While 59% of Organizations Still Have No AI Anywhere in the Revenue Cycle

The AMA's **CPT 2027 release**, published this month, added **10 new AI-related codes**, bringing the total number of AI codes in CPT to **43**. Alongside them, the CPT Editorial Panel refreshed **Appendix S — the Taxonomy for Artificial Intelligence in Medical Services and Procedures** — effective **January 1, 2027**, sharpening the boundary between *assistive* and *augmentative* services and defining what qualifies as a clinically meaningful output.

**Stat cards:**
- **43** — Total AI-related CPT codes as of the 2027 code set, up 10
- **3** — Appendix S categories: assistive, augmentative, autonomous
- **59%** — Organizations that have not implemented AI or automation anywhere in the revenue cycle
- **2%** — Organizations reporting AI fully or mostly integrated across RCM operations

The three-tier taxonomy is worth learning precisely, because it is becoming the language payers use to decide what they will pay for:

| Category | Definition | Billing consequence |
|---|---|---|
| **Assistive** | Identifies clinically relevant data and surfaces it to the physician. No analysis. | Generally not separately reportable |
| **Augmentative** | Analyzes data to produce a clinically meaningful output the physician can act on | Increasingly the level at which discrete codes exist |
| **Autonomous** | Interprets data and makes recommendations | The category where new code creation is concentrated |

For a practice evaluating an AI vendor, the question to put in writing has changed. It is no longer "is this reimbursable." It is **"which Appendix S category does your product fall into, and which CPT code do you believe supports it."** A vendor that cannot answer that in one sentence is selling an efficiency tool, not a revenue tool — which may still be worth buying, but should be priced as a cost reduction rather than a new revenue line.

#### The Adoption Gap Is Wider Than the Conference Circuit Suggests

Set against a code set that now contains 43 AI codes, the deployment data is sobering. While three out of four healthcare executives report implementing or having used AI somewhere in their organization, **59% say they have not yet implemented AI or automation in the revenue cycle**, and just **2% report AI fully or mostly integrated across RCM operations**.

Innovaccer's 2026 *State of Revenue Lifecycle in Healthcare* report found **63% of organizations running AI in at least one workflow** and **52% having expanded implementations across departments**, with **45% having established some form of AI governance or ethics structure**. The gap between "running AI in at least one workflow" and "fully integrated across RCM" is the entire story of 2026: pilots are nearly universal, production is rare.

Independent corroboration comes from outside healthcare. Gartner expects **over 40% of agentic AI projects to be cancelled by the end of 2027**, and only **one in five organizations has a mature governance model** for autonomous agents. The failure mode is consistent across industries — pilots that cannot survive contact with production data.

#### Ambient Documentation Is the Exception That Proves the Rule

One category has escaped pilot purgatory. Voice-based ambient documentation was used by **29% of physicians surveyed in January 2026, up from 20% in April 2025**. Among Epic hospitals, **62.6% have adopted ambient AI**. Roughly one-third of healthcare providers now have access to an ambient scribe, and in **May 2026** ambient documentation went generally available for nurses across **250-plus U.S. health systems**. Among clinicians who use AI at all, **69% report daily use**, including **36% who use it multiple times a day**.

Ambient documentation succeeded where denial-management AI has stalled for a structural reason worth internalizing: it sits at the point of data creation, requires no payer cooperation, no integration with an adjudication system, and no governance committee to approve an autonomous financial decision. It improves the note, and a better note is the input to every downstream revenue cycle process. **Practices that cannot get an autonomous coding pilot funded should note that the highest-yield AI investment available to them may be upstream of coding entirely.**

#### On the Buy Side

**UF Health announced on September 9** a partnership with **R1** to deploy an AI-native revenue cycle operating model on R1's **Phare OS** platform, consolidating data management, payer intelligence, and AI-driven automation into a single system. Earlier in 2026, R1 partnered with clinical documentation platform **Heidi** to embed ambient documentation directly into its revenue operating system — the same upstream-of-coding logic, executed as a corporate strategy.

**The Automation Stack, September 2026:**
- **Generative AI** — Ambient documentation, appeal letter drafting, peer-to-peer synopsis generation, payer correspondence summarization
- **AI / Machine Learning** — Autonomous and computer-assisted coding, denial prediction and propensity scoring, medical necessity review, payment variance detection
- **RPA** — Eligibility verification, prior authorization submission and status checking, payment posting, claim status inquiry, statement cycles

**Sources:** [AMA — AMA Releases CPT 2027 Code Set](https://www.ama-assn.org/press-center/ama-press-releases/ama-releases-cpt-2027-code-set) • [AMA — CPT Appendix S: Taxonomy for Artificial Intelligence](https://www.ama-assn.org/practice-management/cpt/cpt-appendix-s-taxonomy-artificial-intelligence-medical-services-procedures) • [AMA — CPT Editorial Panel Strengthens AI Taxonomy](https://www.ama-assn.org/practice-management/cpt/cpt-editorial-panel-strengthens-ai-taxonomy-keep-pace-tech) • [Healthcare Finance News — New AMA CPT Codes Reflect Medical Innovation and AI-Related Services](https://www.healthcarefinancenews.com/news/new-ama-cpt-codes-reflect-medical-innovation-and-ai-related-services) • [Becker's — Hospital Revenue Cycle Teams Evolve as AI "Arms Race" Heats Up](https://www.beckershospitalreview.com/finance/hospital-revenue-cycle-teams-shift-as-ai-arms-race-heats-up/) • [Becker's — Why AI Is Failing in Revenue Cycle, and How to Fix It](https://www.beckershospitalreview.com/finance/why-ai-is-failing-in-revenue-cycle-and-how-to-fix-it/) • [Doximity — 2026 State of AI in Medicine Report](https://www.doximity.com/reports/state-of-ai-medicine-report/2026) • [AJMC — Ambient AI Tool Adoption in US Hospitals and Associated Factors](https://www.ajmc.com/view/ambient-ai-tool-adoption-in-us-hospitals-and-associated-factors) • [Healthcare Dive — New Mountain Combines Portfolio Companies to Launch AI Revenue Cycle Firm](https://www.healthcaredive.com/news/new-mountain-capital-creates-ai-revenue-cycle-management-company-smarter-technologies/748748/)

---

## Section 04 — Coding Updates

### Two Code Sets, Thirteen Days Apart and 105: FY 2027 ICD-10-CM Lands October 1, and CPT 2027 Publishes 453 Editorial Changes Including 80 Deletions

**Stat cards:**
- **13** — Days until FY 2027 ICD-10-CM takes effect, October 1, 2026
- **453** — Total CPT 2027 editorial changes: 299 new, 74 revised, 80 deleted
- **190** — New billable ICD-10-CM codes (238 total new entries including non-billable headers)
- **105** — Days until CPT 2027 takes effect, January 1, 2027

#### FY 2027 ICD-10-CM: Reconciling the Numbers Your Vendors Are Quoting

If three of your vendors have given you three different counts for the October 1 update, none of them is necessarily wrong. They are counting different things, and the difference matters operationally:

| Framing | Count | What it counts |
|---|---|---|
| New **billable** codes | **190** | Codes you can actually report |
| New **entries** in the code set | **238** | 190 billable plus 48 non-billable category headers |
| Codes **deleted** outright | **21** | Removed from the code set entirely |
| Codes **no longer reportable** | **30** | 21 deletions plus codes demoted to headers and other invalidations |
| **Revised** code titles | **4** | Descriptor changes only |

The number your charge templates care about is the third and fourth rows, not the first. **Deleted and demoted codes deny from day one.** A new code you fail to adopt costs you specificity; an invalid code left sitting in a template costs you the claim.

The effective date is governed by **date of service or discharge, not claim submission date**. Services through September 30 continue to use FY 2026 codes regardless of when you bill them.

#### The Demotions Are the Dangerous Part

The clearest example this year is cardiac. **I42.0 (Dilated cardiomyopathy)** stops being billable on October 1 and becomes a category header. It splits into:

- **I42.00** — Dilated cardiomyopathy, unspecified
- **I42.01** — Familial-genetic dilated cardiomyopathy
- **I42.09** — Other dilated cardiomyopathy

Any cardiology practice with I42.0 hard-coded in a problem list, a favorites list, or a charge template is generating invalid claims on October 1 unless it is remapped. The same pattern applies to BMI: **Z68.1 is deleted** and replaced by **Z68.18 (BMI 18.4 or less, adult)** and **Z68.19 (BMI 18.5–19.9, adult)** — a change that touches every primary care practice reporting low-BMI diagnoses for nutritional counseling or HCC capture. Among deletions, the **S23.42 sternoclavicular sprain series** is the most notable removal for orthopedics and urgent care.

Other areas of concentration: expanded specificity for secondary neoplasm sites, a revised exclusion note for breast carcinoma in situ, additional detail in cardiomyopathy and rare cardiac conditions, musculoskeletal specificity, and new codes for plantar fasciitis and sinusitis.

**Insight:** CMS publishes a **2027 Conversion Table** identifying every code inactive as of 10/1/2026 alongside its replacement. That file is the single most efficient remediation tool available, and it is free. Run your active diagnosis list against it, not against the new-code list.

#### CPT 2027: 80 Deletions Are the Line Item

The AMA released the **CPT 2027 code set** this month: **453 editorial changes — 299 new codes, 74 revisions, and 80 deletions** — effective **January 1, 2027**.

The 80 deletions deserve more attention than the 299 additions, because a deleted CPT code is a hard claim rejection and, where it is a bundled code, a contract renegotiation.

Substantive changes by area:

- **Maternity care** — The decades-old global obstetric bundle is replaced with a framework reflecting contemporary team-based practice. Every global maternity contract you hold needs to be repriced against the new structure.
- **Ventricular assist devices** — Three new codes for left ventricular assist device procedures
- **Hernia repair** — Nine new codes covering traumatic and non-traumatic diaphragmatic repairs
- **Prostate biopsy** — Updated codes and guidelines improving data specificity
- **Biofeedback** — Converted to a new time-based code structure
- **Radiology** — New codes plus a new head and neck MRA table
- **Sleep medicine** — Six new codes for unattended sleep studies
- **Artificial intelligence** — 10 new codes, bringing the CPT total to 43, with Appendix S refreshed

**Sources:** [AMA — AMA Releases CPT 2027 Code Set](https://www.ama-assn.org/press-center/ama-press-releases/ama-releases-cpt-2027-code-set) • [TechTarget — New 2027 CPT Codes Released as AMA Faces Mounting Criticism](https://www.techtarget.com/revcyclemanagement/news/366650230/New-2027-CPT-codes-released-as-AMA-faces-mounting-criticism) • [CMS — ICD-10 Codes](https://www.cms.gov/medicare/coding-billing/icd-10-codes) • [AAPC — Sneak a Peek at the 2027 ICD-10-CM Updates](https://www.aapc.com/blog/94184-sneak-a-peek-at-the-2027-icd-10-cm-updates/) • [AHCA/NCAL — CMS Posts FY 2027 ICD-10-CM Update Effective Oct. 1](https://www.ahcancal.org/News-and-Communications/Blog/Pages/CMS-Posts-FY-2027-ICD-10-CM-Update-Effective-Oct.-1.aspx) • [AGS Health — FY 2027 ICD-10-CM Code Updates: What Coders and Revenue Cycle Teams Need to Know](https://www.agshealth.com/blog/fy-2027-icd-10-cm-code-updates-what-coders-and-revenue-cycle-teams-need-to-know/) • [MedCentral — New ICD-10-CM Codes for 2027: Low BMI, Plantar Fasciitis and More](https://www.medcentral.com/coding-reimbursement/new-codes-for-low-bmi-plantar-fasciitis-sinusitis-and-more) • [CDC — ICD-10-CM Files](https://www.cdc.gov/nchs/icd/icd-10-cm/files.html)

---

## Section 05 — Revenue Velocity / KPIs

### The 24-Minute Problem Has a New Number: Electronic Prior Auth Adoption Hits 40% but Only 35% Is True X12 278 — and A/R Days Rose 2.4 at the Median

**Stat cards:**
- **40%** — Electronic prior authorization adoption rate
- **35%** — Share of medical prior authorizations conducted fully electronically via X12 278
- **$11.7B** — Additional annual savings available to the medical industry from full electronic adoption
- **+2.4** — Days added to median A/R in 2026, driven by MA prior authorization backlogs

The CAQH Index data — drawn from 600 organizations covering **63% of insured lives** — quantifies more than **$20 billion** in additional annual savings available from shifting remaining manual transactions to fully electronic workflows. Claim status inquiry has reached **81%** electronic adoption and claim payment **78%**. Prior authorization sits at **40%** — and the more revealing figure is that only **35% of medical prior authorizations are conducted fully electronically using the X12 278 transaction**.

That five-point gap between "electronic" and "fully electronic X12 278" is where most practices actually live. A payer portal is electronic in the sense that it is not a fax. It is not electronic in the sense that matters: it does not integrate, it does not populate from your practice management system, it cannot be worked in a queue, and it consumes a staff member's full attention for its duration. **Portal work is manual work with a browser.**

#### A/R Days Moved the Wrong Direction

In 2026, **A/R days trended up by 2.4 days at the industry median**, driven by Medicare Advantage prior authorization backlogs and pended claims awaiting medical record review. This is the operational counterweight to the prior authorization good news in Section 02 — the volume of authorizations is starting to fall, but the ones that remain are taking longer and dragging cash with them.

Denials remain elevated: **41% of providers now report a claim denial rate above 10%**, against an HFMA top-quartile target of under 5% and a published industry average of 9–12%.

#### Where You Should Be — 2026 KPI Targets

| Metric | Industry average | Target | Top quartile |
|---|---|---|---|
| Days in A/R | 40–45 | **< 35** | < 30 |
| A/R > 90 days | 18–22% | **< 15%** | < 10% |
| First-pass clean claim rate | 90–93% | **≥ 95%** | 97%+ |
| First-pass denial rate | 9–12% | **< 8%** | < 5% |
| Denial overturn rate | 40–55% | **> 65%** | > 85% |
| Net collection rate | 93–95% | **≥ 96%** | 98%+ |
| Cost to collect | 3–5% of net revenue | **< 3.5%** | < 2.5% |
| Electronic prior auth (X12 278) | 35% | **≥ 75%** | 90%+ |
| Pre-service patient collection share | 21% | **≥ 30%** | 40%+ |
| Patient bad debt | 3–5% of net patient revenue | **< 3%** | < 2% |

Note the distinction between the third and fourth rows, because practices routinely conflate them. **Clean claim rate measures whether a claim passes your edits before submission. First-pass yield measures whether it gets paid on first submission.** A claim can be perfectly clean and still deny for eligibility, medical necessity, or a payer-specific rule your scrubber does not know about. A high clean claim rate sitting on top of a low first-pass yield is a diagnostic finding, not a contradiction: it means your edits are checking format and your payers are denying on substance.

#### The Two Interventions With the Best Documented Return

**Move eligibility verification to scheduling.** Practices that run real-time eligibility at scheduling rather than at check-in **reduce eligibility-related denials by over 40%**. The mechanism is lead time, not technology: verifying 24 to 48 hours ahead creates room to fix a coverage problem before the visit instead of after the claim. Practices on AI-integrated billing platforms report up to a **30% increase in first-pass acceptance** versus manual scrubbing.

**Collect before the visit.** Health systems reported collecting **31% of total patient billings in 2026, up from 24% in 2025**, with pre-service collections rising from **16% to 21%** of self-pay collections. **91.5% of surveyed organizations now encourage payment, require payment, or capture a payment method on file during the estimate process, up from 81.3%** a year earlier. The urgency is arithmetic: patient responsibility is now **30–35% of total revenue**, a balance over **90 days has under a 50% chance of collection**, and past **120 days that falls to 20% or less**.

**Sources:** [CAQH — 2025 CAQH Index](https://www.caqh.org/) • [CAQH CORE — A Guide for Implementing Prior Authorization Requirements](https://www.caqh.org/hubfs/CORE%20-%20Prior%20Authorization%20Whitepaper_062124-2.pdf) • [HFMA — Health Systems Boost Front-End Collections](https://www.hfma.org/fast-finance/health-systems-boost-front-end-collections/) • [MGMA/HFMA benchmarks via Clinic Finance Benchmarks 2026](https://www.thesorso.com/state-of-clinic-finances-2026) • [Inovalon — Clean Claim Rate vs. First Pass Yield](https://www.inovalon.com/blog/first-pass-yield-vs-clean-claim-rate/) • [Plutus Health — RCM KPI Guide 2026](https://www.plutushealthinc.com/post/revenue-cycle-management-kpi) • [Healthcare Finance News — Payer Denials and Prior Authorization Delays Are Top RCM Concerns](https://www.healthcarefinancenews.com/news/payer-denials-and-prior-authorization-delays-are-top-rcm-concerns) • [Cedar — Self-Pay Collections: What "Good" Looks Like](https://www.cedar.com/blog/why-self-pay-collections-matter-what-good-looks-like)

---

## Section 06 — Technology Spotlight

### Waystar Tops the 2026 KLAS Suites Report as a $189B Market Heads to $505B and 70% of Systems Plan to Outsource More

**Stat cards:**
- **$189.28B** — Healthcare RCM market size in 2026
- **$505.8B** — Projected 2035 market size, an 11.54% CAGR
- **70%** — Hospitals and health systems planning to expand RCM outsourcing
- **9** — Best in KLAS categories awarded in revenue cycle technology for 2026

KLAS Research published **"Revenue Cycle Management Suites 2026: Partnership Is Key in Making the Suite Experience a Success"** in July, evaluating how *deep adopters* — organizations running three or more distinct RCM modules from a single vendor — actually experience their vendors. **Waystar led on overall satisfaction.** Across the broader 2026 Best in KLAS awards, **Abridge, Microsoft, Waystar, and FinThrive** took honors across **nine revenue cycle technology categories**.

The most useful finding in the KLAS report is not the ranking. It is the diagnosis: **many RCM suites were assembled rapidly through acquisition**, leaving customers with inconsistent product integration, uneven software maturity, and variable support quality across modules sold as one platform. The report's framing — that partnership, not feature count, determines whether a suite succeeds — is a direct consequence of that assembly history.

For a practice evaluating a suite, that converts into a specific diligence question: **for each module you are buying, when did the vendor acquire it, and what is the current state of its integration with the core platform?** A five-module suite where three modules were acquired in the last thirty-six months is three separate implementations wearing one contract.

#### Market Size and the Outsourcing Decision

The healthcare RCM market is projected to grow from **$189.28 billion in 2026 to $505.8 billion by 2035**, an **11.54% CAGR**. The outsourcing segment specifically was valued at **$61.7 billion in 2025** and is expected to reach **$126.5 billion by 2032**, a **10.8% CAGR** — and **70% of hospitals and health systems plan to expand their RCM outsourcing engagements**. Industry estimates put the potential annual savings from AI and automation in the revenue cycle at up to **$360 billion**.

Treat the $360 billion figure as a market-sizing number, not a budget input. The operational figures in Section 05 — a 40% reduction in eligibility denials from moving verification to scheduling, a 30% lift in first-pass acceptance — are the ones you can actually underwrite.

#### Vendors and Platforms in the News

- **Suites and clearinghouse** — Waystar, FinThrive, R1, Availity, Change Healthcare/Optum, Experian Health
- **Autonomous and computer-assisted coding** — CodaMetrix, Nym, AKASA, Maverick Medical AI, AGS Health
- **Ambient documentation** — Abridge, Heidi, Microsoft/Nuance, Suki
- **Denials, appeals, and payer intelligence** — Adonis, Candid Health, Xsolis, Aspirion, EnableComp
- **Practice-scale platforms** — athenahealth, Tebra, Quadax, Inovalon, Cedar

#### On the Calendar

**Becker's 11th Annual Health IT + Digital Health + RCM Conference** ran **September 14–17 in Chicago**, closing yesterday, with **560-plus hospital and health system speakers** and over **90% of sessions led by provider-side leaders**. The agenda's center of gravity is itself a data point: sessions titled *"From Pilot to Production: Real-World Lessons on Scaling AI in Revenue Cycle"* and *"From Reactive to Proactive: How AI Is Redefining Revenue Integrity"* reflect an industry that has stopped asking whether to adopt AI and started asking why its pilots will not scale — the same question the 2% integration figure in Section 03 answers from the other direction.

**Sources:** [KLAS Research — Revenue Cycle Management Suites 2026](https://klasresearch.com/report/revenue-cycle-management-suites-2026-partnership-is-key-in-making-the-suite-experience-a-success/3849) • [HIT Consultant — KLAS 2026 RCM Suites Report: Waystar Leads in Overall Satisfaction](https://hitconsultant.net/2026/07/22/klas-2026-revenue-cycle-management-suites-report-insights/) • [TechTarget — Abridge, Microsoft Earn Top Spots for Revenue Cycle Tech](https://www.techtarget.com/revcyclemanagement/news/366638784/Abridge-Microsoft-earn-top-spots-for-revenue-cycle-tech) • [Towards Healthcare — Healthcare Revenue Cycle Management Market Sizing](https://www.towardshealthcare.com/insights/healthcare-revenue-cycle-management-market-sizing) • [Reanin — RCM Outsourcing Market Insights](https://www.reanin.com/reports/revenue-cycle-management-outsourcing-market) • [Auxis — 2026 Healthcare Revenue Cycle Management Trends](https://www.auxis.com/2026-healthcare-revenue-cycle-management-trends/) • [Becker's — 385+ Revenue Cycle Management Companies to Know, 2026](https://www.beckershospitalreview.com/finance/revenue-cycle-management/385-revenue-cycle-management-companies-to-know-2026/) • [Becker's Healthcare — Health IT + Digital Health + RCM Conference 2026 Agenda](https://conferences.beckershospitalreview.com/hit_rcm_2026/agenda)

---

## Section 07 — Compliance Corner

### Price Transparency Enforcement Passes Its Sixth Month, Four FHIR APIs Come Due in 105 Days, and WISeR Clears Its Senate Challenge

**Stat cards:**
- **105** — Days until the CMS-0057-F FHIR API deadline, January 1, 2027
- **4** — Required APIs: Patient Access, Provider Access, Payer-to-Payer, Prior Authorization
- **7 days / 72 hours** — Mandated decision clocks for standard and expedited prior authorization
- **~5.5** — Months of active enforcement of the updated price transparency requirements

#### The API Deadline That Is Not Yours, and Depends On You Anyway

**CMS-0057-F** requires impacted payers to operate **four FHIR APIs by January 1, 2027**: Patient Access, Provider Access, Payer-to-Payer, and Prior Authorization. The Prior Authorization API standardizes electronic submission and response, replacing fax, portal, and phone, with **standard decisions required within 7 calendar days and expedited decisions within 72 hours**.

The technical stack is **HL7 FHIR R4, OAuth 2.0 / OpenID Connect, the Da Vinci implementation guides (CRD, DTR, PAS), and SMART on FHIR** for EHR-embedded workflows. The rule binds Medicare Advantage organizations, Medicaid and CHIP managed care plans, state Medicaid and CHIP fee-for-service programs, and QHP issuers on the federally facilitated exchanges. Note the staggered compliance dates: MA, Medicaid and CHIP managed care, and QHP issuers were obligated as of **January 1, 2026**; state Medicaid and CHIP fee-for-service programs have until **January 1, 2027**.

**Your practice has no obligation under this rule, and therefore no deadline — which is exactly why it gets missed.** The mandate lands on your payers. The benefit only reaches you if your EHR or practice management system can consume the Prior Authorization API. If it cannot, your payers will have eliminated the fax while you continue to use the portal, and you will have paid for none of the savings and received none of them either.

Combine this with Section 02: UnitedHealthcare's voluntary 1,700-code reduction on October 1 and the industry pledge's January 1, 2027 framework target converge on the same date as the federal API mandate. Prior authorization in 2027 will involve fewer transactions, moving faster, over a standardized pipe. A practice still working authorizations through browser tabs in February will be the slowest party in its own revenue cycle.

#### Price Transparency: Enforcement, Not Guidance

Enforcement of the updated Hospital Price Transparency requirements finalized in the **CY 2026 OPPS/ASC final rule** began **April 1, 2026** — roughly five and a half months ago. The regulations became effective January 1, 2026, with CMS delaying enforcement one quarter to allow hospitals to update machine-readable files and related compliance processes.

The updates represent the most comprehensive change to price transparency since the rule's inception, moving it from a basic disclosure obligation toward a standardized, data-driven pricing framework. The direct obligation sits with hospitals, but physician practices with any hospital-affiliated, provider-based, or joint-venture ASC arrangement should confirm which entity owns the machine-readable file for services rendered under that arrangement — and that the rates published in it match the rates in your own contracts. A mismatch between a published MRF and a negotiated rate is a discoverable fact.

#### The Rest of the Compliance Calendar

| Item | Date | Who it binds |
|---|---|---|
| FY 2027 ICD-10-CM effective | October 1, 2026 | All providers |
| UnitedHealthcare prior auth reductions | October 1, 2026 | UHC-contracted practices |
| CY 2027 PFS final rule expected | Early November 2026 | All Medicare providers |
| CPT 2027 and Appendix S effective | January 1, 2027 | All providers |
| CMS-0057-F four FHIR APIs | January 1, 2027 | Impacted payers |
| Industry prior auth framework target | January 1, 2027 | Pledge signatory payers |
| WISeR model runs through | December 31, 2031 | AZ, NJ, OH, OK, TX, WA |

**Sources:** [CMS — Interoperability and Prior Authorization Final Rule CMS-0057-F](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) • [PilotFish — CMS-0057-F Compliance Fact Sheet](https://healthcare.pilotfishtechnology.com/cms-0057-f-compliance-fact-sheet/) • [Health Samurai — Understanding the CMS-0057-F Interoperability and Prior Authorization Final Rule](https://www.health-samurai.io/articles/understanding-the-cms-0057-f-interoperability-and-prior-authorization-final-rule) • [CMS — Hospital Price Transparency](https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency) • [Dentons — CMS Enforcement of Updated Hospital Price Transparency Requirements Begins April 1, 2026](https://www.dentonshealthlaw.com/cms-enforcement-of-updated-hospital-price-transparency-requirements-to-begin-on-april-1-2026/) • [HFMA — CMS's Latest Transparency Rule Aims to Make Price Estimates More Exact](https://www.hfma.org/price-transparency/cmss-latest-transparency-rule-aims-to-make-price-estimates-more-exact/) • [CMS — WISeR Model](https://www.cms.gov/priorities/innovation/innovation-models/wiser)

---

## Section 08 — Independent Practice Watch

### 89% Say Staying Independent Got Harder — Against Medicare Payment Up 10% and Practice Costs Up 63% Since 2001

**Stat cards:**
- **89%** — Physicians saying staying independent has become harder (athenahealth 2026 Physician Sentiment Survey)
- **88%** — Same answer among practices with five or fewer physicians
- **+10% vs +63%** — Medicare physician payment growth vs. practice cost growth, 2001–2026
- **−33%** — Inflation-adjusted decline in Medicare physician payment since 2001

The structural arithmetic underneath every consolidation headline has not changed, and this year it is unusually clean. Between **2001 and 2026, Medicare physician payment rose approximately 10% while the cost of running a medical practice rose approximately 63%**, according to AMA analysis. Adjusted for practice cost inflation, **Medicare physician payment has declined roughly 33% since 2001**.

In athenahealth's **2026 Physician Sentiment Survey**, **89% said staying independent has become harder** — including **88% of physicians in practices with five or fewer physicians**. A separate survey found **80% of independent primary care physicians worried about money, yet only 2% considering leaving independence**. Those two findings are not in tension; they describe the same population under strain and unwilling to sell. The financial pressure is nearly universal. The willingness to consolidate is not.

#### How This Week's News Lands Differently on a Small Practice

**The modifier 25 proposal is regressive by structure.** A large multispecialty group can absorb a 50% haircut on same-day secondary services across a diversified service mix. A three-physician dermatology or podiatry practice — where see-and-treat in one visit *is* the business model — cannot diversify away from it. The specialties CMS's own impact analysis shows taking the largest reductions are disproportionately small-practice specialties.

**The UnitedHealthcare prior auth reduction is progressive, and only if you can operationalize it.** The 1,700-code change is worth real staff hours to a small practice — proportionally more than to a health system, because authorization work is a larger share of a small practice's total administrative load. But capturing it requires pulling five plan-specific code lists, updating a payer matrix at the code-and-plan level, and monitoring denials weekly. A health system has a payer-relations department that does this as routine work. A five-physician practice has an office manager who also handles payroll. **The benefit is larger and the capacity to capture it is smaller.**

**The CMS-0057-F API mandate has the same shape.** A large group can require its EHR vendor to deliver FHIR integration on a contractual timeline. An independent practice on a small-vendor platform can ask, and wait.

**The G2211 ACO doubling is the one clear opportunity.** A 16% add-on becoming 32% inside a qualifying ACO is the largest single upside available to independent primary care in the 2027 proposal, and it is the one lever a small practice can actually pull without vendor cooperation, capital, or payer consent.

#### Where You Should Be — Independent Practice Benchmarks

| Metric | Where most independents are | Where you should be |
|---|---|---|
| Days in A/R | 42–50 | **< 35** |
| First-pass clean claim rate | 88–92% | **≥ 95%** |
| Denial rate | 10–14% | **< 8%** |
| Denial overturn rate | 35–50% | **> 65%** |
| Electronic prior auth (X12 278) | < 35% | **≥ 75%** |
| Pre-service collection share | 12–18% | **≥ 30%** |
| Cost to collect | 5–8% of net revenue | **< 4%** |
| Administrative FTEs per physician | 2.5–3.0 | **< 2.0** |
| Payer matrix review cadence | Annual or ad hoc | **Monthly** |

**What to prioritize next, in order:** (1) run the modifier 25 exposure model against twelve months of your own claims — it is free and it is the largest 2027 variable; (2) remediate deleted and demoted ICD-10 codes before October 1; (3) build the UnitedHealthcare code-and-plan matrix; (4) if you are primary care and not in an ACO, price the 32% G2211 add-on against your eligible visit volume.

**Sources:** [athenahealth/Forbes — Why Medicare's Payment System Wasn't Built for Independent Practices](https://www.forbes.com/sites/athenahealth/2026/07/16/why-medicares-payment-system-wasnt-built-for-independent-practices/) • [Medical Economics — 80% of Independent PCPs Are Worried About Money; Only 2% Are Considering Leaving](https://www.medicaleconomics.com/view/80-of-independent-pcps-are-worried-about-money-only-2-are-considering-leaving-) • [Medical Economics — Why Payment Policy, Not Ownership Structure, Is Driving Practice Consolidation](https://www.medicaleconomics.com/view/why-payment-policy-not-ownership-structure-is-driving-practice-consolidation) • [Medical Economics — Hospital Takeovers of Physician Practices Tied to Higher Prices](https://www.medicaleconomics.com/view/hospital-takeovers-of-physician-practices-tied-to-higher-prices-threaten-patient-access-report-finds) • [AMA — 2027 Proposed Medicare Fee Schedule: What Physicians Need to Know](https://www.ama-assn.org/practice-management/medicare-medicaid/2027-proposed-medicare-fee-schedule-what-physicians-need-know) • [DoctorsManagement — The 2026 Private Practice Playbook: Surviving Margin Compression](https://www.doctorsmanagement.com/blog/the-2026-private-practice-playbook-how-independent-groups-are-surviving-margin-compression/) • [HFMA — 2027 Medicare Primary Care Payment Changes](https://www.hfma.org/payment-reimbursement-and-managed-care/2027-medicare-primary-care-payment/)

---

## Section 09 — Specialty RCM Spotlight

### Dermatology and ENT at −9%, Orthopedics −7%, Hem/Onc −1.5%, Cardiology +1% — and Nearly Every One of Them Gets Prior Auth Relief on October 1

Two things happen to most specialties in the next 105 days, and they point in opposite directions: a proposed CY 2027 payment impact, and a prior authorization reduction on October 1. Read them together — an authorization burden lifted does not offset a rate cut, but it does change where your staff hours go.

| Specialty | CY 2027 proposed impact | What else changes | Priority action |
|---|---|---|---|
| **Primary Care** | Net positive via G2211 | G2211 converts to a **modifier** paying **16% of base E/M, 32% in a qualifying ACO**; **Z68.1 deleted** → Z68.18 / Z68.19 for low BMI | Price the 32% ACO add-on against eligible visit volume; remap BMI codes before October 1 |
| **Cardiology** | **~+1%** overall | **I42.0 becomes non-billable** → I42.00 / I42.01 / I42.09; UHC drops PA on cardiology codes Oct 1; 3 new LVAD codes in CPT 2027 | Remap I42.0 everywhere it is hard-coded; pull the UHC cardiology code list |
| **Orthopedics** | **−7%** (hand surgery **−5%**) | UHC drops PA on arthroscopies, fracture care, joint injections, soft tissue tumor removal; **S23.42 sternoclavicular sprain series deleted**; knee arthroscopy still under **WISeR** in 6 states | Model modifier 25 exposure on same-day injection + E/M; separate UHC from WISeR logic by payer |
| **Oncology** | **Hem/onc −1.5%**; radiation oncology **+1.5% to +3%** depending on which read of the impact table you use | UHC drops PA on oncology codes Oct 1; new ICD-10 specificity for **secondary neoplasm sites** | Update secondary neoplasm coding; verify which oncology codes left the UHC list |
| **Dermatology** | **−9%** — among the largest proposed reductions | Highest modifier 25 exposure of any specialty; **skin substitutes move to 3 flat FDA-based tiers** | Run the modifier 25 model first; re-tier the skin substitute product mix before 2027 purchasing |
| **Otolaryngology** | **−9%** | Significant modifier 25 exposure; new ICD-10 **sinusitis** codes effective October 1 | Model same-day procedure + E/M encounters; update sinusitis coding |
| **Radiology** | **Interventional radiology +3%** | CPT 2027 adds radiology codes and a new **head and neck MRA table**; UHC drops PA on imaging codes Oct 1 | Load the new MRA table; confirm which imaging codes left the UHC PA list |
| **Gastroenterology** | Carries the **2.5% efficiency adjustment** to work RVUs on endoscopy and other non-time-based codes | UHC drops PA on **colonoscopy and endoscopy** Oct 1 | Recalculate endoscopy margin post-adjustment; update scheduling scripts that reference authorization |
| **Neurology** | Smaller proposed decrease | Denial rates average **18%** — roughly double the 9–12% industry average | Segment the 18% by root cause before buying any denial tool |
| **Mental / Behavioral Health** | **Clinical psychologists and clinical social workers among the largest proposed increases** | Digital prescription therapeutics billable incident-to; in-person requirements for tele-mental health enforced since January 31, 2026 | Verify in-person compliance documentation; evaluate digital therapeutic billing |
| **Physical / Occupational Therapy** | Smaller proposed increases | UHC drops PA on PT, OT, and speech therapy codes Oct 1 | Re-scope authorization staffing after October 1 |
| **Obstetrics** | Framework change rather than rate change | CPT 2027 **replaces the global maternity bundle** with a team-based framework | Reprice every global maternity contract before January 1 |

The single cross-cutting observation: **the specialties facing the deepest proposed cuts — dermatology at −9%, ENT at −9%, orthopedics at −7% — are also the specialties with the heaviest modifier 25 exposure.** The impact tables and the same-day E/M proposal are not independent risks. They compound, and CMS's published impact percentage may understate the effect on a practice whose visit pattern is procedure-plus-E/M by default.

**Sources:** [HFMA — CY 2027 Physician Fee Schedule Proposed Specialty Impact Tables](https://www.hfma.org/payment-reimbursement-and-managed-care/cy-2027-physician-fee-schedule-proposed-specialty-impact-tables/) • [ASCO — 1.5% Reimbursement Cut for Medicare Physician Services Proposed for 2027](https://www.asco.org/news-initiatives/policy-news-analysis/medicare-physician-reimbursement-cut-proposed-2027) • [American College of Cardiology — CMS Releases 2027 Medicare Physician Fee Schedule Proposed Rule](https://www.acc.org/Latest-in-Cardiology/Articles/2026/07/14/21/36/cms-releases-2027) • [ECG Management Consultants — CMS Issues CY 2027 Medicare PFS Proposed Rule](https://www.ecgmc.com/insights/blog/cms-issues-cy-2027-medicare-physician-fee-schedule-proposed-rule) • [Becker's Spine Review — UnitedHealthcare Drops Some Prior Auth for Cardiology, Orthopedic Services](https://www.beckersspine.com/orthopedic/unitedhealthcare-drops-some-prior-auth-requirements-for-cardiology-orthopedic-services/) • [American College of Gastroenterology — 2026 Payment Shifts](https://gi.org/2026/02/27/2026-payment-shifts/) • [Neolytix — Neurology Billing and Coding Guide 2026](https://neolytix.com/billing-coding-guides/neurology-medical-billing-coding-guide/) • [AMA — AMA Releases CPT 2027 Code Set](https://www.ama-assn.org/press-center/ama-press-releases/ama-releases-cpt-2027-code-set) • [MedCentral — New ICD-10-CM Codes for 2027](https://www.medcentral.com/coding-reimbursement/new-codes-for-low-bmi-plantar-fasciitis-sinusitis-and-more)

---

## Section 10 — This Week's Action Items

### Ten Moves for the Week of September 18, 2026

1. **Run the modifier 25 exposure model — this is the highest-value hour of your quarter.** Pull twelve months of claims, filter to office/outpatient E/M billed with modifier 25 alongside a 0-, 10-, or 90-day global procedure, pay the highest-allowed service at 100% and halve everything else. That number is your CY 2027 exposure as proposed. The comment window is closed; the modeling window is not.

2. **Remediate deleted and demoted ICD-10 codes before October 1 — 13 days.** Run your active diagnosis list against the CMS 2027 Conversion Table, not the new-code list. Start with **I42.0** (now a non-billable header → I42.00 / I42.01 / I42.09), **Z68.1** (→ Z68.18 / Z68.19), and the **S23.42** sternoclavicular sprain series. An invalid code in a template denies from day one.

3. **Pull all five UnitedHealthcare plan-specific prior authorization code lists.** Commercial, Medicare Advantage, Community Plan, Individual Exchange, and Oxford each have their own list, and they differ. Update your payer matrix at the **code-and-plan** level.

4. **Retrain the front desk on the distinction between "UHC dropped it" and "nobody requires it."** The 1,700-code reduction applies only to specified UnitedHealthcare plan variants. Other payers, delegated vendors, carve-outs, and state Medicaid rules are unaffected. Then monitor authorization denials weekly through November, segmented by payer, to catch over-application early.

5. **If you are primary care and not in an ACO, price the 32% G2211 add-on.** G2211 becomes a modifier paying 16% of the base E/M — **32% inside a qualifying ACO**. Multiply the 16-point spread by your eligible visit volume. That is the clearest upside in the 2027 proposal for independent primary care, and it requires no vendor and no capital.

6. **Ask your EHR vendor in writing for a CMS-0057-F consumption date.** Four payer FHIR APIs come due **January 1, 2027 — 105 days**. You have no obligation and therefore no deadline, which is precisely why this slips. If your system cannot consume the Prior Authorization API, fax elimination happens around you.

7. **Separate clean claim rate from first-pass yield in your monthly KPI package.** They measure different failures. A high clean claim rate atop a low first-pass yield means your edits check format while your payers deny on substance — and it tells you to invest in eligibility and medical necessity, not in more scrubber rules.

8. **Move eligibility verification from check-in to scheduling.** Verifying 24–48 hours ahead **reduces eligibility-related denials by over 40%**. This is a workflow change, not a purchase.

9. **Put a number on the pre-service collection gap.** Industry pre-service collection has risen from 16% to 21% of self-pay, and **91.5% of organizations now request payment or a card on file at estimate**. With patient responsibility at 30–35% of revenue and sub-50% collectability past 90 days, this is the fastest-moving line in the cycle.

10. **If you bill obstetrics or skin substitutes, open contract conversations now.** The CPT 2027 global maternity bundle is replaced January 1, and skin substitutes move to three flat FDA-classification tiers. Both reprice agreements you are signing this quarter. Model your own number before the payer's crosswalk arrives.

**Sources:** [CMS — CY 2027 PFS Proposed Rule Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-proposed-rule) • [Coker — CMS Proposes Major Cuts to Modifier-25 Billing for 2027](https://www.cokergroup.com/insights/cms-2027-modifier-25-payment-cuts) • [CMS — ICD-10 Codes](https://www.cms.gov/medicare/coding-billing/icd-10-codes) • [UHCprovider.com — October 2026 Prior Authorization Reductions](https://www.uhcprovider.com/en/resource-library/news/2026/october-prior-auth-reductions.html) • [Healthcare Dive — UnitedHealthcare Cuts Prior Authorization From 1,700 Codes](https://www.healthcaredive.com/news/unitedhealthcare-prior-authorization-codes-cut-1700/829406/) • [HFMA — 2027 Medicare Primary Care Payment Changes](https://www.hfma.org/payment-reimbursement-and-managed-care/2027-medicare-primary-care-payment/) • [CMS — Interoperability and Prior Authorization Final Rule CMS-0057-F](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) • [Inovalon — Clean Claim Rate vs. First Pass Yield](https://www.inovalon.com/blog/first-pass-yield-vs-clean-claim-rate/) • [HFMA — Health Systems Boost Front-End Collections](https://www.hfma.org/fast-finance/health-systems-boost-front-end-collections/) • [AMA — AMA Releases CPT 2027 Code Set](https://www.ama-assn.org/press-center/ama-press-releases/ama-releases-cpt-2027-code-set)

---

## The Big Stat

# 1,700 Codes

**Roughly 30% of one national payer's entire prior authorization book, deleted in a single day — 13 days from now.** On October 1, 2026, UnitedHealthcare eliminates prior authorization on approximately **1,700 CPT codes** across its commercial, Medicare Advantage, Community Plan, Individual Exchange, and Oxford plans — lesion excisions, fracture treatment, joint injections, arthroscopies, colonoscopies, endoscopies, biopsies, hernia repairs, soft tissue tumor removals, genetic and lab testing, chiropractic care, therapy services, home health, and DME. It is the largest single prior authorization reduction a national payer has executed, and it arrives alongside Cigna's commitment to standardize **more than 70%** of its medical prior authorization volume by year end and a federal mandate putting **four FHIR APIs** in production on January 1. The administrative burden that has defined the last decade of practice management is, measurably, beginning to recede. And the practices that will capture the least of it are the ones that treat this as good news rather than as a project — because a code leaving UnitedHealthcare's list is still on somebody else's, and the only thing worse than an authorization you did not need is a denial for one you did.

---

**RCM Pulse Weekly** — Revenue Cycle Management Intelligence for Medical Practices

Researched and compiled from public domain sources including CMS.gov, the Federal Register, AMA, AAPC, CAQH, MGMA, HFMA, ASCO, ACC, ACG, KFF, KLAS Research, athenahealth, Becker's Healthcare, Medical Economics, Fierce Healthcare, Healthcare Dive, TechTarget, and payer policy portals.

Volume 9, Issue 3 • September 18, 2026 • **Next issue: September 25, 2026**
