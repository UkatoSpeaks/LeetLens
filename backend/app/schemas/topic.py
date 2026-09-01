from pydantic import BaseModel, ConfigDict

class TopicCreate(BaseModel):
    name:str


class TopicResponse(BaseModel):
    id:int
    name:str

    model_config=ConfigDict(from_attributes=True)