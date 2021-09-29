from analysis.rate_of_change import rate_of_change
from constants import COVID_URL
from lib.date import get_todays_date
from lib.http import HttpGetRequest

locations = {}

http = HttpGetRequest(COVID_URL)


def fetch_locations():
    date = get_todays_date()
    if date in locations:
        print("From Cache...")
        print(locations)
        print(date)
        return locations[date]
    else:
        print("From External...")
        data = http.get("/")
        locations.clear()
        print("Caching...")
        locations[date] = data["locations"]
        print(locations)
        return data["locations"]


def fetch_country(country_id):
    data = http.get("/" + country_id)
    return data
