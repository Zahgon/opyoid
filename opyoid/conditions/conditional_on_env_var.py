from typing import Callable, Optional, Type, TypeVar

from opyoid.bindings import AbstractModule
from .env_var_condition import EnvVarCondition

ModuleClassT = TypeVar("ModuleClassT", bound=Type[AbstractModule])


def conditional_on_env_var(
    env_var_name: str, *, expected_value: Optional[str] = None
) -> Callable[[ModuleClassT], ModuleClassT]:
    pass
