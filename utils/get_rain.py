def get_rain(data_block):
    if ( 'next_1_hours' in data_block['data']):
        return data_block['data']['next_1_hours']['details']['precipitation_amount']
    elif ( 'next_6_hours' in data_block['data']):
        return data_block['data']['next_6_hours']['details']['precipitation_amount']
    return 0