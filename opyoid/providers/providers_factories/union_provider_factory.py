from typing import cast, Union

from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.target import Target
from opyoid.type_checker import TypeChecker
from opyoid.utils import InjectedT
from .provider_factory import ProviderFactory
from ...exceptions import IncompatibleProviderFactory, NoBindingFound


class UnionProviderFactory(ProviderFactory):
    """Returns the Provider for a Union type target."""

    def create(self, context: InjectionContext[InjectedT]) -> Provider[InjectedT]:
        pass
