# storage.py

# Stores all registered agents
agents = {}

# Stores usage logs
usage_logs = []

# Tracks processed request_ids (for idempotency)
processed_requests = set()