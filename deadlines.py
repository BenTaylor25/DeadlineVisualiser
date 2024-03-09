from datetime import date

deadlines = []

try:
    from private_deadlines import deadlines as p_deadlines
    deadlines = p_deadlines
except FileNotFoundError:
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
