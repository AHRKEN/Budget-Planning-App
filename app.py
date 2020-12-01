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
account_total = 0

while run_app:

    print('What you wanna do?\n' + '(a) verify/plan budget\n' + '(b) add income\n' + '(c) spend\n'
          + '(quit) to end program')
    answer = input()

    if answer == 'a':
        print('Select, add or delete category')

    elif answer == 'b':
        print('How many?')
        amount = input()
        account_total += float(amount)

        print('Select category:')
        for i in func.categories:
            print(i)

        selected = input()

        if selected in func.categories:
            pos = func.categories.index(selected)

            print('How many would you like to establish for ' + func.categories[pos] + '?')
            sub_amount = input()
            cat = func.categories.pop(pos)
            cat_amo = cat + ' ' + str(sub_amount)
            print(cat_amo)

        else:
            print()

        print()

    elif answer == 'c':
        print('Select category')

    elif answer == 'quit':
        # raise SystemExit
        sys.exit()
