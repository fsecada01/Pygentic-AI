from typing import Any

from backend.db.db import meta


def get_base_class():
    """
    Generate base SQLModel class for project
    :return:
    """
    from sqlmodel import SQLModel

    class Base(SQLModel):
        def __new__(cls, *args: Any, **kwargs: Any) -> Any:
            """
            Updated to Pydantic V2.5 results in an error with
            `__pydantic_extra__` attribute not being found. This is a workaround
            taken from the GitHub issues page:
            https://github.com/tiangolo/sqlmodel/pull/632#discussion_r1280895115
            Args:
                *args: positional args as tuple; explodes into Any type
                **kwargs: keyword arguments as dict; explodes into Any type

            Returns:
                Any
            """
            new_obj = super().__new__(cls)
            object.__setattr__(new_obj, "__pydantic_fields_set__", set())
            object.__setattr__(new_obj, "__pydantic_extra__", {})
            return new_obj

    Base.metadata = meta

    return Base


Base = get_base_class()
Base.__mapper_args = {"eager_defaults": True}
