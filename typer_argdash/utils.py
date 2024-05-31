import logging

import typer


def config_logging(
    verbose: int = 0,
) -> None:
    """Configure logging for stream and file."""
    level = logging.ERROR
    if verbose == 1:
        level = logging.INFO
    elif verbose > 1:
        level = logging.DEBUG

    logger = logging.getLogger()

    logger.setLevel(level)


def get_logger(name: str) -> logging.Logger:
    """Create a new logger with the given name."""
    logger = logging.getLogger(name)
    return logger
