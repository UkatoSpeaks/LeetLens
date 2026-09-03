from app.schemas.analytics import TopicPerformance


WEAK_THRESHOLD = 50.0
AVERAGE_THRESHOLD = 70.0


def classify_topic_performance(
    topics: list[TopicPerformance],
) -> dict:
    strengths = []
    average = []
    weaknesses = []

    for topic in topics:
        if topic.performance < WEAK_THRESHOLD:
            weaknesses.append(topic)
        elif topic.performance < AVERAGE_THRESHOLD:
            average.append(topic)
        else:
            strengths.append(topic)

    return {
        "strengths": strengths,
        "average": average,
        "weaknesses": weaknesses,
    }


def get_weakest_topics(
    topics: list[TopicPerformance],
    limit: int = 5,
) -> list[TopicPerformance]:
    return sorted(
        topics,
        key=lambda topic: topic.performance,
    )[:limit]