# Backend Server (Django)
A server which provides user to perform three tasks:-
  1. CRUD operations for agents: User can add agents organizing campaigns
  2. CRUD operations for Campaigns: User can add campaigns information(organize campaigns) by particular agents
  3. CRUD operations for Campaign-Results: User can add the information about the results of those campaigns.

1. Agents API:
    POST /api/agents/ - Create a new agent
    GET /api/agents/ - List all agents (supports pagination)
    GET /api/agents/{id}/ - Retrieve a single agent by ID
    PUT /api/agents/{id}/ - Update an agent
    DELETE /api/agents/{id}/ - Delete an agent
2. Campaigns API:
    Similar to agents, using ```/api/campaigns/```.
3. Campaign Results API:
    Similar to agents, using ```/api/campaign-results/```.
