# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_searchparams import SearchParams
from ..types.classes.cls_withreasoning import WithReasoning
from ..types.enums.enm_tag import Tag
from ..types.partial.classes.cls_searchparams import PartialSearchParams
from ..types.partial.classes.cls_withreasoning import PartialWithReasoning
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


IGetQueryOutput = SearchParams

@runtime_checkable
class IGetQuery(Protocol):
    """
    This is the interface for a function.

    Args:
        query: str

    Returns:
        SearchParams
    """

    async def __call__(self, *, query: str) -> SearchParams:
        ...

   

@runtime_checkable
class IGetQueryStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        query: str

    Returns:
        AsyncStream[SearchParams, PartialSearchParams]
    """

    def __call__(self, *, query: str
) -> AsyncStream[SearchParams, PartialSearchParams]:
        ...
class IBAMLGetQuery(BaseBAMLFunction[SearchParams, PartialSearchParams]):
    def __init__(self) -> None:
        super().__init__(
            "GetQuery",
            IGetQuery,
            ["default_config"],
        )

    async def __call__(self, *args, **kwargs) -> SearchParams:
        return await self.get_impl("default_config").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[SearchParams, PartialSearchParams]:
        res = self.get_impl("default_config").stream(*args, **kwargs)
        return res

BAMLGetQuery = IBAMLGetQuery()

__all__ = [ "BAMLGetQuery" ]
