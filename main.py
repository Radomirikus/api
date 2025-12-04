import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    url = "https://calendarific.com/api/v2/holidays"
    payload = {"api_key": token, "country": "RU", "year": "2025"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    holidays = response.json()['response']['holidays']
    for holiday in holidays:
        print(f"""День: {holiday['date']['datetime']['day']}/{holiday['date']['datetime']['month']}
Название праздника: {holiday['name']}
Описание: {holiday['description']} \n""")

if __name__ == '__main__':
    main()