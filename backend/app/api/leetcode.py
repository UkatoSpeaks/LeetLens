from fastapi import APIRouter, HTTPException

from app.schemas.leetcode import LeetCodeProfileResponse
from app.services.leetcode_service import (
    get_leetcode_profile,
    get_leetcode_submissions,
)


router = APIRouter(
    prefix="/leetcode",
    tags=["LeetCode"],
)


@router.get(
    "/{username}/profile",
    response_model=LeetCodeProfileResponse,
)
async def leetcode_profile(username: str):
    try:
        data = await get_leetcode_profile(username)

        profile = data.get("profile", {})
        submit_stats = data.get("submitStats", {})

        return {
            "username": data["username"],
            "real_name": profile.get("realName"),
            "about_me": profile.get("aboutMe"),
            "ranking": profile.get("ranking"),
            "reputation": profile.get("reputation"),
            "star_rating": profile.get("starRating"),
            "submissions": submit_stats,
        }

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )


@router.get(
    "/{username}/submissions",
)
async def leetcode_submissions(
    username: str,
    limit: int = 20,
):
    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 100",
        )

    try:
        submissions = await get_leetcode_submissions(
            username,
            limit,
        )

        return {
            "username": username,
            "count": len(submissions),
            "submissions": submissions,
        }

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )