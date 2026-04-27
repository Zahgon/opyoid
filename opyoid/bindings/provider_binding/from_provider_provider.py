from opyoid.provider import Provider
from opyoid.utils import InjectedT


class FromProviderProvider(Provider[InjectedT]):
    def __init__(self, provider_provider: Provider[Provider[InjectedT]]) -> None:
        pass

    def get(self) -> InjectedT:
        pass
