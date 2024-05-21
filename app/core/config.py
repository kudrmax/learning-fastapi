from pydantic import BaseModel
from pydantic import PostgresDsn  # валидация строки подключения к PostgreSQL
from pydantic.v1 import BaseSettings


class RunConfig(BaseModel):
    host: str = 'localhost'
    port: int = 5555


class ApiPrefix(BaseModel):
    prefix: str = '/api'


class DatabaseConfig(BaseModel):
    url: PostgresDsn


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    bd: DatabaseConfig


settings = Settings()
