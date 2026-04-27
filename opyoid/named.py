from inspect import Parameter, Signature, signature
from typing import Callable, cast, Generic, Mapping, Type, TypeVar, Union

from opyoid.exceptions import NamedError

WrappedT = TypeVar("WrappedT")


class Named(Generic[WrappedT]):
    name: str
    original_type: Type[WrappedT]

    @classmethod
    def get_named_class(cls, original_type: Union[Type[WrappedT], str], name: str) -> Type["Named[WrappedT]"]:
        pass


def named_arg(arg_name: str, name: str) -> Callable[[Callable[..., None]], Callable[..., None]]:
    """Decorator used to name constructor arguments.

    Use it to specify multiple bindings for the same type.
    """
    pass
