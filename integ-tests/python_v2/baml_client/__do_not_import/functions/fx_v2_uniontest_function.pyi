# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_uniontest_returntypev2 import UnionTest_ReturnTypev2
from ..types.enums.enm_datatype import DataType
from ..types.partial.classes.cls_uniontest_returntypev2 import PartialUnionTest_ReturnTypev2
from baml_core.stream import AsyncStream
from typing import Callable, Protocol, Union, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["default_config"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IV2_UnionTest_FunctionOutput = Union[UnionTest_ReturnTypev2, DataType]

@runtime_checkable
class IV2_UnionTest_Function(Protocol):
    """
    This is the interface for a function.

    Args:
        input: Union[str, bool]

    Returns:
        Union[UnionTest_ReturnTypev2, DataType]
    """

    async def __call__(self, *, input: Union[str, bool]) -> Union[UnionTest_ReturnTypev2, DataType]:
        ...

   

@runtime_checkable
class IV2_UnionTest_FunctionStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        input: Union[str, bool]

    Returns:
        AsyncStream[Union[UnionTest_ReturnTypev2, DataType], Union[UnionTest_ReturnTypev2, DataType]]
    """

    def __call__(self, *, input: Union[str, bool]
) -> AsyncStream[Union[UnionTest_ReturnTypev2, DataType], Union[UnionTest_ReturnTypev2, DataType]]:
        ...
class BAMLV2_UnionTest_FunctionImpl:
    async def run(self, *, input: Union[str, bool]) -> Union[UnionTest_ReturnTypev2, DataType]:
        ...
    
    def stream(self, *, input: Union[str, bool]
) -> AsyncStream[Union[UnionTest_ReturnTypev2, DataType], Union[UnionTest_ReturnTypev2, DataType]]:
        ...

class IBAMLV2_UnionTest_Function:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IV2_UnionTest_Function, IV2_UnionTest_FunctionStream], None]:
        ...

    async def __call__(self, *, input: Union[str, bool]) -> Union[UnionTest_ReturnTypev2, DataType]:
        ...

    def stream(self, *, input: Union[str, bool]
) -> AsyncStream[Union[UnionTest_ReturnTypev2, DataType], Union[UnionTest_ReturnTypev2, DataType]]:
        ...

    def get_impl(self, name: ImplName) -> BAMLV2_UnionTest_FunctionImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the V2_UnionTest_FunctionInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.V2_UnionTest_Function.mock() as mocked:
                    mocked.return_value = ...
                    result = await V2_UnionTest_FunctionImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_UnionTest_FunctionInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.V2_UnionTest_Function.test
            async def test_logic(V2_UnionTest_FunctionImpl: IV2_UnionTest_Function) -> None:
                result = await V2_UnionTest_FunctionImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_UnionTest_FunctionInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.V2_UnionTest_Function.test(exclude_impl=["implname"])
            async def test_logic(V2_UnionTest_FunctionImpl: IV2_UnionTest_Function) -> None:
                result = await V2_UnionTest_FunctionImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.V2_UnionTest_Function.test(stream=True)
            async def test_logic(V2_UnionTest_FunctionImpl: IV2_UnionTest_FunctionStream) -> None:
                async for result in V2_UnionTest_FunctionImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_UnionTest_FunctionInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.V2_UnionTest_Function.test
        class TestClass:
            def test_a(self, V2_UnionTest_FunctionImpl: IV2_UnionTest_Function) -> None:
                ...
            def test_b(self, V2_UnionTest_FunctionImpl: IV2_UnionTest_Function) -> None:
                ...
        ```
        """
        ...

BAMLV2_UnionTest_Function: IBAMLV2_UnionTest_Function
