from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SentinelOps"
    check_interval: int = 60
    log_level: str = "INFO"

    glpi_url: str

    postgres_host: str
    postgres_port: int

    sqlite_db_path: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()