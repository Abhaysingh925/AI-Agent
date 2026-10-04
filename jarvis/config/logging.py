from __future__ import annotations

import logging
import sys
from typing import Optional

from config.settings import get_settings


def get_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """Return a configured logger instance."""
    settings = get_settings()
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, (level or settings.log_level).upper(), logging.INFO))

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))
        logger.addHandler(handler)

    logger.propagate = False
    return logger
