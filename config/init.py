from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # LLM
    openai_api_key: str
    anthropic_api_key: str | None = None

    # Vector Store
    pinecone_api_key: str
    pinecone_environment: str = "gcp-starter"
    pinecone_index_name: str = "enterprise-genai"

    # Graph DB
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str

    # Database
    database_url: str

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # App
    env: str = "development"
    log_level: str = "INFO"
    api_host: str = "0.0.0.0"
    api_port: int = 8000


@lru_cache()
def get_settings() -> Settings:
    return Settings()