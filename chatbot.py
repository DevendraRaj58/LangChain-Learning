from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.09
)


chat_history=[
    SystemMessage(content="You are smart ai assistant who can summarize any type of information for user")
]

while True:
    user_input= input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower()=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ",result.content)


print(chat_history)