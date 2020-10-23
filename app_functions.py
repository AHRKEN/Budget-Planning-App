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
    user_money -= mortgage_pymt
    car_loan = float(input("Car loan: "))
    user_money -= car_loan
    house_maintenance = float(input("House maintenance: "))
    user_money -= house_maintenance
    car_maintenance = float(input("Car maintenance: "))
    user_money -= car_maintenance
    groceries = float(input("Groceries: "))
    user_money -= groceries
    cellphone = float(input("Cellphone: "))
    user_money -= cellphone
    health_insurance = float(input("Health insurance: "))
    user_money -= health_insurance
    hobbies = float(input("Hobbies: "))
    user_money -= hobbies
    hangouts = float(input("Hangouts: "))
    user_money -= hangouts
    vacations = float(input("Vacations: "))
    user_money -= vacations
    miscellaneous = float(input("Miscellaneous: "))
    user_money -= miscellaneous

    categories = [mortgage_pymt, car_loan, house_maintenance, car_maintenance, groceries, cellphone, health_insurance,
                  hobbies, hangouts, vacations, miscellaneous]
    categ_cols = ['mortgage_pymt', 'car_loan', 'house_maintenance', 'car_maintenance', 'groceries', 'cellphone',
                       'health_insurance', 'hobbies', 'hangouts', 'vacations', 'miscellaneous']

    d = dict(zip(categ_cols, categories))
    df = pd.DataFrame(d, index=range(1, 2))
    print(df)
    print("You have $" + str(user_money) + " for free spend.")
    return df


