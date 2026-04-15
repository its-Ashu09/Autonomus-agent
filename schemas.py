# schemas.py

from pydantic import BaseModel

class AgentCreate(BaseModel):
    name: str
    description: str
    endpoint: str


class UsageCreate(BaseModel):
    caller: str
    target: str
    units: int
    request_id: str