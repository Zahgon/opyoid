import logging
from inspect import Parameter
from typing import Any, Generic, List, Optional, Type, TYPE_CHECKING, TypeVar

import attr

from .exceptions import CyclicDependencyError
from .provider import Provider
from .target import Target
from .utils import InjectedT

if TYPE_CHECKING:
    from .bindings import RegisteredBinding
    from .injection_state import InjectionState


InjectedSubT = TypeVar("InjectedSubT", bound=Any)


@attr.s(auto_attribs=True)
class InjectionContext(Generic[InjectedT]):
    logger = logging.getLogger(__name__)

    target: Target[InjectedT]
    injection_state: "InjectionState"
    parent_context: Optional["InjectionContext[Any]"] = attr.ib(default=None, eq=False)
    allow_jit_provider: bool = True
    current_class: Optional[Type[InjectedT]] = None
    current_parameter: Optional[Parameter] = None

    def __attrs_post_init__(self) -> None:
        pass

    @property
    def _dependency_chain(self) -> List[Target[Any]]:
        pass

    def get_child_context(
        self,
        new_target: Target[InjectedSubT],
        *,
        allow_jit_provider: bool = True,
        current_class: Optional[Type[InjectedSubT]] = None,
        current_parameter: Optional[Parameter] = None,
    ) -> "InjectionContext[InjectedSubT]":
        pass

    def get_new_state_context(self, new_state: "InjectionState") -> "InjectionContext[InjectedT]":
        pass

    def get_provider(self) -> Provider[InjectedT]:
        pass

    def has_binding(self) -> bool:
        pass

    def get_binding(self) -> Optional["RegisteredBinding[InjectedT]"]:
        pass
