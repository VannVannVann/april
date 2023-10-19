def celsius_to_fahrenheit(celsius):
    """ convert value given to fahrenheit"""
    fah = celsius * 9/5 + 32
    return fah

def fahrenheit_to_celsius(fahrenheit):
    """ convert value given to celsius"""
    celsius = fahrenheit - 32
    return celsius


# Program to convert Celsius to Fahrenheit
celsius = 25
fah=celsius_to_fahrenheit(celsius)
print(f"{celsius} degree is {fah} in Fahrenheit")

celsius=fahrenheit_to_celsius(fah)
print(f"{fah} degree Fahrenheit is {celsius} in Celsius")
