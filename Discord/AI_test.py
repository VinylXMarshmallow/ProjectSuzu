import openai
from Tokens.AI_API_KEY import AI_KEY

openai.api_key = AI_KEY



def SendToOpenAI(history):
    prompt = "Suzu is sarcastic and creative. Answer as Suzu: \nLonelyCloud: Hello, who are you?\nSuzu: I am Suzu! Your new friend!\n"

    for content in history:
        prompt += content[0] + ": " + content[1] + "\n"

    prompt += "Suzu: "

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.6,
    max_tokens=60,
    top_p=0.2,
    frequency_penalty=0.0,
    presence_penalty=0.6
    )

    return response["choices"][0]["text"]
