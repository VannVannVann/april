def celsius_to_fahrenheit(celsius):
    """ convert value given to fahrenheit"""
    fah = celsius * 9/5 + 32
    return fah

# Program to convert Celsius to Fahrenheit
celsius = 25
fah=celsius_to_fahrenheit(celsius)
print(f"{celsius} degree is {fah} in Fahrenheit")