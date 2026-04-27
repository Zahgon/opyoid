from types import GenericAlias

# noinspection PyProtectedMember
from typing import _GenericAlias, Any, Union  # type: ignore[attr-defined]

from opyoid.named import Named
from opyoid.provider import Provider


class Pep585TypeChecker:
    """Various helpers to check type hints."""

    @staticmethod
    def is_list(target_type: Any) -> bool:
        """Returns True if target_type is List[<Any>] or list[Any]"""
        pass

    @staticmethod
    def is_pep585_list(target_type: Any) -> bool:
        """Returns True if target_type is list[<Any>]"""
        pass

    @staticmethod
    def is_set(target_type: Any) -> bool:
        """Returns True if target_type is Set[<Any>]"""
        pass

    @staticmethod
    def is_tuple(target_type: Any) -> bool:
        """Returns True if target_type is Tuple[<Any>]"""
        pass

    @staticmethod
    def is_provider(target_type: Any) -> bool:
        """Returns True if target_type is Provider[<Any>]"""
        pass

    @staticmethod
    def is_named(target_type: Any) -> bool:
        """Returns True if target_type is Named[<Any>]"""
        pass

    @staticmethod
    def is_union(target_type: Any) -> bool:
        """Returns True if target_type is Union[<Any>, <Any>...] or Optional[<Any>]"""
        pass

    @staticmethod
    def is_type(target_type: Any) -> bool:
        """Returns True if target_type is Type[<Any>]"""
        pass
