import requests

def fetch_weather(city: str):
    api_url = "http://geocoding-api.open-meteo.com/v1/search"
    params={
        "name":city,
        "count":1
    }
    response=requests.get(api_url,params=params)
    data=response.json()

    if "results" not in data:
        return None

    location = data["results"][0]
    return {
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }