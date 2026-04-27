import logging
from inspect import Parameter, signature
from typing import Any, Callable, Dict, List, Optional, Type

from opyoid.bindings.instance_binding import FromInstanceProvider
from opyoid.exceptions import NoBindingFound, NonInjectableTypeError
from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.target import Target
from opyoid.type_checker import TypeChecker
from opyoid.utils import EMPTY, get_class_full_name, InjectedT
from .from_callable_provider import FromCallableProvider
from ...scopes import Scope


class CallableToProviderAdapter:
    """Creates a Provider from a callable."""

    logger = logging.getLogger(__name__)

    def create(
        self,
        type_or_function: Callable[..., InjectedT],
        context: InjectionContext[InjectedT],
        scope: Type[Scope],
    ) -> Provider[InjectedT]:
        pass

    def _get_parameter_provider(
        self, parameter: Parameter, type_or_function: Callable[..., InjectedT], context: InjectionContext[InjectedT]
    ) -> Provider[InjectedT]:
        pass

    def _get_positional_parameter_provider(
        self, parameter: Parameter, type_or_function: Callable[..., InjectedT], context: InjectionContext[InjectedT]
    ) -> Provider[List[InjectedT]]:
        pass

    @staticmethod
    def _get_provider(
        targets: List[Target[InjectedT]], parent_context: InjectionContext[Any]
    ) -> Optional[Provider[InjectedT]]:
        pass
