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

amounts = func.load_total('total.txt')
account_total = float(amounts[0])
current_income = float(amounts[1])
plan = func.load_plan("plan.json")
categories = plan[0]
values = plan[1]
# print(amounts)
# print(account_total)
# print(current_income)
# print(plan)
# print(categories)
# print(values)

# func.setup()
print('Welcome to BudgeMaster!\nWhere planning budget is as easy like chewing a gum.\n')


def run_app():
    while True:

        answer = func.main_screen(account_total)

        if answer == 'a':  # verify or plan budget
            planning = True
            amounts_2 = func.plan_budget(planning, amounts, categories, values)

        elif answer == 'b':  # establish new income
            planning = True
            amounts_mods = func.set_income()
            amounts_2 = func.plan_budget(planning, amounts_mods, categories, values)

        elif answer == 'c':  # report a spend
            planning = True
            print('Select category')

        elif answer == 'quit':
            # save account total, current income, the plan and raise SystemExit
            func.save_total((amounts_2[0], amounts_2[1]), 'total.txt')
            func.save_plan((categories, values), "plan.json")
            sys.exit()


run_app()
