from pydantic_settings import BaseSettings

from backend.settings.consts import BACKEND_DIR, FRONTEND_DIR


class Settings(BaseSettings):
    backend_dir: str = BACKEND_DIR
    frontend_dir: str = FRONTEND_DIR

    DB_URL: str = "sqlite+aiosqlite:///backend/pygentic_ai.sqlite3"
    DEBUG: bool = False
