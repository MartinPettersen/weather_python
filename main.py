from utils.get_user_input import get_city, get_variables
from utils.get_api_weather_data import get_api_weather_data
from utils.get_weather_forecast import get_weather_forecast

def main():
    city = get_city()
    variables = get_variables()
    weather_data = get_api_weather_data(city)
    get_weather_forecast(weather_data, variables)


main()

