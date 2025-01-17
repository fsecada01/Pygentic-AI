import os

from decouple import config


def get_db_url(env: str = "dev"):
    """

    :param env:
    :return:
    """
    if env == "dev":
        un, pw, db, host, port = (
            config(x)
            for x in (
                "LOCAL_DB_UN",
                "LOCAL_DB_PW",
                "LOCAL_DB_DB",
                "LOCAL_DB_HOST",
                "LOCAL_DB_PORT",
            )
        )

        # url = f"mysql://{un}:{pw}@{host}:{port}/{db}"
        # url = f"mariadb+pymysql://{un}:{pw}@{host}:{port}/{db}"
    elif env == "prod":
        un, pw, db, host, port = (
            config(x)
            for x in (
                "POSTGRES_USER",
                "POSTGRES_PASSWORD",
                "POSTGRES_DB",
                "db",
                "5432",
            )
        )
    else:
        return None

    url = f"postgresql://{un}:{pw}@{host}:{port}/{db}"
    return url


def get_val(val: str, default: str | int | bool | None = None, **kwargs):
    """
    A utility function that checks the platform environment or an .env file to
    pull a key:value pair and return the value. If the value does not exist, a
    ValueError will be raised
    Args:
        val: str
        default: Union[str, None]: default is None

    Returns val: str

    """
    if os.environ.get(val, None) is not None:
        val = os.environ.get(val)
    elif config(val, None, **kwargs) is not None:
        val = config(val)
    elif default:
        val = default
    else:
        raise ValueError(
            f"Env Var {val} is not populated in the environment "
            f"or within the configuration files",
        )

    return val
