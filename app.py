"""
Main file for the Budge Master App.
This is an app for budget management.
All the print statements are being used just in the current developing
phase for testing and debugging purposes.

Authors: Gabriel Martinez and Estalin Martinez
Date: Oct 18, 2019
"""
import sys
import functions as func


def run_app():
    """
    A management of the main loop.
    :return: This is a procedure (unfruitful function)
    """

    # amounts variable stores a list with 2 strings elements.
    amounts = func.load_total('total.txt')
    # account_total includes the sum of all money in the user account(s)
    account_total = float(amounts[0])
    # user last income
    current_income = float(amounts[1])
    # ' plan.json' is a 2 dimensional dictionary.
    plan = func.load_plan("plan.json")

    # func.setup()
    print('Welcome to BudgeMaster!\nWhere planning budget is as easy like chewing a gum.\n')
    table = func.pd.DataFrame(plan)

    while True:

        # User initial input (a), (b), (c) or (quit)
        # These commands will be applied as buttons.
        answer = func.main_screen(account_total, current_income)

        if answer == 'a':
            # this flag activate planning while loop inside plan_budget() function
            amounts = func.plan_budget(account_total, current_income, table)

        elif answer == 'b':
            amounts_mods = func.set_income(account_total)
            amounts = func.plan_budget(amounts_mods[0], amounts_mods[1], table)

        elif answer == 'c':
            print('Select category')

        elif answer == 'quit':
            # save account total, current income, the plan and raise SystemExit
            func.save_total((amounts[0], amounts[1]), 'total.txt')
            sys.exit()


run_app()
