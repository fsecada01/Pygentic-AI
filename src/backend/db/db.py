import asyncio
import inspect
from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Form
from pydantic import BaseModel
from sqlalchemy import MetaData, event
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import merge_frozen_result, sessionmaker
from sqlalchemy.pool import NullPool
from sqlmodel import Session, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from backend.logger import logger
from backend.utils import get_val

# echo, create = True, True
echo, create = False, False
# echo, create = False, True
# echo, create = True, False

db_url = get_val("PROJECT_DB_URL")

schema = "pygentic_ai"
meta = MetaData(schema=schema)


def as_form(cls: type[BaseModel]):
    """

    :param cls:
    :return:
    """
    new_params = [
        inspect.Parameter(
            field_name,
            inspect.Parameter.POSITIONAL_ONLY,
            default=model_field.default,
            annotation=Annotated[
                model_field.annotation, *model_field.metadata, Form()
            ],
        )
        for field_name, model_field in cls.model_fields.items()
    ]

    async def as_form_func(**data):
        # logger.debug(pformat(data))
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_params)
    as_form_func.__signature__ = sig  # type: ignore
    cls.as_form = as_form_func

    return cls


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Get async SQLA session via generator function
    """
    async with async_session_maker() as session_obj:
        yield session_obj


def get_sync_session():
    """
    Get SQLA session via generator function
    """
    with sessionmaker(db_url, expire_on_commit=False) as session:
        yield session


async def run_out_of_band(
    async_sessionaker: sessionmaker,
    session_inst: AsyncSession,
    statement,
    merge_results: bool = True,
):
    """

    :param async_sessionaker:
    :param session_inst:
    :param statement:
    :param merge_results:
    :return:
    """
    async with async_sessionaker() as oob_session:
        await oob_session.connection(
            execution_options={"isolation_level": "AUTOCOMMIT"}
        )

    result = await oob_session.execute(statement)

    if merge_results:
        return (
            await session_inst.run_sync(
                merge_frozen_result, statement, result.freeze(), load=False
            )
        )()
    else:
        await result.close()


async def check_db_exists(engine_inst):
    """

    :param engine_inst:
    :return:
    """
    # async with Session(engine_inst) as conn:
    async with engine_inst.connect() as conn:
        from sqlalchemy import inspect  # noqa

        tables = await conn.run_sync(
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )
        logger.info(tables)
        if not tables:
            return False
        return True


async def create_db(
    engine_inst: AsyncEngine,
    create_bool: bool = False,
):
    """

    :param engine_inst:
    :param create_bool:
    :return:
    """
    url = engine_inst.url
    exists = await check_db_exists(engine_inst)
    if not exists or create_bool:
        from backend.db.base_model import Base  # noqa

        async with engine_inst.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

            logger.info(f"Database {url.database} created")

    return engine_inst


def create_db_engine(
    db_url: str, async_bool: bool = False, echo_bool: bool = False
):
    """

    :param db_url:
    :param async_bool:
    :param echo_bool:
    :return:
    """
    engine_inst = (
        create_engine(db_url, echo=echo_bool)
        if async_bool is False
        else create_async_engine(db_url, echo=echo_bool, poolclass=NullPool)
    )

    return engine_inst


engine = create_db_engine(db_url, async_bool=True, echo_bool=False)


@event.listens_for(engine.sync_engine, "connect", insert=True)
def set_current_schema(dbapi_connection, connection_record):
    """
    This is a helper event listener to ensure that the current
    schema is set when bootstrapping the database tables.
    Taken from:

    https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#setting-alternate
    -search-paths-on-connect

    :param dbapi_connection:
    :param connection_record:
    :return:
    """
    existing_autocommit = dbapi_connection.autocommit
    dbapi_connection.autocommit = True
    cursor_obj = dbapi_connection.cursor()
    cursor_obj.execute("SET SESSION search_path='%s'" % schema)
    cursor_obj.close()
    dbapi_connection.autocommit = existing_autocommit


sync_engine = create_db_engine(db_url, echo_bool=echo)

session_inst = Session(sync_engine, expire_on_commit=False)

async_session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

session_maker = sessionmaker(
    bind=engine, class_=Session, expire_on_commit=False
)

if __name__ == "__main__":
    import sys

    from backend.db.models import *  # noqa F403

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(create_db(engine_inst=engine, create_bool=True))
