import math
import os

def enter_line():                   #to leave an 'enter' space between lines 
    print(' ')                       #to make it easier for users to read
    return

print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
enter_line()

print('\033[1m' + 'Basic calculations avaliable: ')
enter_line()

print('\033[0m' + '1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exit')
enter_line()

while True:
    basic_calc = input('Which basic calculation from the list would you like to calculate? ')
    enter_line()
    os.system('cls')
'''
    if basic_calc == '1':
        numericals = []

        print('''☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲
              ☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲
              ☲☲☲☲''')
        enter_line()
        while True:
            number = input("What is the first number you'd like to add? ")
            os.system('cls')
            if number > '0':
                number = float
                numericals.append(number)
                os.system('cls')
                break
            elif number == 'None': #how to get this to print what it's ment to?!
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('Thank you for usuing the program!!')
                enter_line()
                another_calculation = input('Would you like to complete another calculation?')
                break
            else:
                print('Invaild input, try a number larger then 1')
                enter_line()
                continue
            
        
        while True:
            print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
            enter_line()
            next_number = input("What is the next number you'd like to add? ")
            os.system('cls')
            if next_number > '0':
                next_number = float
                numericals.append(next_number)
                continue

            elif next_number == 'None': #how to get this to print what it's ment to?!
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                numericals.sort()
                print(f"The addition of your {len(numericals)} values is equal to : " + "\\033[1m" + f'{sum(numericals)}')
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                break

            else:
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('Invaild input, try a number larger then 1')
                enter_line()
                continue

    

    elif basic_calc == '2':
        print(':)')
        break
    elif basic_calc == '3':
        print(':(')
        break   
    elif basic_calc == '4':
        #remainder = x%y        for remainder use '%' instead of '/'
        print(':3')
        break 
    else:
        print('Invalid input, try a number between 1 and 5')
        enter_line()
        continue
'''