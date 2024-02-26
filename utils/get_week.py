from utils.get_day import get_day


def get_week(uke_liste, data_timeseries):
    for i in range(len(uke_liste)):
        get_day(data_timeseries, uke_liste[i])

