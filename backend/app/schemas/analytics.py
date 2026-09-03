from pydantic import BaseModel

class TopicPerformance(BaseModel):
    topic:str
    solved:str
    performance:float