# Backend Server (Django)
A server which provides user to perform three tasks:-
  1. CRUD operations for agents: User can add agents organizing campaigns
  2. CRUD operations for Campaigns: User can add campaigns information(organize campaigns) by particular agents
  3. CRUD operations for Campaign-Results: User can add the information about the results of those campaigns.

a. Agents API:
  1. POST /api/agents/ - Create a new agent
  2. GET /api/agents/ - List all agents (supports pagination)
  3. GET /api/agents/{id}/ - Retrieve a single agent by ID
  4. PUT /api/agents/{id}/ - Update an agent
  5. DELETE /api/agents/{id}/ - Delete an agent
b.  Campaigns API:
    Similar to agents, using ```/api/campaigns/```.
c.  Campaign Results API:
    Similar to agents, using ```/api/campaign-results/```.
