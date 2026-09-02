from pydantic import BaseModel


class LeetCodeProfileResponse(BaseModel):
    username: str
    real_name: str | None = None
    about_me: str | None = None
    ranking: int | None = None
    reputation: int | None = None
    star_rating: float | None = None
    submissions: dict