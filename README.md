# Enterprise GenAI Knowledge & Agent Platform 
> [**Under Development**]

Production-ready hybrid RAG platform with vector + graph retrieval, multi-LLM routing, autonomous agents, evaluation, and full MLOps.

## Features
- Hybrid Retrieval (Vector DB + Knowledge Graph)
- Multi-LLM support & intelligent routing
- Autonomous AI agents for compliance, research, reporting
- End-to-end evaluation & monitoring
- Containerized deployment with CI/CD


## Initial Project Structure
```
enterprise-genai-platform/
├── .env                  # Local environment variables (gitignored)
├── .env.example          # Template for env vars
├── .gitignore
├── pyproject.toml        # Poetry config + dependencies
├── README.md
├── docs/
│   ├── vision.md         # Product scope, use cases, non-goals
│   └── architecture.md   # High-level architecture description (reference the diagram)
├── ingestion/
│   ├── __init__.py
│   ├── loaders/          # LangChain/Unstructured loaders for PDF, MD, API, etc.
│   ├── parsers/          # Custom parsers for structure preservation
│   └── metadata_extractor.py
├── chunking/
│   ├── __init__.py
│   ├── fixed.py
│   ├── semantic.py
│   └── structural.py
├── embeddings/
│   ├── __init__.py
│   └── models.py         # OpenAI, HuggingFace embedding wrappers
├── vector_store/
│   ├── __init__.py
│   └── client.py         # Pinecone / Weaviate wrapper
├── knowledge_graph/
│   ├── __init__.py
│   ├── schema.py
│   ├── entity_extractor.py
│   └── queries.cql
├── retrieval/
│   ├── __init__.py
│   ├── vector_retriever.py
│   ├── graph_retriever.py
│   └── hybrid_ranker.py
├── llm_router/
│   ├── __init__.py
│   ├── providers/        # openai.py, anthropic.py, huggingface.py, etc.
│   └── router.py
├── evaluation/
│   ├── __init__.py
│   ├── datasets/         # Sample eval datasets
│   ├── metrics.py
│   └── benchmark_runner.py
├── agents/
│   ├── __init__.py
│   ├── tools/            # RAG tool, graph query tool, SQL tool, API tools
│   ├── compliance_agent.py
│   ├── research_agent.py
│   └── report_generator.py
├── api/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   ├── routes/           # query.py, agent.py, etc.
│   └── auth/             # Middleware / RBAC stubs
├── mlops/
│   ├── docker/
│   │   └── Dockerfile
│   ├── ci_cd/            # GitHub Actions workflows
│   └── monitoring/       # Prometheus config stubs, logging
├── tests/                # Unit + integration tests
└── scripts/              # Helper scripts (ingest_data.py, build_graph.py, etc.)
```