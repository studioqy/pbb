'''
Week 13 Assignment Wind Chill
Prints a chart calculating the wind chill at various temperatures
December 14 2020
'''

windspeeds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


def celc_to_fahr(celcius):
    fahr = ((9/5) * celcius) + 32
    return fahr


def calc_wind_chill(given_temp):
    for speed in windspeeds:
        chill = 35.74 + 0.6215 * given_temp - 35.75 * \
            (speed ** 0.16) + 0.4275 * given_temp * (speed ** 0.16)
        print(
            f"At temperature {given_temp}F and wind speed {speed} mph, the windchill is {chill:.2f}F")


temperature = float(input("What is the temperature? "))
fahr_or_celc = input("Fahrenheit or Celcius (F/C)? ")

if fahr_or_celc.upper() == "C":
    temperature = celc_to_fahr(temperature)

calc_wind_chill(temperature)
