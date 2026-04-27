import logging
import os
import re
from typing import Any, Optional

from opyoid.bindings import FromInstanceProvider
from opyoid.exceptions import IncompatibleProviderFactory
from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.utils import InjectedT
from .provider_factory import ProviderFactory


class FromEnvVarProviderFactory(ProviderFactory):
    """Creates a Provider from an environment variable."""

    logger = logging.getLogger(__name__)

    def create(self, context: InjectionContext[InjectedT]) -> Provider[InjectedT]:
        pass

    def _get_matching_env_var_name(self, context: InjectionContext[InjectedT]) -> Optional[str]:
        pass

    @staticmethod
    def _to_upper_case(string: str) -> str:
        pass

    @staticmethod
    def _get_converted_value(env_var_name: str, context: InjectionContext[InjectedT]) -> Any:
        pass
