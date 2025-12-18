# Enterprise GenAI Knowledge & Agent Platform 
> [**Under Development**]

Production-ready hybrid RAG platform with vector + graph retrieval, multi-LLM routing, autonomous agents, evaluation, and full MLOps.

## Features
- Hybrid Retrieval (Vector DB + Knowledge Graph)
- Multi-LLM support & intelligent routing
- Autonomous AI agents for compliance, research, reporting
- End-to-end evaluation & monitoring
- Containerized deployment with CI/CD

## Quick Start
```bash
poetry install
cp .env.example .env  # Add your API keys
poetry run uvicorn api.main:app --reload