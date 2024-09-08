# Full Stack LangGraph Example

This is an example app that uses LangGraph to create an AI agent. It will be a simpler application that uses React/Python/FastAPI/ Postgres and LLMs to perform analysis on customer feedback for products for a fictional company called 'Acme'.

## Todo:

### Backend

- Seed DB with products
- Decide on vector DB and add to docker compose file. (Between Milvus or PGVector)
- Add a tool to get user information at login and insert it into the graph start so the agent knows the user.
- Add a tool to search DB with products using text to SQL.
- Add a tool to provide feedback about a product
- Finish integrating Alembic for migrations

### Frontend

- Initialize the frontend repo with CRA + Bulma for easy CSS
- Create Register Component
- Create Login Component
- Create provider to save user info
- Create Dashboard to chat with agent + streaming support
- Add to dashboard graphs to show customer sentiment about all products/specific products

## Prereqs

1. Have poetry installed
1. Have docker installed

## How to run

## To start the backend

1. `cd backend/`
1. `poetry install --no-root`
1. `docker-compose up --build --remove-orphans`
