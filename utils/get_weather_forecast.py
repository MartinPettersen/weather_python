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
        # print(date_isoformat +datetime.timedelta(days=(1 + i)))
        ny_dato = date_isoformat + datetime.timedelta(days=(1 + i))
        # print("-------------------------------------")
        # print(ny_dato)
        # print(date_isoformat)
        ukedag = ny_dato.weekday()
        # print(ukedag)
        # print(date_isoformat.weekday())

        # print("-------------------------------------")

        uke_liste.append(Dag(ny_dato, ukedag, variabler))

    # print(date_isoformat)

    # print(uke_liste[0].date_isoformat)

    get_week(uke_liste, data_timeseries)
    display_uke(uke_liste)
   # map( tester(data_timeseries) , data_timeseries)