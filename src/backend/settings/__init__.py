import enum
import os
from functools import lru_cache

from backend.settings.dev import Settings as DevSettings
from backend.settings.prod import Settings as ProdSettings
from backend.utils import get_val

server_types = enum.StrEnum(
    "ServerTypes", {x.upper(): x for x in ("dev", "uat", "staging", "prod")}
)


@lru_cache
def get_settings(server: server_types = "dev", debug: bool = False):
    if server == "dev":
        settings = DevSettings()
    else:
        settings = ProdSettings()

    if debug:
        settings.DEBUG = debug

    return settings


debug_arg = get_val(val="DEBUG", default=False, cast=bool)
env_arg = get_val("SERVER_ENV", default="dev")

app_settings = get_settings(server=env_arg, debug=debug_arg)
os.environ["PROJECT_DB_URL"] = app_settings.DB_URL
