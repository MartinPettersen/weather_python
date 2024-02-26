from utils.city_checker import city_checker

def get_city():

    city = input("Hvilken by ønsker du å vite om?: ")
    lat_lon = city_checker(city)
    while lat_lon == False:
        print(f"Feil: Kan ikke finne en by med navnet '{city}'")
        city = input("Skriv in navn på nytt: ")    
        lat_lon = city_checker(city)

    return lat_lon

def get_variables():
    variabler = input("Hva vil du vite? (regn, temperatur, vind)?: ")
    return variabler.split(", ")

