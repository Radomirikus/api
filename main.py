import requests
from pprint import pprint
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    url = "https://calendarific.com/api/v2/holidays"
    payload = {"api_key": TOKEN, "country": "RU", "year": "2025"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    holidays = response.json()['response']['holidays']
    for holiday in holidays:
        print(f"День: {holiday['date']['datetime']['day']}/{holiday['date']['datetime']['month']}")
        print("Название праздника: ", holiday['name'])
        print("Описание: ", holiday['description'], "\n")

if __name__ == '__main__':
    main()