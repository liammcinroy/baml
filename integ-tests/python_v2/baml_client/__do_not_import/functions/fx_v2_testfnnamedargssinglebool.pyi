# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from baml_core.stream import AsyncStream
from typing import Callable, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["default_config"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IV2_TestFnNamedArgsSingleBoolOutput = str

@runtime_checkable
class IV2_TestFnNamedArgsSingleBool(Protocol):
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
class IV2_TestFnNamedArgsSingleBoolStream(Protocol):
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
class BAMLV2_TestFnNamedArgsSingleBoolImpl:
    async def run(self, *, myBool: bool) -> str:
        ...
    
    def stream(self, *, myBool: bool
) -> AsyncStream[str, str]:
        ...

class IBAMLV2_TestFnNamedArgsSingleBool:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IV2_TestFnNamedArgsSingleBool, IV2_TestFnNamedArgsSingleBoolStream], None]:
        ...

    async def __call__(self, *, myBool: bool) -> str:
        ...

    def stream(self, *, myBool: bool
) -> AsyncStream[str, str]:
        ...

    def get_impl(self, name: ImplName) -> BAMLV2_TestFnNamedArgsSingleBoolImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the V2_TestFnNamedArgsSingleBoolInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.V2_TestFnNamedArgsSingleBool.mock() as mocked:
                    mocked.return_value = ...
                    result = await V2_TestFnNamedArgsSingleBoolImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_TestFnNamedArgsSingleBoolInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.V2_TestFnNamedArgsSingleBool.test
            async def test_logic(V2_TestFnNamedArgsSingleBoolImpl: IV2_TestFnNamedArgsSingleBool) -> None:
                result = await V2_TestFnNamedArgsSingleBoolImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_TestFnNamedArgsSingleBoolInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.V2_TestFnNamedArgsSingleBool.test(exclude_impl=["implname"])
            async def test_logic(V2_TestFnNamedArgsSingleBoolImpl: IV2_TestFnNamedArgsSingleBool) -> None:
                result = await V2_TestFnNamedArgsSingleBoolImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.V2_TestFnNamedArgsSingleBool.test(stream=True)
            async def test_logic(V2_TestFnNamedArgsSingleBoolImpl: IV2_TestFnNamedArgsSingleBoolStream) -> None:
                async for result in V2_TestFnNamedArgsSingleBoolImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_TestFnNamedArgsSingleBoolInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.V2_TestFnNamedArgsSingleBool.test
        class TestClass:
            def test_a(self, V2_TestFnNamedArgsSingleBoolImpl: IV2_TestFnNamedArgsSingleBool) -> None:
                ...
            def test_b(self, V2_TestFnNamedArgsSingleBoolImpl: IV2_TestFnNamedArgsSingleBool) -> None:
                ...
        ```
        """
        ...

BAMLV2_TestFnNamedArgsSingleBool: IBAMLV2_TestFnNamedArgsSingleBool
