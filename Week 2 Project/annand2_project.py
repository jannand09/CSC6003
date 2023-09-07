# Write a program that checks if two positive integers are divisble

def main():
    # Create infinite loop so if numbers are not divisible
    # Process will repeat
    while True:
        # Ask user for two positive integers
        print("Enter positive integers.")
        dividend = int(input("Enter dividend: "))
        divisor = int(input("Enter divisor: "))

        #Declare result variable as None to be assigned and returned later
        result = None

        # Check if integers entered are positive
        if dividend < 0 or divisor < 0:
            print("Negative integers are not permitted.")
        else:
            # Check if numbers are divisible and assign Boolean to
            # result variable; break loop if result is True
            if dividend % divisor != 0:
                result = False
                print(result)
            else:
                result = True
                print(result)
                break

# Call the main function
main()



