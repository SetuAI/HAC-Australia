# import libraries

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

import os
api_key = os.getenv("OPENAI_API_KEY")


model = ChatOpenAI(
    model ="gpt-4o",
    max_tokens = 500, # if you dont want any limit, set it to None
    api_key = api_key
)

# LCEL : Langchain Expression Language
# apply , .invoke()

result = model.invoke("Can you tell me about the latest advancements in GPU?")

# print(result) # result is used when i want content + metadata

print(result.content) # result.content is used when i want only content