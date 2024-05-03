# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


ITestFnNamedArgsSingleBoolOutput = str

@runtime_checkable
class ITestFnNamedArgsSingleBool(Protocol):
    """
    This is the interface for a function.

    Args:
        myBool: bool

    Returns:
        str
    """

    async def __call__(self, *, myBool: bool) -> str:
        ...

   

@runtime_checkable
class ITestFnNamedArgsSingleBoolStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        myBool: bool

    Returns:
        AsyncStream[str, str]
    """

    def __call__(self, *, myBool: bool
) -> AsyncStream[str, str]:
        ...
class IBAMLTestFnNamedArgsSingleBool(BaseBAMLFunction[str, str]):
    def __init__(self) -> None:
        super().__init__(
            "TestFnNamedArgsSingleBool",
            ITestFnNamedArgsSingleBool,
            ["v1"],
        )

    async def __call__(self, *args, **kwargs) -> str:
        return await self.get_impl("v1").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[str, str]:
        res = self.get_impl("v1").stream(*args, **kwargs)
        return res

BAMLTestFnNamedArgsSingleBool = IBAMLTestFnNamedArgsSingleBool()

__all__ = [ "BAMLTestFnNamedArgsSingleBool" ]
