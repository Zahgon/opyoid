from opyoid.provider import Provider
from opyoid.utils import InjectedT


class FromInstanceProvider(Provider[InjectedT]):
    def __init__(self, instance: InjectedT) -> None:
        pass

    def get(self) -> InjectedT:
        pass
