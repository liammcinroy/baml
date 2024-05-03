# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_uniontest_returntype import UnionTest_ReturnType
from ..types.partial.classes.cls_uniontest_returntype import PartialUnionTest_ReturnType
from baml_core.stream import AsyncStream
from typing import Callable, Protocol, Union, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IUnionTest_FunctionOutput = UnionTest_ReturnType

@runtime_checkable
class IUnionTest_Function(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: Union[str, bool]

    Returns:
        UnionTest_ReturnType
    """

    async def __call__(self, arg: Union[str, bool], /) -> UnionTest_ReturnType:
        ...

   

@runtime_checkable
class IUnionTest_FunctionStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: Union[str, bool]

    Returns:
        AsyncStream[UnionTest_ReturnType, PartialUnionTest_ReturnType]
    """

    def __call__(self, arg: Union[str, bool], /) -> AsyncStream[UnionTest_ReturnType, PartialUnionTest_ReturnType]:
        ...
class BAMLUnionTest_FunctionImpl:
    async def run(self, arg: Union[str, bool], /) -> UnionTest_ReturnType:
        ...
    
    def stream(self, arg: Union[str, bool], /) -> AsyncStream[UnionTest_ReturnType, PartialUnionTest_ReturnType]:
        ...

class IBAMLUnionTest_Function:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IUnionTest_Function, IUnionTest_FunctionStream], None]:
        ...

    async def __call__(self, arg: Union[str, bool], /) -> UnionTest_ReturnType:
        ...

    def stream(self, arg: Union[str, bool], /) -> AsyncStream[UnionTest_ReturnType, PartialUnionTest_ReturnType]:
        ...

    def get_impl(self, name: ImplName) -> BAMLUnionTest_FunctionImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the UnionTest_FunctionInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.UnionTest_Function.mock() as mocked:
                    mocked.return_value = ...
                    result = await UnionTest_FunctionImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the UnionTest_FunctionInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.UnionTest_Function.test
            async def test_logic(UnionTest_FunctionImpl: IUnionTest_Function) -> None:
                result = await UnionTest_FunctionImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the UnionTest_FunctionInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.UnionTest_Function.test(exclude_impl=["implname"])
            async def test_logic(UnionTest_FunctionImpl: IUnionTest_Function) -> None:
                result = await UnionTest_FunctionImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.UnionTest_Function.test(stream=True)
            async def test_logic(UnionTest_FunctionImpl: IUnionTest_FunctionStream) -> None:
                async for result in UnionTest_FunctionImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the UnionTest_FunctionInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.UnionTest_Function.test
        class TestClass:
            def test_a(self, UnionTest_FunctionImpl: IUnionTest_Function) -> None:
                ...
            def test_b(self, UnionTest_FunctionImpl: IUnionTest_Function) -> None:
                ...
        ```
        """
        ...

BAMLUnionTest_Function: IBAMLUnionTest_Function
