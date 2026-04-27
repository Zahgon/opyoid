from typing import Any, Set

from opyoid.frozen_target import FrozenTarget
from .abstract_module import AbstractModule
from .registered_binding import RegisteredBinding


class PrivateModule(AbstractModule):
    def __init__(self) -> None:
        pass

    def configure(self) -> None:
        raise NotImplementedError

    def is_exposed(self, target: FrozenTarget[Any]) -> bool:
        pass

    def expose(self, *bindings: RegisteredBinding[Any]) -> None:
        pass
