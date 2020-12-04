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
planning = True
account_total = 0

print('Welcome to BudgeMaster!\nWhere planning budget is as easy like chewing a gum.\n')

while run_app:

    print('What you wanna do?\n' + '(a) verify/plan budget\n' + '(b) add income\n' + '(c) spend\n'
          + '(quit) to end program')
    answer = input()

    if answer == 'a':
        planning = True
        print('Select, add or delete category')

    elif answer == 'b':
        planning = True

        print('How many?')
        amount = input()
        account_total += float(amount)

        while planning:

            print('Select category:')
            for i in func.categories.keys():
                print(i)

            selected = input()

            if selected in func.categories.keys():

                print('How many would you like to establish for ' + selected + '?')
                sub_amount = input()
                cat_amount = func.categories[selected] = sub_amount

            else:
                print()

            print('Category >> sub amount')
            for k, v in func.categories.items():
                print(k + ' >> ' + str(v))

            print('\n(keep) planning\n(main) menu')
            answer = input()

            if answer == 'keep':
                continue
            elif answer == 'main':
                planning = False

    elif answer == 'c':
        planning = True
        print('Select category')

    elif answer == 'quit':
        # raise SystemExit
        sys.exit()
