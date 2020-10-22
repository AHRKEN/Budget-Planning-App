"""
Main file for the Budge Master App.
This is an app for budget management.
*** This program needs a 64-bit Python interpreter for ram memory advantage and optimization purposes.

Authors: Gabriel Martinez and Estalin Martinez
Date: Oct 18, 2019
"""


import app_functions

flag = True
user_money = 0

while flag:

    if user_money > 0:
        prompt = input("Do you want to add (+) or substract (-) from your account?"
                       " Or do you want to exit app? (quit) \n ")

        if prompt == "+":
            user_money = app_functions.add_to_acct(user_money)

        elif prompt == "-":
            user_money = app_functions.debit_from_acct(user_money)

        elif prompt.title() == 'Quit':
            flag = False
            print("Thanks for using Budge Master. Where managing your money is easier than chewing gum! ;) ")

        else:
            print("You wrote something that is not this symbol (+) of this symbol (-). \n Please try again. \n")

    else:
        prompt = input("Do you want to add to your account? Yes or No?\n ")
        if prompt.title() == "Yes":
            user_money = app_functions.add_to_acct(user_money)

        elif prompt.title() == 'No':
            flag = False

            print("Thanks for using Budge Master. Where managing your money is easier than chewing gum! ;) ")

        else:
            print("You typed other than 'yes' or 'no'. Please try again. \n ")