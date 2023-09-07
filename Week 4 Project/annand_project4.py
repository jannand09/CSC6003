# Create a class function Rectangle that builds rectangle with length and width attributes
# Create a child class that inherits from Rectangle and adds height attribute and volume method

# Define Rectangle class
class Rectangle:

    # Define length and width parameters
    def __init__(self, l, w):
        self.length = l
        self.width = w
    #Calculate perimeter
    def perimeter(self):
        return (self.length)*2 + (self.width)*2
    #Calculate area
    def area(self):
        return self.length * self.width
    # Display Length, width, perimeter, and area to the console
    def display(self):
        print(" Length: ", str(self.length), "\n", "Width: ", str(self.width), "\n", "Perimeter: ", str(Rectangle.perimeter(self)), "\n", "Area: ", str(Rectangle.area(self)))

# Define Parallelepiped class that inherits methods from Rectangle class
class Parallelepipede(Rectangle):

    #Inherit parameters from Rectangle class and define height parameter
    def __init__(self, l, w, h):
        Rectangle.__init__(self, l, w)
        self.height = h
    #Calculate the volume
    def volume(self):
        return self.length * self.width * self.height
    #Display the volume
    def displayVolume(self):
        print("Volume: ", str(Parallelepipede.volume(self)))

#Ask user to input length and width
length = eval(input("Enter length: "))
width = eval(input("Enter width:  "))

#Create new Rectangle instance with inputted values
user_shape = Rectangle(length, width)

#Display information about rectangle by calling display method
user_shape.display()

#Ask for height
height = eval(input("Enter height: "))

#Create new instance of Parallelpiped using length, width, and height
user_parallelepipede = Parallelepipede(length, width, height)

#Display volume by calling displayVolume method from Parallelpiped class
user_parallelepipede.displayVolume()
