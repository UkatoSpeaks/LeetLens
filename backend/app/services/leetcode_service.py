from app.integrations.leetcode.client import LeetCodeClient


async def get_leetcode_profile(username: str) -> dict:
    client = LeetCodeClient()

    try:
        return await client.get_user_profile(username)
    finally:
        await client.close()


async def get_leetcode_submissions(
    username: str,
    limit: int = 20,
) -> list[dict]:
    client = LeetCodeClient()

    try:
        return await client.get_user_submissions(
            username,
            limit,
        )
    finally:
        await client.close()