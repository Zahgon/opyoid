from typing import Optional, Type

import attr

from opyoid.bindings.binding import Binding
from opyoid.scopes import Scope, SingletonScope
from opyoid.utils import InjectedT


@attr.s(auto_attribs=True, frozen=True, repr=False)
class SelfBinding(Binding[InjectedT]):
    _target_type: Type[InjectedT]
    scope: Type[Scope] = attr.ib(default=SingletonScope, kw_only=True)
    _named: Optional[str] = attr.ib(default=None, kw_only=True)

    @property
    def target_type(self) -> Type[InjectedT]:
        pass

    @property
    def named(self) -> Optional[str]:
        pass

    def __repr__(self) -> str:
        pass
