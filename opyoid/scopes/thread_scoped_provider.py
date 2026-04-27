import threading
from typing import cast

from opyoid.provider import Provider
from opyoid.utils import InjectedT


class ThreadScopedProvider(Provider[InjectedT]):
    """Always provides the same instance if called in the same thread, creates a new one if not."""

    def __init__(self, inner_provider: Provider[InjectedT]) -> None:
        pass

    def get(self) -> InjectedT:
        pass
