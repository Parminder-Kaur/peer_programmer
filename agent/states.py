

from pydantic import BaseModel, Field
from pydantic import ConfigDict

class File(BaseModel):
    path: str = Field(description="")
    purpose: str = Field(description="")


class Plan(BaseModel):
    name: str = Field(description= "")
    description: str = Field(description= "")
    stack: str = Field(description= "")
    features: list[str] = Field(description= "")
    files: list[File] = Field(description= "")

class TaskDetails(BaseModel):
    filepath: str = Field(description= "")
    description: str = Field(description= "")

class ImplementationSteps(BaseModel):
    tasks: list[TaskDetails] = Field(description= "")
    model_config = ConfigDict(extra="allow")
