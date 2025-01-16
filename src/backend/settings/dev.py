from backend.settings.backend_options import local_db_config
from backend.settings.base import Settings as BaseSettings


class Settings(BaseSettings):
    DB_URL: str = local_db_config
    SQLALCHEMY_DATABASE_URL: str = local_db_config
    DEBUG: bool = True
