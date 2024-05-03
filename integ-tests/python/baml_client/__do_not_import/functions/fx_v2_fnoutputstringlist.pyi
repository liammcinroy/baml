# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from baml_core.stream import AsyncStream
from typing import Callable, List, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["default_config"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IV2_FnOutputStringListOutput = List[str]

@runtime_checkable
class IV2_FnOutputStringList(Protocol):
    """
    This is the interface for a function.

    Args:
        input: str

    Returns:
        List[str]
    """

    async def __call__(self, *, input: str) -> List[str]:
        ...

   

@runtime_checkable
class IV2_FnOutputStringListStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        input: str

    Returns:
        AsyncStream[List[str], List[str]]
    """

    def __call__(self, *, input: str
) -> AsyncStream[List[str], List[str]]:
        ...
class BAMLV2_FnOutputStringListImpl:
    async def run(self, *, input: str) -> List[str]:
        ...
    
    def stream(self, *, input: str
) -> AsyncStream[List[str], List[str]]:
        ...

class IBAMLV2_FnOutputStringList:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IV2_FnOutputStringList, IV2_FnOutputStringListStream], None]:
        ...

    async def __call__(self, *, input: str) -> List[str]:
        ...

    def stream(self, *, input: str
) -> AsyncStream[List[str], List[str]]:
        ...

    def get_impl(self, name: ImplName) -> BAMLV2_FnOutputStringListImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the V2_FnOutputStringListInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.V2_FnOutputStringList.mock() as mocked:
                    mocked.return_value = ...
                    result = await V2_FnOutputStringListImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_FnOutputStringListInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.V2_FnOutputStringList.test
            async def test_logic(V2_FnOutputStringListImpl: IV2_FnOutputStringList) -> None:
                result = await V2_FnOutputStringListImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_FnOutputStringListInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.V2_FnOutputStringList.test(exclude_impl=["implname"])
            async def test_logic(V2_FnOutputStringListImpl: IV2_FnOutputStringList) -> None:
                result = await V2_FnOutputStringListImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.V2_FnOutputStringList.test(stream=True)
            async def test_logic(V2_FnOutputStringListImpl: IV2_FnOutputStringListStream) -> None:
                async for result in V2_FnOutputStringListImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the V2_FnOutputStringListInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.V2_FnOutputStringList.test
        class TestClass:
            def test_a(self, V2_FnOutputStringListImpl: IV2_FnOutputStringList) -> None:
                ...
            def test_b(self, V2_FnOutputStringListImpl: IV2_FnOutputStringList) -> None:
                ...
        ```
        """
        ...

BAMLV2_FnOutputStringList: IBAMLV2_FnOutputStringList
