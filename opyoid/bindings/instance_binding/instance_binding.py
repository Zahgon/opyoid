from typing import Any, Optional, Type, TypeVar, Union

import attr

from opyoid.bindings.binding import Binding
from opyoid.utils import InjectedT


@attr.s(auto_attribs=True, frozen=True, repr=False)
class InstanceBinding(Binding[InjectedT]):
    _target_type: Union[Type[InjectedT], TypeVar, Any]
    bound_instance: InjectedT
    _named: Optional[str] = attr.ib(default=None, kw_only=True)

    @property
    def target_type(self) -> Union[Type[InjectedT], TypeVar]:
        pass

    @property
    def named(self) -> Optional[str]:
        pass

    def __repr__(self) -> str:
        pass
