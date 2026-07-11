from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt1= PromptTemplate(
    template = " Wrtie a joke about {topic}",
    input_variables=['topic']
)

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

parser = StrOutputParser()

chain = RunnableSequence(
    prompt1,model,parser
)

print(chain.invoke({'topic':'AI'})) 