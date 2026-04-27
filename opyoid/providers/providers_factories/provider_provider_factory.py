from typing import Any, cast

from opyoid.bindings import FromInstanceProvider
from opyoid.exceptions import IncompatibleProviderFactory
from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.target import Target
from opyoid.type_checker import TypeChecker
from opyoid.utils import InjectedT
from .provider_factory import ProviderFactory


class ProviderProviderFactory(ProviderFactory):
    """Returns the provider for a provider target by transforming a Provider into a FromInstanceProvider."""

    def create(self, context: InjectionContext[InjectedT]) -> Provider[InjectedT]:
        pass
