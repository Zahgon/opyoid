from typing import Any, cast, TYPE_CHECKING

from opyoid.bindings.binding_to_provider_adapter import BindingToProviderAdapter
from opyoid.exceptions import IncompatibleAdapter, NoBindingFound, NonInjectableTypeError
from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.scopes import Scope
from opyoid.target import Target
from opyoid.utils import InjectedT
from .list_provider import ListProvider
from .multi_binding import MultiBinding
from ..registered_binding import RegisteredBinding
from ..registered_multi_binding import RegisteredMultiBinding

if TYPE_CHECKING:
    from opyoid.providers.providers_factories.from_registered_binding_provider_factory import (
        FromRegisteredBindingProviderFactory,
    )


class MultiBindingToProviderAdapter(BindingToProviderAdapter):
    """Creates a Provider from an MultiBinding."""

    def __init__(self, item_provider_factory: "FromRegisteredBindingProviderFactory") -> None:
        pass

    def create(self, binding: RegisteredBinding[InjectedT], context: InjectionContext[InjectedT]) -> Provider[Any]:
        pass
