"""
This file contains all the functions of Budge Master App
All print statements are being used just in the current developing phase for testing and debugging
purposes.
"""
import json
import numpy as np
import pandas as pd

global_amount = 0
# category_amount = float

"""
Main menu function
"""


def main_screen(account_total):
    """
    Display the "main screen" of the app showing the global amount (money left) and
    showing the options for the user.

    :return: the user command (input) to be evaluated
    """
    print('The total amount left is ' + str(account_total))

    print('\nWhat you wanna do?\n' + '(a) verify/plan budget\n' + '(b) add income\n' + '(c) spend\n'
          + '(quit) to end program')

    answer = input()

    return answer


"""
Functions to establish values
"""


def set_income():
    """
    Ask the user for his or hers current income, add it to account_total and return the income.

    :return: the current income
    """
    amounts = load_total('total.txt')
    account_total = float(amounts[0])

    print('How much is your current income?')
    amount = input()
    account_total += float(amount)
    amounts = [account_total, float(amount)]

    return amounts


def plan_budget(planning, amounts, categories, values):
    """
    Create a loop to be kept for the planning.

    :param amounts:
    :param values:
    :param planning:
    :param categories:
    :return: Doesn't return anything
    """
    while planning:
        print(amounts)
        print(prep_table(categories, values))

        print('\nWrite (create) and the name of the category to create it\n'
              'Write (delete) and the name of the category to delete it\n'
              'Or just write the name of an existing category to set its budget:'
              '\n(main) for Main menu')

        selected = input()

        if selected in categories:
            print('Would you like to plan the ' + selected + ' budget by a (percentage) '
                                                             'or by an specific (amount)?\n')
            answer = input()
            print('What amount?\n')
            amount = input()

            index = categories.index(selected)
            manage_values(values, answer, amount, index=index)

            table = prep_table(categories, values)
            print(table)

        elif selected == 'main':
            planning = False

        elif selected[:6] == 'create':
            categories.append(selected[7:])
            print('Would you like to plan the ' + selected[7:] + ' budget by a (percentage) '
                                                                 'or by an specific (amount)?\n')
            answer = input()
            print('What amount?\n')
            amount = input()

            manage_values(values, answer, amount, new=True)

            print('A category with the name ' + selected[7:] + ' has been created')

            table = prep_table(categories, values)
            print(table)

            # show_table(categories, values)

        elif selected[:6] == 'delete' and selected[7:] in categories.keys():
            del categories[selected[7:]]
            print('The category with the name ' + selected[7:] + ' has been deleted')

        elif selected[:6] == 'delete' and selected[7:] not in categories.keys():
            print('There is no category with the name ' + selected[7:])

        #show_table(categories, values)

        print('\n(keep) planning\n(main) menu')
        answer1 = input()

        if answer1 == 'keep':
            continue
        elif answer1 == 'main':
            planning = False
            print(amounts)
            return amounts


def prep_table(categories, values, modify=False):
    """

    :param categories:
    :param values:
    :return:
    """
    if not modify:
        new_table = pd.DataFrame(values, index=categories)
        return new_table
    '''elif modify:
        table.append
        return table'''


def show_table(categories, values):
    """
    A function to print all categories and their sub-amounts.

    :param values:
    :param categories:
    :return: doesn't return anything
    """
    table = pd.DataFrame(values, index=categories)

    print(table)


def decide(category, values):
    """

    :return:
    """
    print('Would you like to plan the ' + category + ' budget by a (percentage)'
                                                     'or by an specific (amount)?')
    answer = input()
    index = int

    if answer == 'percentage':
        values[answer.title()][index] = 0
        index = 1
    elif answer == 'amount':
        index = 0

    return index


def manage_values(values, answer, amount, index=None, new=False):
    """
    A value manager function.

    :param new:
    :param answer:
    :param values:
    :param index:
    :param amount:
    :return:
    """
    if answer.title() not in values:
        pass
    if not new:
        values[answer.title()][index] = float(amount)
        # then calculate amounts
    elif new:
        values[answer.title()].append(float(amount))
        values['Percentage'].append(0)
        values['Total Left'].append(0)
        values['In Card'].append(0)
        values['Cash'].append(0)
        print(values[answer.title()])
        print(values['Percentage'])
        print(values['Total Left'])
        print(values['In Card'])
        print(values['Cash'])

        return values


def add_amount(amount):
    """
    A function to add founds to the global amount
    :param
    :return:
    """
    global global_amount
    global_amount += amount
    return global_amount


def set_percentage(category):
    """
    A function to establish a percentage for the selected category

    :param category: the selected category from the categories dictionary
    :return: an integer
    :precondition: category should be a valid category from the 'categories' dictionary
    or a new one with string type
    """
    print('What percentage would you like to establish for ' + category + '?')
    percentage = input()
    return float(percentage)


def set_sub_amount(category):
    """
    A function to establish an amount for the selected category

    :param category: the selected category from the categories dictionary
    :return: an integer
    :precondition: category should be a valid category from the 'categories' dictionary
    or a new one with string type
    """
    print('How many would you like to establish for ' + category + '?')
    sub_amount = input()
    return float(sub_amount)


def debit_sub_amount(categories, category, amount):
    """
    A function to debit an amount from the category sub amount.

    :return: Doesn't return anything
    """
    if category in categories.keys():
        categories[category]['amount left'] -= amount


def debit_amount(account_total, amount):
    """

    :param account_total:
    :param amount:
    :return:
    """
    account_total -= amount
    return account_total


def percentage_to_amount(perc, amount):
    """Return the sub amount of the given percentage based on 'amount'."""
    return amount * (perc / 100)


def sub_amount_to_percentage(sub, amount):
    """Return the percentage of the given sub-amount based on 'amount'."""
    return 100 * (sub / amount)


"""
Functions to load and save files
"""


def load_total(filename):
    """
    Returns the contents read from the text file filename.

    :param filename: the file to read
    precondition: filename is a string, referring to a file that exists, and that file
    is a valid text file

    :return: the content in the text file
    """
    data = []

    with open(filename) as file:
        for line in file:
            data.append(line.rstrip('\n'))

    return data


def save_total(data, filename):
    """
    Writes the given data to a text file filename

    :param data:
    :param filename:
    :return:
    """
    print(data)
    with open(filename, 'w') as file:
        file.write(str(data[0]) + '\n' + str(data[1]))

    '''file = open(filename, 'w')

    file.write(data)

    file.close()'''


def load_plan(filename):
    """
    Returns the contents read from the JSON file filename.

    This function reads the contents of the file filename, and will use the json module
    to covert these contents into a Python data value.  This value will either be a
    a dictionary or a list.

    :parameter filename: the file to read
    precondition: filename is a string, referring to a file that exists, and that file
    is a valid JSON file

    :return: the content in the JSON file
    """
    with open(filename) as file:
        data = file.read()
        content = json.loads(data)

    '''file = open(filename)
    data = file.read()
    content = json.loads(data)
    file.close()'''

    return content


def save_plan(data, filename):
    """
    Writes the given data out as a JSON file filename.

    To be a proper JSON file, data must be a a JSON valid type.  That is, it must be
    one of the following:
        (1) a number
        (2) a boolean
        (3) a string
        (4) the value None
        (5) a list
        (6) a dictionary
    The contents of lists or dictionaries must be JSON valid type.

    When written, the JSON data should be nicely indented four spaces for readability.

    :parameter data: The Python value to encode as a JSON file
    Precondition: data is a JSON valid type

    :parameter filename: The file to write
    Precondition: filename is a string representing a path to a file with extension
    .json or .JSON.  The file may or may not exist.

    :return:
    """
    data = [data[0], data[1]]
    file = open(filename, 'w')

    info = json.dumps(data, indent=4)
    file.write(info)

    file.close()
