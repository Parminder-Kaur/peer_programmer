
from typing import Optional
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

class CoderState(BaseModel):
    task_plan: ImplementationSteps = Field(description="The plan for the task to be implemented")
    current_step_idx: int = Field(0, description="The index of the current step in the implementation steps")
    current_file_content: Optional[str] = Field(None, description="The content of the file currently being edited or created")