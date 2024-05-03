# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..clients.client_gpt4turbo import GPT4Turbo
from ..functions.fx_describeimage2 import BAMLDescribeImage2
from ..types.classes.cls_classwithimage import ClassWithImage
from ..types.classes.cls_fakeimage import FakeImage
from ..types.partial.classes.cls_classwithimage import PartialClassWithImage
from ..types.partial.classes.cls_fakeimage import PartialFakeImage
from baml_core.jinja.render_prompt import RenderData
from baml_core.provider_manager.llm_response import LLMResponse
from baml_core.stream import AsyncStream
from baml_lib._impl.deserializer import Deserializer


import typing
# Impl: default_config
# Client: GPT4Turbo
# An implementation of DescribeImage2.

__prompt_template = """\
{{ _.chat(role="user") }}
You should return 2 answers that answer the following commands.

1. Describe this in 5 words:
{{ classWithImage.myImage }}

2. Also tell me what's happening here in one sentence:
{{ img2 }}\
"""

# We ignore the type here because baml does some type magic to make this work
# for inline SpecialForms like Optional, Union, List.
__deserializer = Deserializer[str](str)  # type: ignore

# Add a deserializer that handles stream responses, which are all Partial types
__partial_deserializer = Deserializer[str](str)  # type: ignore

__output_format = """
string
""".strip()

__template_macros = [
]


async def default_config(*, classWithImage: ClassWithImage, img2: Image) -> str:
    response = await GPT4Turbo.run_jinja_template(
        jinja_template=__prompt_template,
        output_format=__output_format, template_macros=__template_macros,
        args=dict(classWithImage=classWithImage, img2=img2)
    )
    deserialized = __deserializer.from_string(response.generated)
    return deserialized


def default_config_stream(*, classWithImage: ClassWithImage, img2: Image
) -> AsyncStream[str, str]:
    def run_prompt() -> typing.AsyncIterator[LLMResponse]:
        raw_stream = GPT4Turbo.run_jinja_template_stream(
            jinja_template=__prompt_template,
            output_format=__output_format, template_macros=__template_macros,
            args=dict(classWithImage=classWithImage, img2=img2)
        )
        return raw_stream
    stream = AsyncStream(stream_cb=run_prompt, partial_deserializer=__partial_deserializer, final_deserializer=__deserializer)
    return stream

BAMLDescribeImage2.register_impl("default_config")(default_config, default_config_stream)