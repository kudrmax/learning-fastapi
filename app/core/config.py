from pydantic import BaseModel
from pydantic.v1 import BaseSettings


class RunConfig(BaseModel):
    host: str = 'localhost'
    port: int = 5432


class ApiPrefix(BaseModel):
    prefix: str = '/api'


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    # db_url: str


settings = Settings()
