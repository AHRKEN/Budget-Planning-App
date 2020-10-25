"""
This file contains all the functions of Budge Master App
"""

import pandas as pd


def add_to_acct(user_money):
    """
    This is a function that prompts the user for an amount and adds it to the user_money accumulator
    variable. If the user type something that is not an integer or a float, the user is going to
    receive a message notifying that he entered a wrong answer. And is going to be asked again how
    much does he wants to add to the his account. This is a fruitful function.

    :param user_money: it has to be an integer or a float.
    :return: float
    """
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
    """
    This is a function that prompts the user for an amount and subtract it from the user_money accumulator
    variable. If the user type something that is not an integer or a float, the user is going to
    receive a message notifying that he entered a wrong answer. And is going to be asked again about
    how much does he wants to debit from his account. This is a fruitful function.
    :param user_money: it has to be an integer or a float.
    :return:
    """
    try:
        debit_money = float(input("How much do you want to debit from your account? \n "))
        user_money -= debit_money
        print("Now you have " + str(user_money) + " in your account. \n ")
        return user_money

    except:
        print("Oh! Seems like you've entered something that is not a number. \n Please try again. \n")
        debit_from_acct(user_money)
        return user_money


def repartition(user_money):

    print("How do you want to divide your deposit? \n")

    mortgage_pymt = float(input("Mortgage payment: "))
    car_loan = float(input("Car loan: "))
    house_maintenance = float(input("House maintenance: "))
    car_maintenance = float(input("Car maintenance: "))
    groceries = float(input("Groceries: "))
    cellphone = float(input("Cellphone: "))
    health_insurance = float(input("Health insurance: "))
    hobbies = float(input("Hobbies: "))
    hangouts = float(input("Hangouts: "))
    vacations = float(input("Vacations: "))
    miscellaneous = float(input("Miscellaneous: "))

    categories = [mortgage_pymt, car_loan, house_maintenance, car_maintenance, groceries, cellphone, health_insurance,
                  hobbies, hangouts, vacations, miscellaneous]

    for c in categories:
        user_money -= c

    categ_cols = ['mortgage_pymt', 'car_loan', 'house_maintenance', 'car_maintenance', 'groceries', 'cellphone',
                       'health_insurance', 'hobbies', 'hangouts', 'vacations', 'miscellaneous']

    d = dict(zip(categ_cols, categories))
    df = pd.DataFrame(d, index=range(1, 2))
    print(df)
    print("You have $" + str(user_money) + " for free spend.")
    return df



