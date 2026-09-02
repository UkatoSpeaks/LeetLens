import httpx


LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"


class LeetCodeClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            timeout=30.0,
            headers={
                "Content-Type": "application/json",
                "Referer": "https://leetcode.com/",
                "User-Agent": "LeetLens/0.1",
            },
        )

    async def get_user_profile(self, username: str) -> dict:
        query = """
        query getUserProfile($username: String!) {
            matchedUser(username: $username) {
                username
                profile {
                    realName
                    aboutMe
                    ranking
                    reputation
                    starRating
                }
                submitStats {
                    acSubmissionNum {
                        difficulty
                        count
                    }
                    totalSubmissionNum {
                        difficulty
                        count
                    }
                }
            }
        }
        """

        response = await self.client.post(
            LEETCODE_GRAPHQL_URL,
            json={
                "query": query,
                "variables": {
                    "username": username,
                },
            },
        )

        response.raise_for_status()

        data = response.json()

        if data.get("errors"):
            raise ValueError(
                f"LeetCode API error: {data['errors']}"
            )

        user = data.get("data", {}).get("matchedUser")

        if user is None:
            raise ValueError(
                f"LeetCode user '{username}' not found"
            )

        return user

    async def close(self):
        await self.client.aclose()