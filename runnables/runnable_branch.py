from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableBranch,RunnableParallel,RunnableLambda,RunnablePassthrough
load_dotenv()

prompt1= PromptTemplate(
    template = " Wrtie a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= 'Summarize the following text \n {text}',
    input_variables=['text']
)
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

parser = StrOutputParser()

chain = prompt1 |model | parser




branched_chain = RunnableBranch(
    (lambda x:len(x.split()) > 200, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = chain | branched_chain

result = final_chain.invoke({'topic' : 'Semiconductor Future for students in India'})
print(result)