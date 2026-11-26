#!/usr/bin/env python3
"""Build the Insights articles, readiness checklist and industry pages.

Standard library only. Run from anywhere:  python3 scripts/build_pages.py
Writes static HTML into insights/, resources/ and industries/ and refreshes sitemap.xml.
"""
import json
import math
import os
import re
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://privarynadvisory.com"
CAL = "https://calendly.com/sareen-dev/30min"
PUBLISHED = "2026-11-25"
PUBLISHED_HUMAN = "November 25, 2026"

# ------------------------------------------------------------------ content

ARTICLES = [
    {
        "slug": "why-privacy-platforms-stall-after-go-live",
        "title": "Why privacy platforms stall after go-live, and how to keep yours delivering",
        "short": "Why privacy platforms stall after go-live",
        "desc": "Most privacy technology programs don't fail at implementation. They fade afterward. Five patterns that cause it, and a practical way to prevent each one.",
        "body": """
<p class="lede">Go-live feels like the finish line. The workflows are configured, training is done and the project team is ready to move on. It is also the moment a privacy platform either becomes part of how the business runs or starts, slowly, to drift away from it.</p>

<h2>The quiet failure mode</h2>
<p>Privacy platform programs rarely fail loudly. There is no outage and no dramatic missed deadline. Instead, usage tapers off. Teams drift back to spreadsheets for the requests that do not quite fit. The platform holds an increasingly out-of-date picture of the business. Eventually someone asks what the organization is getting from the investment, and nobody can answer with confidence.</p>
<p>The cause is almost never the technology. It is what happens, or does not happen, once the project ends. Five patterns show up again and again.</p>

<h2>1. Nobody owns it after the project team leaves</h2>
<p>During implementation there is a project manager, a delivery team and an executive sponsor. After go-live those roles dissolve, and the platform becomes everyone's tool and no one's responsibility. Configuration requests sit in a queue, small issues go unfixed, and people stop reporting them because nothing happens.</p>
<p><strong>What helps:</strong> name an operational owner before go-live, give them time in their role to do the job, and make it clear who decides when the platform changes.</p>

<h2>2. It was configured for the demo, not for the work</h2>
<p>A workflow that looks elegant in a walkthrough can be painful in daily use: too many required fields, approvals routed to people who are not the real decision-makers, forms that ask for information the requester does not have. Teams are practical. If the tool is slower than the spreadsheet, the spreadsheet wins.</p>
<p><strong>What helps:</strong> design each workflow with the people who will run it, test it with real cases, and check whether it is actually faster than what it replaced.</p>

<h2>3. The business keeps changing and the platform does not</h2>
<p>New products launch, new vendors are onboarded, a business unit is acquired, a new jurisdiction becomes relevant. If the platform's picture of the business is not updated, its records, assessments and data maps decay. The privacy team then has two choices: trust information they know is stale, or work around the system.</p>
<p><strong>What helps:</strong> connect the platform to the moments when the business changes, such as project intake, vendor onboarding and system changes, so updates are triggered rather than remembered.</p>

<h2>4. New capabilities go unused</h2>
<p>Privacy platforms evolve quickly. Vendors add automation, integrations and reporting continuously. Organizations that treat go-live as the final configuration pay for capabilities they never switch on, while their teams keep doing by hand what the platform could now do for them.</p>
<p><strong>What helps:</strong> review releases on a regular schedule and decide deliberately which new features are worth adopting, and which are not.</p>

<h2>5. "Launched" was the only definition of success</h2>
<p>If the goal was to go live, the project succeeded the day it did. Nothing in that goal asks whether requests are completed faster, assessments are finished more consistently or leaders have better visibility. Without outcome measures there is no way to see the platform stalling, and no basis for defending its budget.</p>
<p><strong>What helps:</strong> agree a small set of measures before launch and review them on a fixed rhythm.</p>

<h2>A practical rhythm for keeping value flowing</h2>
<p>You do not need a large program to prevent a stall. A light, steady operating rhythm is usually enough:</p>
<ul>
<li><strong>An owner.</strong> One accountable person for the platform and its roadmap.</li>
<li><strong>A quarterly review.</strong> Usage, open issues, upcoming regulatory changes, and which new platform features are worth adopting.</li>
<li><strong>A short list of measures.</strong> For example, how long it takes to complete a data subject request, how long assessments stay open, and what share of vendors have a current review for their risk tier. Choose the few that matter to your leaders.</li>
<li><strong>A change backlog.</strong> A visible, ranked list of improvements so small fixes do not disappear.</li>
<li><strong>A regulatory horizon.</strong> A forward view of law changes that will require configuration updates, so changes are planned rather than rushed.</li>
</ul>

<h2>A quick check you can run this week</h2>
<p>If you already have a privacy platform, these questions will tell you quickly whether it is at risk:</p>
<ol>
<li>Can you name the person responsible for the platform today, and do they have time to do it?</li>
<li>When did someone last ask the people using it what slows them down?</li>
<li>Which processes still run mostly in spreadsheets or email, and why?</li>
<li>When was the information in the platform last compared with how the business actually operates?</li>
<li>Can you show leadership one or two numbers that prove the platform is saving time or reducing risk?</li>
</ol>
<p>If several of these are hard to answer, the platform is probably drifting. Drift is much cheaper to correct early than after a full re-implementation.</p>
""",
        "takeaways": [
            "Go-live is the start of the work that determines whether a platform pays back.",
            "Name an operational owner before launch, and give them time to do the job.",
            "Design workflows with the people who run them, and test with real cases.",
            "Trigger updates from business change, such as intake, onboarding and system changes.",
            "Agree a few outcome measures and review them every quarter.",
        ],
    },
    {
        "slug": "turning-privacy-regulation-into-workflows",
        "title": "From regulation to workflow: how to make privacy requirements operational",
        "short": "From regulation to workflow",
        "desc": "Legal requirements only reduce risk when they become work that teams actually do. A four-step method for translating privacy law into workflows your organization will adopt.",
        "body": """
<p class="lede">Privacy laws are written for lawyers and regulators. The work they require is done by customer service teams, marketers, engineers, procurement and HR. The gap between the two is where most compliance risk lives.</p>

<h2>The translation problem</h2>
<p>A policy that says "respond to data subject requests within the required time" is a legal statement. It does not tell a service agent where the request lands, who verifies identity, which systems to search, who approves the response or where the evidence is stored. Programs that stop at the policy rely on individual effort and good intentions. Programs that continue into workflow rely on process, and process scales.</p>

<h2>A four-step method</h2>
<h3>1. Break each requirement into obligations</h3>
<p>For every requirement, write down four things: what must happen, who is accountable, by when, and what evidence proves it happened. Most requirements turn out to be several obligations, each owned by a different team.</p>
<h3>2. Anchor each obligation in a process that already exists</h3>
<p>New projects already go through intake. New vendors already go through procurement. New hires already go through onboarding. Attaching privacy steps to these existing moments is far more reliable than inventing a separate form that people must remember to use.</p>
<h3>3. Design the workflow around the people running it</h3>
<p>Decide how work arrives, who it routes to, what reminders and escalations keep it moving, who approves, and how evidence is captured automatically. Ask each role what they need to finish their step in minutes, not hours. A workflow that respects people's time is one they will actually use.</p>
<h3>4. Configure technology last, and only what the process needs</h3>
<p>Once the process is clear, configure your platform to support it. Over-configuration is a common trap: every extra field, rule and exception becomes something to maintain when the law or the business changes.</p>

<h2>Three examples</h2>
<ul>
<li><strong>Data subject requests.</strong> Requests arrive through many channels, including web forms, email and customer service. A good workflow brings them into one queue, verifies identity, tracks the systems to search, routes reviews and stores the response and evidence together. The usual failure is requests that sit in an inbox outside the process.</li>
<li><strong>Privacy and data protection assessments.</strong> The best triggers come from project and system change, not from someone remembering. Questions are sized to risk, so low-risk projects move quickly and higher-risk ones get the attention they need, with clear decision rights.</li>
<li><strong>Vendor risk.</strong> Vendors are tiered by the data they handle and the impact of a failure. Diligence scales with the tier, renewals are tracked, and leaders get a view of risk without reading individual assessments.</li>
</ul>

<h2>Build once, map to many laws</h2>
<p>Organizations that operate in several jurisdictions often end up building a separate process for each law. A better approach is a common set of controls describing what the organization does, mapped to each applicable requirement describing why. When a law changes, you update the mapping and adjust the controls where needed, instead of rebuilding workflows from scratch.</p>

<h2>Traps to avoid</h2>
<ul>
<li><strong>Designing for the auditor instead of the user.</strong> If the process is painful, people will route around it, and the audit trail will show gaps.</li>
<li><strong>Over-customizing.</strong> Every exception you build is an exception you must maintain.</li>
<li><strong>Skipping evidence.</strong> If a step is not recorded, you cannot show it happened. Capture evidence as a by-product of the work.</li>
<li><strong>Treating training as a substitute for process.</strong> Training helps, but a well-designed process works even when people are busy.</li>
</ul>
""",
        "takeaways": [
            "A legal requirement only reduces risk once it becomes work that someone does.",
            "Break requirements into obligations with an owner, a deadline and evidence.",
            "Attach privacy steps to processes that already exist, such as intake and onboarding.",
            "Design for the people running the workflow, then configure technology last.",
            "Build a common control set and map it to many laws, instead of one process per law.",
        ],
    },
    {
        "slug": "questions-executives-should-ask-before-investing-in-privacy-technology",
        "title": "Eight questions executives should ask before investing in privacy technology",
        "short": "Eight questions executives should ask before investing",
        "desc": "Buying or expanding a privacy platform is a leadership decision, not only a technology one. Eight questions to ask before you commit budget, and what good answers sound like.",
        "body": """
<p class="lede">Privacy technology decisions often start in a vendor demo and end in a budget approval. The questions that decide whether the investment pays off are rarely about features. They are about ownership, process and what happens after launch. These eight are worth asking before you commit.</p>

<h2>1. What specific risk or decision does this improve?</h2>
<p><strong>Why it matters:</strong> Technology bought to "improve privacy" in general tends to be configured in general, and measured never.</p>
<p><strong>A good answer sounds like:</strong> "It cuts the time to fulfill data subject requests and gives us evidence for regulators," or "It lets us see third-party privacy risk by tier."</p>

<h2>2. Who will own it a year from now?</h2>
<p><strong>Why it matters:</strong> Projects have owners until they finish. Platforms need owners after.</p>
<p><strong>A good answer sounds like:</strong> A named role, with time set aside for the job and authority to decide on changes.</p>

<h2>3. Which processes will change, and are their owners involved?</h2>
<p><strong>Why it matters:</strong> A privacy platform changes how marketing, customer service, procurement and IT work. If those teams meet it for the first time at launch, adoption suffers.</p>
<p><strong>A good answer sounds like:</strong> The affected process owners have helped design the workflows and agreed their part.</p>

<h2>4. What do we already own?</h2>
<p><strong>Why it matters:</strong> Many organizations already have a privacy platform or other tools that cover part of the need. Buying something new before making the most of what exists adds cost and complexity.</p>
<p><strong>A good answer sounds like:</strong> A clear view of current capabilities, what is unused, and the specific gaps a new purchase would close.</p>

<h2>5. How will we know it is working?</h2>
<p><strong>Why it matters:</strong> "Go-live" is an event, not an outcome. Without measures, you cannot defend the budget or see problems early.</p>
<p><strong>A good answer sounds like:</strong> Two or three measures agreed before launch, such as request turnaround, assessment cycle time or vendor coverage, reviewed on a regular rhythm.</p>

<h2>6. How will it cope with laws that keep changing?</h2>
<p><strong>Why it matters:</strong> Requirements evolve. A setup tied tightly to today's rules becomes expensive to change.</p>
<p><strong>A good answer sounds like:</strong> A common control set mapped to requirements, a regulatory horizon someone watches, and a plan for configuration updates.</p>

<h2>7. What does it connect to, and who maintains the connections?</h2>
<p><strong>Why it matters:</strong> Value often depends on integrations with HR, CRM, ticketing, identity and data systems. Integrations break when upstream systems change.</p>
<p><strong>A good answer sounds like:</strong> A list of connected systems, a named technical owner for each, and a way to find out when something fails.</p>

<h2>8. What does it cost to run, beyond the license?</h2>
<p><strong>Why it matters:</strong> Licenses are the visible cost. Configuration, integration, ongoing tuning and the people time to operate the platform are often larger.</p>
<p><strong>A good answer sounds like:</strong> A multi-year view that includes people, change management and support, not just the subscription.</p>

<h2>Red flags</h2>
<ul>
<li>The decision rests mainly on a feature checklist.</li>
<li>No one can say who will own the platform after launch.</li>
<li>Success is defined as "launched".</li>
<li>The implementation plan has no post-launch phase.</li>
<li>Process owners outside the privacy team have not been consulted.</li>
</ul>

<h2>How to use these questions</h2>
<p>Bring them to vendor meetings, steering committees and budget reviews. Strong answers do not need to be long, but they should be specific. If the answers are vague, treat that as useful information: it usually means the foundations need attention before the technology does.</p>
""",
        "takeaways": [
            "Tie the investment to a specific risk or decision, not to privacy in general.",
            "Name the owner for after launch, and involve the teams whose work will change.",
            "Check what you already own before buying more.",
            "Agree outcome measures up front, and budget for running the platform, not just licensing it.",
        ],
    },
]

ARTICLES.insert(0, {
    "slug": "ai-privacy-regulation-zero-trust",
    "title": "AI is rewriting privacy risk: how to stay ahead with zero trust and privacy principles",
    "short": "AI, privacy regulation and zero trust",
    "desc": "AI is changing how personal data is used and how regulators respond. How organizations can stay ahead of shifting rules and keep trust, using zero trust and core privacy principles.",
    "body": """
<p class="lede">Artificial intelligence has not created an entirely new set of privacy problems. It has magnified the old ones: more personal data, used in more ways, by more systems, moving faster than most governance can follow. Regulators are responding, and the rules are still changing. The organizations that stay ahead will be the ones that build on durable principles, not on any single law.</p>

<h2>How AI is disrupting privacy</h2>
<p>Five shifts matter most for privacy and security leaders:</p>
<ul>
<li><strong>A growing appetite for data.</strong> Training, tuning and grounding AI systems often involves large volumes of personal data, which strains the principles of purpose limitation and data minimization.</li>
<li><strong>Inference and profiling.</strong> AI can infer sensitive details, such as health, finances or personal circumstances, from data that looked harmless on its own.</li>
<li><strong>Opacity.</strong> When an automated system influences a decision about a person, the organization must be able to explain it. That is hard when a model's reasoning is not easy to see.</li>
<li><strong>New ways for data to leak.</strong> Employees paste confidential or personal information into public AI tools. AI features appear inside software you already use, sometimes switched on without a privacy review. Prompts, outputs and logs become new places where personal data is stored.</li>
<li><strong>A larger attack surface.</strong> AI agents that can read data and take actions introduce new risks, including prompt injection and over-broad access. This is where privacy and security stop being separate problems.</li>
</ul>

<h2>How regulation is responding</h2>
<p>Three patterns stand out, and none of them depends on a single law.</p>
<ul>
<li><strong>Existing privacy laws already apply to AI.</strong> Requirements on transparency, lawful use of data, impact assessments and rights around automated decisions apply whether or not AI is mentioned. The GDPR's rules on solely automated decision-making are one long-standing example.</li>
<li><strong>AI-specific rules are arriving, unevenly.</strong> The EU AI Act takes a risk-based approach with obligations phased in over time, and the EU has moved to delay some high-risk obligations. In the U.S., states are acting individually: California's privacy regulator has adopted rules on automated decision-making technology, while Colorado has replaced its original AI law with a narrower one. The picture differs by jurisdiction and keeps shifting.</li>
<li><strong>Frameworks are becoming the common yardstick.</strong> Voluntary standards such as the NIST AI Risk Management Framework and ISO/IEC 42001 are increasingly used to show that a program is well run, even where they are not legally required.</li>
</ul>
<p>Across all three, the direction is consistent: more documentation, more impact assessment, more transparency, meaningful human oversight and tighter accountability for vendors. Because dates and scope change often, confirm the current position for the places you operate with your legal counsel.</p>

<h2>Why zero trust is the right security lens for AI</h2>
<p>Zero trust starts from a simple stance: do not grant access because something is "inside" the network. Verify every request, give only the access needed, and assume something may go wrong. NIST describes the approach in its zero trust architecture guidance. It suits AI well, because AI systems and the agents built on them behave like new, very fast users with very broad curiosity.</p>
<ul>
<li><strong>Verify explicitly.</strong> Give every user, service and AI agent a verified identity, and authenticate each request, not just the first.</li>
<li><strong>Use least privilege.</strong> Limit which data an AI system can reach, scope credentials narrowly and let them expire. An assistant that can see everything will eventually reveal something it should not.</li>
<li><strong>Assume breach.</strong> Segment data, log prompts, outputs and access, and monitor for unusual behavior. Plan for the day a model, a plug-in or a vendor is compromised.</li>
<li><strong>Verify continuously.</strong> Permissions that made sense at launch drift over time. Re-check them on a schedule.</li>
</ul>

<h2>Privacy principles are the design rules</h2>
<p>Zero trust protects data. Privacy principles decide whether the data should be used at all, and how. For AI they translate into practical rules:</p>
<ul>
<li><strong>Data minimization.</strong> Use the least personal data the use case needs, and prefer de-identified or synthetic data where it works.</li>
<li><strong>Purpose limitation.</strong> Decide what a data set may be used for before it goes anywhere near an AI system, and keep to it.</li>
<li><strong>Transparency.</strong> Tell people when AI is used and how it affects them, in plain language.</li>
<li><strong>Accountability.</strong> Give every AI use case a named owner, a record of what it does and evidence of the checks performed.</li>
<li><strong>Privacy by design and by default.</strong> Build protections in from the start, including retention and deletion rules for prompts, outputs and logs.</li>
</ul>

<h2>Where the two meet</h2>
<p>Zero trust and privacy ask the same questions from different angles: who or what is accessing which data, for what purpose, for how long, and what evidence do we have? Treating them as one program avoids duplicated controls and gaps between security and privacy teams. A single set of controls covering data classification, access policy, logging, vendor review and assessments can serve both, and can be mapped to many laws and frameworks at once.</p>

<h2>A practical playbook</h2>
<ol>
<li><strong>Find your AI.</strong> Build a register of AI use across the organization, including tools staff adopted on their own and AI features embedded in existing software. Record the owner, vendor, data involved and purpose.</li>
<li><strong>Set data rules.</strong> Classify data, and state plainly what may and may not be entered into AI tools. Give people approved options, so they are not tempted to use unapproved ones.</li>
<li><strong>Tier by risk.</strong> Extend your privacy and data protection assessments to cover AI. Use light checks for low-risk uses and deeper review for anything affecting people's rights, finances, health or employment.</li>
<li><strong>Apply zero trust to AI.</strong> Give agents and services their own identities, apply least-privilege access and segmentation, and keep logging and monitoring in place.</li>
<li><strong>Tighten vendor oversight.</strong> Ask whether your data is used to train models, how long it is kept, who the sub-processors are and what security evidence the vendor can provide. Write the answers into contracts.</li>
<li><strong>Keep a regulatory horizon.</strong> Assign someone to track changes, map your controls to the laws and frameworks that apply, and review the picture every quarter so updates are planned, not rushed.</li>
</ol>

<h2>Staying ahead without chasing every rule</h2>
<p>New AI rules will keep appearing, and some will be delayed, narrowed or replaced. Programs built around one regulation have to be rebuilt each time. Programs built on a small set of durable principles, applied through well-designed workflows, adapt with a mapping update. Our articles on <a href="/insights/turning-privacy-regulation-into-workflows/">turning privacy regulation into workflows</a> and <a href="/insights/why-privacy-platforms-stall-after-go-live/">why privacy platforms stall after go-live</a> show how to make that stick, and <a href="/insights/questions-executives-should-ask-before-investing-in-privacy-technology/">eight questions executives should ask before investing in privacy technology</a> is a useful checklist for leaders.</p>

<h2>Sources and further reading</h2>
<ul>
<li>European Commission: <a href="https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai" target="_blank" rel="noopener noreferrer">Regulatory framework for AI</a></li>
<li>CMS: <a href="https://cms.law/en/gbr/publication/the-eu-s-digital-omnibus-on-ai-what-the-provisional-agreement-really-changes" target="_blank" rel="noopener noreferrer">The EU's Digital Omnibus on AI: what the provisional agreement really changes</a></li>
<li>Skadden: <a href="https://www.skadden.com/insights/publications/2026/06/colorado-repeals-and-replaces-its-ai-act" target="_blank" rel="noopener noreferrer">Colorado repeals and replaces its AI Act</a></li>
<li>NIST: <a href="https://csrc.nist.gov/pubs/sp/800/207/final" target="_blank" rel="noopener noreferrer">SP 800-207, Zero Trust Architecture</a></li>
<li>NIST: <a href="https://www.nist.gov/itl/ai-risk-management-framework" target="_blank" rel="noopener noreferrer">AI Risk Management Framework</a></li>
</ul>
""",
    "takeaways": [
        "AI magnifies existing privacy risk: more data, more inference and more ways for data to leak.",
        "Existing privacy laws already apply to AI, and AI-specific rules are arriving unevenly and keep shifting.",
        "Zero trust protects the data AI touches; privacy principles decide whether and how that data is used.",
        "Start with a register of AI use, clear data rules, risk-tiered assessments and a vendor review.",
        "Build on durable principles and map them to many laws, so each new rule is an update, not a rebuild.",
    ],
})

INDUSTRIES = [
    {
        "slug": "financial-services",
        "name": "Financial services",
        "title": "Privacy technology for financial services",
        "desc": "Sensitive financial data, close regulator attention and heavy reliance on third parties. How Privaryn designs privacy programs and technology for financial services organizations.",
        "lead": "Sensitive financial data, close regulator attention and heavy reliance on third parties make financial services one of the most demanding places to run a privacy program.",
        "pressures": [
            ("Sensitive data, everywhere", "Customer financial and identity data sits across core systems, channels and partners. That makes data mapping, retention and access requests harder to run consistently."),
            ("Regulators who ask for evidence", "It is not enough for a control to exist. Teams need to show that it ran, who approved it and when. In the U.S., financial institutions also face sector rules such as the Gramm-Leach-Bliley Act, alongside state and global privacy laws."),
            ("Reliance on third parties", "Processors, technology partners and other vendors handle customer data on your behalf. Third-party risk is privacy risk, and it needs a process that scales with the number of vendors."),
        ],
        "help": [
            ("Third-party risk and GRC", "Risk-tiered vendor intake, assessment workflows and reporting that gives leaders a clear view of exposure."),
            ("Privacy operations", "Data subject request and assessment workflows that capture evidence as the work happens, so you can show regulators what was done."),
            ("Data discovery and governance", "A clear picture of where personal data lives, how it moves and how long it is kept."),
            ("Consent and preferences", "Marketing and communication preferences managed consistently across channels and jurisdictions."),
        ],
    },
    {
        "slug": "telecommunications",
        "name": "Telecommunications",
        "title": "Privacy technology for telecommunications",
        "desc": "Large volumes of customer data, where consent, retention and data subject requests have to work at scale. How Privaryn designs privacy programs for telecommunications organizations.",
        "lead": "Large volumes of customer data mean consent, retention and data subject requests have to work at scale, across many systems and customer touchpoints.",
        "pressures": [
            ("Scale and system sprawl", "Large customer bases and many systems for billing, network, retail and support make it hard to find data quickly and respond to requests on time."),
            ("Sector rules on top of privacy law", "In the U.S., carriers also face rules about customer network information, on top of general state and global privacy laws, so controls need to reflect more than one set of requirements."),
            ("Retention for many reasons", "Data is kept for billing, network operations and legal obligations. Clear retention schedules, applied consistently, are essential and difficult."),
        ],
        "help": [
            ("Privacy operations", "Request fulfillment that works across many systems, with automation for intake, routing, reminders and evidence."),
            ("Consent and preferences", "Preference management across retail, app, web and contact center channels, with rules that vary by region."),
            ("Data discovery and governance", "Discovery, classification and retention programs that reflect how data is really used."),
            ("Third-party risk and GRC", "Vendor and partner oversight tiered by the data involved."),
        ],
    },
    {
        "slug": "media-entertainment",
        "name": "Media and entertainment",
        "title": "Privacy technology for media and entertainment",
        "desc": "Fan, subscriber and audience data, with consent and digital rights questions across many platforms. How Privaryn designs privacy programs for media, entertainment and sports organizations.",
        "lead": "Fan, subscriber and audience data, with consent and digital rights questions across many platforms, make privacy a daily operating issue for media and entertainment.",
        "pressures": [
            ("Audience data across many platforms", "Websites, apps, streaming services, ticketing and partners all collect and share data. Knowing what is collected where, and under what consent, is the starting point."),
            ("Consent and tracking at scale", "Digital properties depend on advertising and measurement, so cookie and preference management has to be accurate, current and different by region."),
            ("Special categories of audience", "Children's data and viewing information carry additional rules in many places. In sports, ticketing, membership, fan engagement and athlete data move between venues, apps and partners."),
        ],
        "help": [
            ("Consent and preferences", "Cookie and tracking consent, preference centers and regional rules that stay accurate as properties change."),
            ("Data discovery and governance", "A clear map of audience data and how it flows between platforms and partners."),
            ("Privacy operations", "Request and assessment workflows for launches, campaigns and partnerships."),
            ("Third-party risk and GRC", "Oversight of the many vendors and partners that handle fan and subscriber data."),
        ],
    },
]

CHECKLIST = {
    "slug": "privacy-technology-readiness-checklist",
    "title": "Privacy technology readiness checklist",
    "desc": "A one-page checklist to find out whether your privacy platform and program are set up to deliver, across ownership, process, configuration and measurement.",
    "groups": [
        ("Ownership and governance", [
            "A named person owns the privacy platform and has time set aside for the role.",
            "There is a clear owner for each privacy workflow, including the teams outside privacy.",
            "Someone decides when and how the platform changes, and the decision is recorded.",
            "Leadership receives regular reporting on the program, not only when something goes wrong.",
            "The platform and its roadmap are reviewed at least quarterly.",
        ]),
        ("Process design", [
            "Each key workflow was designed with the people who run it.",
            "Privacy steps are attached to existing processes such as project intake, vendor onboarding and system change.",
            "Requests and assessments arrive through defined channels, not scattered inboxes.",
            "Reminders, escalations and approvals are defined for every workflow.",
            "Requirements are broken into obligations with an owner, a deadline and evidence.",
        ]),
        ("Platform and configuration", [
            "We know which platform features we use and which we have not switched on.",
            "Workflows are no slower than the spreadsheets and email they replaced.",
            "Integrations to HR, CRM, ticketing and data systems have named owners.",
            "Data maps, records of processing and vendor lists reflect how the business runs today.",
            "Evidence is captured automatically as the work happens.",
        ]),
        ("Measurement and change", [
            "We track two or three outcome measures, such as request turnaround or assessment cycle time.",
            "We have a ranked list of improvements, and small fixes do not disappear.",
            "Someone watches upcoming law changes and plans configuration updates in advance.",
            "We ask the people using the platform what slows them down, at least twice a year.",
            "We can show leadership how the platform saves time or reduces risk.",
        ]),
    ],
}

# ------------------------------------------------------------------ helpers

def css_version():
    import hashlib
    with open(os.path.join(ROOT, "styles.css"), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]

def words(html_text):
    return len(re.sub(r"<[^>]+>", " ", html_text).split())

def read_minutes(body):
    return max(3, math.ceil(words(body) / 210))

def url(path):
    return SITE + path

def head(title, desc, path, og_type="website", jsonld=None, extra=""):
    ld = ""
    for obj in (jsonld or []):
        ld += '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>\n"
    full_title = escape(title + " | Privaryn")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{escape(desc, quote=True)}">
<link rel="canonical" href="{url(path)}">
<meta name="theme-color" content="#121a2c">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Privaryn">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(desc, quote=True)}">
<meta property="og:url" content="{url(path)}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title, quote=True)}">
<meta name="twitter:description" content="{escape(desc, quote=True)}">
<meta name="twitter:image" content="{SITE}/og-image.png">
<link rel="preload" href="/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/newsreader-latin.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.classList.add("js")</script>
<link rel="stylesheet" href="/styles.css?v={css_version()}">
{extra}{ld}</head>
"""

def header(current=""):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    return f"""<body>
<a class="skip" href="#main">Skip to main content</a>
<header>
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="Privaryn home"><img src="/logo.png" alt="Privaryn" width="184" height="52"></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="primary" aria-label="Menu"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    <nav id="primary" aria-label="Primary">
      <ul>
        {a("/", "Home", "home")}
        {a("/#services", "Services", "services")}
        {a("/#industries", "Industries", "industries")}
        {a("/insights/", "Insights", "insights")}
        {a("/#about", "About", "about")}
        {a("/#contact", "Contact", "contact")}
      </ul>
    </nav>
    <a class="btn top" href="/#contact">Start a conversation</a>
  </div>
</header>
"""

CTA = f"""<div class="cta">
  <div class="wrap">
    <div><h2>Ready to get more from your privacy technology?</h2><p>Whether you are fixing what is broken, automating what is manual or starting fresh, let's talk.</p></div>
    <div class="actions"><a class="btn dark" href="/#contact">Start a conversation</a><a class="btn ghost" href="{CAL}" target="_blank" rel="noopener noreferrer" aria-label="Book a 30-minute call (opens Calendly in a new tab)">Book a 30-minute call</a></div>
  </div>
</div>
"""

FOOT_JS = r'''<script>
(function(){var mb=document.querySelector(".menu-btn"),nav=document.getElementById("primary");if(mb&&nav)mb.addEventListener("click",function(){var o=nav.classList.toggle("open");mb.setAttribute("aria-expanded",o?"true":"false");});
if(!("IntersectionObserver" in window)||window.matchMedia("(prefers-reduced-motion: reduce)").matches)return;
var els=document.querySelectorAll(".cols>div,.list>div,.takeaways,.ins-item,.prose h2");
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target);}});},{threshold:.1,rootMargin:"0px 0px -5% 0px"});
els.forEach(function(el){el.classList.add("rv");io.observe(el);});})();
</script>
</body>
</html>
'''

def footer():
    return f"""<footer>
  <div class="wrap">
    <div class="f-top">
      <div><img src="/logo.png" alt="Privaryn" width="120" height="34"><p>Privacy technology consulting that turns regulation into working, automated programs.</p></div>
      <div><p class="fh">Insights</p><ul>{"".join(f'<li><a href="/insights/{a["slug"]}/">{escape(a["short"])}</a></li>' for a in ARTICLES)}<li><a href="/resources/{CHECKLIST["slug"]}/">Readiness checklist</a></li></ul></div>
      <div><p class="fh">Industries</p><ul>{"".join(f'<li><a href="/industries/{i["slug"]}/">{escape(i["name"])}</a></li>' for i in INDUSTRIES)}</ul></div>
      <div><p class="fh">Company</p><ul><li><a href="/#about">About</a></li><li><a href="/#contact">Contact</a></li><li><a href="{CAL}" target="_blank" rel="noopener noreferrer" aria-label="Book a 30-minute call (opens Calendly in a new tab)">Book a 30-minute call</a></li><li><a href="/#privacy">Privacy notice</a></li></ul></div>
    </div>
    <div class="f-bot">
      <p class="pf">A privacy-first website: no trackers, no third-party fonts, and nothing loads from other companies until you choose to. See our <a href="/#privacy">privacy notice</a>.</p>
      <p>&copy; 2026 Privaryn. All rights reserved.</p>
      <p><button type="button" class="linkbtn" onclick="window.scrollTo(0,0)">Back to top &uarr;</button></p>
      <p>The views expressed are my own and do not constitute legal advice, nor do they constitute an attorney-client relationship. They do not represent the views of any employer or other company.</p>
    </div>
  </div>
</footer>
""" + FOOT_JS


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def org_ref():
    return {"@type": "Organization", "name": "Privaryn", "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/apple-touch-icon.png"}}

def crumbs(items):
    out = ['<a href="/">Home</a>']
    for href, label in items[:-1]:
        out.append(f'<a href="{href}">{escape(label)}</a>')
    out.append(escape(items[-1][1]))
    return '<p class="crumbs">' + " / ".join(out) + "</p>"

def breadcrumb_ld(items):
    elems = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for n, (href, label) in enumerate(items, start=2):
        elems.append({"@type": "ListItem", "position": n, "name": label, "item": SITE + href})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elems}

# ------------------------------------------------------------------ builders

def build_article(a, others):
    path = f"/insights/{a['slug']}/"
    mins = read_minutes(a["body"])
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
         "datePublished": PUBLISHED, "dateModified": PUBLISHED, "image": SITE + "/og-image.png",
         "mainEntityOfPage": url(path), "author": {"@type": "Person", "name": "Dev Sareen"}, "publisher": org_ref()},
        breadcrumb_ld([("/insights/", "Insights"), (path, a["short"])]),
    ]
    takeaways = "".join(f"<li>{escape(t)}</li>" for t in a["takeaways"])
    keep = "".join(f'<li><a href="/insights/{o["slug"]}/">{escape(o["title"])}</a></li>' for o in others)
    keep += f'<li><a href="/resources/{CHECKLIST["slug"]}/">Privacy technology readiness checklist (one page)</a></li>'
    html = head(a["title"], a["desc"], path, "article", ld) + header("insights") + f"""
<main id="main">
  <div class="page-head article-head"><div class="wrap">
    {crumbs([("/insights/", "Insights"), (path, a["short"])])}
    <h1>{escape(a["title"])}</h1>
    <p class="a-meta"><span>By Dev Sareen</span><span>{PUBLISHED_HUMAN}</span><span>{mins} min read</span></p>
  </div></div>
  <section><div class="wrap"><article class="prose">
{a["body"]}
<div class="takeaways"><h3>Key takeaways</h3><ul>{takeaways}</ul></div>
<div class="a-cta">
  <h3>Want to talk this through for your organization?</h3>
  <p>We help teams design, build and run privacy programs that last. <a href="{CAL}" target="_blank" rel="noopener noreferrer" aria-label="Book a 30-minute call (opens Calendly in a new tab)">Book a 30-minute call</a> or <a href="/#contact">send us a note</a>.</p>
</div>
<h3>Keep reading</h3>
<ul class="keep">{keep}</ul>
  </article></div></section>
</main>
""" + CTA + footer()
    write(f"insights{path[len('/insights'):]}index.html", html)
    return mins

def build_insights_index(mins):
    path = "/insights/"
    desc = "Practical thinking on privacy technology, program design and compliance with global privacy laws, from Privaryn."
    items = ""
    for a in ARTICLES:
        items += f"""<a class="ins-item" href="/insights/{a["slug"]}/"><time datetime="{PUBLISHED}">{PUBLISHED_HUMAN}<br>{mins[a["slug"]]} min read</time><div><h2>{escape(a["title"])}</h2><p>{escape(a["desc"])}</p></div></a>
"""
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Privaryn Insights", "url": url(path), "description": desc},
          breadcrumb_ld([(path, "Insights")])]
    html = head("Insights", desc, path, "website", ld) + header("insights") + f"""
<main id="main">
  <div class="page-head"><div class="wrap">
    {crumbs([(path, "Insights")])}
    <h1>Insights.</h1>
    <p class="lead">Practical thinking on privacy technology, program design and compliance with global privacy laws.</p>
  </div></div>
  <section><div class="wrap">
    <div class="ins-list">
{items}    </div>
    <div class="res-card">
      <p class="eyebrow">Resource</p>
      <h2>Privacy technology readiness checklist</h2>
      <p>A one-page checklist to find out whether your platform and program are set up to deliver. Free to use and print, with no sign-up.</p>
      <a class="btn ghost" href="/resources/{CHECKLIST["slug"]}/">Open the checklist</a>
    </div>
  </div></section>
</main>
""" + CTA + footer()
    write("insights/index.html", html)

def build_checklist():
    c = CHECKLIST
    path = f"/resources/{c['slug']}/"
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": c["title"], "description": c["desc"], "url": url(path),
           "author": {"@type": "Person", "name": "Dev Sareen"}, "publisher": org_ref(), "datePublished": PUBLISHED},
          breadcrumb_ld([("/insights/", "Insights"), (path, "Readiness checklist")])]
    groups = ""
    n = 0
    for title, items in c["groups"]:
        rows = ""
        for it in items:
            n += 1
            rows += f'<label class="cl-item"><input type="checkbox" data-cl><span>{escape(it)}</span></label>\n'
        groups += f'<div class="cl-group"><h2>{escape(title)}</h2>\n{rows}</div>\n'
    total = n
    html = head(c["title"], c["desc"], path, "website", ld, "") + header("insights") + f"""
<main id="main">
  <div class="page-head"><div class="wrap">
    <div class="noprint">{crumbs([("/insights/", "Insights"), (path, "Readiness checklist")])}</div>
    <h1>{escape(c["title"])}.</h1>
    <p class="lead">Tick each statement that is true for your organization today. Be honest: the gaps are where the value is.</p>
  </div></div>
  <section><div class="wrap">
    <div class="cl-wrap">
      <div class="cl-grid">
{groups}      </div>
      <div class="cl-score" aria-live="polite">
        <p class="cl-count"><strong id="cl-n">0</strong> of {total} ticked</p>
        <p id="cl-msg">Tick the statements that are true today to see where you stand.</p>
        <p class="cl-note">This checklist is a conversation starter, not an assessment, and does not constitute legal advice.</p>
        <div class="actions noprint"><button type="button" class="btn" onclick="window.print()">Print or save as PDF</button><a class="btn ghost" href="{CAL}" target="_blank" rel="noopener noreferrer" aria-label="Book a 30-minute call (opens Calendly in a new tab)">Talk it through</a></div>
        <p class="cl-print">Privaryn | privarynadvisory.com</p>
      </div>
    </div>
  </div></section>
</main>
<div class="noprint">{CTA}</div>
<script>
(function(){{var boxes=document.querySelectorAll("[data-cl]"),n=document.getElementById("cl-n"),m=document.getElementById("cl-msg"),t={total};
function upd(){{var c=0;boxes.forEach(function(b){{if(b.checked)c++;}});n.textContent=c;
m.textContent=c===0?"Tick the statements that are true today to see where you stand.":c<=7?"Several foundations are missing. This is common, and it is the best time to fix them: start with ownership and one or two outcome measures.":c<=14?"You have a good base with some gaps. Focus on the unticked items in the group with the fewest ticks.":"You are in a strong position. Keep the rhythm going: quarterly reviews, a regulatory horizon and regular check-ins with the people using the platform.";}}
boxes.forEach(function(b){{b.addEventListener("change",upd);}});upd();}})();
</script>
""" + footer()
    write(f"resources/{c['slug']}/index.html", html)

def build_industry(ind):
    path = f"/industries/{ind['slug']}/"
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": ind["title"], "description": ind["desc"], "url": url(path), "publisher": org_ref()},
          breadcrumb_ld([("/#industries", "Industries"), (path, ind["name"])])]
    pressures = "".join(f"<div><h3>{escape(t)}</h3><p>{escape(d)}</p></div>" for t, d in ind["pressures"])
    helps = "".join(f"<div><p><strong>{escape(t)}</strong>{escape(d)}</p></div>" for t, d in ind["help"])
    rel = "".join(f'<li><a href="/insights/{a["slug"]}/">{escape(a["title"])}</a></li>' for a in ARTICLES)
    others = "".join(f'<a class="btn ghost" href="/industries/{o["slug"]}/">{escape(o["name"])}</a>' for o in INDUSTRIES if o["slug"] != ind["slug"])
    html = head(ind["title"], ind["desc"], path, "website", ld) + header("industries") + f"""
<main id="main">
  <div class="page-head"><div class="wrap">
    {crumbs([("/#industries", "Industries"), (path, ind["name"])])}
    <p class="eyebrow">Industries</p>
    <h1>{escape(ind["title"])}.</h1>
    <p class="lead">{escape(ind["lead"])}</p>
  </div></div>
  <section class="alt"><div class="wrap">
    <h2>What we see in the sector.</h2>
    <p class="sub">Each sector carries its own data, risks and regulators. These are the pressures we design around.</p>
    <div class="cols">{pressures}</div>
  </div></section>
  <section><div class="wrap journey">
    <div>
      <h2>How we help.</h2>
      <p class="sub" style="margin-bottom:28px">The same practice areas, shaped around how your organization operates and the regulators you answer to.</p>
      <a class="btn ghost" href="/#services">All practice areas</a>
    </div>
    <div class="list rows">{helps}</div>
  </div></section>
  <section class="alt"><div class="wrap">
    <h2>Related reading.</h2>
    <ul class="keep" style="max-width:720px">{rel}<li><a href="/resources/{CHECKLIST["slug"]}/">Privacy technology readiness checklist (one page)</a></li></ul>
    <p class="sub" style="margin:40px 0 18px">Other sectors</p>
    <div class="actions">{others}<a class="btn ghost" href="/#industries">All industries</a></div>
  </div></section>
</main>
""" + CTA + footer()
    write(f"industries{path[len('/industries'):]}index.html", html)

def update_sitemap():
    urls = ["/", "/insights/"] + [f"/insights/{a['slug']}/" for a in ARTICLES] + [f"/resources/{CHECKLIST['slug']}/"] + [f"/industries/{i['slug']}/" for i in INDUSTRIES]
    rows = ""
    for u in urls:
        pr = "1.0" if u == "/" else ("0.8" if u.count("/") == 2 else "0.7")
        rows += f"  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{PUBLISHED}</lastmod>\n    <changefreq>{'weekly' if u == '/' else 'monthly'}</changefreq>\n    <priority>{pr}</priority>\n  </url>\n"
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "</urlset>\n")

def sync_index_css():
    path = os.path.join(ROOT, "index.html")
    with open(path, encoding="utf-8") as f:
        h = f.read()
    h2 = re.sub(r'href="styles\.css(\?v=[0-9a-f]+)?"', 'href="styles.css?v=' + css_version() + '"', h, count=1)
    if h2 != h:
        with open(path, "w", encoding="utf-8") as f:
            f.write(h2)

def sync_home_teaser():
    """Keep the home page's 'latest insights' cards in step with the newest three articles."""
    path = os.path.join(ROOT, "index.html")
    with open(path, encoding="utf-8") as f:
        h = f.read()
    cards = "".join(
        f'<article class="card"><h3><a href="insights/{a["slug"]}/" style="text-decoration:none">{a["title"]}</a></h3><p>{a["desc"]}</p></article>'
        for a in ARTICLES[:3]
    )
    m = re.search(r'(<section class="alt" id="insights-teaser">.*?<div class="cards" style="grid-template-columns:repeat\(3,1fr\)">)(.*?)(</div>\s*</div>\s*</section>)', h, re.S)
    if not m:
        return
    h2 = h[:m.start(2)] + cards + h[m.end(2):]
    if h2 != h:
        with open(path, "w", encoding="utf-8") as f:
            f.write(h2)

def main():
    mins = {}
    for a in ARTICLES:
        others = [o for o in ARTICLES if o["slug"] != a["slug"]]
        mins[a["slug"]] = build_article(a, others)
    build_insights_index(mins)
    build_checklist()
    for i in INDUSTRIES:
        build_industry(i)
    update_sitemap()
    sync_home_teaser()
    sync_index_css()
    print("built:", len(ARTICLES), "articles,", len(INDUSTRIES), "industry pages, 1 checklist, index, sitemap")

if __name__ == "__main__":
    main()
