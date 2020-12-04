"""
This file contains all the functions of Budge Master App
All print statements are being used just in the current developing phase for testing and debugging
purposes.
"""

global_amount = 0
category_amount = float

suggested_categories = ['mortgage', 'car loan', 'groceries']
categories = {'mortgage': 0, 'car loan': 0, 'groceries': 0}
show_cat = []


def add_amount(amount):
    """
    A function to add founds to the global amount
    :param
    :return:
    """
    global global_amount
    global_amount += amount
    return global_amount


def debit_amount(amount):
    """

    :param amount:
    :return:
    """
    global category_amount
    category_amount -= amount
    return category_amount


def percentage_to_amount(perc, amount):
    """Return the sub amount of the given percentage based on 'amount'."""
    return amount * (perc / 100)


def sub_amount_to_percentage(sub, amount):
    """Return the percentage of the given sub-amount based on 'amount'."""
    return 100 * (sub / amount)


def set_categories(amount):
    for i in categories:
        show_cat.append(i + str(amount))
