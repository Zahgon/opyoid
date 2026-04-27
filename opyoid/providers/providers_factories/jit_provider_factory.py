from opyoid.bindings import RegisteredBinding, SelfBinding, SelfBindingToProviderAdapter
from opyoid.exceptions import IncompatibleProviderFactory
from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.utils import EMPTY, InjectedT
from .provider_factory import ProviderFactory


class JitProviderFactory(ProviderFactory):
    def __init__(self) -> None:
        pass

    def create(self, context: InjectionContext[InjectedT]) -> Provider[InjectedT]:
        pass
