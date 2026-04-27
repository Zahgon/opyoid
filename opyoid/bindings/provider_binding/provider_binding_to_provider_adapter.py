from typing import cast, Type

from opyoid.bindings.binding_to_provider_adapter import BindingToProviderAdapter
from opyoid.bindings.registered_binding import RegisteredBinding
from opyoid.exceptions import IncompatibleAdapter, NoBindingFound, NonInjectableTypeError
from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.scopes import Scope
from opyoid.target import Target
from opyoid.utils import InjectedT
from .from_provider_provider import FromProviderProvider
from .provider_binding import ProviderBinding
from ..self_binding import CallableToProviderAdapter


class ProviderBindingToProviderAdapter(BindingToProviderAdapter):
    """Creates a Provider from a ProviderBinding."""

    def __init__(self) -> None:
        pass

    def create(
        self, binding: RegisteredBinding[InjectedT], context: InjectionContext[InjectedT]
    ) -> Provider[InjectedT]:
        pass
