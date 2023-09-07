# Write program that give us largest and smallest numbers in list of
# numbers rpovided by user

def main():
    s = input("Enter list of numbers: ")
    numStr = s.split(",")
    numbers = []
    for x in numStr:
        numbers.append(eval(x))

    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    print("Largest number is", largest)
    print("Smallest number is", smallest)

main()

    