"""
This file contains the functions of Budge Master App
"""

def add_to_acct(user_money):
    try:
        adding_money = float(input("How much do you want to add to your account? \n "))
        user_money += adding_money
        print("Now you have $" + str(user_money) + " in your account.\n ")
        return user_money

    except:
        print("Oh! Seems like you've entered something that is not a number. \n Please try again. \n")
        add_to_acct(user_money)
        return user_money


def debit_from_acct(user_money):
    try:
        debit_money = float(input("How much do you want to debit from your account? \n "))
        user_money -= debit_money
        print("Now you have " + str(user_money) + " in your account. \n ")
        return user_money

    except:
        print("Oh! Seems like you've entered something that is not a number. \n Please try again. \n")
        debit_from_acct(user_money)
        return user_money

