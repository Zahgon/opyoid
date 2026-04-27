from typing import Any, List, Optional, Type, TypeVar, Union

from .bindings import Binding
from .bindings.abstract_module import AbstractModule
from .bindings.root_module import RootModule
from .injection_context import InjectionContext
from .injection_state import InjectionState
from .injector_options import InjectorOptions
from .providers import ProviderCreator
from .target import Target
from .utils import InjectedT


class Injector:
    """Injection entry point.

    Registers all modules and bindings, then prepares all providers.
    """

    def __init__(
        self,
        modules: Optional[List[Union[AbstractModule, Type[AbstractModule]]]] = None,
        bindings: Optional[List[Binding[Any]]] = None,
        options: Optional[InjectorOptions] = None,
    ) -> None:
        pass

    def inject(self, target_type: Union[Type[InjectedT], TypeVar, Any], *, named: Optional[str] = None) -> InjectedT:
        pass
