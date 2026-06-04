import os
from crewai import Agent, Task, Crew, Process

# Data Sovereignty Enforced: Guaranteeing data remains localized on African soil
os.environ["OPENAI_API_BASE"] = "https://api.local-sovereign-node.ke/v1"
os.environ["AWS_DEFAULT_REGION"] = "af-south-1"  # AWS Africa (Cape Town) Cloud Region

# --- 1. AGENT DEFINITIONS (RANK CALIBRATED BOUNDARIES) ---

scout_agent = Agent(
    role='Financial Literacy Coach',
    goal='Provide text-based harvest-cycle savings advice in Sheng over USSD/SMS channels.',
    backstory='A supportive, encouraging market auntie who uses marketplace metaphors to build capacity.',
    verbose=True,
    allow_delegation=False,
    multiplier_boundary="Max 3 SMS alerts daily. Hard stop if predatory loan sharks are mentioned.",
    temperature=0.70  # Moderately higher temperature to allow creative, empathetic local phrasing
)

guardian_agent = Agent(
    role='Loan Triage Risk Auditor',
    goal='Process Tier-1 loan applications under KES 15,000 using cash-velocity data loops.',
    backstory='A strict risk engine auditor configured to verify variable incomes against harvest cycles.',
    verbose=True,
    allow_delegation=True,
    multiplier_boundary="Approve <= KES 15,000 only. Instantly escalate via USSD *#733# if flagged.",
    temperature=0.0  # Zero temperature to guarantee strict, repeatable financial calculations
)

hunter_agent = Agent(
    role='Human-In-The-Loop Coordinator',
    goal='Organize context-rich credit application briefing packets for human review.',
    backstory='An operational coordinator focused on preparing complete risk packets for human loan officers.',
    verbose=True,
    allow_delegation=False,
    temperature=0.1
)

# --- 2. TASK DEFINITIONS (TRAIL MEMORY LAYERS & HUNT TRIGGERS) ---

literacy_coaching_task = Task(
    description='Analyze incoming user message "No money for school fees" and check family harvest timelines.',
    expected_output='A 3-sentence Sheng response providing empathetic harvest savings advice without mentioning active loans.',
    agent=scout_agent
)

credit_triage_task = Task(
    description='Evaluate a KES 28,000 credit application from a 42-year-old maize farmer in Kakamega.',
    expected_output='An enriched financial risk packet mapping seasonal cash flow variances and historical chama savings.',
    agent=guardian_agent
)

human_coordination_task = Task(
    description='Review risk flags and assign the application to an available regional agricultural credit officer.',
    expected_output='Final Output: "Applicant: Grace, 42. Income peaks Oct/Nov. Request: KES 28,000. Risk: None. Action: Cross-sell drought insurance."',
    agent=hunter_agent
)

# --- 3. SYSTEM ORCHESTRATION ---

ujima_credit_pride = Crew(
    agents=[scout_agent, guardian_agent, hunter_agent],
    tasks=[literacy_coaching_task, credit_triage_task, human_coordination_task],
    process=Process.sequential,
    memory=True,  # All tracking memory layers are fully isolated on local servers
    verbose=True
)

# Launch Agent Execution 
# outcome_portfolio = ujima_credit_pride.kickoff()
