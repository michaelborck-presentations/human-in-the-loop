---
format:
  html:
    embed-resources: true
  pdf: default
--- 

# Humans in the Loop: Frequently Asked Questions

**Resource companion to the "Why Your AI Needs a Co-Pilot" presentation**

---

## Table of Contents

- [Understanding AI Basics](#understanding-ai-basics)
- [The Three-Level Framework](#the-three-level-framework)
- [Implementation & Getting Started](#implementation--getting-started)
- [Cost & ROI](#cost--roi)
- [Technical Questions](#technical-questions)
- [Organizational & People](#organizational--people)
- [Mining-Specific Applications](#mining-specific-applications)
- [Risk & Governance](#risk--governance)
- [Choosing Solutions](#choosing-solutions)

---

## Understanding AI Basics

### What exactly is AI, and how does it differ from traditional software?

Traditional software follows explicit rules that programmers write: "If X happens, do Y." AI systems learn patterns from data and can handle situations they weren't explicitly programmed for. 

For example, a traditional dispatch system might use a fixed algorithm: "Assign the closest available truck." An AI dispatch system learns from thousands of historical assignments to optimize for multiple factors simultaneously—distance, truck capacity, operator skill, fuel levels, traffic patterns—and adapts as conditions change.

Think of traditional software as following a recipe exactly, while AI is more like a chef who's learned from watching thousands of meals being prepared and can adapt to available ingredients.

### What's the difference between AI, Machine Learning, and Deep Learning?

**AI (Artificial Intelligence)** is the umbrella term for any system that performs tasks requiring human-like intelligence—recognizing patterns, making predictions, understanding language.

**Machine Learning (ML)** is a subset of AI where systems learn from data rather than being explicitly programmed. Most practical AI applications today use ML.

**Deep Learning** is a subset of ML that uses neural networks with multiple layers. It's particularly good at handling unstructured data like images, audio, and text.

**For practical purposes in mining:** You don't need to know which specific technique is being used. You need to know what the system can do, how accurate it is, and where humans should oversee it.

### What are Large Language Models (LLMs)?

LLMs are AI systems trained on massive amounts of text data that can understand and generate human language. ChatGPT, Claude, and similar tools are LLMs.

**What makes them revolutionary:** They can read unstructured text (reports, emails, procedures), extract key information, answer questions in plain English, and generate coherent summaries or analyses.

**In mining contexts:** LLMs can analyze shift reports, summarize safety incidents, answer questions about geological data, draft routine documents, and help non-technical managers explore data using natural conversation rather than SQL queries or specialized software.

### What are "agentic workflows" or "AI agents"?

An **agent** is an AI system that can take actions, not just make predictions or recommendations. 

A **non-agentic AI** might analyze sensor data and display "High vibration detected on Truck 47."

An **agentic AI** might detect the vibration, check the maintenance schedule, identify that this truck is due for service anyway, find an available maintenance slot tomorrow afternoon, and automatically generate a work order.

**Agentic workflows** are when multiple AI agents coordinate to accomplish complex tasks. For example: predictive maintenance AI flags equipment → inventory management AI checks parts availability → scheduling AI finds optimal service window → work order AI notifies maintenance team → all automatically.

**Why it matters:** Agentic systems can handle entire workflows autonomously, but they require very careful design of boundaries and oversight. This is where the "Human-in-Command" level of the framework becomes critical.

### Is AI the same as automation?

Not exactly. Automation executes fixed, pre-programmed tasks. AI can adapt and learn.

**Traditional automation:** "When temperature exceeds 85°C, trigger an alarm." The rule is fixed.

**AI:** "Learn what normal temperature patterns look like for this equipment under different conditions, and flag anomalies." The system adapts based on data.

Many mining operations have used automation for decades (automated crushing circuits, ventilation control). AI takes automation further by adding learning and adaptation capabilities.

---

## The Three-Level Framework

### Can you explain the three levels of human oversight more simply?

**Level 1 - Human-in-the-Loop:** AI is your advisor. It suggests, you decide. Like a GPS suggesting a route—you choose whether to follow it.

**Level 2 - Human-on-the-Loop:** AI can act automatically, but you're watching and can intervene. Like cruise control—it's driving, but you're monitoring and can take over.

**Level 3 - Human-in-Command:** You set the strategic rules and boundaries that AI must operate within, even if you're not involved in each decision. Like setting speed limits on roads.

### How do I know which level is right for a specific application?

Ask three questions:

1. **What are the stakes if the AI is wrong?**
   - High stakes (safety, major cost, legal) → Human-in-the-Loop
   - Medium stakes (reversible, limited impact) → Human-on-the-Loop might work
   - Defining what's acceptable → Human-in-Command

2. **What's the volume of decisions?**
   - Low volume (10s per day) → Human-in-the-Loop is feasible
   - High volume (1000s per day) → Human-on-the-Loop is necessary
   
3. **How clearly can you define success?**
   - Ambiguous, context-dependent → Human-in-the-Loop
   - Clear, measurable criteria → Human-on-the-Loop possible

### Can a system use different levels of oversight for different situations?

Absolutely, and this is common in well-designed systems.

**Example:** An autonomous haul truck might operate:
- **Human-on-the-Loop** for normal driving on established haul roads
- **Human-in-the-Loop** when approaching a loading area with manned equipment
- **Human-in-Command** setting boundaries like "never operate within 50m of blast areas"

The level of oversight can escalate based on context and risk.

### What happens when AI and human disagree?

In **Human-in-the-Loop:** The human decision wins, always. The AI is advisory only.

In **Human-on-the-Loop:** You need clear protocols. Humans should be able to override AI actions and escalate concerns. Track these disagreements—they're valuable data. If humans constantly override the AI, either the AI needs retraining or the task isn't appropriate for automation.

**Best practice:** Implement a feedback mechanism. When a human overrides AI, they should be able to note why. This data helps improve the system.

---

## Implementation & Getting Started

### Where should we start with AI in our mining operation?

Start with the **3-question test:**

1. **Where do we have a clear pain point?** (high volume, repetitive task, or valuable insight buried in data)
2. **Where do we have clean, accessible data?** (don't start where data is a mess)
3. **Where would a mistake be tolerable and fixable?** (don't start with highest-stakes decisions)

**Common good starting points in mining:**
- Predictive maintenance on a subset of equipment
- Automated summarization of daily shift reports
- Initial screening of geological data with expert review
- Optimization of already-established processes (dispatch, scheduling)

**Poor starting points:**
- Replacing a geologist's judgment on resource estimates
- Fully autonomous blast design
- Anything where "the AI did it" wouldn't be an acceptable explanation

### Do we need to hire data scientists?

**Initially:** No. You can start with vendor solutions and consultants who build the initial systems.

**As you scale:** Yes, eventually. Once you have 3-5 AI applications running, you'll want internal capability to:
- Manage vendor relationships knowledgeably
- Coordinate AI strategy across departments
- Customize and tune systems to your specific context
- Troubleshoot when things don't work as expected

**But your first hire shouldn't be a data scientist.** It should be someone who understands your operations AND has enough technical literacy to bridge between business needs and AI solutions. This might be an industrial engineer, a mining engineer who's done some coding, or an operations manager who's curious about technology.

### What if our data is messy or siloed across multiple systems?

This is the **#1 barrier** to AI adoption, and almost every organization faces it.

**Don't wait for perfect data.** Here's the pragmatic approach:

1. **Find your cleanest data source** and start there. Maybe it's your fleet management system or your geological database. Prove value with that one source.

2. **Use early AI projects to justify data infrastructure investment.** "The predictive maintenance pilot saved us $200K. To roll it out to the whole fleet, we need to integrate our maintenance database with our fleet management system."

3. **Consider AI that can handle messy data.** Some modern LLMs are surprisingly good at working with inconsistent, poorly structured data. They're not as accurate as they would be with clean data, but they might be "good enough" to prove value.

4. **Be realistic about timelines.** If your data is truly a mess, allocate 6-12 months for data preparation before expecting AI to deliver magic results.

### How long does it take to implement an AI solution?

**Rough timelines by complexity:**

**Simple pilot (e.g., LLM analyzing shift reports):**
- 1-2 months for setup and testing
- Another 1-2 months to validate accuracy
- Total: 2-4 months to prove concept

**Medium complexity (e.g., predictive maintenance on one equipment type):**
- 2-3 months for data collection and baseline
- 2-3 months for model development
- 3-6 months for validation and tuning
- Total: 6-12 months to production

**High complexity (e.g., autonomous haulage):**
- 6-12 months for infrastructure and safety case
- 6-12 months for pilot with limited fleet
- 12-24 months for full rollout
- Total: 2-4 years to full deployment

**Golden rule:** Double your initial estimate. AI projects almost always take longer than expected, but usually because of organizational and data challenges, not technology limitations.

### Should we build custom AI or buy off-the-shelf solutions?

**For 90% of applications: Buy, don't build.**

**Buy when:**
- The application is common across industries (predictive maintenance, document analysis, anomaly detection)
- Vendors have proven solutions in your domain
- You want faster time-to-value
- You have limited internal AI expertise

**Build (or heavily customize) when:**
- The application is unique to your specific operation
- It's a core competitive advantage you want to protect
- Off-the-shelf solutions don't exist for your use case
- You have a specific integration requirement vendors can't meet

**Hybrid approach (most common):** Buy platform solutions and customize them. For example, buy a predictive maintenance platform from a vendor but train it on your specific equipment and operational patterns.

---

## Cost & ROI

### How much does AI implementation actually cost?

Costs vary dramatically by scope and approach. Here are realistic ranges:

**Small pilot projects:**
- LLM-based document analysis: $10-30K (software subscription + setup)
- Predictive maintenance for 5-10 assets: $50-100K (sensors if needed + software + integration)
- Geological data analysis tool: $20-50K (software + training)

**Medium implementations:**
- Fleet-wide predictive maintenance: $200K-500K (year 1)
- Autonomous truck pilot (3-5 trucks): $1-3M (equipment modifications + systems)
- Mine-wide operational optimization: $300K-800K (software + integration + change management)

**Large transformations:**
- Full autonomous haulage (50+ trucks): $10-50M+ (multi-year program)
- Integrated smart mine platform: $5-20M+ (depends on scale)

**Ongoing costs:** Budget 15-25% of initial implementation cost annually for maintenance, support, and continuous improvement.

### What ROI should we expect, and how quickly?

**Realistic ROI expectations by application:**

**Predictive maintenance:**
- ROI: 3-5x investment over 3 years
- Payback period: 12-18 months
- Primary benefits: Reduced downtime (20-40%), lower maintenance costs (10-20%)

**Operational optimization (dispatch, scheduling):**
- ROI: 2-4x investment over 3 years
- Payback period: 6-12 months
- Primary benefits: Increased throughput (5-15%), better resource utilization

**Autonomous operations:**
- ROI: 1.5-3x investment over 5 years
- Payback period: 2-4 years
- Primary benefits: Lower operating costs (15-30%), increased uptime, improved safety

**Generative AI for analysis:**
- ROI: Harder to quantify (time savings, better decisions)
- Payback period: 3-6 months (relatively low investment)
- Primary benefits: Faster insights, more thorough analysis, freed-up expert time

**Warning signs of unrealistic ROI projections:**
- Vendor promises 10x ROI in year 1
- Benefits claimed without clear measurement methodology
- ROI based entirely on "time saved" without productivity redeployment plan

### What are the hidden costs we should budget for?

Beyond the obvious software and hardware costs, budget for:

**Data preparation:** Often 30-40% of total project effort. Cleaning, standardizing, and integrating data sources.

**Change management:** 15-25% of project cost. Training people, adjusting processes, managing organizational resistance.

**Integration with existing systems:** Can double implementation costs if your systems don't talk to each other easily.

**Ongoing monitoring and tuning:** AI isn't "set and forget." Budget 0.5-1 FTE for ongoing system monitoring once deployed.

**Failed experiments:** Not every AI project succeeds. Budget for 2-3 pilots with the expectation that 1-2 will deliver value worth scaling.

**Organizational opportunity cost:** Your best people will spend significant time on AI projects. What aren't they doing instead?

---

## Technical Questions

### How does AI actually "learn"?

Most practical AI uses **supervised learning:**

1. **Training phase:** The AI is shown many examples where you know the right answer. For predictive maintenance: "Here are 1000 equipment failures with the sensor data leading up to each failure."

2. **Pattern recognition:** The AI identifies patterns. "When vibration increases by X% while temperature rises by Y°, failure occurs 85% of the time within 48 hours."

3. **Testing:** The AI makes predictions on data it hasn't seen before. You check accuracy.

4. **Deployment:** If accurate enough, the AI starts making predictions on real operational data.

5. **Continuous learning:** As new data comes in (including cases where the AI was wrong), the system can be retrained to improve.

**Key insight:** AI doesn't "understand" anything. It finds statistical patterns. That's why human oversight remains critical—the AI might find a spurious correlation that happens to work in training data but isn't actually causal.

### What data do we need to make AI work?

**Quality matters more than quantity.** Good AI needs:

**Sufficient volume:**
- For pattern recognition in sensor data: thousands of data points
- For predictive models: hundreds of examples of the outcome you're trying to predict
- For LLMs: these are pre-trained, so you can start with smaller amounts of your specific data

**Consistency:**
- Data collected the same way over time
- Standardized formats and definitions
- Minimal gaps or missing values

**Relevance:**
- Data that actually relates to the outcome you care about
- Features that an expert would consider meaningful

**Example:** For predicting haul truck engine failure, you need consistent sensor data (temperature, vibration, oil quality) collected at regular intervals, along with records of when failures actually occurred. 500 trucks × 6 months of data would be a good starting point.

### Can AI work with legacy systems and old data?

**Short answer:** Often yes, but with limitations.

**Integration approaches:**
1. **API connections:** If your legacy system has any kind of data export, AI can read it
2. **Data extraction:** Pull data into a modern database regularly, AI works from there
3. **Screen scraping (last resort):** AI can sometimes read data from old user interfaces
4. **Manual bridging:** For truly antiquated systems, you might need manual data extraction

**Old data challenges:**
- Different measurement standards or units over time
- Incomplete records or poor documentation
- Systems that didn't capture data AI would now find useful

**Pragmatic approach:** Start with whatever data you can access. If early results show promise, use that to justify infrastructure upgrades for better data access.

### How accurate does AI need to be before we trust it?

**There's no universal threshold.** It depends entirely on the stakes and the baseline.

**Questions to ask:**

1. **What's the current human accuracy?** If geologists identify viable drill targets 60% of the time, and AI does it 65% of the time, that's valuable even though it's "only" 65%.

2. **What's the cost of false positives vs. false negatives?** For safety alerts, you might accept 80% false alarms (false positives) to catch 95% of real hazards (minimize false negatives).

3. **Can errors be caught by downstream processes?** If AI generates a report that humans review, you can tolerate lower accuracy than if AI takes direct action.

**Practical benchmarks:**
- **Predictive maintenance:** 70-80% accuracy is often good enough (much better than reactive maintenance)
- **Document analysis:** 90%+ accuracy typically needed (humans won't trust it otherwise)
- **Safety-critical alerts:** 95%+ for detecting genuine hazards (but high false alarm rate might be acceptable)

**Best practice:** Start with human-in-the-loop oversight regardless of accuracy, then relax to human-on-the-loop only after consistent performance over months.

### What happens when the AI encounters something it's never seen before?

This is called **out-of-distribution data** and it's a critical limitation of AI.

**What good AI systems do:**
- Flag when they're uncertain: "I'm only 40% confident in this prediction"
- Alert humans: "This situation is outside my training data"
- Fall back to safe defaults: "Stopping autonomous operation and requesting human operator"

**What poorly designed systems do:**
- Make a confident prediction anyway (dangerous)
- Fail silently without alerting anyone
- Generate nonsensical outputs

**Why this matters for governance:** This is why Human-in-Command is critical. You must define what the AI should do when it's unsure, and this requires human judgment about acceptable risk.

**Mining example:** An autonomous truck encountering unexpected equipment on a haul road should stop and alert a human operator, not try to navigate around it based on a "best guess."

---

## Organizational & People

### Will AI eliminate jobs in mining?

**Evidence to date says: No, but jobs change significantly.**

**What actually happens:**

**Jobs that decrease:**
- Manual operators in autonomous systems (but note: many become remote operators)
- Routine data entry and compilation
- Some first-line maintenance roles (replaced by condition-based maintenance)

**Jobs that increase or emerge:**
- Remote operation and monitoring roles
- Data analysts and AI system managers
- Advanced maintenance technicians (predictive/preventive focus)
- Automation engineers and system integrators
- Change management and training specialists

**Jobs that transform:**
- Geologists spend less time on data compilation, more on interpretation
- Mine managers focus more on strategy, less on routine operational decisions
- Engineers work more on optimization and system design

**Net employment impact:** Rio Tinto and Fortescue, with extensive automation, still employ tens of thousands. But the skill profile shifted higher—more technical, more analytical, higher pay on average.

**Critical factor:** How well you manage workforce transition. Companies that invest in reskilling see less resistance and better outcomes.

### How do we address workforce concerns about AI?

**Be transparent and proactive:**

1. **Acknowledge the concern directly.** Don't dismiss fears. "I understand why AI raises concerns about job security."

2. **Show, don't just tell.** Pilot projects where people can see AI augmenting rather than replacing them are more convincing than any PowerPoint.

3. **Involve workers in design.** The people doing the job know where AI would actually help vs. where it would cause problems. Their input makes better systems.

4. **Invest in transition.** If someone's role will change, provide training and a clear path to the new role. Don't expect them to "figure it out."

5. **Focus on what AI can't do.** Emphasize judgment, relationships, creativity, complex problem-solving—distinctly human capabilities that become more valuable as AI handles routine tasks.

**What NOT to do:**
- Claim "AI won't change anything" (people won't believe you)
- Introduce AI secretly and spring it on workers
- Automate first, figure out people impacts later

**Example messaging:** "AI will handle the repetitive data analysis so you can spend more time on the complex interpretations where your experience really matters. We'll train you on working with the AI tools, and this will make you more valuable, not less."

### Who should lead AI initiatives in a mining company?

**Not your IT department alone.** AI strategy is a **business and operational challenge** that happens to use technology.

**Ideal structure:**

**Executive sponsor:** Senior operations or technical leader who:
- Understands mining operations deeply
- Has authority to make cross-functional decisions
- Can secure budget and navigate politics
- Doesn't need to be technical, but must be curious and willing to learn

**Working team:**
- **Operations lead:** Identifies problems worth solving and validates solutions
- **Technical lead:** Understands AI capabilities and limitations (might be external initially)
- **Data/IT lead:** Ensures data access and system integration
- **Change management lead:** Handles organizational adoption

**Governance committee:** Cross-functional group meeting quarterly to:
- Review AI portfolio and priorities
- Set standards and boundaries
- Resolve conflicts between departments
- Own accountability for AI outcomes

**Critical point:** The person who understands the business problem must drive the project. The technologists support them, not the other way around.

### How do we build internal AI capability over time?

**Phase 1 (Months 0-12): Learn by doing with external help**
- Partner with vendors and consultants for first 2-3 projects
- Assign your best people to work alongside them (even if it hurts short-term)
- Focus on learning, not just delivery

**Phase 2 (Year 2): Develop internal champions**
- Send 2-3 people for formal AI training/courses
- Start managing vendor relationships more actively
- Begin doing simpler customizations internally

**Phase 3 (Year 3+): Build internal team**
- Hire 1-2 data scientists or AI engineers
- Develop centers of excellence
- Internal team leads projects, vendors provide specialized support

**Investment approach:**
- Year 1: 80% external, 20% internal
- Year 2: 60% external, 40% internal
- Year 3+: 40% external, 60% internal

**Don't try to build Google inside your mining company.** You need enough internal capability to be a smart buyer and to customize solutions to your context, not to compete with AI companies.

---

## Mining-Specific Applications

### Which AI applications are most mature and proven in mining?

**High maturity (widely deployed, proven ROI):**
- Autonomous haul trucks (Pilbara iron ore operations)
- Predictive maintenance on mobile equipment
- Ore sorting and grade control systems
- Fleet optimization and dispatch
- Basic anomaly detection in sensor data

**Medium maturity (successful pilots, early commercial deployment):**
- AI-assisted geological interpretation and targeting
- Ventilation optimization (underground)
- Blast optimization
- Safety monitoring (fatigue detection, proximity alerts)
- Generative AI for operational reporting

**Early stage (promising research, limited deployment):**
- Fully autonomous drilling
- AI-driven mine planning and optimization
- Complex multi-agent coordination
- Metallurgical process optimization using AI
- Automated compliance and regulatory reporting

**Recommended strategy:** Start with high-maturity applications where the technology risk is low. Use success to build capability and credibility for medium-maturity applications.

### Can AI help with exploration and finding new deposits?

Yes, and this is one of AI's most exciting applications in mining.

**What AI is good at:**
- Analyzing massive geochemical, geophysical, and geological datasets simultaneously
- Identifying subtle patterns that indicate mineralization
- Comparing your site data against global deposit databases
- Rapidly screening large areas to prioritize targets

**Real example:** KoBold Metals used AI to analyze regional data in Zambia and identified a major copper deposit announced in 2023. The AI found patterns across multiple data types that pointed to a high-probability target.

**What AI can't replace:**
- Geological judgment and interpretation
- Field verification and core logging
- Understanding structural and tectonic context
- Making the final decision on where to drill

**Best practice:** AI does the initial data analysis and ranking (human-on-the-loop), geologists review top targets and add context (human-in-the-loop), leadership decides drill program based on strategy and budget (human-in-command).

**Limitations:** AI can only find deposits similar to ones in its training data. It's less useful for completely novel deposit types.

### How can AI improve safety in mining operations?

**Current applications:**

**Fatigue monitoring:**
- Cameras in haul truck cabs detect eye closure and head nodding
- System alerts operator and supervisor if fatigue detected
- Human-on-the-loop: AI monitors continuously, humans intervene

**Proximity detection:**
- AI combines GPS, radar, and cameras to detect potential collisions
- Warnings to operators or automatic speed reduction
- Prevents interactions between light vehicles and heavy equipment

**Hazard identification:**
- AI analyzes video feeds for unsafe behaviors or conditions
- Computer vision identifies missing PPE, unsafe acts, hazardous conditions
- Alerts supervisors to intervene

**Predictive geotechnical monitoring:**
- AI analyzes slope stability data to detect early warning signs
- Flags areas requiring evacuation or additional monitoring
- Critical application of human-on-the-loop with clear escalation protocols

**Incident analysis:**
- LLMs analyze incident reports to identify recurring themes
- Spots patterns invisible to humans reading individual reports
- Enables proactive intervention on trending issues

**Key principle:** AI enhances safety by providing continuous monitoring at scale, but humans must remain accountable for safety decisions.

### Can AI optimize blast designs?

Yes, but this is a complex application requiring careful oversight.

**What AI can do:**
- Analyze historical blast performance data
- Optimize burden and spacing based on rock properties
- Predict fragmentation outcomes
- Suggest drill patterns for specific geological conditions
- Learn from post-blast fragmentation analysis

**Where humans must stay involved:**
- Final approval of blast designs (human-in-the-loop)
- Adjustments based on current ground conditions
- Safety reviews and regulatory compliance
- Handling unexpected geological features
- Defining constraints (vibration limits, flyrock risk)

**Maturity level:** Still emerging. Several vendors offer AI-assisted blast design, but fully autonomous blast design is not widely deployed.

**Recommended approach:** Use AI to generate initial designs and predict outcomes, but require shot-firer review and approval before execution. This is a clear human-in-the-loop application.

---

## Risk & Governance

### What are the biggest risks of AI in mining operations?

**Technical risks:**
- AI making wrong predictions or decisions (false positives/negatives)
- Systems failing or behaving unpredictably in edge cases
- Integration failures causing operational disruptions
- Data quality issues leading to poor AI performance

**Operational risks:**
- Over-reliance on AI eroding human skills and judgment
- Alert fatigue if AI generates too many false alarms
- Automation complacency (humans stop paying attention)
- Systems optimizing for the wrong objectives

**Safety risks:**
- Autonomous equipment encountering unexpected situations
- Safety-critical systems failing without adequate backup
- Unclear accountability when AI is involved in incidents
- Inadequate testing before deployment

**Business risks:**
- Failed implementations damaging credibility of future AI projects
- Vendor lock-in to proprietary systems
- Competitive disadvantage if competitors adopt AI faster
- Regulatory or legal challenges

**Mitigation:** The three-level oversight framework addresses most of these risks by ensuring appropriate human involvement and clear accountability.

### How do we ensure accountability when AI is involved?

**Golden rule: Accountability always remains human.**

**Clear accountability structure:**

1. **Human-in-Command level:** Executive leadership owns the decision to deploy AI for specific purposes and sets boundaries. If the AI application causes harm, they're accountable for choosing to use AI this way.

2. **Human-in-the-Loop level:** The human making the final decision is accountable for that decision, even if AI influenced it. "The AI recommended it" is not an acceptable excuse.

3. **Human-on-the-Loop level:** The human monitoring the system is accountable for intervening when needed. If the AI takes a wrong action and the monitor didn't catch it, that's a monitoring failure, not an AI failure.

**Documentation is critical:**
- Who decided to use AI for this application and why?
- What oversight level was chosen and why?
- Who is responsible for monitoring?
- What are the escalation procedures?
- How are AI decisions logged and auditable?

**Example:** If an autonomous truck is involved in an incident, the accountability chain is: operator monitoring (if any) → autonomous systems manager → operations manager who approved autonomous operation in that area → executive who approved autonomous program. The AI isn't accountable; the humans who deployed and oversaw it are.

### Do we need an AI ethics committee or governance board?

**Yes, especially as you scale beyond 2-3 AI applications.**

**Purpose of governance body:**
- Set organization-wide AI policies and standards
- Review and approve high-risk AI applications
- Ensure consistency across departments
- Own the "Human-in-Command" role for enterprise AI strategy
- Provide forum for escalating AI-related concerns

**Composition (6-10 people):**
- Executive sponsor (chair)
- Operations leaders from major departments
- Legal/compliance representative
- IT/technology leader
- Safety manager
- HR/workforce representative
- External advisor (optional)

**Meeting cadence:**
- Quarterly for mature programs
- Monthly during early scaling phase
- Ad-hoc for major decisions or incidents

**Key policies to establish:**
- What types of decisions can/cannot use AI
- Required oversight levels for different applications
- Data privacy and security standards
- Vendor evaluation criteria
- Workforce impact assessment requirements
- Incident response procedures

**Don't create bureaucracy:** The governance body sets policy, not reviews every AI decision. Day-to-day decisions stay with operations.

### What regulations apply to AI in mining?

**Currently (2025):** Mining-specific AI regulations are limited. Most regulation is indirect:

**Existing frameworks that apply:**
- **Mine safety regulations:** Any AI system affecting safety must meet existing safety case requirements
- **Environmental regulations:** If AI controls environmental systems (water, emissions), standard regulations apply
- **Employment law:** AI in hiring or performance management must comply with discrimination laws
- **Privacy law:** AI using personal data (fatigue monitoring, location tracking) must comply with privacy regulations
- **Autonomous vehicle regulations:** Vary by jurisdiction for on-road vs. off-road autonomous equipment

**Emerging regulations to watch:**
- **EU AI Act:** Categorizes AI by risk level, may affect operations in Europe
- **Industry standards:** ICMM and similar bodies developing AI guidance for mining
- **Insurance requirements:** Insurers starting to require specific AI governance for coverage

**Best practice:** Don't wait for regulation. Establish governance proactively. Companies with mature AI governance will find compliance easier as regulations emerge.

### How do we protect against AI bias?

**Types of bias to watch for:**

**Historical bias:** AI learns from past data. If past decisions were biased, AI perpetuates them.
- *Example:* If your hiring history favored certain demographics, AI trained on this data will do the same

**Measurement bias:** AI optimizes what you measure, which may not capture what you care about.
- *Example:* Optimizing for production tonnage might sacrifice safety or equipment longevity

**Representation bias:** If training data doesn't represent all situations, AI performs poorly on underrepresented cases.
- *Example:* Predictive maintenance trained only on data from one climate may fail in different conditions

**Mitigation strategies:**

1. **Diverse training data:** Ensure data represents all conditions, people, and situations
2. **Regular auditing:** Check AI outputs for patterns of bias, especially in people-affecting decisions
3. **Human oversight:** Maintain human-in-the-loop for decisions that could be discriminatory
4. **Transparency:** Make AI decision factors visible and explainable
5. **Feedback mechanisms:** Enable people to challenge AI decisions they believe are biased

**Remember:** AI doesn't create bias, it reflects and amplifies bias in data and processes. Fixing AI bias often means fixing human bias first.

---

## Choosing Solutions

### How do we evaluate AI vendors and solutions?

**Key evaluation criteria:**

**1. Proof of value (most important)**
- Do they have case studies in similar operations?
- Can they demonstrate the system working?
- Will they agree to a paid pilot with success metrics?
- What are realistic ROI expectations?

**2. Technology maturity**
- How long has this solution been in production?
- How many clients are using it?
- What's the typical implementation timeline?
- What accuracy/reliability can we expect?

**3. Integration and data requirements**
- What data does it need, and do we have it?
- Can it integrate with our existing systems?
- What's the data preparation effort?
- Does it require ongoing data feeds or periodic updates?

**4. Oversight and control**
- Can we set boundaries and constraints?
- Does it provide confidence/uncertainty estimates?
- Can we override or intervene?
- How transparent are its decisions?

**5. Support and partnership**
- What implementation support is included?
- What are ongoing support and maintenance costs?
- Do they provide training?
- What's their track record of long-term client relationships?

**6. Commercial terms**
- Pricing model (subscription, license, usage-based)
- Lock-in risk (can we switch vendors if needed?)
- Data ownership (do we own our data and models?)
- Scalability (cost to expand beyond pilot)

**Red flags:**
- Vendor won't agree to measurable success criteria
- "Black box" with no visibility into how it works
- Requires extensive custom development before seeing results
- No references from similar operations
- Promises that sound too good to be true

**Best practice:** Run competitive pilots. Test 2-3 vendors on a small-scale problem with clear success metrics before committing to large-scale deployment.

### Should we use open-source AI or commercial solutions?

**Commercial solutions:**
**Pros:**
- Faster implementation with vendor support
- Pre-built integrations and user interfaces
- Ongoing maintenance and updates included
- Clear accountability (you can blame the vendor)

**Cons:**
- Higher ongoing costs
- Potential vendor lock-in
- Less customization flexibility
- Dependent on vendor's roadmap

**Open-source AI:**
**Pros:**
- Lower licensing costs (but implementation costs can be higher)
- Full customization capability
- No vendor lock-in
- Control over your roadmap

**Cons:**
- Requires internal technical expertise
- You own all implementation and maintenance
- No one to call when things break
- May lack industry-specific features

**Recommended approach for mining:**
- **Start with commercial solutions** for your first 2-3 AI applications (reduce risk, learn faster)
- **Consider open-source** once you have internal capability and clear requirements
- **Hybrid approach:** Use commercial platforms with open-source models (e.g., using LLMs like Llama deployed on your infrastructure)

**Exception:** If you have a very specific, proprietary use case that vendors don't address, custom development with open-source tools might be your only option.

### What about using LLMs like ChatGPT in our operations?

**Consumer LLMs (ChatGPT, Claude, etc.) - Good for:**
- Quick analysis of public information
- Drafting routine documents
- Brainstorming and ideation
- Learning and education
- Proof-of-concept testing

**Critical limitations for operations:**
- **Data privacy:** Your data goes to the vendor and may be used for training
- **Security:** Not suitable for confidential or sensitive information
- **Accuracy:** Can "hallucinate" or make confident mistakes
- **Compliance:** May not meet your regulatory or audit requirements
- **Reliability:** Consumer services have no uptime guarantees

**Enterprise alternatives:**
- **ChatGPT Enterprise / Claude for Enterprise:** Business versions with data privacy, no training on your data, admin controls
- **Microsoft Azure OpenAI:** Deploy OpenAI models in your own secure environment
- **On-premise LLMs:** Deploy open-source models (Llama, Mistral) on your infrastructure

**Recommended approach:**
1. **Experiment freely** with consumer LLMs for non-sensitive use cases
2. **Upgrade to enterprise** if you find valuable applications
3. **Deploy on-premise** for truly sensitive applications (geological interpretations, financial data)

**Never put in consumer LLMs:**
- Proprietary geological data
- Financial information
- Personal employee data
- Upcoming M&A or business strategy
- Anything covered by confidentiality agreements

### How do we know if an AI solution is "good enough"?

**Define "good enough" before you start:**

**Benchmark against current state:**
- If current process is 70% accurate, AI at 75% is valuable
- If current process costs $X, AI must cost <$X or deliver >$X in value
- If current process takes 2 days, AI delivering same quality in 2 hours is valuable

**Consider the full picture:**
- Accuracy alone isn't enough; also consider speed, cost, scalability
- 80% accuracy with instant results might be better than 95% accuracy taking a week
- Lower accuracy with good uncertainty estimates can be valuable (AI says "I'm only 60% confident" lets you decide)

**Set minimum viable thresholds:**
- Below what accuracy is the system useless or dangerous?
- What false alarm rate makes the system more annoying than helpful?
- What response time is required for the application to work?

**Pilot testing approach:**
1. **Baseline:** Measure current performance quantitatively
2. **Pilot:** Run AI system alongside current process for 2-3 months
3. **Compare:** Is AI measurably better? If yes, by how much?
4. **Decide:** Is the improvement worth the cost and change?

**Example decision:** 
- Current: Geologists identify viable drill targets 65% of the time, takes 3 weeks
- AI system: Identifies targets 68% accurately, takes 3 days
- Decision: Valuable. Slightly better accuracy, dramatically faster, frees geologist time for other work. Worth implementing.

---

## Additional Resources

### Where can I learn more about AI in mining?

**Industry Reports:**
- Deloitte Insights: "Mining and Metals AI Revolution" series
- McKinsey: "The Future of Mining" reports
- Mining3 research publications
- ICMM (International Council on Mining & Metals) technology guides

**Academic Sources:**
- Mining Engineering journals (SME, CIM)
- Papers on AI applications in extractive industries
- University mining research centers (JKMRC, Luleå, McGill)

**Case Studies:**
- Rio Tinto automation reports (publicly available)
- Fortescue Metals autonomous operations
- KoBold Metals exploration AI
- Vendor case study libraries (Komatsu, Hexagon, Wenco)

**Courses and Training:**
- Curtin University Executive Education: "AI in Leadership & Project Management" and "AI to Drive Business Innovation"
- Mining industry conferences (IMARC, MINExpo, etc.)
- Online platforms (Coursera, edX) for technical foundations

### How do I stay current on AI developments?

**Subscribe to:**
- Mining technology newsletters (e.g., MINING.COM Technology)
- AI in industry publications (MIT Technology Review, AI Business)
- Vendor blogs and webinars
- LinkedIn groups focused on mining innovation

**Attend:**
- Mining technology conferences (at least annually)
- Vendor demonstration days
- Industry workshops and webinars

**Network:**
- Join mining technology peer groups
- Connect with colleagues at other operations
- Engage with university research groups

**Key insight:** AI is evolving rapidly. What's cutting-edge today will be standard practice in 2-3 years. Continuous learning is essential.

### Can we get help implementing AI in our operation?

**Yes. Multiple pathways:**

**1. Vendor-led implementation:**
- AI software vendors typically offer implementation services
- They handle setup, training, initial tuning
- Good for first projects where you're learning

**2. Consulting firms:**
- Major consultancies (Deloitte, McKinsey, etc.) have mining AI practices
- Specialized mining consultants partner with AI vendors
- Good for strategy and change management

**3. Research institutions:**
- University mining departments often do applied research projects
- Can be more affordable, though slower
- Good for novel applications without commercial solutions

**4. System integrators:**
- Engineering firms specializing in mining automation
- Handle integration of AI with existing systems
- Good for complex technical implementations

**5. Training and capability building:**
- Executive education courses (like Curtin's offerings)
- Internal capability development programs
- Learning by doing with expert coaching

**Recommended path:** Start with vendor-led implementation for your first project, but assign your best people to work alongside them. Use early projects to build internal knowledge. Consider executive training to develop strategic AI leadership.

---

## Course Information

### How do the executive courses relate to this presentation?

This presentation introduced the **framework**—the three levels of human oversight and how to think about AI strategically.

The **courses go much deeper:**

**"AI in Leadership and Project Management"** is for people who will lead AI initiatives:
- How to identify high-value AI opportunities in your operations
- Building and managing cross-functional AI project teams
- Taking AI from pilot to production deployment
- Managing organizational change around AI
- Real project work on your actual challenges

**"AI to Drive Business Innovation"** is for strategic thinking:
- Evaluating emerging AI technologies (what's real vs. hype)
- Where AI creates competitive advantage in mining
- Building compelling business cases for AI investment
- Strategic frameworks for AI-driven transformation
- Industry benchmarking and best practices

**Both courses:**
- Are hands-on and practical (not theoretical)
- Use mining-specific examples and case studies
- Include working sessions on your real challenges
- Provide frameworks you can apply immediately
- Connect you with peers facing similar challenges

### Who should attend each course?

**"AI in Leadership and Project Management" is ideal for:**
- Mine managers and superintendents
- Department heads (geology, maintenance, operations)
- Technical services managers
- Project managers assigned to AI initiatives
- Anyone who will champion and lead AI projects

**"AI to Drive Business Innovation" is ideal for:**
- Senior executives and general managers
- Strategic planning roles
- Business development leaders
- Innovation and technology managers
- Anyone setting direction for AI strategy

**Can you take both?** Yes, and they complement each other. Leadership course is tactical (how to execute), Innovation course is strategic (what to execute).

### What will I be able to do after completing a course?

**After "AI in Leadership and Project Management":**
- Identify and prioritize AI opportunities in your area
- Frame business problems as AI projects with clear success criteria
- Build project teams and manage AI implementation
- Navigate vendor relationships and solution evaluation
- Design appropriate human oversight for different AI applications
- Manage organizational change and address workforce concerns

**After "AI to Drive Business Innovation":**
- Distinguish AI hype from genuine opportunities
- Evaluate emerging AI technologies for your context
- Build business cases that secure executive buy-in
- Develop multi-year AI roadmaps for your organization
- Benchmark against industry leaders
- Position your operation for AI-driven competitive advantage

**Both courses emphasize:**
- Practical application over theory
- Mining-specific examples and challenges
- Frameworks you can use Monday morning
- Connection with peers for ongoing learning

### How do I register or get more information?

**Visit:** [Course registration website URL]

**Contact:** [Curtin Executive Education contact details]

**Course dates:**
- October-November 2025 (specific dates on website)

**Format:**
- In-person intensive workshops
- Optional online pre-work
- Post-course resources and community access

**Investment:**
- [Course fee information]
- Group discounts available for multiple attendees from same organization

**Questions?**
Email: [contact email]
Phone: [contact phone]

---

## Still Have Questions?

If your question isn't answered here, we'd love to hear from you:

**Email:** [Your email]

**Phone:** [Your phone]

**Website:** [Support website URL]

**LinkedIn:** [Your LinkedIn profile]

---

**Download the presentation slides:** [Link to PDF]

**View case study references:** [Link to references page]

**Take the AI readiness assessment:** [Link to assessment tool]

---

*This FAQ document accompanies the "Humans in the Loop: Why Your AI Needs a Co-Pilot" presentation delivered as part of Curtin University Executive Education's Lunch & Learn series.*

*Last updated: [Date]*

---

## Document Map

**Quick Navigation:**

**New to AI?** Start with [Understanding AI Basics](#understanding-ai-basics)

**Ready to implement?** Jump to [Implementation & Getting Started](#implementation--getting-started)

**Concerned about costs?** Check [Cost & ROI](#cost--roi)

**Technical questions?** See [Technical Questions](#technical-questions)

**Worried about people impacts?** Read [Organizational & People](#organizational--people)

**Mining-specific applications?** Go to [Mining-Specific Applications](#mining-specific-applications)

**Governance and risk?** Review [Risk & Governance](#risk--governance)

**Evaluating solutions?** See [Choosing Solutions](#choosing-solutions)

**Want formal training?** Check [Course Information](#course-information)
-
