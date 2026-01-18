# https://github.com/SirDank/dankware

"""
Colored logging integration for dankware.
"""

import logging
from typing import Optional


class ColoredFormatter(logging.Formatter):
    """
    Custom logging formatter with dankware colors.

    __________________________________________

    [ EXAMPLE ]

    ```python
    import logging
    from dankware.logging import ColoredFormatter

    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter())
    logger = logging.getLogger("myapp")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.info("This is an info message")
    logger.error("This is an error message")
    ```
    """

    LEVEL_COLORS = {
        logging.DEBUG: 3,  # Random colors
        logging.INFO: 1,  # Default preset
        logging.WARNING: 1,  # Default with yellow-ish
        logging.ERROR: 2,  # Error preset
        logging.CRITICAL: 2,  # Error preset
    }

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record with colors."""
        from .text import clr

        message = super().format(record)
        preset = self.LEVEL_COLORS.get(record.levelno, 1)
        return clr(message, preset)


class ColoredLogger(logging.Logger):
    """
    A logger subclass that adds colored formatting by default.
    """

    def __init__(self, name: str, level: int = logging.NOTSET):
        super().__init__(name, level)
        handler = logging.StreamHandler()
        handler.setFormatter(ColoredFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        self.addHandler(handler)


def get_logger(name: str, level: int = logging.INFO, fmt: Optional[str] = None) -> logging.Logger:
    """
    Get a colored logger instance.

    Args:
        name: Logger name.
        level: Logging level.
        fmt: Optional format string.

    Returns:
        Configured logger with colored output.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.logging import get_logger

    logger = get_logger("myapp")
    logger.info("Application started")
    logger.error("Something went wrong!")
    ```
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()

    handler = logging.StreamHandler()
    format_str = fmt or "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    handler.setFormatter(ColoredFormatter(format_str))
    logger.addHandler(handler)

    return logger


def setup_logging(level: int = logging.INFO, fmt: Optional[str] = None) -> None:
    """
    Setup colored logging for the root logger.

    Args:
        level: Logging level.
        fmt: Optional format string.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.logging import setup_logging
    import logging

    setup_logging(level=logging.DEBUG)
    logging.info("Now all logging is colored!")
    ```
    """
    format_str = fmt or "%(asctime)s - %(levelname)s - %(message)s"
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter(format_str))

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers.clear()
    root_logger.addHandler(handler)
