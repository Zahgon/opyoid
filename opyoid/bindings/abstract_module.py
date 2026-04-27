from typing import Any, Callable, cast, Dict, List, Optional, Tuple, Type, Union

from opyoid.exceptions import BindingError
from opyoid.provider import Provider
from opyoid.scopes import Scope, SingletonScope
from opyoid.utils import EMPTY, InjectedT
from .binding import Binding
from .binding_registry import BindingRegistry
from .class_binding import ClassBinding
from .condition import Condition
from .instance_binding import InstanceBinding
from .multi_binding import ItemBinding, MultiBinding
from .provider_binding import ProviderBinding
from .registered_binding import RegisteredBinding
from .registered_multi_binding import RegisteredMultiBinding
from .self_binding import SelfBinding


class AbstractModule:
    """Base class for Modules, should not be used outside the library."""

    conditions: Tuple[Condition, ...] = ()

    def __init__(
        self,
        log_bindings: bool = False,
        shared_modules: Optional[Dict[Type["AbstractModule"], "AbstractModule"]] = None,
    ):
        pass

    @property
    def binding_registry(self) -> BindingRegistry:
        pass

    @classmethod
    def add_condition(cls, condition: Condition) -> None:
        pass

    def __repr__(self) -> str:
        pass

    def configure(self) -> None:
        """Contains all bindings, called at injector initialization.

        Should not be called directly, but through configure_once.
        Only public to have a simpler API.
        """
        raise NotImplementedError

    def install(self, module: Union["AbstractModule", Type["AbstractModule"]]) -> None:
        """Adds bindings from another Module to this one."""
        pass

    # pylint: disable=too-many-arguments
    def bind(
        self,
        target_type: Any,
        *,
        to_class: Type[Any] = EMPTY,  # type: ignore[assignment]
        to_instance: Any = EMPTY,
        to_provider: Union[Provider[Any], Type[Provider[Any]], Callable[..., Any]] = EMPTY,  # type: ignore[assignment]
        scope: Type[Scope] = SingletonScope,
        named: Optional[str] = None,
    ) -> RegisteredBinding[InjectedT]:
        pass

    def configure_once(self) -> None:
        """Calls configure if it has not already been called."""
        pass

    def multi_bind(
        self,
        item_target_type: Any,
        item_bindings: List[ItemBinding[Any]],
        *,
        scope: Type[Scope] = SingletonScope,
        named: Optional[str] = None,
        override_bindings: bool = False,
    ) -> RegisteredMultiBinding[Any]:
        pass

    @staticmethod
    def bind_item(
        *,
        to_class: Type[InjectedT] = EMPTY,  # type: ignore[assignment]
        to_instance: InjectedT = EMPTY,  # type: ignore[assignment]
        to_provider: Union[
            Provider[InjectedT],
            Type[Provider[InjectedT]],
            Callable[..., InjectedT],
        ] = EMPTY,  # type: ignore[assignment]
        scope: Type[Scope] = EMPTY,  # type: ignore[assignment]
        named: Optional[str] = EMPTY,  # type: ignore[assignment]
    ) -> ItemBinding[InjectedT]:
        pass

    def _get_module_instance(self, module: Union["AbstractModule", Type["AbstractModule"]]) -> "AbstractModule":
        # pylint: disable=import-outside-toplevel
        pass

    @staticmethod
    def _create_binding(
        *,
        target_type: Any,
        bound_class: Type[Any],
        bound_instance: Any,
        bound_provider: Union[Provider[Any], Type[Provider[Any]], Callable[..., Any]],
        scope: Type[Scope],
        named: Optional[str],
    ) -> Binding[Any]:
        pass

    def _register(self, binding: Binding[Any]) -> RegisteredBinding[Any]:
        pass

    def _register_multi_binding(self, binding: MultiBinding[InjectedT]) -> RegisteredMultiBinding[InjectedT]:
        pass
