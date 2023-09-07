#Implement a double-ended queue

import pydoc

class Deque:
    def __init__(self):
        '''
    Constructs Deque object and intializes its items as empty list
    Parameters:
        self
    Returns:
        None   
    '''
        self.items = []
    def isEmpty(self):
        '''
    Checks if the list is empty 
    Parameters:
        self
    Returns:
        Boolean   
    '''
        return self.items == []
    def addToStart(self,item):
        '''
    Uses insert method to add item to start of list 
    Parameters:
        self, item: the item to be added
    Returns:
         self.items: List of items in string including added item  
    '''
        self.items.insert(0, item)
        return self.items
    def addToEnd(self,item):
        '''
    Uses insert method to add item to end of list 
    Parameters:
        self, item: the item to be added
    Returns:
         self.items: List of items in string including added item  
    '''
        self.items.append(item)
        return self.items
    def removeFromStart(self):
        '''
    Uses pop method to remove item at start of the list 
    Parameters:
        self
    Returns:
         self.items.pop(0): item at start if the list that was removed  
    '''
        return self.items.pop(0)
    def removeFromEnd(self):
        '''
    Uses pop method to remove item at end of the list 
    Parameters:
        self
    Returns:
         self.items.pop(): item at start if the list that was removed  
    '''
        return self.items.pop()
    def End(self):
        '''
    Checks what the last item in the list is 
    Parameters:
        self
    Returns:
         self.items.[len(self.items) - 1]: item of index len minus 1 in the list 
    '''
        return self.items[len(self.items) - 1]
    def Start(self):
        '''
    Checks what the first item in the list is 
    Parameters:
        self
    Returns:
         self.items.[0]: item with index 0 in the list  
    '''
        return self.items[0]
    def size(self):
        '''
    Shows how many items are in the list 
    Parameters:
        self
    Returns:
         len(self.list): length of the list  
    '''
        return len(self.items)

deque = Deque()

def main():
    '''
    Uses infinite loop to continously take user input where user can add/remove items from deque or get information
    about deque by calling methods from Deque class
    Parameters:
        none
    Returns:
         Prints information depending on the emthod called to the console  
    '''
    while True:
        value = input("Enter value here: ")
        if value.lower() == "quit":
            break
        elif value.lower() == "list":
            print(deque.items)
        elif value.lower() == "size":
            print(deque.size())
        elif value.lower() == "end":
            print(deque.End())
        elif value.lower() == "start":
            print(deque.Start())
        else:
            add_or_remove = input("Would you like to add or remove element from deque? ")
            start_or_end = input("Would you like to add/remove to/from the start or end of the deque? ")

            if add_or_remove.lower() == "add":
                if start_or_end.lower() == "start":
                    deque.addToStart(value)
                else:
                    deque.addToEnd(value)
            else:
                if start_or_end.lower() == "start":
                    deque.removeFromStart()
                else:
                    deque.removeFromEnd()

main()



