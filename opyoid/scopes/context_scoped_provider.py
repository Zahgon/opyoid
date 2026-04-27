from typing import cast

from opyoid.provider import Provider
from opyoid.utils import EMPTY, InjectedT


class ContextScopedProvider(Provider[InjectedT]):
    """Always provides the same instance in the same context, a new instance in each context."""

    def __init__(self, unscoped_provider: Provider[InjectedT]):
        pass

    def get(self) -> InjectedT:
        pass

    def enter(self) -> None:
        pass

    def exit(self) -> None:
        pass
