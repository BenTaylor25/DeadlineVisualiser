from datetime import date, timedelta
from deadlines import DEADLINE_FILE_EXTENSION, DEADLINES_PATH

def get_sample_data() -> str:
    today = date.today()
    five_days = today + timedelta(days=5)
    ten_days = today + timedelta(days=10)

    return (
        '[\n'
        '\t{\n'
        '\t\t"label": "test 1",\n'
        f'\t\t"day": {five_days.day},\n'
        f'\t\t"month": {five_days.month},\n'
        f'\t\t"year": {five_days.year}\n'
        '\t},'
        '\t{\n'
        '\t\t"label": "test 2",\n'
        f'\t\t"day": {ten_days.day},\n'
        f'\t\t"month": {ten_days.month},\n'
        f'\t\t"year": {ten_days.year}\n'
        '\t}\n'
        ']'
    )

    # return (
    #     f'[\n'
    #     f'\t\{\n'
    #     f'"label": "test 1",
    #             "day": {five_days.day},
    #             "month": {five_days.month},
    #             "year": {five_days.year}
    #         },
    #         {
    #             "label": "test 2",
    #             "day": {ten_days.day},
    #             "month": {ten_days.month},
    #             "year": {ten_days.year}
    #         }
    #     ]
    # )

def generate_deadline_format():
    filename = f"test{DEADLINE_FILE_EXTENSION}"
    full_path = f"{DEADLINES_PATH}/{filename}"

    with open(full_path, 'w') as file:
        file.write(get_sample_data())

if __name__ == "__main__":
    generate_deadline_format()
