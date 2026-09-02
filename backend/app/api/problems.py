from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.problem import Problem
from app.schemas.problem import ProblemCreate, ProblemResponse


router=APIRouter(
    prefix="/problems",
    tags=["Problems"],
)


@router.post(
    "/",
    response_model=ProblemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_problem(
    problem_data: ProblemCreate,
    db:Session=Depends(get_db),
):
    exisiting_problem=db.scalar(
        select(Problem).where(
            Problem.slug == problem_data.slug
        )
    )

    if exisiting_problem:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Problem with this slug already exists",
        )

    problem=Problem(
        title=problem_data.title,
        slug=problem_data.slug,
        difficulty=problem_data.difficulty,
        leetcode_id=problem_data.leetcode_id,
        
    )