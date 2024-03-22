from os import walk
from datetime import date
import json

DEADLINES_PATH = "./deadline_files"
DEADLINE_FILE_EXTENSION = ".json"

def get_deadline_filenames() -> list[str]:
    filenames = []

    for (_, _, walk_filenames) in walk(DEADLINES_PATH):
        for filename in walk_filenames:
            filenames.append(filename)

    return filenames

def get_user_filename():
    user_filename = input("Enter deadline file name: ")

    # Allow the user to omit file extension.
    if DEADLINE_FILE_EXTENSION not in user_filename:
        user_filename += DEADLINE_FILE_EXTENSION

    return user_filename

def get_deadlines():
    filenames = get_deadline_filenames()

    for filename in filenames:
        print(f"- '{filename}'")

    while True:
        user_filename = get_user_filename()

        if user_filename not in filenames:
            print("Filename not recognised, try again.")
        else:
            break

    with open(F"{DEADLINES_PATH}/{user_filename}") as f:
        deserialised_json = json.load(f)

    deadlines = []
    for entry in deserialised_json:
        deadline = {
            "label": entry["label"],
            "deadline": date(
                entry["year"],
                entry["month"],
                entry["day"]
            )
        }

        deadlines.append(deadline)

    # The graph plots from bottom to top,
    # so we reverse the data in order to
    # show top to bottom.
    deadlines.reverse()

    return deadlines
