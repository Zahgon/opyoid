import logging
import os
from typing import Optional, Type

from opyoid.bindings import AbstractModule, Condition


class EnvVarCondition(Condition):
    logger = logging.getLogger(__name__)

    def __init__(self, env_var_name: str, module: Type[AbstractModule], expected_value: Optional[str] = None):
        pass

    def is_valid(self) -> bool:
        pass
