from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.submission import Submission
from app.models.user import User
from app.schemas.submission import SubmissionCreate, SubmissionResponse


router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"],
)


@router.post(
    "/",
    response_model=SubmissionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_submission(
    submission_data: SubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if submission_data.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only create submissions for yourself",
        )

    submission = Submission(
        user_id=current_user.id,
        problem_id=submission_data.problem_id,
        status=submission_data.status,
        language=submission_data.language,
        runtime=submission_data.runtime,
        memory=submission_data.memory,
        code=submission_data.code,
        is_accepted=submission_data.is_accepted,
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    return submission


@router.get(
    "/me",
    response_model=list[SubmissionResponse],
)
def get_my_submissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.scalars(
        select(Submission)
        .where(Submission.user_id == current_user.id)
        .order_by(Submission.submitted_at.desc())
    ).all()


@router.get(
    "/{submission_id}",
    response_model=SubmissionResponse,
)
def get_submission(
    submission_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    submission = db.scalar(
        select(Submission).where(
            Submission.id == submission_id,
            Submission.user_id == current_user.id,
        )
    )

    if submission is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Submission not found",
        )

    return submission