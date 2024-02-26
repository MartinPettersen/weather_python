
from utils.update_day import update_day


def get_day(data_timeseries, dag):
    # print(len(data_timeseries))
    
    for i in range(len(data_timeseries)):
        if (data_timeseries[i]['time'][0: 10] == dag.date_isoformat):
            # print(i)
            update_day(dag, data_timeseries[i])
        # print(data_timeseries[i]['time'][0: 10])
