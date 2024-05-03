# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.enums.enm_namedargssingleenumlist import NamedArgsSingleEnumList
from baml_core.stream import AsyncStream
from typing import Callable, List, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


ITestFnNamedArgsSingleEnumListOutput = str

@runtime_checkable
class ITestFnNamedArgsSingleEnumList(Protocol):
    """
    This is the interface for a function.

    Args:
        myArg: List[NamedArgsSingleEnumList]

    Returns:
        str
    """

    async def __call__(self, *, myArg: List[NamedArgsSingleEnumList]) -> str:
        ...

   

@runtime_checkable
class ITestFnNamedArgsSingleEnumListStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        myArg: List[NamedArgsSingleEnumList]

    Returns:
        AsyncStream[str, str]
    """

    def __call__(self, *, myArg: List[NamedArgsSingleEnumList]
) -> AsyncStream[str, str]:
        ...
class BAMLTestFnNamedArgsSingleEnumListImpl:
    async def run(self, *, myArg: List[NamedArgsSingleEnumList]) -> str:
        ...
    
    def stream(self, *, myArg: List[NamedArgsSingleEnumList]
) -> AsyncStream[str, str]:
        ...

class IBAMLTestFnNamedArgsSingleEnumList:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[ITestFnNamedArgsSingleEnumList, ITestFnNamedArgsSingleEnumListStream], None]:
        ...

    async def __call__(self, *, myArg: List[NamedArgsSingleEnumList]) -> str:
        ...

    def stream(self, *, myArg: List[NamedArgsSingleEnumList]
) -> AsyncStream[str, str]:
        ...

    def get_impl(self, name: ImplName) -> BAMLTestFnNamedArgsSingleEnumListImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the TestFnNamedArgsSingleEnumListInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.TestFnNamedArgsSingleEnumList.mock() as mocked:
                    mocked.return_value = ...
                    result = await TestFnNamedArgsSingleEnumListImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the TestFnNamedArgsSingleEnumListInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.TestFnNamedArgsSingleEnumList.test
            async def test_logic(TestFnNamedArgsSingleEnumListImpl: ITestFnNamedArgsSingleEnumList) -> None:
                result = await TestFnNamedArgsSingleEnumListImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the TestFnNamedArgsSingleEnumListInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.TestFnNamedArgsSingleEnumList.test(exclude_impl=["implname"])
            async def test_logic(TestFnNamedArgsSingleEnumListImpl: ITestFnNamedArgsSingleEnumList) -> None:
                result = await TestFnNamedArgsSingleEnumListImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.TestFnNamedArgsSingleEnumList.test(stream=True)
            async def test_logic(TestFnNamedArgsSingleEnumListImpl: ITestFnNamedArgsSingleEnumListStream) -> None:
                async for result in TestFnNamedArgsSingleEnumListImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the TestFnNamedArgsSingleEnumListInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.TestFnNamedArgsSingleEnumList.test
        class TestClass:
            def test_a(self, TestFnNamedArgsSingleEnumListImpl: ITestFnNamedArgsSingleEnumList) -> None:
                ...
            def test_b(self, TestFnNamedArgsSingleEnumListImpl: ITestFnNamedArgsSingleEnumList) -> None:
                ...
        ```
        """
        ...

BAMLTestFnNamedArgsSingleEnumList: IBAMLTestFnNamedArgsSingleEnumList
