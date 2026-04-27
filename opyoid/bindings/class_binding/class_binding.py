from typing import Any, Optional, Type

import attr

from opyoid.bindings.binding import Binding
from opyoid.exceptions import BindingError
from opyoid.scopes import Scope, SingletonScope
from opyoid.utils import get_class_full_name, InjectedT


@attr.s(auto_attribs=True, frozen=True, repr=False)
class ClassBinding(Binding[InjectedT]):
    _target_type: Any
    bound_class: Type[InjectedT]
    scope: Type[Scope] = attr.ib(default=SingletonScope, kw_only=True)
    _named: Optional[str] = attr.ib(default=None, kw_only=True)

    def __attrs_post_init__(self) -> None:
        pass

    @property
    def target_type(self) -> Any:
        pass

    @property
    def named(self) -> Optional[str]:
        pass

    def __repr__(self) -> str:
        pass
