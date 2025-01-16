"""
backend configuration variables for Django Database settings. Import these \
into the appropriate settings file and then fit them into the value slot of \
the DATABASES variable
"""

import os
from dataclasses import dataclass
from pathlib import Path

from backend.settings.consts import BASE_DIR, all_dialects
from backend.utils import get_val


@dataclass
class DBConfs:
    name: str | None
    user: str | None
    password: str | None
    host: str | None
    port: str | int | None


# rebased for Flask and Tortoise ORM


def get_db_val(
    db_configs: DBConfs,
    dialect: all_dialects = "sqlite",
    ssl_dict: dict | None = None,
    **kwargs,
):
    """
    This utility function generates an SQL DB url based on provided parameters.
    Dialects are checked against a whitelist composed of accepted entries from
    SQLA 2.0's documentation. Further dialects to be added from MSSQL and
    Oracle DBs.

    Parameters
    ----------
    db_configs: DBConfs: dataclass
    dialect: Literal[all_dialects]: defaults to `sqlite`
    ssl_dict: Optional[dict]: defaults to None
    kwargs: keyword_args that are compacted

    Returns url: str
    -------
    """

    if isinstance(db_configs.host, Path):
        pass

    schema_sep = "://" if "sqlite" not in dialect else ":///"

    if "sqlite" in dialect and not any(
        [
            hasattr(db_configs, x)
            for x in ("name", "user", "password", "host", "port", "kwargs")
        ]
    ):
        url = f"{dialect}:{schema_sep}{db_configs.host}"
    else:
        url = (
            f"{dialect}{schema_sep}{db_configs.user}:{db_configs.password}"
            f"@{db_configs.host}:{db_configs.port}"
            f"/{db_configs.name}"
        )
        if ssl_dict:
            ssl_uri = "&".join([f"{k}={v}" for k, v in ssl_dict.items()])
            url = f"{url}?{ssl_uri}"

        if kwargs:
            uri = "&".join([f"{k}={v}" for k, v in kwargs.items()])
            url = f"{url}?{uri}"

    return url


cloud_backend = {
    "name": get_val("CLOUD_DB_DB"),
    "user": get_val("CLOUD_DB_UN"),
    "password": get_val("CLOUD_DB_PW"),
    "host": get_val("CLOUD_DB_HOST"),
    "port": get_val("CLOUD_DB_PORT"),
}

local_db = {
    "name": get_val("LOCAL_DB_DB"),
    "user": get_val("LOCAL_DB_UN"),
    "password": get_val("LOCAL_DB_PW"),
    "host": get_val("LOCAL_DB_HOST"),
    "port": get_val("LOCAL_DB_PORT"),
}

dialect = "postgresql+asyncpg"

local_db_config = get_db_val(db_configs=DBConfs(**local_db), dialect=dialect)
# local_db_config = get_db_val(**local_db, dialect="postgresql")
cloud_db_config = get_db_val(
    db_configs=DBConfs(**cloud_backend),
    dialect=dialect,
)

sqlite_db_config = get_db_val(
    db_configs=DBConfs(
        name=None,
        user=None,
        password=None,
        port=None,
        host=os.path.join(BASE_DIR, "backend", "db.sqlite"),
    ),
    dialect="sqlite",
)
