from types import TracebackType
from typing import Any, List, Optional, Type

from opyoid.provider import Provider
from opyoid.utils import InjectedT
from .context_scoped_provider import ContextScopedProvider
from .scope import Scope


class ContextScope(Scope):
    """Always provides the same instance in the same context, a new instance in each context."""

    def __init__(self) -> None:
        pass

    def get_scoped_provider(self, inner_provider: Provider[InjectedT]) -> Provider[InjectedT]:
        pass

    def __enter__(self) -> None:
        pass

    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]
    ) -> None:
        pass
