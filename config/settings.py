from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # LLM
    openai_api_key: str
    anthropic_api_key: str | None = None
    
    # Databases
    postgres_url: str
    redis_url: str
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str
    
    # Vector DB
    pinecone_api_key: str
    pinecone_environment: str
    
    # App
    log_level: str = "INFO"
    environment: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()

