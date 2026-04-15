# main.py

from fastapi import FastAPI
from schemas import AgentCreate, UsageCreate
from services import (
    add_agent_service,
    list_agents_service,
    search_agents_service,
    log_usage_service,
    usage_summary_service
)

# Create FastAPI app
app = FastAPI(title="Autonomous Agent System with FastAPI + LangChain")


# -------- AGENT APIs -------- #

@app.post("/agents")
def add_agent(agent: AgentCreate):
    """
    API to register a new agent.
    """
    return add_agent_service(agent)


@app.get("/agents")
def list_agents():
    """
    API to list all agents.
    """
    return list_agents_service()


@app.get("/search")
def search_agents(q: str):
    """
    API to search agents by query.
    """
    return search_agents_service(q)


# -------- USAGE APIs -------- #

@app.post("/usage")
def log_usage(data: UsageCreate):
    """
    API to log usage between agents.
    """
    return log_usage_service(data)


@app.get("/usage-summary")
def usage_summary():
    """
    API to get aggregated usage summary.
    """
    return usage_summary_service()