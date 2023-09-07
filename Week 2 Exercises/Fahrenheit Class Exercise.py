# Write program that receives Fahrenheit tmeperature and
# print show it feels

def main(): 
    temperature = eval(input('Enter Fahrenheit temperature: '))
    if temperature <= 0:
        print("polar")
    elif temperature > 0 and temperature <= 32:
        print("freezing")
    elif temperature > 32 and temperature <= 50:
        print("cold")
    elif temperature > 50 and temperature <= 80:
        print("warm")
    elif temperature > 80 and temperature <= 100:
        print("hot")
    else:
        print("unbearable")

main()
