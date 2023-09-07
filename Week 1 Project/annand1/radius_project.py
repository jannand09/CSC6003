# Write a program that calculates the circumference and area of a circle
# and volume of a sphere with a radius given by the user

# import pi to use in calculations
from cmath import pi

# Accept value of radius inputted by the user, convert value from str to
# int and set radius variable equal to int value
userRadius = eval(input("Enter radius here:"))

# Calculate the circumference
def calculate_circumference(radius):
    circumference = 2*pi*radius
    return circumference

# Calculate the area
def calculate_area(radius):
    area = pi*radius**2
    return area

# Calculate the volume
def calculate_volume(radius):
    volume = (4/3)*pi*radius**3
    return volume

# Pass userRadius through each function to calculate each quantity
# and print result in a string
print("The circumference of a circle with a radius of " + str(userRadius) + " is " + str(calculate_circumference(userRadius)))
print("The area of a circle with a radius of " + str(userRadius) + " is " + str(calculate_area(userRadius)))
print("The volume of a sphere with a radius of " + str(userRadius) + " is " + str(calculate_volume(userRadius)))
