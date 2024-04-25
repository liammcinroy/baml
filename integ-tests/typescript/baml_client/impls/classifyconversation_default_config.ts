// This file is auto-generated. Do not edit this file manually.
//
// Disable formatting for this file to avoid linting errors.
// tslint:disable
// @ts-nocheck
/* eslint-disable */


import { GPT4 } from '../client';
import { ClassifyConversation } from '../function';
import { schema } from '../json_schema';
import { InternalMessage } from '../types_internal';
import { Deserializer } from '@boundaryml/baml-core/deserializer/deserializer';


// Impl: default_config
// Client: GPT4
// An implementation for ClassifyConversation


const prompt_template = `Classify the following conversation into following:
{{ ctx.output_schema }}


{% for m in messages %}
{{ _.chat(role=m.role) }}
{{ m.message }}
{% endfor %}`;
const output_format = `"Category as string"[]

Category
---
Refund
CancelOrder
TechnicalSupport
AccountIssue
Question`;

const template_macros = [
]

const deserializer = new Deserializer<Category[]>(schema, {
  $ref: '#/definitions/ClassifyConversation_output'
});

ClassifyConversation.registerImpl('default_config', async (
  args: {
    messages: Message[]
  }
): Promise<Category[]> => {
    const result = await GPT4.run_jinja_template(
      prompt_template,
      args,
      output_format,
      template_macros,
    );

    return deserializer.coerce(result.generated);
  }
);


