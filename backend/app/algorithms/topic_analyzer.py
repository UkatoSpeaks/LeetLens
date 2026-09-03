from collections import defaultdict
from app.schemas.leetcode import LeetCodeProblem


DIFFICULTY_WEIGHT={
    "Easy":1.0,
    "Medium":2.0,
    "Hard":3.0
}


def calculate_topic_performance(
        problems: list[LeetCodeProblem],
)->list[dict]:
    topic_stats=defaultdict(
        lambda:{
            "solved":0,
            "weighted_score":0.0
        }
    )

    for problem in problems:
        weight=DIFFICULTY_WEIGHT.get(
            problem.difficulty,
            1.0,
        )

        for topic in problem.topics:
            topic_stats[topic.name]["solved"]+=1
            topic_stats[topic.name]["weighted_score"]+=weight


        results=[]

        for topic, stats in topic_stats.items():
            solved=stats["solved"]
            weight_score=stats["weighted_score"]


            max_possible_score=solved*3.0

            performance=(
                weight_score/max_possible_score
            )*100

            results.append(
                {
                    "topic":topic,
                    "solved":solved,
                    "performance":round(performance,2),
                }
            )

            return sorted(
                results,
                key=lambda item: item["performance"],
                reverse=True
            )