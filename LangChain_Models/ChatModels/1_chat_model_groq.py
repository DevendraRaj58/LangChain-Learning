from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

model= ChatGroq(model='llama-3.1-8b-instant',temperature=0.2)

result=model.invoke('WHo is the prime minister of India?')


print(result.content)
print(result.response_metadata)
