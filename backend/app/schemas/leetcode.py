from pydantic import BaseModel


class LeetCodeProfileResponse(BaseModel):
    username: str
    real_name: str | None = None
    about_me: str | None = None
    ranking: int | None = None
    reputation: int | None = None
    star_rating: float | None = None
    submissions: dict



class LeetCodeSubmission(BaseModel):
    title:str
    title_slug:str
    timestamp:int


class LeetCodeTopic(BaseModel):
    name:str
    slug:str


class LeetCodeProblem(BaseModel):
    question_id:str
    title:str
    title_slug:str
    difficulty:str
    is_paid_only:bool
    topics:list[LeetCodeTopic]
