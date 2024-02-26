from utils.get_day import get_day


def get_week(uke_liste, data_timeseries):
    for i in range(len(uke_liste)):
        # print(i)
        # print(uke_liste[i].date_isoformat)
        get_day(data_timeseries, uke_liste[i])

