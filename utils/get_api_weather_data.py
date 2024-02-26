import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()



def get_api_weather_data(city_location):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?{city_location}"
    headers = {"User-Agent": f"weather app practice, email: {os.getenv('CONTACT_INFO')}"}
    res = requests.get(url, headers=headers)
    return res.json()