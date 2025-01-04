import openai
from openai import OpenAI

client = OpenAI(api_key="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")


try:
    # API Key 
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "hi!"}])
    print("API Key is valid")
except openai.AuthenticationError:
    print("API Key is not valid")
except openai.OpenAIError as e:
    print(f"another error  : {e}")