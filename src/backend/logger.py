"""
Custom Logger Using Loguru
"""

import json
import logging
import sys
from datetime import date
from pathlib import Path

from loguru import logger

from backend.settings.consts import BACKEND_DIR

dir_path = Path(BACKEND_DIR).joinpath("logs")

log_file = Path(dir_path).joinpath(f"log_{date.today()}.log")

list(
    map(
        lambda x: logger.add(
            Path(dir_path).joinpath(f"{x}_{log_file.name}"),
            filter=lambda record: record["level"].name == x.upper(),
            rotation="1 day",
            retention="1 week",
            enqueue=True,
        ),
        ["info", "debug", "error", "success", "warning", "critical"],
    ),
)


class InterceptHandler(logging.Handler):
    loglevel_mapping = {
        50: "CRITICAL",
        40: "ERROR",
        30: "WARNING",
        20: "INFO",
        10: "DEBUG",
        0: "NOTSET",
    }

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        log = logger.bind(request_id="app")
        log.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


class CustomizeLogger:
    @classmethod
    def make_logger(cls, config_path: Path):
        config = cls.load_logging_config(config_path)
        logging_config = config.get("logger")

        logger = cls.customize_logging(
            logging_config.get("path"),
            level=logging_config.get("level"),
            retention=logging_config.get("retention"),
            rotation=logging_config.get("rotation"),
            format=logging_config.get("format"),
        )
        return logger

    @classmethod
    def customize_logging(
        cls,
        filepath: Path,
        level: str,
        rotation: str,
        retention: str,
        format: str,
    ):
        logger.remove()
        logger.add(
            sys.stdout,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=format,
        )
        logger.add(
            str(filepath),
            rotation=rotation,
            retention=retention,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=format,
        )
        logging.basicConfig(handlers=[InterceptHandler()], level=0)
        logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
        for _log in ["uvicorn", "uvicorn.error", "fastapi"]:
            _logger = logging.getLogger(_log)
            _logger.handlers = [InterceptHandler()]

        return logger.bind(request_id=None, method=None)

    @classmethod
    def load_logging_config(cls, config_path):
        config = None
        with open(config_path) as config_file:
            config = json.load(config_file)
        return config
