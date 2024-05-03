# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..__do_not_import.generated_baml_client import baml
from ..baml_types import IV2_TestFnNamedArgsSingleEnumList, IV2_TestFnNamedArgsSingleEnumListStream, NamedArgsSingleEnumList2
from baml_lib._impl.deserializer import Deserializer
from json import dumps
from pytest_baml.ipc_channel import BaseIPCChannel
from typing import Any, List


@baml.V2_TestFnNamedArgsSingleEnumList.test(stream=True)
async def test_case1(V2_TestFnNamedArgsSingleEnumListImpl: IV2_TestFnNamedArgsSingleEnumListStream, baml_ipc_channel: BaseIPCChannel):
    def to_str(item: Any) -> str:
        if isinstance(item, str):
            return item
        return dumps(item)

    case = {""myArg"": ["ONE", "ONE", "TWO"], }
    deserializer_myArg = Deserializer[List[NamedArgsSingleEnumList2]](List[NamedArgsSingleEnumList2]) # type: ignore
    myArg = deserializer_myArg.from_string(to_str(case["myArg"]))
    async with V2_TestFnNamedArgsSingleEnumListImpl(
        myArg=myArg
    ) as stream:
        async for response in stream.parsed_stream:
            baml_ipc_channel.send("partial_response", response.json())

        await stream.get_final_response()
