

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