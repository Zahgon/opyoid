from threading import Lock
from typing import cast, Union

from opyoid.provider import Provider
from opyoid.utils import EMPTY, InjectedT


class SingletonScopedProvider(Provider[InjectedT]):
    """Always provides the same instance."""

    def __init__(self, inner_provider: Provider[InjectedT]) -> None:
        pass

    def get(self) -> InjectedT:
        pass
