from backend.settings.backend_options import cloud_db_config
from backend.settings.base import Settings as BaseSettings


class Settings(BaseSettings):
    DB_URL: str = cloud_db_config
    SQLALCHEMY_DATABASE_URI: str = cloud_db_config
    DEBUG: bool = False
