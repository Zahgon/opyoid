from typing import Callable, Optional, Type, TypeVar, Union

import attr

from opyoid.bindings.binding import Binding
from opyoid.exceptions import BindingError
from opyoid.provider import Provider
from opyoid.scopes import Scope, SingletonScope
from opyoid.utils import get_class_full_name, get_function_full_name, InjectedT


@attr.s(auto_attribs=True, frozen=True, repr=False)
class ProviderBinding(Binding[InjectedT]):
    _target_type: Union[Type[InjectedT], TypeVar]
    bound_provider: Union[Type[Provider[InjectedT]], Provider[InjectedT], Callable[..., InjectedT]]
    scope: Type[Scope] = attr.ib(default=SingletonScope, kw_only=True)
    _named: Optional[str] = attr.ib(default=None, kw_only=True)

    def __attrs_post_init__(self) -> None:
        pass

    @property
    def target_type(self) -> Union[Type[InjectedT], TypeVar]:
        pass

    @property
    def named(self) -> Optional[str]:
        pass

    def __repr__(self) -> str:
        pass
