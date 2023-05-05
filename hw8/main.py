from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {"name": "Bill", "birthday": datetime(year=1994, month=5, day=9)},
    {"name": "Jill", "birthday": datetime(year=1995, month=5, day=9)},
    {"name": "Kim", "birthday": datetime(year=2000, month=5, day=10)},
    {"name": "Jan", "birthday": datetime(year=1970, month=5, day=6)},
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
            if not event.weekday() == 5 and not event.weekday() == 6:
                day = event.strftime("%A:")
                birth_dict[day].append(user["name"])
            else:
                day = "Monday"
                birth_dict[day].append(user["name"])
    print(birth_dict)


get_birthdays_per_week(users)
