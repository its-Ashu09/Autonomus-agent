# services.py

from storage import agents, usage_logs, processed_requests
from llm import generate_tags


# ---------------- AGENT FUNCTIONS ---------------- #

def add_agent_service(agent):
    """
    This function handles adding a new agent.
    """

    # Check if agent already exists (avoid duplicates)
    if agent.name in agents:
        return {"error": "Agent already exists"}

    # Generate tags using LLM (bonus feature)
    tags = generate_tags(agent.description)

    # Convert Pydantic object to dictionary
    agent_data = agent.dict()

    # Add generated tags to agent data
    agent_data["tags"] = tags

    # Store agent in memory
    agents[agent.name] = agent_data

    return {
        "message": "Agent added successfully",
        "agent": agent_data
    }


def list_agents_service():
    """
    Returns all registered agents.
    """
    return list(agents.values())


def search_agents_service(query: str):
    """
    Search agents based on name or description.
    Case-insensitive search.
    """

    result = []

    for agent in agents.values():
        # Convert both to lowercase for case-insensitive match
        if query.lower() in agent["name"].lower() or query.lower() in agent["description"].lower():
            result.append(agent)

    return result


# ---------------- USAGE FUNCTIONS ---------------- #

def log_usage_service(data):
    """
    Logs usage between agents.
    Also handles edge cases like duplicates and invalid agents.
    """

    # Check if target agent exists
    if data.target not in agents:
        return {"error": "Target agent not found"}

    # Idempotency check: prevent duplicate request
    if data.request_id in processed_requests:
        return {"message": "Duplicate request ignored"}

    # Mark request as processed
    processed_requests.add(data.request_id)

    # Store usage log
    usage_logs.append(data.dict())

    return {"message": "Usage logged successfully"}


def usage_summary_service():
    """
    Aggregates total usage per target agent.
    """

    summary = {}

    for log in usage_logs:
        target = log["target"]

        # Add units to existing total OR initialize
        summary[target] = summary.get(target, 0) + log["units"]

    return summary