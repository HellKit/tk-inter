import os
import re
from datetime import datetime


BASE_DIR = os.getcwd()
DATA_NOW = datetime.now().strftime('%d.%m.%Y').split('.')

YEAR = int(DATA_NOW[2])
DAY = (
    29 if YEAR % 4 == 0 or YEAR % 100 == 0 and YEAR % 400 == 0 else 28
)
YEAR_TYPE = (
    366 if YEAR % 4 == 0 or YEAR % 100 == 0 and YEAR % 400 == 0 else 365
)


def get_month_days(day=DAY):
    month_days = {
        1: 31, 2: day, 3: 31,
        4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }
    return month_days

def read_file_and_get_date_and_text(file_name):
    path = os.path.join(BASE_DIR, file_name)
    rec = re.compile(r'(\d+\.\d+\.\d+)')
    with open(path, encoding='utf') as f:
        data = f.readlines()
        date = [rec.search(value)[0] for value in data]
        text = [rec.split(value)[-1].strip() for value in data]
        full_date_text = {val: text[idx] for idx, val in enumerate(date)}
    return date, text, full_date_text



def get_days_time(date):
    days = []
    for value in date:
        value = value.split('.')
        date_day, day_now = int(value[0]), int(DATA_NOW[0])
        date_month, month_now = int(value[1]), int(DATA_NOW[1])
        date_year, year_now = int(value[2]), int(DATA_NOW[2])
        day = (
            29 if date_year % 4 == 0 or date_year % 100 == 0 and date_year % 400 == 0 else 28
        )
        month_days = get_month_days(day)
        if date_day >= day_now and date_month == month_now and date_year == year_now:
            days.append(date_day - day_now)
        elif (date_day >= day_now or date_month >= month_now) and date_year == year_now:
            if date_month - month_now > 0:
                for _ in range(date_month - month_now):
                    days_month_now = (
                        sum(
                            [month_days[i] for i in range(month_now, date_month)]
                        ) + date_day - day_now
                    )
                days.append(days_month_now)
            elif date_month - month_now == 0:
                days.append(month_days[month_now] - day_now + date_day)
        elif date_day >= day_now or date_month >= month_now or date_year >= year_now:
            if date_year - year_now > 0:
                result = []
                for _ in range(date_year - year_now):
                    days_year_now = (
                        YEAR_TYPE - sum(
                            [month_days[i] for i in range(1, month_now)]
                        ) - day_now
                    )
                    result.append(
                        days_year_now + sum(
                            [month_days[i] for i in range(1, date_month)]
                        ) + date_day - 1
                    )
                days.append(sum(result))
    return days

        



if __name__ == '__main__':
    date, text, full_date_text = (
        read_file_and_get_date_and_text('do.txt')
    )
    # print(f'{date=}\n')
    # print(f'{text=}\n')
    # print(f'{full_date_text=}\n')
    month_days = get_month_days()
    # print(month_days)
    days = get_days_time(date)
    if len(set(days)) == len(days):
        result = {}
        for idx, key in enumerate(days):
            result[key] = text[idx]
    
    last_result = {}
    for day in set(days):
        last_result[day] = result[day]

    print(last_result)