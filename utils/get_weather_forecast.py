import datetime
from utils.dagClass import Dag

from utils.display_info import display_uke
from utils.get_week import get_week

def get_weather_forecast(data, variabler):
    data_properties = data['properties']
    data_timeseries = data_properties['timeseries']

    date_isoformat = datetime.datetime.now()

    uke_liste = []

    for i in range(7):
        ny_dato = date_isoformat + datetime.timedelta(days=(1 + i))
        ukedag = ny_dato.weekday()
        uke_liste.append(Dag(ny_dato, ukedag, variabler))
    get_week(uke_liste, data_timeseries)
    display_uke(uke_liste)