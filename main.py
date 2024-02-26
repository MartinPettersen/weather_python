from utils.get_user_input import get_city, get_variables
from utils.get_api_weather_data import get_api_weather_data

def main():
    city = get_city()
    variables = get_variables()
    weather_data = get_api_weather_data(city)
    

main()

