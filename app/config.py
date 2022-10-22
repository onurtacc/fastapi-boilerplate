from pydantic import BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api/v1"
    API_VERSION: str = "v1"

    PROJECT_NAME: str = "Simple API"
    # DB
    DB_HOST: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_USER: str
    DB_PORT: int

    # Secrets
    SECRET_KEY: str

    # JWT Settings
    JWT_EXPIRES_TIME = 60 * 60
    JWT_ALGORITHM = "HS256"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
