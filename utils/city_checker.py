import json

def city_checker(city):
    f = open('./utils/by_liste.json')

    byer = json.load(f)
    
    for by in byer['byListe']:
        if by['city'].lower() == city.lower() :
            return (by['location'])
    return False