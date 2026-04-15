# Autonomous Agent System

## Overview

In this assignment, I built a simple system where different agents (tools/services) can:

- Register themselves  
- Be discovered using search  
- Interact with each other  
- Have their usage tracked  

The idea is similar to a small platform where agents can call other agents and we keep track of how much they are used.

---

## What I Built

I implemented the following:

### 1. Agent Registration
- Add a new agent with name, description, and endpoint  
- Store agents in memory  

### 2. Agent Listing and Search
- View all registered agents  
- Search agents based on name or description (case-insensitive)  

### 3. Usage Logging
- Log when one agent uses another  
- Each request has a `request_id`  

To avoid duplicate logging, I used a set to track processed request IDs.

---

### 4. Usage Summary
- Returns total usage per agent  
- Calculated dynamically from stored logs  

---

## AI / Bonus Part

For the bonus part, I used LangChain to generate tags from the agent description.

Example:

Input:
"Extracts structured data from PDFs"

Output:
["pdf", "data", "extraction"]

If the LLM fails (for example due to API issues), I added a simple fallback method using basic keyword extraction so the system still works.

---

## Project Structure

- `main.py` → Handles API routes  
- `services.py` → Contains main logic  
- `storage.py` → Stores data in memory  
- `schemas.py` → Input validation using Pydantic  
- `llm.py` → Handles LangChain logic  

---

## How to Run

 Install dependencies:
 pip install -r requirements.txt
 Run the server --> uvicorn main:app --reload




4. Open:
http://127.0.0.1:8000/docs

---

## Edge Cases Handled

- If an agent does not exist → returns error  
- If the same request is sent twice → ignored  
- Missing fields → handled using validation  

---

## Design Thoughts

### Billing without double charging
To avoid double counting, I used `request_id` and stored it in a set.  
If the same request comes again, it is ignored.  
In a real system, this can be stored in a database with a unique constraint.

---

### Scaling the system
If the system grows:

- Replace in-memory storage with a database (like PostgreSQL)  
- Add indexing for faster search  
- Use caching (like Redis)  
- Possibly split into services  

---

## AI Usage

Yes, I used ChatGPT to understand the problem better and structure the solution.

I mainly used it for:
- Planning the approach  
- Improving code structure  
- Checking edge cases  

However, I wrote the logic myself and made changes wherever needed to ensure I understood everything.

---

## Final Note

I tried to keep the system simple but focused on handling real-world cases like duplicate requests and validation.  