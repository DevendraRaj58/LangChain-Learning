# from langchain_groq import ChatGroq
from dotenv import load_dotenv

# load_dotenv()


# model= ChatGroq(model='llama-3.1-8b-instant')

# result=model.invoke('WHo is the prime minister of India?')


# print(result.content)

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2:3b")

response = llm.invoke("Who is the prime minister of India?")
print(response)