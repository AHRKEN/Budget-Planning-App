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
        prompt = input("Do you want to add (+) or substract (-) from your account? ")

        if prompt == "+":
            adding_money = float(input('How much do you want to add to your account? '))
            user_money += format(adding_money, '.6f')
            print("Now you have $" + str(format(user_money, '.2f')) + " in your account.\n ")

        elif prompt == "-":
            substracting_money = float(input('How much do want to substract from your account? '))
            user_money -= np.round(substracting_money, 2)
            print("Now you have $" + str(user_money) + " in your account.\n ")

        else:
            print("You wrote something that is not this symbol (+) of this symbol (-). \n Please try again. ")

    else:
        prompt = input("Do you want to add to your account? Yes or No?\n ")
        if prompt.title() == "Yes":
            adding_money = float(input('How much do you want to add to your account?\n '))
            user_money += np.round(adding_money, 2)
            print("Now you have $" + str(user_money) + " in your account.\n ")

        elif prompt.title() == 'No':
            flag = False

            print("Thanks for using Budge Master. Where managing your money is easier than chewing gum! ;) ")

        else:
            print("Please type 'yes' to add money to your account or 'no' to exit the app. \n ")


