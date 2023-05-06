from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {"name": "Bill", "birthday": datetime(year=1994, month=5, day=8)},
    {"name": "Jill", "birthday": datetime(year=1995, month=5, day=9)},
    {"name": "Kim", "birthday": datetime(year=2000, month=5, day=10)},
    {"name": "Jan", "birthday": datetime(year=1970, month=5, day=7)},
]

current_datetime = datetime.now().date()
delta = timedelta(weeks=1)


def get_birthdays_per_week(users):
    delta_week = current_datetime + delta
    birth_dict = defaultdict(list)
    for user in users:
        event = datetime(
            year=delta_week.year,
            month=user["birthday"].month,
            day=user["birthday"].day,
        ).date()

        if current_datetime < event <= delta_week:
            if event.weekday() == 5:
                event += timedelta(days=2)
            elif event.weekday() == 6:
                event += timedelta(days=1)
            day = event.strftime("%A:")
            birth_dict[day].append(user["name"])

    for key, value in birth_dict.items():
        print(key, ", ".join(value))


get_birthdays_per_week(users)
