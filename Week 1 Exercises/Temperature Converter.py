#Create program that converts temperature form Fahrenehit to Celsius
# and vice versa

temp = input("Enter temperature value:")
unit = input("Enter current unit:")

temp = float(temp)

def convertFahrenheit(temperature):
    celsius = (5/9)*(temp - 32)
    print(str(celsius) + " degrees Celsius")

def convertCelsius(temperature):
    fahrenheit = (9/5)*temp + 32
    print(str(fahrenheit) + " degrees Fahrenheit")

if (unit == "Fahrenheit"):
    convertFahrenheit(temp)
elif (unit == "Celsius"):
    convertCelsius(temp)
elif (unit == "Kelvin"):
    print("Come back another time!")
else:
    print("Not a temperature, silly!")
    
