import requests
import os
from dotenv import load_dotenv


MONTHS = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря",
]

def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    url = "https://calendarific.com/api/v2/holidays"
    payload = {"api_key": token, "country": "RU", "year": "2025"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    holidays = response.json()['response']['holidays']
    for holiday in holidays:
        month = holiday['date']['datetime']['month']
        print(f"""День: {holiday['date']['datetime']['day']} {MONTHS[month-1]}
Название праздника: {holiday['name']}
Описание: {holiday['description']}\n""")


if __name__ == '__main__':
    main()