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
        introcs.isfloat(prompt)

        if prompt == "+":
            adding_money = np.round(input('How much do you want to add to your account? '), 2)
            user_money += float(adding_money)
            print("Now you have $" + str(user_money) + " in your account.\n")

        elif prompt == "-":

            substracting_money = np.round(input('How much do want to substract from your account? '), 2)
            user_money -= float(substracting_money)
            print("Now you have $" + str(user_money) + " in your account.\n")

        else:
            print("You wrote something that is not this symbol (+) of this symbol (-). \n")

    else:
        prompt = input("Do you want to add to your account? ")
        if prompt.title() == "Yes":
            adding_money = np.round(input('How much do you want to add to your account? '), 2)
            user_money += float(adding_money)
            print("Now you have $" + str(user_money) + " in your account.\n")

        elif type(prompt) == type(int) or type(float):
            print("You typed something that are not words. ")

        else:
            keep_up = input("Type 'yes' if you want to add money to your account. If not, type No.")
            if keep_up.title() == "No":
                flag = False
                print("Bye!")
