from utils.update_day import update_day

def get_day(data_timeseries, dag):
    for i in range(len(data_timeseries)):
        if (data_timeseries[i]['time'][0: 10] == dag.date_isoformat):
            update_day(dag, data_timeseries[i])
