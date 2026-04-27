import logging
from typing import Any, cast, Dict, Optional, Type, TypeVar, Union

from opyoid.exceptions import NonInjectableTypeError
from opyoid.frozen_target import FrozenTarget
from opyoid.target import Target
from opyoid.utils import InjectedT
from .binding import Binding
from .class_binding import ClassBinding
from .instance_binding import InstanceBinding
from .multi_binding import MultiBinding
from .provider_binding import ProviderBinding
from .registered_binding import RegisteredBinding
from .registered_multi_binding import RegisteredMultiBinding
from .self_binding import SelfBinding

InjectedItemT = TypeVar("InjectedItemT", bound=Any)


class BindingRegistry:
    """Contains all bindings from a Module."""

    logger = logging.getLogger(__name__)

    def __init__(self, log_bindings: bool = False):
        pass

    def __contains__(self, item: Union[Target[Any], FrozenTarget[Any]]) -> bool:
        pass

    def register(self, registered_binding: RegisteredBinding[Any], add_self_binding: bool = True) -> None:
        pass

    @staticmethod
    def _should_append_to_multi_binding(
        new_binding: RegisteredBinding[InjectedItemT],
        previous_binding: Optional[RegisteredBinding[InjectedItemT]],
    ) -> bool:
        pass

    def _append_to_multi_binding(
        self,
        registered_binding: RegisteredMultiBinding[InjectedItemT],
        previous_binding: RegisteredMultiBinding[InjectedItemT],
    ) -> None:
        pass

    def _create_or_override_binding(
        self, registered_binding: RegisteredBinding[InjectedT], previous_binding: Optional[RegisteredBinding[InjectedT]]
    ) -> None:
        pass

    def _register_self_binding(self, registered_binding: RegisteredBinding[Any]) -> None:
        pass

    def get_bindings_by_target(self) -> Dict[FrozenTarget[Any], RegisteredBinding[Any]]:
        pass

    def get_binding(
        self, target: Union[Target[InjectedT], FrozenTarget[InjectedT]]
    ) -> Optional[RegisteredBinding[InjectedT]]:
        pass

    @staticmethod
    def _is_object_builtin(target: Any) -> bool:
        pass
