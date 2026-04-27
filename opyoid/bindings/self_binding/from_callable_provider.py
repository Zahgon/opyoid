from typing import Any, Callable, Dict, List, Optional

from opyoid.provider import Provider
from opyoid.utils import InjectedT


class FromCallableProvider(Provider[InjectedT]):
    def __init__(
        self,
        injected_callable: Callable[..., InjectedT],
        positional_providers: List[Provider[Any]],
        args_provider: Optional[Provider[List[Any]]],
        keyword_providers: Dict[str, Provider[Any]],
    ) -> None:
        pass

    def get(self) -> InjectedT:
        pass
