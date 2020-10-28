"""
This file contains all the functions of Budge Master App
All print statements are being used just in the current developing phase for testing and debugging
purposes.
"""
# Pandas is imported to organize user data on a spreadsheet
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
    """
    This is a function that stores user disbursement (repartition of money) across the different
    categories. User inputs are going to be cast to floats so they can be subtracted from the user_money
    variable value.
    :param user_money: float
    :return: dataframe of the repartition breakdown
    """
    print("How do you want to divide your deposit? \n")
    # We should let the user know how much is left on his account balance each time he enters an amount
    # to a category. Maybe with a for loop.

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

    # A list of all user inputs type(strings to floats) stored in each categories list values.
    categories = [mortgage_pymt, car_loan, house_maintenance, car_maintenance, groceries, cellphone, health_insurance,
                  hobbies, hangouts, vacations, miscellaneous]

    # A for loop to subtract each repartition from the main user balance.
    for c in categories:
        # We should limit and notify the user when he have not more balance to assign on his account.
        user_money -= c


    # A list of names for every column of the dataframe.
    categ_cols = ['mortgage_pymt', 'car_loan', 'house_maintenance', 'car_maintenance', 'groceries', 'cellphone',
                  'health_insurance', 'hobbies', 'hangouts', 'vacations', 'miscellaneous']

    # zip method used to cast categories and categ_cols to a dictionary and use this dictionary to cast it
    # into a dataframe.
    d = dict(zip(categ_cols, categories))

    # Creating the dataframe with pandas. For the moment a dataframe of 1 row and 11 columns.
    df = pd.DataFrame(d, index=range(1, 2))
    print(df)

    # Printing the balance left on user account after repartition.
    print("You have $" + str(user_money) + " for free spend.")
    return df



"""
This file contains the functions of Budge Master App
"""

