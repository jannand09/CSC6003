# Find ratio between two integers and catch exception for division by 0

def main():
    a = eval(input("Enter first number: "))
    b = eval(input("Enter second number "))

    try:
        print(a/b)
    except ValueError:
        print("You must enter a number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except:
        print("Something else went wrong")

main()