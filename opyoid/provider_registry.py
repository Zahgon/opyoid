from typing import Any, Dict, List, Optional, Tuple

from .exceptions import InjectException, NonInjectableTypeError
from .frozen_target import FrozenTarget
from .provider import Provider
from .target import Target
from .utils import InjectedT


class ProviderRegistry:
    """Stores Providers for each Target to create a cache."""

    def __init__(self) -> None:
        pass

    def __contains__(self, item: Target[Any]) -> bool:
        pass

    def set_provider(self, target: Target[InjectedT], provider: Provider[InjectedT]) -> None:
        pass

    def get_provider(self, target: Target[InjectedT]) -> Optional[Provider[InjectedT]]:
        pass
