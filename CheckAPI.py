import openai
from openai import OpenAI

client = OpenAI(api_key="")


try:
    # API Key 
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "hi!"}])
    print("API Key is valid")
except openai.AuthenticationError:
    print("API Key is not valid")
except openai.OpenAIError as e:
    print(f"another error  : {e}")