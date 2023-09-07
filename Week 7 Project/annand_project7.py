import random
import time
import pydoc

def bubblesort(list):
    '''
    Sort list using Bubble Sort algorithm
    Parameters:
        unsorted list
    Returns:
        Prints sorted list
    ''' 
    # Swap elements to arrange in order 
    for iter_num in range(len(list)-1,0,-1): 
        print(f"iter_num is {iter_num}")
        for idx in range(iter_num): 
            print(f"\tidx is {idx}")
            if list[idx]>list[idx+1]: 
                temp = list[idx] 
                list[idx] = list[idx+1] 
                list[idx+1] = temp
                print(f"\t\tFlipping {idx} and {idx+1}")
                print(f"\t\t{list}")

def merge_sort(unsorted_list):
    '''
    Sorts list by separating unsorted list into two lists and then calling Merge function
    Parameters:
        unsorted list
    Returns:
        returns sorted list 
    ''' 
    print(f"Calling merge_sort with an unsorted list of {unsorted_list}")
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and divide it
    middle = len(unsorted_list) // 2
    print(f"Middle is {middle}")
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    print(f"left list is {left_list}")
    print(f"right list is {right_list}")
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))
# Merge the sorted halves
def merge(left_half,right_half):
    '''
    Sorts list by comparing values from two halves of unsorted list and stores them in new sorted list
    Parameters:
        left half of unsorted list, right half of unsorted list
    Returns:
        returns sorted list
    ''' 
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

def main():
    '''
    Creates random list of user-defined amount of numbers and records time taken for list to be sorted using Bubble and Merge Sort algorithm
    Parameters:
        None
    Returns:
        prints time taken to sort list using Bubble and Merge sort and which algorithm is faster
    '''
    #Explain the program and ask user for the size of random list they want to sort
    print("This program runs random lists through the Bubble Sort and Merge Sort algorithms.", "\n","Following the completion of the tests,", "\n","the size of each random list and the time taken to sort each of them will be outputted to the console.")
    x = eval(input("How many elements would you like in the random list? "))

    #Create random list
    random_list = [random.randrange(0,x) for i in range(x)]
    list_to_sort = random_list

    #Sort list with Bubble sort and record time
    start_bubble = time.time()
    bubblesort(list_to_sort)
    end_bubble = time.time()

    #Sort list with Merge sort and record time
    start_merge = time.time()
    merge_sort(list_to_sort)
    end_merge = time.time()
    
    #Print the time taken for each algorithm to sort the list
    print("Merge sort for list of ", str(len(list_to_sort)), " elements took ", str(end_merge - start_merge), " seconds to run.")
    print("Bubble sort for list of ", str(len(list_to_sort)), " elements took ", str(end_bubble - start_bubble), " seconds to run.")

    #Determine which algorithm is faster
    if (end_merge - start_merge) < (end_bubble - start_bubble):
        print("Merge sort algorithm is better!")
    else:
        print("Bubble sort algorithm is better!")
    

main()

    
