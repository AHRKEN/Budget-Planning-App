"""
Main file for the Budge Master App.
This is an app for budget management.
*** This program needs a 64-bit Python interpreter for ram memory advantage and optimization purposes.
All the print statements are being used just in the current developing phase for testing and
debugging purposes.

Authors: Gabriel Martinez and Estalin Martinez
Date: Oct 18, 2019
"""
import sys
import functions as func

# Maybe the next line can be deleted because of the sys.exit() function
run_app = True
planning = False
account_total = 0

print('Welcome to BudgeMaster!\nWhere planning budget is as easy like chewing a gum.\n')
categories = func.load_plan("plan.json")

while run_app:

    print('What you wanna do?\n' + '(a) verify/plan budget\n' + '(b) add income\n' + '(c) spend\n'
          + '(quit) to end program')
    answer = input()

    if answer == 'a':
        planning = True

        func.plan_budget(planning)

    elif answer == 'b':
        planning = True

        print('How many?')
        amount = input()
        account_total += float(amount)

        func.plan_budget(planning)

    elif answer == 'c':
        planning = True
        print('Select category')

    elif answer == 'quit':
        # save the plan and raise SystemExit
        func.save_plan(func.categories, "plan.json")
        sys.exit()
