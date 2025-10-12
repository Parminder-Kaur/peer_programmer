from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b")



from pydantic import BaseModel, Field


class File(BaseModel):
    path: str = Field(description="")
    purpose: str = Field(description="")


class Plan(BaseModel):
    name: str = Field(description= "")
    description: str = Field(description= "")
    techstack: str = Field(description= "")
    features: list[str] = Field(description= "")
    files: list[File] = Field(description= "")

user_prompt = "create a simple calculator web application"

prompt = f""" 
you are the planner agent. Convert the user prompt into a complete engineering project plan

User request: {user_prompt}"""


resp = llm.with_structured_output(Plan).invoke(prompt)
print(resp)
