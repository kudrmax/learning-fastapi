from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql://postgres:1234@localhost:5432/TestingFastAPI'
    # SECRET_KEY: str = "your-secret-key"
    # ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # class Config:
    #     env_file = ".env"

settings = Settings()