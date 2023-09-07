#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Joey Annand 
# Created Date: 01/07/2022
# version ='1.0'
# ---------------------------------------------------------------------------
# "This program represents a bank with different options for users(bank clients) to interact
# with the bank manager and their own accounts"
# ---------------------------------------------------------------------------

import random

class Account:
    '''
    Account class that creates an account object and the methods available for each account object
    '''
    def __init__(self, num, fname, lname, ssn, pin, balance):
        '''
        Constructor for Accout class takes account information as paramaters
        Parameters:
            self, account number, first name, last name, SSN, Pin number, and balance
        Returns:
            None
        '''
        self.account_num = num
        self.ownerFirstName = fname
        self.ownerLastName = lname
        self.ownerSSN = ssn
        self.pin_num = pin
        self.acc_balance = balance

    def get_accountNum(self):
        '''
        Getter for account number
        Parameters:
            self
        Returns:
            account number
        '''
        return self.account_num
    def set_accountNum(self, num):
        '''
        Setter for account number
        Parameters:
            self, new account num
        Returns:
            None
        '''
        self.account_num = num

    def get_ownerFirstName(self):
        '''
        Getter for first name
        Parameters:
            self
        Returns:
            first name on account
        '''
        return self.ownerFirstName
    def set_ownerFirstName(self, fname):
        '''
        Setter for first name
        Parameters:
            self, first name
        Returns:
            None
        '''
        self.ownerFirstName = fname
    
    def get_ownerLastName(self):
        '''
        Getter for last name
        Parameters:
            self
        Returns:
            last name on account
        '''
        return self.ownerLastName
    def set_ownerLastName(self, lname):
        '''
        Setter for last name
        Parameters:
            self, last name
        Returns:
            None
        '''
        self.ownerLastName = lname

    def get_SSN(self):
        '''
        Getter for SSN
        Parameters:
            self
        Returns:
            SSN of owner
        '''
        return self.ownerSSN
    def set_SSN(self, social):
        '''
        Setter for SSN number
        Parameters:
            self, social security number
        Returns:
            None
        '''
        self.ownerSSN = social
    
    def get_PIN(self):
        '''
        Getter for PIN number
        Parameters:
            self
        Returns:
            PIN number of account
        '''
        return self.pin_num
    def set_PIN(self, pin):
        '''
        Setter for PIN number
        Parameters:
            self, new PIN number
        Returns:
            None
        '''
        self.pin_num = pin
    
    def get_balance(self):
        '''
        Getter for balance
        Parameters:
            self
        Returns:
            account balance
        '''
        return self.acc_balance
    def set_balance(self, balance):
        '''
        Setter for account number
        Parameters:
            self, new balance
        Returns:
            None
        '''
        self.acc_balance = balance

    def deposit(self, amount):
        '''
        Method to deposit money into account
        Parameters:
            self, amount of deposit
        Returns:
            account balance
        '''
        self.acc_balance = self.acc_balance + amount 
        return self.acc_balance
    
  
    def withdraw(self, amount):
        '''
        Method to withdraw money from account
        Parameters:
            self, amount of withdrawl
        Returns:
            account balance
        '''
        self.acc_balance = self.acc_balance - amount
        return self.acc_balance 
    
    
    def isValidPIN(self, pin):
        '''
        Checks if inputted PIN number matches PIN associated with account
        Parameters:
            self, inputted pin
        Returns:
            bool
        '''
        return self.pin_num == pin 
    
    def information(self):
        '''
        Method to print all account information
        Parameters:
            self
        Returns:
            None
        '''
        print("Account number: ",str(self.account_num))
        print("Owner First Name: ",self.ownerFirstName)
        print("Owner Last Name: ",self.ownerLastName)
        print("Owner SSN: ",self.ownerSSN)
        print("PIN Number: ",str(self.pin_num))
        print("Balance: $",str(self.acc_balance))

class Bank:
    
    def __init__(self):
        '''
        Constructs bank object and intitlaizes empty list of accounts and maximum number of accounts Bank can store
        Parameters:
            self
        Returns:
            None
        '''
        self.accounts = []
        self.maximum_accounts = 100

    def addAccountToBank(self, account):
        '''
        Checks if there is available space for a new account and adds new account to list if there is
        Parameters:
            self, account
        Returns:
            bool
        '''       
        if len(self.accounts) == self.maximum_accounts:
            print("No more accounts available.")
            return False
        else:
            self.accounts.append(account)
            return True
         
    def removeAccountFromBank(self, account):
        '''
        Checks if account exists in the bank and removes it if it does
        Parameters:
            self, account
        Returns:
            bool
        ''' 
        i = 0
        for x in range(len(self.accounts)):
            if self.accounts[x] == account:
                self.accounts.pop(x)
                print("Account has been removed.")
                i = i + 1
                return True
        if i == 0:
            return False
    
    def findAccount(self, accountNumber):
        '''
        Checks if account associated with inputted account number exists in the bank
        Parameters:
            self, account number
        Returns:
            account, None
        ''' 
        i = 0
        for x in range(len(self.accounts)):
            if self.accounts[x].get_accountNum() == accountNumber:
                i = i + 1
                return self.accounts[x]
        if i == 0:
            return None
    

class CoinCollector:
    
    def parseChange(coins):
        '''
        Determines value of the coins inputted by the user
        Parameters:
            coins
        Returns:
            value of the coins in cents
        '''        
        value = 0
        for x in coins:
            if x == 'P':
                value += 1
            elif x == 'N':
                value += 5
            elif x == 'D':
                value += 10
            elif x == 'Q':
                value += 25
            elif x == 'H':
                value += 50
            elif x == 'W':
                value += 100
        return value

class BankUtility:
        
    def promptUserForString(prompt):
        '''
        Prompts user to enter string value
        Parameters:
            prompt
        Returns:
            user input
        '''         
        user_string = input(prompt)
        return user_string 

    def promptUserForPositiveNumber(prompt):
        '''
        Prompts user to enter positive number
        Parameters:
            prompt
        Returns:
            user input
        '''            
        user_num = int(input(prompt))
        return user_num 
    
    def generateRandomInteger(min, max):
        '''
        Generates random number
        Parameters:
            minimum value, maximum value
        Returns:
            returns random number between min and max values
        '''        
        rand_num = random.randint(min, max)
        return rand_num 
    
    def convertFromDollarsToCents(amount):             
        '''
        Converts dollars to cents
        Parameters:
            dollar amount
        Returns:
            returns dollar amount in cents
        '''            
        return amount*100
    
    def isNumeric(numberToCheck):
        '''
        Checks if value is a number
        Parameters:
            number
        Returns:
            bool
        '''    
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False

class BankManager: 
   def __init__(self): 
        '''
        Main function of program that allows user to interact with bank and different options of the program
        Parameters:
            self
        Returns:
            None
        '''    
        my_bank = Bank()
        while True:
            print("What would you like to do?")
            print("1. Open an Account")
            print("2. Get account information and balance")
            print("3. Change PIN")
            print("4. Deposit money into account")
            print("5. Transfer money between accounts")
            print("6. Withdraw money from my account")
            print("7. ATM Withdrawl")
            print("8. Deposit Change")
            print("9. Close an account")
            print("10. End Program")

            user_option = BankUtility.promptUserForString("Write the number corresponding to your desired option ") 

            if user_option == '1':
                print("OPEN AN ACCOUNT")
                ownerFirstName = BankUtility.promptUserForString("Enter Account owner's first name: ")
                ownerLastName = BankUtility.promptUserForString("Enter Account owner's last name: ")
                ownerSSN = BankUtility.promptUserForString("Enter the Account owner's Social Security number: ")
                newAccountNum = BankUtility.generateRandomInteger(10000000,99999999)
                newAccountPIN = BankUtility.generateRandomInteger(1000,9999)
                initialDeposit = BankUtility.promptUserForPositiveNumber("Enter amount of initial deposit: ")

                if len(ownerSSN) == 9:

                    new_account = Account(newAccountNum, ownerFirstName, ownerLastName, ownerSSN, newAccountPIN, initialDeposit)

                    my_bank.addAccountToBank(new_account)
                    new_account.information()
                else:
                    print("Invalid SSN. Please try again.")

            elif user_option == '2':
                print("SEARCH FOR ACCOUNT INFORMATION")
                acc = self.promptForAccountNumberAndPIN(my_bank)
            
            elif user_option == '3':
                acc = self.promptForAccountNumberAndPIN(my_bank)
                if acc != None:
                    changePIN_num = BankUtility.promptUserForPositiveNumber("Enter new PIN number: ")
                    confirmPIN_num = BankUtility.promptUserForPositiveNumber("Confirm new PIN number: ")
                    if changePIN_num == confirmPIN_num:
                        user_account = acc
                        user_account.set_PIN(confirmPIN_num)
                        print("PIN updated")
                    else:
                        print("PIN numbers do not match. Please try again.")
            elif user_option == '4':
                acc = self.promptForAccountNumberAndPIN(my_bank)
                if acc != None:
                    new_deposit = BankUtility.promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.75): ")
                    if new_deposit > 0:
                        acc.deposit(new_deposit)
                        print("New balance: $", str(acc.get_balance()))
                    else:
                        print("Cannot deposit negative amount of dollars. Please try again.")
            elif user_option == '5':
                print("Account to transfer from: ")
                first_account = self.promptForAccountNumberAndPIN(my_bank)
                if first_account != None:
                    print("Account to transfer to: ")
                    second_account = self.promptForAccountNumberAndPIN(my_bank)
                    transfer_amt = BankUtility.promptUserForPositiveNumber("Enter dollar amount to transfer (e.g. 2.75): ")
                    if transfer_amt > first_account.get_balance():
                        print("Insufficient funds in account ", str(first_account.get_accountNum()))
                    elif transfer_amt <= 0:
                        print("Amount must be greater than zero.")
                    else:
                        first_account.withdraw(transfer_amt)
                        second_account.deposit(transfer_amt)
                        print("Transfer complete")
                        print("New balance for account: ",str(first_account.get_accountNum)," ",str(first_account.get_balance))
                        print("New balance for account: ",str(second_account.get_accountNum)," ",str(second_account.get_balance))
            elif user_option == '6':
                print("Account to withdraw from: ")
                acc = self.promptForAccountNumberAndPIN(my_bank)
                if acc != None:
                    new_withdrawl = BankUtility.promptUserForPositiveNumber("Enter dollar amount to withdraw (e.g. 2.75): ")
                    if new_withdrawl > acc.get_balance():
                        print("Insufficient funds in account ", str(acc.get_accountNum()))
                    else:
                        acc.withdraw(new_withdrawl)
                        print("New balance: $", str(acc.get_balance()))
            elif user_option == '7':
                print("ATM WITHDRAWL")
                acc = self.promptForAccountNumberAndPIN(my_bank)
                if acc != None:
                    atm_withdrawl = BankUtility.promptUserForPositiveNumber("Enter whole dollar amount that is less than 1000 and divisible by 5: ")
                    if atm_withdrawl > acc.get_balance():
                        print("Insufficient funds in account ", str(acc.get_accountNum()))
                    else:
                        if atm_withdrawl % 5 != 0 or atm_withdrawl > 1000:
                            print("Invalid withdrawl amount. Please try again.")
                        else:
                            max_20s = atm_withdrawl // 20
                            max_10s = atm_withdrawl // 10
                            max_5s = atm_withdrawl // 5

                            if atm_withdrawl > 0:
                                num_of_20s = BankUtility.promptUserForPositiveNumber("Enter number of $20 bills: ")
                                num_of_10s = BankUtility.promptUserForPositiveNumber("Enter number of $10 bills: ")
                                num_of_5s = BankUtility.promptUserForPositiveNumber("Enter number of $5 bills: ")

                                amt_requested = (20*num_of_20s + 10*num_of_10s + 5*num_of_5s)

                                if num_of_20s > max_20s or num_of_10s > max_10s or num_of_5s > max_5s:
                                    print("Invalid Amount. Please try again.")
                                else:
                                    if atm_withdrawl == amt_requested:
                                        acc.withdraw(atm_withdrawl)
                                        print("New balance: $", str(acc.get_balance()))
                                    else:
                                        print("Does not match desired withdrawl amount. Please try again.")
                            else:
                                print("Amount must be postive. Please try again.")
            elif user_option == '8':
                print("COIN DEPOSIT")
                acc = self.promptForAccountNumberAndPIN(my_bank)
                if acc != None:
                    user_coins = BankUtility.promptUserForString("Enter coins as uppercase letters (e.g. QDPN): ").upper()
                    amt_deposited = CoinCollector.parseChange(user_coins)
                    acc.deposit(amt_deposited / 100)
                    print("$ ", str(amt_deposited/100), "of coins deposited into account")
                    print("New balance: $", str(acc.get_balance()))
            elif user_option == '9':
                print("CLOSE ACCOUNT")
                acc = self.promptForAccountNumberAndPIN(my_bank)
                if acc != None:
                    my_bank.removeAccountFromBank(acc)
                    print("Account has been successfully removed")
            elif user_option == '10':
                break
            else:
                print("Not a valid option. Please try again.")
                
   @staticmethod     
   def promptForAccountNumberAndPIN(bank): 
        '''
        Prompts user to enter account number and PIN and checks if both are valid
        Parameters:
            bank
        Returns:
            account, None
        '''     
        num = BankUtility.promptUserForPositiveNumber("Enter account number: ")
        pin = BankUtility.promptUserForPositiveNumber("Enter PIN Number ")

        if bank.findAccount(num) == None:
            print("Account not found for account number: ", str(num))
            return None
        else:
            if bank.findAccount(num).isValidPIN(pin):
                print(bank.findAccount(num).information())
                return bank.findAccount(num)
            else:
                print("Invalid PIN")
                return None

BankManager()


