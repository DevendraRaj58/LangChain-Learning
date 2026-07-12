from langchain_classic.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)


prompt1= PromptTemplate(
    template= 'Write a summary for the following poem \n {poem}',
    input_variables=['poem']
)

parser= StrOutputParser()


loader = TextLoader(
    'sample.txt'
)

data = loader.load()

print(data)
print(type(data))

content = data[0].page_content



chain = prompt1 | model | parser

print(chain.invoke({'poem':content}))

