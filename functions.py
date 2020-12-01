"""
This file contains all the functions of Budge Master App
All print statements are being used just in the current developing phase for testing and debugging
purposes.
"""

categories = ['mortgage', 'car loan', 'groceries']
show_cat = []


def percentage_to_amount(perc, amount):
    """Return the sub amount of the given percentage based on 'amount'."""
    return amount * (perc / 100)


def sub_amount_to_percentage(sub, amount):
    """Return the percentage of the given sub-amount based on 'amount'."""
    return 100 * (sub / amount)


def set_categories(amount):
    for i in categories:
        show_cat.append(i + str(amount))
