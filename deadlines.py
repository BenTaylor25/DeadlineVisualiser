from datetime import date

deadlines = []

try:
    from private_deadlines import deadlines as p_deadlines
    deadlines = p_deadlines
except ModuleNotFoundError:
    # If `private_deadlines.py` does not exist, use default data.
    deadlines = [
        {
            "label": "test 1",
            "deadline": date(2024, 3, 10)
        },
        {
            "label": "test 2",
            "deadline": date(2024, 3, 15)
        },
        {
            "label": "test 3",
            "deadline": date(2024, 3, 19)
        },
        {
            "label": "test 4",
            "deadline": date(2024, 3, 22)
        },
        {
            "label": "test 5",
            "deadline": date(2024, 3, 20)
        }
    ]

deadlines.reverse()

from os import walk
import json

DEADLINES_PATH = "./deadline_files"

def get_deadline_filenames() -> list[str]:
    filenames = []

    for (_, _, walk_filenames) in walk(DEADLINES_PATH):
        for filename in walk_filenames:
            filenames.append(filename)

    return filenames

def get_deadlines():
    filenames = get_deadline_filenames()

    for filename in filenames:
        print(f"- '{filename}'")

    while True:
        user_filename = input("Enter deadline file name: ")

        if user_filename not in filenames:
            print("Filename not recognised, try again.")
        else:
            break

    with open(F"{DEADLINES_PATH}/{user_filename}") as f:
        deserialised_json = json.load(f)

    deadlines = []

    for entry in deserialised_json:
        deadline = {
            "label": entry.get("label"),
            "deadline": date(
                entry.get("year"),
                entry.get("month"),
                entry.get("day")
            )
        }

        deadlines.append(deadline)

    deadlines.reverse()

    return deadlines
