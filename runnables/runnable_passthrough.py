from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt1= PromptTemplate(
    template = " Wrtie a joke about {topic}",
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='Explain the {joke}',
    input_variables=['joke']
)



model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel(
    {
        'print_joke': RunnablePassthrough(),
        'explain': RunnableSequence(prompt2,model,parser)
    }
)

final_chain = RunnableSequence(chain,parallel_chain)

result = final_chain.invoke({'topic':'LIFE'})
print(result)