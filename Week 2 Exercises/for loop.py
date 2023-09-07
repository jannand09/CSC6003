# Using a for loop, write a code fragment that counts backwards from 50 
# to 25 by 5’s and only prints out the values 50, 45, 40…etc. until 25

def counting_down():
    for x in range(50, 20, -5):
        print(x)

counting_down()
