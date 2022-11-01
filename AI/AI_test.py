import openai
from Token.AI_API_KEY import AI_KEY

openai.api_key = AI_KEY

prompt = """
Say this is test
"""

response = openai.Completion.create(model="text-davinci-002",
          prompt=prompt,
          temperature=0.9,
          max_tokens=40,
          top_p=0.2,
          frequency_penalty=0.5,
          presence_penalty=0.0)

print(response["choices"][0]["text"])
