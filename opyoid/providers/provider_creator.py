import logging
from threading import RLock
from typing import List

from opyoid.exceptions import IncompatibleProviderFactory, NoBindingFound
from opyoid.injection_context import InjectionContext
from opyoid.provider import Provider
from opyoid.utils import InjectedT
from .providers_factories import (
    FromBindingProviderFactory,
    FromCacheProviderFactory,
    FromEnvVarProviderFactory,
    JitProviderFactory,
    ListFromItemsProviderFactory,
    ListProviderFactory,
    ProviderFactory,
    ProviderProviderFactory,
    SetProviderFactory,
    TupleProviderFactory,
    TypeProviderFactory,
    UnionProviderFactory,
)


class ProviderCreator:
    """Creates Providers and saves them in the ProviderRegistry."""

    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        pass

    def get_provider(self, context: InjectionContext[InjectedT]) -> Provider[InjectedT]:
        pass

    def _get_provider(self, context: InjectionContext[InjectedT]) -> Provider[InjectedT]:
        pass
