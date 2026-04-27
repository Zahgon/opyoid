import logging
from typing import cast

from opyoid.exceptions import IncompatibleProviderFactory
from opyoid.injection_context import InjectionContext
from opyoid.injection_state import InjectionState
from opyoid.provider import Provider
from opyoid.utils import InjectedT
from .from_registered_binding_provider_factory import FromRegisteredBindingProviderFactory
from .provider_factory import ProviderFactory
from ...bindings import RegisteredBinding


class FromBindingProviderFactory(ProviderFactory):
    """Creates Providers, one per binding."""

    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        pass

    def create(self, context: InjectionContext[InjectedT]) -> Provider[InjectedT]:
        pass
