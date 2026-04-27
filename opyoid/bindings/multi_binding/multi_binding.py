from typing import List, Optional, Type, TypeVar, Union

import attr

from opyoid.bindings.binding import Binding
from opyoid.bindings.multi_binding.item_binding import ItemBinding
from opyoid.scopes import Scope, SingletonScope
from opyoid.utils import InjectedT


@attr.s(auto_attribs=True, frozen=True, repr=False)
class MultiBinding(Binding[List[InjectedT]]):
    item_target_type: Union[Type[InjectedT], TypeVar]
    item_bindings: List[ItemBinding[InjectedT]]
    scope: Type[Scope] = attr.ib(default=SingletonScope, kw_only=True)
    _named: Optional[str] = attr.ib(default=None, kw_only=True)
    override_bindings: bool = attr.ib(default=False, kw_only=True)

    @property
    def target_type(self) -> Union[Type[List[InjectedT]], TypeVar]:
        pass

    @property
    def named(self) -> Optional[str]:
        pass

    def __repr__(self) -> str:
        pass
