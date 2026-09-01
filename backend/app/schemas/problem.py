from pydantic import BaseModel, ConfigDict


class ProblemCreate(BaseModel):
    title: str
    slug: str
    difficulty: str
    leetcode_id: int | None = None
    url: str | None = None
    is_paid: bool = False
    topic_id: int


class ProblemResponse(BaseModel):
    id: int
    title: str
    slug: str
    difficulty: str
    leetcode_id: int | None
    url: str | None
    is_paid: bool
    topic_id: int

    model_config = ConfigDict(from_attributes=True)