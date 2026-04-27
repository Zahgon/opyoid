from typing import Any, Callable, Type, TypeVar, Union

from .named import Named

InjectedT = TypeVar("InjectedT", bound=Any)
EMPTY = object()


def get_class_full_name(klass: Union[Type[Any], TypeVar, str]) -> str:
    pass


def get_function_full_name(function: Callable[..., Any]) -> str:
    pass
