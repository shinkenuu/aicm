from csv import DictReader
from random import shuffle

from constants import HUMAN, AI


def read_thematic_descriptions():
    headers = [
        "Format",
        "ID",
        "AI",
        "Human",
    ]

    with open("thematic_descriptions.csv") as file:
        reader = DictReader(file, fieldnames=headers)
        rows = list(reader)

    # skip header row
    return rows[1:]


def roundrobin_challenges():
    thematic_descriptions = read_thematic_descriptions()
    challenges = []

    for thematic_description in thematic_descriptions:
        challenges.append(
            {
                "format": thematic_description["Format"],
                "description": thematic_description["AI"],
                "written_by": AI,
            }
        )

        challenges.append(
            {
                "format": thematic_description["Format"],
                "description": thematic_description["Human"],
                "written_by": HUMAN,
            }
        )

    # challenges = [
    #     {"description": f"{AI} #1", "written_by": AI},
    #     {"description": f"{HUMAN} #2", "written_by": HUMAN},
    #     {"description": f"{AI} #3", "written_by": AI},
    #     {"description": f"{HUMAN} #4", "written_by": HUMAN},
    #     {"description": f"{AI} #5", "written_by": AI},
    # ]

    latest_challenge = None

    assert (
        len(challenges) > 1
    ), "Only 1 challenge is not enough to randomize the order of challenges"

    while 1:
        shuffle(challenges)

        for challenge in challenges:
            if challenge == latest_challenge:
                continue

            latest_challenge = challenge
            yield challenge
