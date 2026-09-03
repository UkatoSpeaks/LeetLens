from app.schemas.leetcode import (
    LeetCodeProblem,
    LeetCodeSubmission,
    LeetCodeTopic,
)


def normalize_submission(
    submission: dict,
) -> LeetCodeSubmission:
    return LeetCodeSubmission(
        title=submission["title"],
        title_slug=submission["titleSlug"],
        timestamp=int(submission["timestamp"]),
    )


def normalize_problem(
    problem: dict,
) -> LeetCodeProblem:
    topics = [
        LeetCodeTopic(
            name=topic["name"],
            slug=topic["slug"],
        )
        for topic in problem.get("topicTags", [])
    ]

    return LeetCodeProblem(
        question_id=str(problem["questionId"]),
        title=problem["title"],
        title_slug=problem["titleSlug"],
        difficulty=problem["difficulty"],
        is_paid_only=problem["isPaidOnly"],
        topics=topics,
    )