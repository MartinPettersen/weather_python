from utils.get_rain import get_rain


def update_day(dag, data_block):
    tid = int(data_block['time'][11: 13])
    temperatur = data_block['data']['instant']['details']['air_temperature']
    vind = data_block['data']['instant']['details']['wind_speed']
    regn = get_rain(data_block)
    dag.update_day(tid, temperatur, vind, regn)