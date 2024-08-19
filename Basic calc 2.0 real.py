import math
import os

#def invaild_basic_num

print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
print(' ')

print('\033[1m' + 'Basic calculations avaliable: ')
print(' ')


print('\033[0m' + '1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exit')
print(' ')

basic_calc = (int(input(f'Which basic calculation from the list would you like '
                   f'to calculate? ')))
print(' ')
os.system('cls')

while basic_calc != 5:
    if basic_calc == 1:
        numericals = []
        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
              f'☲☲☲☲')
        number = (int(input("What is the first number you'd like to add? ")))
        number = float
        numericals.append(number)

        next_number = input("What is the next number you'd like to add? ")
        next_number = float
        numericals.append(next_number)

        while next_number != 0:
            next_number = input("What is the next number you'd like to add? ")
            next_number = float
            numericals.append(next_number)
        if next_number == 0:
            answer = sum(numericals) 
            print(answer)        