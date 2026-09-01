from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SubmissionCreate(BaseModel):
    user_id:int
    problem_id:int
    status:str
    language:str|None=None
    runtime:int|None=None
    memory:int|None=None
    code:str|None=None
    is_accepted:bool=False



class SubmissionResponse(BaseModel):
    id:int
    user_id:int
    problem_id:int
    status:str
    language:str|None
    runtime:str|None
    memory:int|None
    code:str|None
    submitted_at:datetime
    is_accepted:bool


    model_config=ConfigDict(from_attributes=True)