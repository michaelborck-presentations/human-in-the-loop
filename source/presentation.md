---
title: "Humans in the Loop"
subtitle: "Why Your AI Needs a Co-Pilot"
author: "Michael Borck"
format:
  html:
    theme: 
      - cosmo
    toc: true
    toc-expand: 2
    code-fold: true
    embed-resources: true
    fig-cap-location: bottom
    css: assets/css/module-styles.css
  pptx: default
  pdf:
    toc: false
    colorlinks: true
    geometry:
      - top=30mm
      - left=20mm
---

# The Vision

**A geologist asked an AI a simple question:**

*"Why is the gold grade dropping in the eastern pit wall?"*

**The AI analysed:**
- 5 years of drill data
- 10,000 geological logs
- Structural models
- Production records

**Quickly, it identified a subtle fault offset** that three experienced geologists had debated for months.

::: {.notes}

"Good afternoon. Before we talk about frameworks or theory, I want to show you what's possible right now."

"A senior geologist, frustrated after weeks of trying to explain why gold grades were underperforming in one section of the pit, decided to try something new. She uploaded five years of drill data, geological logs, and structural interpretations into an AI system—one of the new Large Language Models you've been hearing about."

"She typed a simple question in plain English: 'Why is the gold grade dropping in the eastern pit wall?'"

"The AI didn't just search for keywords. It analysed the entire dataset—cross-referencing drill intercepts, looking for structural patterns, comparing similar geological settings across the mine."

"It came back with a hypothesis: 'There appears to be a northeast-trending fault with approximately 15 meters of vertical offset in this zone, which would explain the grade discontinuity you're seeing.' It even highlighted the specific drill holes that showed the offset."

"Three geologists had been debating this for months."

"Now, here's the critical question: Did the AI replace the geologist?"

"No. She reviewed the AI's hypothesis, went back to the core photos, verified the structural interpretation, and confirmed it was right. Then she and her team updated the geological model and adjusted the mine plan."

"The AI didn't make the decision. It gave her a tool to see patterns she couldn't see buried in thousands of data points. That's what we're going to talk about today—not AI replacing humans, but AI as a co-pilot that makes humans more effective."

"Welcome to 'Humans in the Loop.'"

Note: This type of LLM application for geological analysis is becoming increasingly common. Companies like KoBold Metals have used similar AI approaches to discover major copper deposits in Zambia (Reuters, 2023), demonstrating that the technology is proven and operational.
:::

---

# How do we harness AI's power without losing control?

::: {.columns}
::: {.column width="50%"}
**The Tension:**

- AI can analyze data faster than humans
- AI can spot patterns we miss
- AI can work 24/7 without fatigue

*But...*
:::

::: {.column width="50%"}
**The Reality:**

- We need human judgment
- We need accountability
- We need context and nuance

*So where's the balance?*
:::
:::

::: {.notes}
"If you're in this room, you're probably feeling this tension. On one hand, the capabilities are undeniable, AI is getting remarkably good at specific tasks. On the other hand, you've got operations to run, people to keep safe, decisions where you can't afford to get it wrong."

"You've probably heard two narratives: One says 'adopt AI or get left behind.' The other says 'be very careful, AI makes mistakes.'"

"Both are true. And that's not helpful."

"So today, in 40 minutes, I'm going to give you something practical—a simple framework that cuts through the hype and the fear. A way to think about AI that you can apply tomorrow morning when you're back at your desk."

"We're going to answer: When should AI suggest and humans decide? When can AI act while humans monitor? And who sets the boundaries?"

"Three levels. Clear principles. Real mining examples."

"By the end, you'll have a lens for looking at any AI application—whether it's in your operations today or something you're considering—and asking: 'Is the human in the right place in this system?'"

"Let's dive in."
:::

---

# The Framework (Simplified)

## Three Ways Humans Stay in Control

Think of it like driving a car with different levels of automation:

::: {.incremental}
1. **AI suggests a route, you decide** → Human-in-the-Loop
2. **Cruise control drives, you monitor** → Human-on-the-Loop  
3. **You set the speed limit** → Human-in-Command
:::

**Same principle applies to AI in mining.**

::: {.notes}
"The framework is simple. There are three levels of human control when working with AI."

"Level 1: Human-in-the-Loop. The AI recommends, you decide. Like when your GPS suggests a route—it analyzes traffic, calculates fastest path—but YOU decide whether to follow it. You're in the loop on every decision."

"Level 2: Human-on-the-Loop. The AI can act, but you're monitoring and can intervene. Like cruise control—it's controlling the throttle, but you're watching, hands near the wheel, ready to take over if needed."

"Level 3: Human-in-Command. You set the strategic boundaries. Even if the AI is acting automatically, YOU decided what it's allowed to do. Like setting speed limits on roads—the rules that govern all the driving."

"That's it. Three levels. Now let's see what this looks like in mining operations you know."

Keep this section SHORT. You're giving them the mental model, not exhaustive explanation. Move quickly to examples that bring it to life.
:::

---

# Level 1: When AI Suggests, You Decide

**Dispatch systems** suggest truck assignments
- Dispatcher reviews, then decides
- Can override based on real conditions
- Dispatcher stays accountable

**Why?** Because local knowledge matters. The system doesn't know about that soft spot on Haul Road 3.

::: {.notes}
"You're probably already doing Human-in-the-Loop without calling it that. Your dispatch system, it's optimizing truck movements, suggesting assignments. But does it automatically move the trucks? No. The dispatcher looks at the suggestion and decides."

"Why? Because the dispatcher knows things the AI doesn't. There's a wet patch on one haul road. One operator is new and shouldn't get the tricky route yet. A truck that looks available on the screen is actually being refueled."

"The AI provides speed and data analysis. The human provides judgment and context. That's the partnership."

"This level is appropriate when stakes are high, context matters, and someone needs to be accountable for the outcome."
:::

---

# Level 2: When AI Acts, You Monitor

**Predictive maintenance** systems flag equipment automatically

- AI analyzes sensor data 24/7
- Generates alerts and work orders
- Maintenance team validates and acts

**Why?** Because you can't watch 50 trucks continuously, but humans verify before pulling equipment offline.

::: {.notes}

"Level 2 is where AI starts to feel powerful. Your haul trucks have sensors everywhere, vibration, temperature, pressure, fluid levels. Thousands of data points per truck, 24/7."

"No human can watch all that. So the AI does. It learns what 'normal' looks like and automatically alerts when something deviates. 'Truck 47, bearing temperature rising. Predict failure in 48 hours.'"

"Does a human approve every alert? No—that would defeat the purpose. But the maintenance supervisor reviews the alerts, prioritizes them, and decides: 'Pull that truck tonight' or 'Monitor it, we just changed that component last week.'"

"The AI handles impossible scale. Humans handle judgment and validation. That's Human-on-the-Loop."

"This level works when volume is high, patterns are clear, and mistakes are fixable."

Again, keep it crisp. You're showing possibilities, not technical details.
:::

---

# Level 3: You Set the Rules

**Autonomous trucks** in the Pilbara

- AI drives the trucks
- But YOU decided: where they can go, how fast, what they never do
- Humans set the strategic boundaries

**Why?** Someone must be accountable for safety policies and operational boundaries.

::: {.notes}
"Some of you know that Rio Tinto and Fortescue have hundreds of autonomous trucks operating right now. The AI is driving—steering, accelerating, navigating."

"Does that mean humans aren't in control? Absolutely not."

"Before the first autonomous truck moved, humans made critical decisions: Which areas of the mine are approved for autonomous operation? What are the speed limits? What happens if the truck encounters something unexpected? What are the exclusion zones it can never enter?"

"The AI operates within those boundaries. But the boundaries themselves, the strategy, the risk tolerance, the safety philosophy, those are human decisions at the leadership level."

"That's Human-in-Command. Even when AI is acting autonomously, humans set the rules of the game."

"This level is about governance, strategy, and accountability."
:::

---

# Quick Poll: Which Worries You More?

**A) AI making decisions without human oversight**

**B) Competitors using AI while you move too slowly**

::: {.notes}
"Which actually keeps you up at night? The risk of AI making a wrong decision? Or the risk that while you're being cautious, your competitors are gaining advantage?"

"Here's why this matters: Both risks are real. But they require different responses."

"If you worry about A, AI running unchecked—the framework we just covered is your tool. You intentionally design the level of human control appropriate to each application."

"If you worry about B, moving too slowly—the framework is still your answer. Because it shows you where you CAN automate safely and where you must keep humans engaged."

"The companies winning with AI aren't the ones who automate everything or avoid automation entirely. They're the ones who are thoughtful about WHICH decisions need human judgment and which don't."

"Let me show you what I mean with a scenario."
:::

---

# A Real Dilemma

## Scenario: Autonomous Pit Wall Monitoring

Your new system detects ground movement 24/7.

**Design Choice:**

Critical movement detected →

**Option A:** Alert geo-tech engineer who assesses and decides response *(slower, human judgment)*

**Option B:** Automatically trigger evacuation alarm *(faster, potential false alarms)*

**Which would YOU choose?**

::: {.notes}
"Let me give you a scenario that mining operations are facing right now."

"You've invested in a state-of-the-art pit wall monitoring system. LiDAR, radar, prisms—continuously measuring ground movement down to millimeters. The AI is trained to detect acceleration patterns that might indicate instability."

"It's 2 AM. The AI detects unusual movement. Not catastrophic, but above normal thresholds."

"You have to design this system ahead of time. What should it do?"

Present Option A: "It could alert your on-call geotechnical engineer. They review the data, consider context: Was there blasting today? Recent rain? Historical patterns in this area? and decide whether to evacuate. This takes 15-20 minutes. You get expert judgment, but you lose time."

Present Option B: "Or the system could be programmed to automatically sound evacuation alarms and clear the pit. Immediate response, zero delay. But if it's a false alarm and sensor glitches do happen, you've just stopped production for hours and potentially desensitized people to alarms."

"There's no perfect answer. It depends on your pit geometry, your failure consequences, your risk tolerance."

"This is the art of working with AI. You're making strategic choices about where speed matters most and where judgment matters most."

"The framework doesn't give you THE answer. It gives you the questions to ask: What are the stakes? What's the human's role? Who's accountable?"

"And that clarity, that intentional design, that's what separates organizations that thrive with AI from those that struggle."
:::

---


# The Art of the Possible

## What Changes in 3 Years?

Imagine walking onto your site in 2028...

::: {.incremental}
- **Your morning brief** is AI-generated from overnight sensor data, shift reports, and equipment status
- **Your geologist** spends 90% of time on interpretation, 10% on data compilation (used to be reversed)
- **Your maintenance team** works on predicted failures, not emergencies
- **Your safety meetings** discuss trends the AI spotted across 20 sites
- **Your AI systems coordinate themselves**: Equipment flagged → AI checks parts inventory, finds service windows, schedules crews (agentic workflows in action)
:::

**The work doesn't disappear. It gets elevated.**

::: {.notes}
"Let's fast-forward. It's 2028—just three years from now. You walk onto site Monday morning. What's different?"

"Your morning brief is waiting. The AI has already compiled overnight data—production actuals, equipment alerts, safety incidents, weather forecast, truck utilisation. It's highlighted the three things that need your attention today. This used to take your superintendent an hour to prepare. Now it's done before you arrive, and it's actually MORE comprehensive because the AI looked at patterns across weeks of data."

"Your senior geologist walks in. She's just spent the last hour reviewing the AI's analysis of last week's drill results. The AI did the data compilation, the initial statistical analysis, the comparison to the geological model. She spent her time on what only she can do—interpreting the anomalies, updating the structural interpretation, deciding where to drill next. Three years ago, she spent 70% of her time on spreadsheets. Now it's 90% geology."

"Your maintenance team is working through planned interventions. The truck they're servicing today was flagged three days ago—bearing wear pattern indicating failure in the next week. They're doing the work during scheduled downtime, not responding to a breakdown in the pit at 2 AM. Unplanned downtime is down 60%."

"Your safety meeting discusses trends the AI identified across your whole operation—or even across multiple sites if you're part of a larger company. 'Near-miss reports mentioning 'fatigue' are up 23% in the last month, concentrated in night shift.' That pattern was invisible when you were reading individual reports. Now it's actionable intelligence."

"And here's where it gets really interesting: your AI systems are starting to coordinate with each other. When that truck was flagged for maintenance three days ago, the AI didn't just alert someone. It checked parts inventory, identified that the replacement bearing was in stock, analysed the production schedule to find the optimal service window with minimum impact, and automatically scheduled the maintenance crew. This is what we call 'agentic workflows'—AI systems working together to handle routine coordination tasks without human intervention."

"A human maintenance supervisor still approved the final schedule, but instead of spending two hours coordinating all these moving parts, they spent five minutes reviewing and clicking 'approve.' That's Human-on-the-Loop in action."

"Notice what didn't happen: Nobody lost their job. The work got more valuable."

"The superintendent does strategy instead of spreadsheets. The geologist does geology instead of data entry. The maintenance team prevents problems instead of fighting fires. The supervisor coordinates complex exceptions instead of routine scheduling."

"That's the promise. Not AI replacing humans, but AI handling the routine so humans can focus on the complex, the creative, the judgment-intensive work."

"And it's not science fiction. The technology exists today. The question is: how do we implement it responsibly?"
:::

---

# This Isn't Science Fiction

**Real implementations, today:**

::: {.incremental}
- **KoBold Metals**: AI discovered major copper deposit in Zambia (2023)
- **Komatsu + Mining Fleets**: 40% reduction in unplanned downtime via predictive maintenance
- **Multiple Operators**: Generative AI analyzing shift reports and safety logs at scale
:::

*Sources: Reuters, Deloitte Insights, Global Mining Review, Financial Times*

**More details and references available at [support website](https://michaelborck-presentations.github.io/human-in-the-loop/)**

::: {.notes}
"I know what some of you might be thinking: 'This sounds great in theory, but is it actually happening?' Let me give you three real examples from the last two years."

"KoBold Metals—backed by Bill Gates and partnered with BHP, used AI to analyze geological data across Zambia. In 2023, they announced the discovery of a major copper deposit. The AI identified patterns across geochemical surveys, historical drilling, and geological maps that pointed to a high-probability target. This wasn't a lucky guess, it was systematic pattern recognition at a scale humans couldn't match."

"Komatsu has been working with mining fleets—including operations in Chile and Australia—on predictive maintenance systems. The published results show approximately 40% reduction in unplanned downtime. That's not a pilot project, that's operational, proven, delivering value today."

"And multiple mining operators are now using generative AI—those Large Language Models like the one in my opening story, to analyze shift reports, safety logs, and operational documents. Deloitte's 2024 mining report highlights how companies are extracting insights from unstructured text data that was previously just sitting in databases, unread."

"These aren't future projections. These are implementations happening right now, in operations like yours."

"I've included all the source references on the support website if you want to dig deeper into any of these case studies. Reuters articles, industry reports, company press releases, it's all documented."

"So when I talk about the Art of the Possible, I'm talking about what's already possible. The question is: when does it become possible for YOUR operation?"
:::

---

# The Unexpected Twist

**The biggest barrier isn't the technology.**

::: {.incremental}
- The AI models exist
- The sensors are deployed
- The computing power is affordable

**The barrier is:** Figuring out where humans should be in the loop.
:::

That's a leadership question, not a technical one.

::: {.notes}

"Here's what might surprise you. When companies struggle with AI adoption, it's rarely because the technology doesn't work."

"The AI models are mature. The sensors are already on your equipment. Cloud computing makes it affordable even for mid-tier operations."

"The barrier is this: Nobody's figured out the human-AI division of labour."

"Do we trust the AI to generate the report, or do we require review? If we require review, is someone actually reviewing it, or are they rubber-stamping because they're overwhelmed?"

"When the predictive maintenance system says 'this truck needs service,' do we pull it immediately, or do we wait for human validation? What if the human always ignores the alerts because there are too many false positives?"

"When should the AI alert a human, and when should it just log the data? Get this wrong and either you miss critical signals, or you drown people in noise."

"These aren't technical questions. They're organisational design questions. Leadership questions."

"And that's actually good news. Because it means the path forward isn't 'hire more data scientists'—though you might need some. The path forward is 'get clear on how decisions should be made.'"

"That clarity is what we're offering in the executive courses. Not just understanding AI capabilities, but learning how to design human-AI collaboration in your specific context."

This repositions the courses as leadership development, not technical training. That's the value proposition for executives.
:::

---

# Your Turn to Think

**Think of ONE repetitive task you do regularly.**

*Examples: Weekly reports, data compilation, scheduling, reviewing standard documents*

**Ask yourself:**

1. Could AI handle the initial draft?
2. Where would you need to stay involved?
3. What would free up your time enable you to do instead?

::: {.notes}
"I'm going to give you 60 seconds. Don't write anything down if you don't want to. Just think."

"Pick one task you do regularly that feels repetitive. Maybe it's compiling a weekly report. Maybe it's reviewing routine documents. Maybe it's schedule optimization. Something where you think: 'This takes time but it's not where I add the most value.'"

"Now ask: Could AI handle the first pass of this? Create the initial draft, do the basic analysis, flag the items that need attention?"

"Where would you still need to be involved? Where does your judgment, your experience, your knowledge of context matter?"

"And here's the big question: If AI handled the routine part, what could you do with that freed-up time? What higher-value work aren't you doing now because you're stuck on the routine?"

"Don't share if you don't want to, but I'll bet most of you just identified at least one opportunity. That's the starting point."

"You don't need to transform your entire operation tomorrow. You need to identify one task, design appropriate human oversight, and prove the value. Then you do it again."

"That's how AI adoption actually happens—not through grand transformations, but through thoughtful, incremental improvements."

:::

---

# Where to Go from Here

## Three Levels, One Principle

**Human-in-the-Loop:** AI suggests, you decide *(high stakes, context matters)*

**Human-on-the-Loop:** AI acts, you monitor *(high volume, clear patterns)*

**Human-in-Command:** You set the boundaries *(strategy, accountability)*


> **The principle: Intentional design of human-AI collaboration**
> 
> Not "Should we use AI?" but "Where should humans be in this system?"

::: {.notes}

"We've covered a lot in 40 minutes. Let me bring it back to the core."

"Three levels of human oversight. The first two—in-the-loop and on-the-loop—are about day-to-day operations. Where do humans review, where do humans monitor?"

"The third level—in-command—is about leadership. Setting strategy, defining boundaries, owning accountability."

"But the underlying principle is the same across all three: You make intentional choices about where humans add value and where AI adds value."

"The question isn't 'Should we use AI?' Everyone will use AI. The question is: 'Are we designing human-AI collaboration thoughtfully, or are we just deploying technology and hoping it works out?'"

"The companies that thrive will be the ones who get this design right. Not the most AI, but the most thoughtful AI."

:::

---

# Continue the Conversation

**October/November Executive Courses:**

Learn to design and lead AI initiatives in your organization

::: {.columns}
::: {.column width="50%"}
**AI in Leadership & Project Management**

Lead AI transformation in your operations
:::

::: {.column width="50%"}
**AI to Drive Business Innovation**

Identify strategic AI opportunities
:::
:::

**Today was the spark. The courses are where you build the fire.**

::: {.notes}
"What we covered today is the foundation—a framework for thinking about AI. But it's just the starting point."

"If you want to go deeper—if you want to not just understand these concepts but apply them strategically in your operations—that's what the October and November courses are designed for."

"We offer two pathways:"

"The first, 'AI in Leadership and Project Management,' is for people who want to lead AI initiatives. You'll learn how to identify opportunities in your operations, build cross-functional teams to deliver them, and manage AI projects from pilot to production. It's hands-on—you'll work on real challenges from your own organizations."

"The second, 'AI to Drive Business Innovation,' is more strategic. It's for people who want to identify where AI creates competitive advantage and build the business case for investment."

"Both courses build on what we discussed today. We go from concepts to application, from examples to YOUR examples."

"Today was designed to spark curiosity and inspire new thinking. The courses are where you build capability."

"All the information is available online, and I'll be around after if you want to chat about which might be right for you."
:::

---

# Questions & Connections

**What questions are on your mind?**

::: {.notes}
"We have a few minutes for questions. What's on your mind?"

"Is AI going to eliminate jobs in mining?"
→ "The evidence so far says no—it changes jobs. Autonomous trucks didn't eliminate mining jobs; Rio and Fortescue still employ thousands. But the roles shifted. Fewer operators, more remote controllers and maintenance technicians. The work got more technical. That's why training and development matter—helping people transition to the new roles."

"How much does this actually cost?"
→ "Depends wildly on scope. A predictive maintenance pilot for 10 trucks might be $50-100K. Full autonomous haulage is tens of millions. But here's what's changed: you don't have to build from scratch anymore. There are off-the-shelf solutions now. And you can start small—pilot one application, prove value, scale from there. The barrier isn't cost, it's knowing where to start."

"What if our data is a mess?"
→ "Great question, and very common. You don't need perfect data to start. Pick one application where the data is cleanest and start there. Prove value. The ROI from that first project often funds cleaning up other data. Don't let perfect be the enemy of better."

"How do we know when AI is making mistakes?"
→ "That's why the framework matters. If you're Human-in-the-Loop, you're reviewing outputs. If you're Human-on-the-Loop, you need monitoring systems—tracking false alarm rates, validation accuracy, user override frequency. You build feedback loops. And initially, you compare AI outputs against human outputs to calibrate. It's not 'set and forget'—it's continuous improvement."

"If questions come up later, I'll be around for a bit. And all my contact details are available, don't hesitate to reach out."
:::

---

# Thank You

**Remember: AI doesn't replace judgment. It amplifies it.**

**The question isn't whether to use AI.**

**The question is: Where are the humans in your system?**

---

**Contact:** michael.borck@curtin.edu.au  
**Resources & FAQs:** [Support Website](https://michaelborck-presentations.github.io/human-in-the-loop/)  
**Courses:** [Registration link](https://www.curtin.edu.au/study/professional-development/executive-education/)

::: {.notes}
"Thank you for your time and attention. I want to leave you with one thought:"

"AI doesn't replace human judgment. It amplifies it. It handles scale, speed, pattern recognition. You provide context, accountability, strategic direction."

"The question facing every mining operation, every organisation, isn't whether to use AI. That's inevitable. The question is: Are you intentionally designing where humans sit in your systems?"

"That intentionality is what separates organisations that struggle with AI from those that thrive with it."

"I hope today sparked some curiosity and new thinking. Three things before you go:"

"First, all the resources from today, the presentation slides, case study references, detailed FAQs answering questions we didn't have time for, and additional reading—are available on the support website. The URL is on this slide and I'll share it again in the follow-up email."

"Second, if you want to go deeper and build real capability in AI leadership, the October and November courses are your next step. Information and registration are on the website."

"Third, if you just want to chat about a specific challenge you're facing, I'm here now and my contact details are on the website. Don't hesitate to reach out."

"Thank you."
:::