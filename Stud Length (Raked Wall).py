import math
from math import cos, degrees, radians
import os

math.pi == math.pi
math.cos == math.cos
math.degrees == math.degrees

def invalid_negetive():
      print(' ')
      print(f'Invalid input, please input a ' + '\033[1m' + f'positive' +
            '\033[0m' + f' number')
      print(' ')
def stud_length():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')

      print('\033[1m' + 'Stud Length (/Raked Wall) selected: ' + '\033[0m')
      print(' ')
      print(f'Please remember: The answers will be in the same measurment units you '
            f'input. Unless stated otherwise please keep the units the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect')
      print(' ')
      units = input(f'What units are your measurements in (this will be the same units '
                  f'in the results, all units must be the same unless stated '
                  f'otherwise)? ')
      #while units == int:
      #  invalid_negetive()
      #   units = input('What units are your measurements in? ')
      print(' ')
      print('-----------------------------------------------------------------------')
      print(' ')

      height_outside_edge_lowest_wall = float(input(f'What is the height of the '
                                          f'lowest wall on the outside edge? '))
      while height_outside_edge_lowest_wall < 0:
            invalid_negetive()
            height_outside_edge_lowest_wall = float(input(f'What is the height of the'
                                          f' lowest wall on the outside edge? '))
      print(' ')

      top_plate_thickness = float(input(f'What is the top plates thickness? '))
      while top_plate_thickness < 0:
            invalid_negetive()
            top_plate_thickness = float(input(f'What is the top plates thickness? '))
      print(' ')

      wall_angle = float(input(f'What is the angle of the wall (in degrees (unit), '
                              f'negative values (reflex angles) accepted)? '))
      print(' ')


      #plumb_cut = top_plate_thickness / (math.degrees(math.cos(wall_angle)))
      plumb_cut = (top_plate_thickness / math.sin((90-wall_angle)*(math.pi/180)))
      plumb_cut = round(plumb_cut, 3)


      bottom_plate_thickness = float(input('What is the bottom plate thickness? '))
      while bottom_plate_thickness < 0:
            invalid_negetive()
            bottom_plate_thickness = float(input(f'What is the bottom plate '
                                                f'thickness? '))
      print(' ')

      FIRST_SHORTEST_stud_length = (height_outside_edge_lowest_wall 
                                    - (plumb_cut + bottom_plate_thickness))

      FIRST_SHORTEST_stud_length = round(FIRST_SHORTEST_stud_length, 3)

      print(f"The 'plumb cut' is " + '\033[1m' + f"{plumb_cut}" + f" " + f"{units}" 
            f" " + '\033[0m' )
      print(' ')
      print(f'The very first (shortest) stud length in the raked wall is '
            f'\033[1m' + f'{FIRST_SHORTEST_stud_length}' + f" " + f"{units}" + 
            f'\033[0m' + ' long')
      print(' ')
      continuee=input("Press ENTER to continue")
      os.system('cls')
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      stud_space_running = float(input(f'What is the running stud spacing (the '
                                    f'distance between each of the studs)? '))

      while stud_space_running < 0:
            invalid_negetive()
            stud_space_running = float(input(f'What is the running stud spacing (the '
                                    f'distance between each of the studs)? '))
            
      print(' ')
      what_number_stud = input(f"What number stud along the bottom plate "
                              f"(excluding the very first one on"
                              f" the outside edge, so the miniumum input here is "
                              f"'2') is the one you're calculating the height of? ")

      while what_number_stud < 0:
            invalid_negetive()
            what_number_stud = input(f"What number stud along the bottom plate "
                              f"(excluding the very first one on"
                              f" the outside edge, so the miniumum input here is "
                              f"'2') is the one you're calculating the height of? ")
            
      print(' ')
      rise_of_stud = (math.tan(wall_angle*math.pi/180)*stud_space_running)
      rise_of_stud = round(rise_of_stud, 3)

      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('Your final results/calculation answers are:')
      print(' ')
      print(f'The rise of stud number ' + '\033[1m' + f'{what_number_stud}'  + f" " + 
            f"{units}" + f'\033[0m' + ' is: '   + '\033[1m' + f'{rise_of_stud}' + 
            f'\033[0m')
      print(' ')
      calculated_stud_length = FIRST_SHORTEST_stud_length + rise_of_stud
      calculated_stud_length = round(calculated_stud_length, 3)

      print(f'The stud length for stud number ' + '\033[1m' + f'{what_number_stud}'
            + f'\033[0m' + ' is: '  + '\033[1m' 
            + f'{calculated_stud_length}'  + f" " + f"{units}" + '\033[0m')

      print(' ')
      print('And once again...')
      print(' ')
      print(f"The 'plumb cut' is " + '\033[1m' + f"{plumb_cut}" + f" " + f"{units}" 
            f" " + '\033[0m' )
      print(' ')
      print(f'The very first (shortest) stud length in the raked wall is '
            f'\033[1m' + f'{FIRST_SHORTEST_stud_length}' + f" " + f"{units}" + 
            f'\033[0m' + ' long')
      print(' ')

print('-----------------------------------------------------------------------')
print(' ')
print('Next options:')
print(' ')
print('1. Calulate another stud length (just like you did)')
print(' ')
print('2. Exit')
another_calc = input('Would you like to complete another calculation? ')
if another_calc == 1:
      stud_length()
elif another_calc == 2:
      desired_calculation = main_program_1st_display() #(1)

