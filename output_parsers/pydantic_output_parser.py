from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from pydantic import BaseModel,Field


load_dotenv()


llm= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task= "text-generation"
)


model=ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name : str =Field(description='Name of the person')
    age : int = Field(gt=18,description='Age of the person')
    city : str = Field(description='City from which the person belongs too')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Generate name,age and city of a fictional {place} person \n {format_instructions} ',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser 

result =chain.invoke({'place':'Indian'})

print(result)


