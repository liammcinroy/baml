# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_namedargssingleclasslist2 import NamedArgsSingleClassList2
from ..types.partial.classes.cls_namedargssingleclasslist2 import PartialNamedArgsSingleClassList2
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, List, Protocol, runtime_checkable


IV2_TestFnNamedArgsSingleStringListOutput = str

@runtime_checkable
class IV2_TestFnNamedArgsSingleStringList(Protocol):
    """
    This is the interface for a function.

    Args:
        myArg: List[NamedArgsSingleClassList2]

    Returns:
        str
    """

    async def __call__(self, *, myArg: List[NamedArgsSingleClassList2]) -> str:
        ...

   

@runtime_checkable
class IV2_TestFnNamedArgsSingleStringListStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        myArg: List[NamedArgsSingleClassList2]

    Returns:
        AsyncStream[str, str]
    """

    def __call__(self, *, myArg: List[NamedArgsSingleClassList2]
) -> AsyncStream[str, str]:
        ...
class IBAMLV2_TestFnNamedArgsSingleStringList(BaseBAMLFunction[str, str]):
    def __init__(self) -> None:
        super().__init__(
            "V2_TestFnNamedArgsSingleStringList",
            IV2_TestFnNamedArgsSingleStringList,
            ["default_config"],
        )

    async def __call__(self, *args, **kwargs) -> str:
        return await self.get_impl("default_config").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[str, str]:
        res = self.get_impl("default_config").stream(*args, **kwargs)
        return res

BAMLV2_TestFnNamedArgsSingleStringList = IBAMLV2_TestFnNamedArgsSingleStringList()

__all__ = [ "BAMLV2_TestFnNamedArgsSingleStringList" ]
