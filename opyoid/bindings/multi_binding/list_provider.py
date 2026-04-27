from typing import List

from opyoid.provider import Provider
from opyoid.utils import InjectedT


class ListProvider(Provider[List[InjectedT]]):
    def __init__(self, item_providers: List[Provider[InjectedT]]) -> None:
        pass

    def get(self) -> List[InjectedT]:
        pass
