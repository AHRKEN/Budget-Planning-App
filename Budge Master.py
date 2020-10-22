"""
Main file for the Budge Master App.
This is an app for budget management.
*** This program needs a 64-bit Python interpreter for ram memory advantage and optimization purposes.

Authors: Gabriel Martinez and Estalin Martinez
Date: Oct 18, 2019
"""
import introcs
import numpy as np

flag = True
user_money = 0

while flag:

    if user_money > 0:
        prompt = input("Do you want to add (+) or substract (-) from your account?"
                       " Or do you want to exit app? (quit) \n ")

        if prompt == "+":
            try:
                adding_money = float(input('How much do you want to add to your account? \n '))
                user_money += adding_money
                print("Now you have $" + str(user_money) + " in your account.\n ")
            except:
                print("Oh! Seems like you've entered something that is not a number. \n Please try again.\n")

        elif prompt == "-":
            try:
                substracting_money = float(input('How much do want to substract from your account? \n '))
                user_money -= substracting_money
                print("Now you have $" + str(user_money) + " in your account.\n ")
            except:
                print("Oh! Seems like you've entered something that is not a number. \n Please try again. \n")

        elif prompt.title() == 'Quit':
            flag = False
            print("Thanks for using Budge Master. Where managing your money is easier than chewing gum! ;) ")

        else:
            print("You wrote something that is not this symbol (+) of this symbol (-). \n Please try again. \n")

    else:
        prompt = input("Do you want to add to your account? Yes or No?\n ")
        if prompt.title() == "Yes":
            try:
                adding_money = float(input('How much do you want to add to your account?\n '))
                user_money += adding_money
                print("Now you have $" + str(user_money) + " in your account.\n")
            except:
                print("Oh! Seems like you've entered something that is not a number. \n Please try again. \n")
                # Here the flow is supposed to go to the line 46 to ask the user again about the amount he want to enter.
                # We can then, separate the code in functions so we can recall the process as needed.

        elif prompt.title() == 'No':
            flag = False

            print("Thanks for using Budge Master. Where managing your money is easier than chewing gum! ;) ")

        else:
            print("You typed other than 'yes' or 'no'. Please try again. \n ")