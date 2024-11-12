
# Objective: Create a basic banking system in Python where users can perform various operations such as creating an account, checking balance, depositing money, withdrawing money, and transferring money between accounts. Your solution should make extensive use of functions to handle different tasks.

# Requirements:

#     Account Creation:
#         Implement a function create_account() that allows a user to create a new account. The user should provide their name and an initial deposit amount.

#     Check Balance:
#         Implement a function check_balance(account_id) that allows a user to check the balance of their account. The user should provide their account ID.

#     Deposit Money:
#         Implement a function deposit_money(account_id, amount) that allows a user to deposit money into their account. The user should provide their account ID and the amount to deposit.

#     Withdraw Money:
#         Implement a function withdraw_money(account_id, amount) that allows a user to withdraw money from their account. The user should provide their account ID and the amount to withdraw. Ensure that the withdrawal amount does not exceed the account balance.

#     Transfer Money:
#         Implement a function transfer_money(from_account_id, to_account_id, amount) that allows a user to transfer money from one account to another. The user should provide the source account ID, destination account ID, and the amount to transfer. Ensure that the transfer amount does not exceed the source account balandefce.

#     Main Menu:
#         Implement a function main_menu() that displays a menu with options to create an account, check balance, deposit money, withdraw money, transfer money, or exit the system. The menu should repeatedly prompt the user until they choose to exit.

# Instructions:

#     Use dictionaries or lists to manage account information and balances.
#     Ensure to handle edge cases such as invalid account IDs, insufficient funds, and incorrect input.

# Example:

# python

# def create_account():
#     # Implementation to create a new account
#     pass

# def check_balance(account_id):
#     # Implementation to check the balance of an account
#     pass

# def deposit_money(account_id, amount):
#     # Implementation to deposit money into an account
#     pass

# def withdraw_money(account_id, amount):
#     # Implementation to withdraw money from an account
#     pass

# def transfer_money(from_account_id, to_account_id, amount):
#     # Implementation to transfer money between accounts
#     pass

# def main_menu():
#     # Implementation of the main menu to interact with the user
#     pass

# if __name__ == "__main__":
#     main_menu()

# Notes:

#     Ensure that each function is well-defined and handles all necessary input validation.
#     Maintain the state of accounts and balances throughout the program’s execution.

def menu_list():
    print(">> press 1 to create account")
    print(">> press 2 to check balance")
    print(">> press 3 to deposit money")
    print(">> press 4 to withdraw money")
    print(">> press 5 to transfer money")
    print(">> press 6 to quit")

def create_account():
    pass

def check_balance(account_id):
    pass

def deposit_money(accound_id, amount):
    pass 

def withdraw_money(account_id, amount):
    pass

def transfer_money(from_account_id, to_account_id, amount):
    pass
def validate_userinput(input):
    if input in ["", None]:
        print("user input cannot be empty")
        
def main_menu():
    menu_list() 
    user_input = validate_userinput(input())
def __init__():
    main_menu()
__init__()

