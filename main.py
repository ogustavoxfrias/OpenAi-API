#G.Frias - 19/02/2024
#Antes de tentar, dê uma lida na documentação da API da OpenAi.

import os
from openai import OpenAI
import json
from key import OPENAI_API_KEY

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", OPENAI_API_KEY))

model = "gpt-3.5-turbo"

messages = []

input_message = input('Pergunte: ')
messages.append({"role": "user", "content": input_message})

while input_message != 'obrigado gpt':
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )

    answer = response.choices[0].message.content

    ##print(json.dumps(json.loads(response.model_dump_json()), indent=4))

    messages.append({"role": "assistant", "content": answer})

    print(': ', answer)

    input_message = input('Pergunte: ')
    messages.append({"role": "user", "content": input_message})
