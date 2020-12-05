"""
This file contains all the functions of Budge Master App
All print statements are being used just in the current developing phase for testing and debugging
purposes.
"""
import json

global_amount = 0
category_amount = float


def load_plan(filename):
    """
    Returns the contents read from the JSON file filename.

    This function reads the contents of the file filename, and will use the json module
    to covert these contents into a Python data value.  This value will either be a
    a dictionary or a list.

    :parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file
    is a valid JSON file

    :return:
    """
    file = open(filename)
    data = file.read()
    content = json.loads(data)
    file.close()

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
    file = open(filename, 'w')

    info = json.dumps(data, indent=4)
    file.write(info)

    file.close()


def plan_budget(planning):
    """
    This functions create a loop to be kept for the planning.
    :return:
    """
    while planning:
        show_categories()

        print('Select, type a new or delete a category:\n(main) for Main menu')

        selected = input()

        if selected in categories.keys():

            print('How many would you like to establish for ' + selected + '?')
            sub_amount = input()
            categories[selected] = int(sub_amount)

        elif selected == 'main':
            planning = False

        else:
            loop = True
            while loop:
                print('There is no category with that name\n'
                      'Would you like to create a ' + selected + ' category?\n'
                      '(yes) or (no)')
                ask = input()

                if ask == 'yes':
                    categories[selected] = 0
                    loop = False

                elif ask == 'no':
                    loop = False

                else:
                    continue

        show_categories()

        print('\n(keep) planning\n(main) menu')
        answer = input()

        if answer == 'keep':
            continue
        elif answer == 'main':
            planning = False


def show_categories():
    """

    :return:
    """
    print('Category >> sub amount')
    for key, value in categories.items():
        print(key + ' >> ' + str(value))


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


categories = load_plan("plan.json")