# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_testclasswithenum2 import TestClassWithEnum2
from ..types.enums.enm_enuminclass import EnumInClass
from ..types.partial.classes.cls_testclasswithenum2 import PartialTestClassWithEnum2
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


IFnOutputClassWithEnum_V2Output = TestClassWithEnum2

@runtime_checkable
class IFnOutputClassWithEnum_V2(Protocol):
    """
    This is the interface for a function.

    Args:
        input: str

    Returns:
        TestClassWithEnum2
    """

    async def __call__(self, *, input: str) -> TestClassWithEnum2:
        ...

   

@runtime_checkable
class IFnOutputClassWithEnum_V2Stream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        input: str

    Returns:
        AsyncStream[TestClassWithEnum2, PartialTestClassWithEnum2]
    """

    def __call__(self, *, input: str
) -> AsyncStream[TestClassWithEnum2, PartialTestClassWithEnum2]:
        ...
class IBAMLFnOutputClassWithEnum_V2(BaseBAMLFunction[TestClassWithEnum2, PartialTestClassWithEnum2]):
    def __init__(self) -> None:
        super().__init__(
            "FnOutputClassWithEnum_V2",
            IFnOutputClassWithEnum_V2,
            ["default_config"],
        )

    async def __call__(self, *args, **kwargs) -> TestClassWithEnum2:
        return await self.get_impl("default_config").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[TestClassWithEnum2, PartialTestClassWithEnum2]:
        res = self.get_impl("default_config").stream(*args, **kwargs)
        return res

BAMLFnOutputClassWithEnum_V2 = IBAMLFnOutputClassWithEnum_V2()

__all__ = [ "BAMLFnOutputClassWithEnum_V2" ]
