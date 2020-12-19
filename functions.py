"""
This file contains all the functions of Budge Master App
All print statements are being used just in the current developing phase for testing and debugging
purposes.
"""
import json
import numpy as np
import pandas as pd

"""
Main menu function
"""


def main_screen(account_total, current_income):
    """
    Display the "main screen" of the app, showing the account_total amount,
    the last income (paycheck) and options for the user (through commands,
    that later will be GUI buttons).

    parameter account_total: the total amount of all the accounts
    precondition: is a float

    parameter current_income: the amount of the last income
    precondition: is a float
    :return: the user command (input) to be evaluated
    """
    print('The total amount left is ' + str(account_total))
    print('Your last income was of ' + str(current_income))

    print('\nWhat you wanna do?\n' + '(a) verify/plan budget\n' +
          '(b) add income\n' + '(c) spend\n' + '(quit) to end program')

    answer = input()

    return answer


"""
Functions to establish values
"""


def set_income(account_total):
    """
    Ask the user for his or hers current income, add it to account_total and return the income.

    parameter account_total: the total amount of all the accounts
    precondition: is an integer or a float

    :return: the current income
    """
    print('How much is your current income?')
    amount = input()
    account_total += float(amount)
    amounts = [account_total, float(amount)]

    return amounts


def plan_budget(account_total, current_income, table):
    """
    This is the heart of the app.
    Create a loop to be kept for the planning.

    :param account_total:
    :param table:
    :param current_income:
    :return: amounts
    """
    while True:

        # Display budget plan table (GUI)

        print(table)

        # All commands represented between parenthesis represents buttons (GUI)
        print('\nWrite (create) and the name of the category to create it\n'
              'Write (delete) and the name of the category to delete it\n'
              'Or just write the name of an existing category to set its budget:'
              '\n(main) for Main menu')

        # selected can store a command and a category or just a category.
        selected = input()

        # In case selected is an existing category.
        if selected in table.index:
            print('Would you like to plan the ' + selected + ' budget by a (percentage) '
                                                             'or by an specific (amount)?\n')
            # -------Possible Refactor start
            answer = input()
            if answer.title() == 'Amount':
                print('What amount?\n')
                amount = input()
                manage_values(current_income, table, selected, answer, float(amount))
            elif answer.title() == 'Percentage':
                print('What percentage?\n')
                amount = input()
                manage_values(current_income, table, selected, answer, float(amount))
            # -------Possible Refactor end

            save_plan(table, 'plan.json')
            print(table)

        elif selected == 'main':
            amounts = [float(account_total), float(current_income)]
            return amounts

        elif selected[:6] == 'create':
            print('Would you like to plan the ' + selected[7:] + ' budget by a (percentage) '
                                                                 'or by an specific (amount)?\n')
            answer = input()
            if answer.title() == 'Amount':
                print('What amount?\n')
                amount = input()
                table = manage_values(current_income, table, selected[7:], answer, amount, new=True)
            elif answer.title() == 'Percentage':
                print('What percentage?\n')
                amount = input()
                table = manage_values(current_income, table, selected[7:], answer, amount, new=True)

            save_plan(table, 'plan.json')
            print('What amount?\n')
            amount = input()

            table = manage_values(current_income, table, selected[7:], answer, amount, new=True)

            save_plan(table, "plan.json")

            print('A category with the name ' + selected[7:] + ' has been created')

            print(table)

        elif selected[:6] == 'delete' and selected[7:] in table.index:
            table.drop(selected[7:], axis=0, inplace=True)
            save_plan(table, 'plan.json')
            save_plan(table, "plan.json")
            print('The category with the name ' + selected[7:] + ' has been deleted')
            print(table)

        elif selected[:6] == 'delete' and selected[7:] not in table.index:
            print('There is no category with the name ' + selected[7:])

        print('\n(keep) planning\n(main) menu')
        answer1 = input()

        if answer1 == 'keep':
            continue
        elif answer1 == 'main':
            # print(amounts)
            amounts = [float(account_total), float(current_income)]
            return amounts


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


def manage_values(income, table, category, answer, amount, new=False):
    """
    A value manager function.

    :param income: it's the last establish income
    precondition: income is a float

    :param table: a pandas dataframe
    precondition: table is a pandas dataframe

    :param category: the selected category by the user
    precondition: category is a string based on the dataframe index column

    :param answer: could be percentage or amount (it depends on the user)
    precondition: answer is a string

    :param amount: the amount for budgeting determined by the user
    precondition: amount is float

    :param new: it could be False or True depending on the user selection
    on the main menu
    precondition: new is a boolean

    :return: table
    """
    if not new:
        # Write an if, elif, else chain to evaluate if the user is available to set an amount
        # Subtract the available amount from the current_income to be assigned to the selected category
        table.loc[category, answer.title()] = float(amount)
        if answer.title() == 'Percentage':
            amount = percentage_to_amount(float(amount), income)
            table.loc[category, 'Amount'] = round(float(amount), 2)
            # then calculate the rest of the amounts
        elif answer.title() == 'Amount':
            percentage = sub_amount_to_percentage(amount, income)
            table.loc[category, 'Percentage'] = round(float(percentage), 2)
            # then calculate the rest of the values of the table dataframe
        table.loc[category, 'Total Left'] += table.loc[category, 'Amount']
        table.loc[category, 'In Card'] = table.loc[category, 'Amount']
        table.loc[category, 'Cash'] = 0

    elif new:

        new_category = pd.DataFrame(columns=table.columns, index=[category])
        # Write an if, elif, else chain to evaluate if the user is available to set an amount
        # Subtract the available amount from the current_income to be assigned to the selected category
        new_category.loc[category, answer.title()] = float(amount)
        if answer.title() == 'Percentage':
            amount = percentage_to_amount(float(amount), income)
            new_category.loc[category, 'Amount'] = round(float(amount), 2)
        elif answer.title() == 'Amount':
            percentage = sub_amount_to_percentage(float(amount), income)
            new_category.loc[category, 'Percentage'] = round(float(percentage), 2)

        new_category.loc[category, 'Total Left'] = new_category.loc[category, 'Amount']
        new_category.loc[category, 'In Card'] = new_category.loc[category, 'Amount']
        new_category.loc[category, 'Cash'] = 0.0
        #print('new category')
        #print(new_category)
        table = pd.concat([table, new_category])  # float(amount)
        #print('table')
        #print(table)
    elif answer.title() not in table.columns:
        pass

    return table


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


def percentage_to_amount(perc, income):
    """
    Return the sub amount of the given percentage based on 'amount'.

    parameter perc:
    precondition:

    parameter amount:
    precondition:
    """
    sub_amount = income * (perc / 100)
    return sub_amount


def sub_amount_to_percentage(sub, income):
    """
    Return the percentage of the given sub-amount based on 'amount'.

    parameter sub:
    precondition:

    parameter amount:
    precondition:
    """
    percentage = 100 * (sub / income)
    return percentage


"""
Functions to load and save files
"""


def load_total(filename):
    """
    Returns the contents read from the text file 'total.txt' filename as a list,
    that contains 2 strings values.

    parameter filename: the file to read
    precondition: filename is a string, referring to a file that exists,
    and that file is a valid text file

    :return: a list with the content in the text file
    """
    data = []

    with open(filename) as file:
        for line in file:
            data.append(line.rstrip('\n'))

    return data


def save_total(data, filename):
    """
    Writes the given data to a text file filename

    :parameter data:
    :parameter filename:
    :return:
    """
    #print(data)
    with open(filename, 'w') as file:
        file.write(str(data[0]) + '\n' + str(data[1]))


def load_plan(filename):
    """
    Returns the contents read from the JSON file filename.

    This function reads the contents of the file filename, and will use
    the json module to covert these contents into a Python data value.
    This value will either be a dictionary or a list.

    :parameter filename: the file to read
    precondition: filename is a string, referring to a file that exists,
    and that file is a valid JSON file

    :return: the content in the JSON file
    """
    with open(filename) as file:
        data = file.read()
        content = json.loads(data)
        #print("This is the content return: \n" + str(content))
    return content


def save_plan(table, filename):
    """
    Writes the given data out as a JSON file filename.

    To be a proper JSON file, data must be a a JSON valid type.
    That is, it must be one of the following:
        (1) a number
        (2) a boolean
        (3) a string
        (4) the value None
        (5) a list
        (6) a dictionary
    The contents of lists or dictionaries must be JSON valid type.

    When written, the JSON data should be nicely indented four spaces
    for readability.

    :param table:
    :parameter table: The Python value to encode as a JSON file
    Precondition: table is a JSON valid type

    :parameter filename: The file to write
    Precondition: filename is a string representing a path to a file
    with extension .json or .JSON.  The file may or may not exist.

    :return:
    """
    file = open(filename, 'w')
    # Prepare the data to be a valid json format (in this case a nested dict)
    data = table.to_json()
    parsed = json.loads(data)
    #print(parsed)
    # Organize the data with indentation as 4 spaces
    info = json.dumps(parsed, indent=4)
    file.write(info)

    file.close()
