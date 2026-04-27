import logging
from typing import List

from opyoid.bindings import (
    BindingToProviderAdapter,
    ClassBindingToProviderAdapter,
    InstanceBindingToProviderAdapter,
    MultiBindingToProviderAdapter,
    ProviderBindingToProviderAdapter,
    SelfBindingToProviderAdapter,
)
from opyoid.bindings.registered_binding import RegisteredBinding
from opyoid.exceptions import BindingError, IncompatibleAdapter
from opyoid.injection_context import InjectionContext
from opyoid.injection_state import InjectionState
from opyoid.provider import Provider
from opyoid.utils import InjectedT


class FromRegisteredBindingProviderFactory:
    """Creates Providers, one per binding."""

    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        pass

    def create(
        self,
        binding: RegisteredBinding[InjectedT],
        context: InjectionContext[InjectedT],
        cache_provider: bool = True,
    ) -> Provider[InjectedT]:
        pass

    def _create_from_binding(
        self, binding: RegisteredBinding[InjectedT], context: InjectionContext[InjectedT]
    ) -> Provider[InjectedT]:
        pass
