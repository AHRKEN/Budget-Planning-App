"""
Main file for the Budge Master App.
This is an app for budget management.
All the print statements are being used just in the current developing phase for testing and
debugging purposes.

Authors: Gabriel Martinez and Estalin Martinez
Date: Oct 18, 2019
"""
import sys
import functions as func

account_total = float(func.load_total('total.txt')[0])
current_income = float(func.load_total('total.txt')[1])
plan_file = func.load_plan("plan.json")
categories = plan_file[0]
values = plan_file[1]
print(current_income)
# print(values)
# print(categories)

# func.setup()
print('Welcome to BudgeMaster!\nWhere planning budget is as easy like chewing a gum.\n')


def run_app():
    while True:

        answer = func.main_screen(account_total)

        if answer == 'a':  # verify or plan budget
            planning = True
            func.plan_budget(planning, categories, values)

        elif answer == 'b':  # establish new income
            planning = True
            income = func.set_income(account_total)
            func.plan_budget(planning, categories, values)

        elif answer == 'c':  # report a spend
            planning = True
            print('Select category')

        elif answer == 'quit':
            # save the plan and raise SystemExit
            func.save_plan(account_total, 'total.txt')
            func.save_plan(values, "plan.json")
            sys.exit()


run_app()
