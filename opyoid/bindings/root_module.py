from typing import Any, List, Optional, Type, TYPE_CHECKING, Union

from opyoid.scopes import ContextScope, ImmediateScope, PerLookupScope, SingletonScope, ThreadScope
from .abstract_module import AbstractModule
from .binding import Binding
from .module import Module

if TYPE_CHECKING:
    from opyoid.injector import Injector


class RootModule(Module):
    def __init__(
        self,
        injector: "Injector",
        modules: Optional[List[Union[AbstractModule, Type[AbstractModule]]]],
        bindings: Optional[List[Binding[Any]]],
    ) -> None:
        pass

    def configure(self) -> None:
        # pylint: disable=import-outside-toplevel
        pass
