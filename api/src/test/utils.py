import random
import string
from datetime import datetime


def generate_random_str() -> str:
    return "".join(random.choices(string.ascii_letters, k=random.randint(1, 225)))

def generate_random_datetime() -> datetime:
    months_with_more_than_30_days = [
        1, 3, 5, 7, 8, 10, 12
    ]
    year = random.randint(1900, datetime.now().year)
    month = random.randint(1, 12)
    if month in months_with_more_than_30_days:
        day = random.randint(1, 31)
    elif month == 2: 
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 30)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    seconds = random.randint(1, 59)
    return datetime(year, month, day, hour, minute, seconds)

def generate_random_float() -> float:
    return round(random.random() * 100, 2)
