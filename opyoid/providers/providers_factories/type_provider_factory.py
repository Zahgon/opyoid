from typing import Any, cast, Type

from opyoid.bindings import ClassBinding, FromInstanceProvider, SelfBinding
from opyoid.exceptions import IncompatibleProviderFactory, NoBindingFound
from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.target import Target
from opyoid.type_checker import TypeChecker
from opyoid.utils import InjectedT
from .provider_factory import ProviderFactory


class TypeProviderFactory(ProviderFactory):
    """Returns the provider for a type target by transforming ClassBindings into a FromInstanceProvider."""

    def create(self, context: InjectionContext[InjectedT]) -> Provider[InjectedT]:
        pass
