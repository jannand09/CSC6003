import pydoc

#Define Student class
class Student:
    #Intitialize class attributes for student name and age
    student_name = "John"
    student_age = 21

    #Create constructor function
    def __init__(self) -> None:
        pass

    #Create display method to display name and age
    def display(self):
        print("Name: ", str(self.student_name), "\n", "Age: ", str(self.student_age))

#Define Engineer class that is child class of Student
class Engineer(Student):
    #Intitialize class attribute for courses taken by Engineer student
    courses = ["Linear Algebra", "Fluid Mechanics", "Quantitative Ananlysis"]

    #Create constructor function and call Student constructor
    def __init__(self):
        super().__init__()

    #Create display method that displays name, age, and courses
    def displayEngineer(self):
        print("Name: ", str(self.student_name), "\n", "Age: ", str(self.student_age), "\n", "Courses: ", str(self.courses))

#Define Doctor class that is child class of Student
class Doctor(Student):
    #Initialize class atrribute for hospitals worked at by Doctor student
    hospitals = ["BMC", "MGH", "Tufts"]

    #Create constructor function and call Student constructor
    def __init__(self):
        super().__init__()

    #Create display method that displays name, age, and hospitals
    def displayDoctor(self):
        print("Name: ", str(self.student_name), "\n", "Age: ", str(self.student_age), "\n", "Hospitals: ", str(self.hospitals))

#Create instances of each class and call display method for each object

student1 = Student()
student1.display()

student2 = Engineer()
student2.displayEngineer()

student3 = Doctor()
student3.displayDoctor()



