# Using a do while loop, write a code fragment that reads a 
# String from the keyboard from the user until the user types “EXIT”

while True:
    userString = input("Enter word here: ").upper()
    if userString == "EXIT":
        break
