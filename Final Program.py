import math
import os

#to check if number (works w deciamls)
def is_number(input_str):
     try:
          float(input_str)
          return True
     except ValueError:
          return False
#invalid negative
def invalid_negetive():
      print(' ')
      print(f'Invalid input, please input a more ' + '\033[1m' + f'positive' +
            '\033[0m' + f' number')
      print(' ')

#Main Program
def main_program_1st_display():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲')
    print(' ')

    print('Welcome to the program!!')
    print(' ')

    print(f'How to use the program: You’ll notice that all items in the lists '
          f'shown are numbered, when asked for what you’d like to complete '
          f'please enter the corresponding number to the operation you’d '
          f'like.')
    print(' ')
    print('Operations avaliable: ')
    print(' ')

    print('\033[1m' + 'Complex: ')
    print('\033[0m' + '1. Linear Metres Of Decking Required ')
    print('2. Stud Length (/Raked Wall) ')
    print(' ')

    print('\033[1m' + 'Simple: ')
    print('\033[0m' + '3. Area Of A Shape ')
    print('4. Volume Of A Shape ')

    print(' ')
    print('5. Exit ')
    print(' ')

    desired_calculation = (input(f'What calculation would you like to '
                                    f'complete from the list/s? '))
    
    
    #checking desired_calculation is a number
    while not desired_calculation.isdigit():
      print(' ')
      print('Invalid input, please input a positive integer value.. ')
      print(' ')
      desired_calculation = (input(f'What calculation would you like to '
                                    f'complete from the list/s? '))
    desired_calculation = int(desired_calculation)

    return desired_calculation

#desired_calculation invalid
def desired_calculation_invalid():
      print(' ')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲')
      print(' ')
      print(f'Invalid input, try a number between 1 and 6 from the list '
      f'(above)')
      print(' ')
      desired_calculation = input(f"What calculation would you like to "
                                    f"complete from the list/s?  ")
      desired_calculation = int(desired_calculation)
      return desired_calculation

#DECKING OPTION (1) (a couple calcs over 80 spaces)
def linear_metres_decking_required():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲')
      print(' ')
      print('\033[1m' + 'Linear Metres Of Decking Required Selected: ')
      print('')           
      print(f'\033[0m' + f'Next to the questions, units will be stated. '
            f'Please do not include the units in your input '
            f'it is simply to tell you what units the input '
            f'should be in.')     
      print(' ')
      deck_num = input(f'What number deck are you calculating '
                       f'the linear metres of decking required for? ')

      #input validation
      while not is_number(deck_num) or float(deck_num) < 0:
            print('')

            if not is_number(deck_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(deck_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            deck_num = (input(f'What number deck are you calculating '
                       f'the linear metres of decking required for? '))
      deck_num = float(deck_num)

      print(' ')
      width = (input(f"What is the width of the decking boards "
                        f"you're going to be using (units: millimetres)? "))

      while not is_number(width) or float(width) < 0:
            print('')

            if not is_number(width) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(width) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            width = (input(f"What is the width of the decking boards "
                        f"you're going to be using (units: millimetres)? "))
      width = float(width)
      print(' ')

      gap = (input(f'What is the width of the gap between the '
                        f'decking boards horizontally (units: '
                        f'millimetres)? '))
      
      while not is_number(gap) or float(gap) < 0:
            print('')

            if not is_number(gap) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(gap) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            gap = (input(f'What is the width of the gap between the '
                        f'decking boards horizontally (units: '
                        f'millimetres)? '))
      gap = float(gap)

      print(' ')

      deck_width = (input(f'What is the width of the overall '
                              f'(whole) deck (units: metres)? '))
      
      while not is_number(deck_width) or float(deck_width) < 0:
            print('')

            if not is_number(deck_width) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(deck_width) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            deck_width = (input(f'What is the width of the overall '
                              f'(whole) deck (units: metres)? '))
            
      deck_width = float(deck_width)

      print(' ')

      deck_length = (input(f'What is the length of the overall '
                              f'(whole) deck (units: metres)? '))

      while not is_number(deck_length) or float(deck_length) < 0:
            print('')

            if not is_number(deck_length) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(deck_length) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            deck_length = (input(f'What is the length of the overall '
                              f'(whole) deck (units: metres)? '))
      deck_length = float(deck_length)


      print(f'------------------------------------------'
            f'-----------------------------')
      print(' ')
      print(f'**A waste percentage is how much waste (extra) '
            f'are you allowing for. Between 5 - 15% is '
            f'recommended with 10% usually being a great allowance. '
            f'At least greater then zero**')
      print(' ')
      waste_percentage_num = (input(f"What is the waste percentage "
                                    f"number you would like to allow "
                                    f"(units: whole number (/percentage "
                                    f"without '%' sign))? "))
      while not (is_number(waste_percentage_num) or 
                 float(waste_percentage_num) < 0):
            print('')

            if not is_number(waste_percentage_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(waste_percentage_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            waste_percentage_num = (input(f"What is the waste percentage "
                                    f"number you would like to allow "
                                    f"(units: whole number (/percentage "
                                    f"without '%' sign))? "))
      waste_percentage_num = float(waste_percentage_num)
      
      os.system('cls')

      decking_area = deck_width * deck_length
      decking_area_rounded = round(decking_area, 3)

      waste_percentage = (waste_percentage_num / 100) + 1

      #Amount in m^2 one linear metre (board) takes up
      decking_area_in_m2 = (gap + width) / 1000

      quantity_linear_m = (((decking_area) / decking_area_in_m2) 
                           * waste_percentage)
      quantity_linear_m_rounded = round(quantity_linear_m, 3)

      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲')
      print(' ')
      print('\033[1m' + 'Linear Metres Of Decking Required Selected: ')
      print(' ')
      print(f'\033[0m' + f'For this {decking_area} metres-squared deck, ' 
            + '\033[1m' +  f'{quantity_linear_m_rounded} linear-metres ' 
            + '\033[0m' + f'of decking is required')
      print(' ')
      return quantity_linear_m_rounded, deck_num

def another_calc_linear_decking():            
      print(f'-------------------------------------'
            f'----------------------------------')
      print(' ')
      print('Next options:')
      print(' ')
      print(f'1. Calulate another amount of linear metres '
            f'of decking (just like you did)')
      print('2. Back to main menu')
      another_calc_Ld = (input(f"Would you like to complete "
                                  f"another calculation? (input '1' or '2') "))
      
      #checking another_calc_Ld isn't decimal, or letter or anything but 1 or 2
      while True:
            if ((another_calc_Ld) == '1' or (another_calc_Ld) == '2'):
               another_calc_Ld = int(another_calc_Ld)
               break #valid input
            else: 
                  print(' ')
                  if not another_calc_Ld.isdigit():
                           print(f'Invalid input, please '
                                 f'input a positive integer value.. ')
                           print(' ')
                  else:
                        print(f"Invalid input, please "
                                 f"input either '1' or '2'.. ")
                        print(' ')
                  another_calc_Ld = (input(f"Would you like to complete "
                                  f"another "
                                  f"calculation? (input '1' or '2'): "))

      another_calc_Ld = int(another_calc_Ld)

      return another_calc_Ld

#for stud bit
def another_calc_stud():
      print(f'-----------------------------------------------'
            f'------------------------')
      print(' ')
      print('Next options:')
      print(' ')
      print('1. Calulate another stud length (just like you did)')
      print('2. Back to main menu')
      print(' ')
      another_calc = (input(f"Would you like to complete another "
                               f"calculation? (input '1' or '2') "))
      
      #checking another_calc is a number
      while not another_calc.isdigit() or (int(another_calc) < 1 or 
                                           int(another_calc) > 2):
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            another_calc = (input(f"Would you like to complete another "
                                  f"calculation? (input '1' or '2') "))
      another_calc = int(another_calc)

      return another_calc
#STUD OPTION (2)
def stud_length():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲')
      print(' ')

      print('\033[1m' + 'Stud Length (/Raked Wall) selected: ' + '\033[0m')
      print(' ')
      print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')
      print(' ')
      print(f'Please also remember to input whole numbers during this operation')
      print(' ')
      units = input(f'What units are your measurements in? ')
      while units.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units = input(f'What units are your measurements in? ')
      print(' ')
      print(f'--------------------------------------'
            f'---------------------------------')
      print(' ')

      height_outside_edge_lowest_wall = (input(f'What is the height '
                                                    f'of the '
                                          f'lowest wall on the outside '
                                          f'edge? '))
      while not height_outside_edge_lowest_wall.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a whole '
                        f'positive integer value.. ')
            print(' ')
            height_outside_edge_lowest_wall = (input(f'What is the height '
                                                    f'of the '
                                          f'lowest wall on the outside '
                                          f'edge? '))
      height_outside_edge_lowest_wall = float(height_outside_edge_lowest_wall)
  
      print(' ')

      top_plate_thickness = (input(f'What is the top plates thickness? '))
      while not top_plate_thickness.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a whole '
                        f'positive integer value.. ')
            print(' ')
            top_plate_thickness = (input(f'What is the top plates '
                                         f'thickness? '))
      top_plate_thickness = float(top_plate_thickness)

      print(' ')

      wall_angle = (input(f'What is the angle of the wall '
                               f'(in degrees (unit))? '))
      while not wall_angle.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a whole '
                        f'positive integer value.. ')
            print(' ')
            wall_angle = (input(f'What is the angle of the wall '
                               f'(in degrees (unit))? '))
      wall_angle = float(wall_angle)
      print(' ')

      plumb_cut = (top_plate_thickness/math.sin((90-wall_angle)*(math.pi/180)))
      plumb_cut = round(plumb_cut, 3)


      bottom_plate_thickness = (input(f'What is the bottom '
                                           f'plate thickness? '))
      while not bottom_plate_thickness.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a whole '
                        f'positive integer value.. ')
            print(' ')
            bottom_plate_thickness = (input(f'What is the bottom '
                                           f'plate thickness? '))
      bottom_plate_thickness = float(bottom_plate_thickness)


      print(' ')

      FIRST_SHORTEST_stud_length = (height_outside_edge_lowest_wall 
                                    - (plumb_cut + bottom_plate_thickness))

      FIRST_SHORTEST_stud_length = round(FIRST_SHORTEST_stud_length, 3)
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲')
      print(' ')
      print(f"The 'plumb cut' is " 
            + f'\033[1m' + f"{plumb_cut}" + f" " + f"mm" 
            f" " + '\033[0m' )
      print(' ')
      print(f'The very first (shortest) stud length in the raked wall is '
            f'\033[1m' + f'{FIRST_SHORTEST_stud_length}' + f" " + f"mm" + 
            f'\033[0m' + ' long')
      print(' ')
      continue_stud=input(f"Press " + '\033[1m' + f"ENTER" + '\033[0m' 
                      + f" to continue")
      os.system('cls')
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      stud_space_running = (input(f"What is the running stud "
                                             f"spacing (the "
                                    f"distance from the very first "
                                    f"stud at the lowest side of the wall "
                                    f"to the stud you're currently "
                                    f"calculating the length of)? "))
      while not stud_space_running.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a whole '
                        f'positive integer value.. ')
            print(' ')
            stud_space_running = (input(f"What is the running stud "
                                             f"spacing (the "
                                    f"distance from the very first "
                                    f"stud at the lowest side of the wall "
                                    f"to the stud you're currently "
                                    f"calculating the length of)? "))
      stud_space_running = float(stud_space_running)
            
      print(' ')
      what_number_stud = (input(f"What number stud along the bottom plate "
                              f"(excluding the very first one on"
                              f" the outside edge, so the miniumum "
                              f"input here is "
                              f"'2') is the one you're calculating "
                              f"the height of? "))
      while not what_number_stud.isdigit() or float(what_number_stud) <= 1:
            print(' ')
            print(f"Invalid input, please input a whole '
                        f'positive integer value greater then '1'.. ")
            print(' ')
            what_number_stud = (input(f"What number stud along the "
                                      f"bottom plate "
                              f"(excluding the very first one on"
                              f" the outside edge, so the miniumum "
                              f"input here is "
                              f"'2') is the one you're calculating "
                              f"the height of? "))
      what_number_stud = float(what_number_stud)

      print(' ')
      rise_of_stud = (math.tan(wall_angle*math.pi/180)*stud_space_running)
      rise_of_stud = round(rise_of_stud, 3)

      spacing_along_top_plate = math.sqrt((stud_space_running**2) 
                                          + (rise_of_stud**2))
      
      spacing_along_top_plate = round(spacing_along_top_plate, 3)

      calculated_stud_length = FIRST_SHORTEST_stud_length + rise_of_stud
      calculated_stud_length = round(calculated_stud_length, 3)

      overall_wall_height = (calculated_stud_length + top_plate_thickness 
                             + plumb_cut)
      overall_wall_height =  round(overall_wall_height, 3)

      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('Your final results/calculation answers are:')
      print(' ')
      print(f'The rise of stud number ' + '\033[1m' + f'{what_number_stud}'
            + f'\033[0m' + ' is: '   + '\033[1m' + f'{rise_of_stud}' + 
            f'\033[0m')
      print(' ')

      print(f'The stud length for stud number ' 
            + f'\033[1m' + f'{what_number_stud}'
            + f'\033[0m' + ' is: '  + '\033[1m' 
            + f'{calculated_stud_length}'  + f" " + f"mm" + '\033[0m')
      print(' ')
      print(f'This stud is ' + '\033[1m' + f'{spacing_along_top_plate}'
            + '\033[0m' + f' ' + f'mm' + f' along the top plate')
      print(' ')
      print(f"And at this stud the overall (total) wall height "
            f"is " + "\033[1m" + f"{overall_wall_height} mm " 
            + f"\033[0m" + f"tall")
      print(' ')
      print('And once again...')
      print(' ')
      print(f"The 'plumb cut' is " 
            + f'\033[1m' + f"{plumb_cut}" + f" " + f"mm" 
            f" " + '\033[0m' )
      print(' ')
      print(f'The very first (shortest) stud length in the raked wall is '
            f'\033[1m' + f'{FIRST_SHORTEST_stud_length}' + f" " + f"mm" + 
            f'\033[0m' + ' long')
      print(' ')
      return (calculated_stud_length, what_number_stud, 
              spacing_along_top_plate, FIRST_SHORTEST_stud_length, 
              overall_wall_height, units)

#desired_calculation = 3 ('what shape' calculation functions)
def calc_rectangle_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Rectangle area selected: ')
    print(' ')
    print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')
      
    print(' ')
    rectangle_num = input('\033[0m' + f'What number rectangle are you '
                          f'calculating the area of? ')      
    
    while not is_number(rectangle_num) or float(rectangle_num) < 0:
            print('')

            if not is_number(rectangle_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(rectangle_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            rectangle_num = (input(f'What number rectangle are you '
                          f'calculating the area of? '))
    rectangle_num = float(rectangle_num)
    print(' ')              
    units_rec = input(f"What units (metres, centimetres, etc) are you're "  
                      f"measurements in? ")
    while units_rec.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_rec = input(f'What units are your measurements in? ')
    print(' ')
    width = (input('\033[0m' + 'What is the width of the rectangle? '))

    while not is_number(width) or float(width) < 0:
            print('')

            if not is_number(width) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(width) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            width = (input(f'What is the width of the rectangle? '))
    width = float(width)
    print('')
    
    length = (input('What is the length of the rectangle? '))

    while not is_number(length) or float(length) < 0:
            print('')

            if not is_number(length) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(length) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            length = (input('What is the length of the rectangle? '))
    length = float(length)

    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Rectangle volume selected: ')
    print('')
    
    rectangle_area = width * length
    rectangle_area_rounded = round(rectangle_area, 3)
    return rectangle_area_rounded, rectangle_num, units_rec

def calc_square_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲')
    print('') 
    print('\033[1m' + 'Square area selected: ')
    print('')  
    print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')

    print(' ')
    square_num = input('\033[0m' + f'What number square are you '
                       f'calculating the area of? ')      
    print(' ')              
    units_square = input(f"What units (metres, centimetres, etc) are you're "       
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
    while units_square.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_square = input(f'What units are your measurements in? ')
    print(' ')
    measurement = (input('\033[0m' + f'What is the side length of the '
                              f'square? '))
    while not is_number(measurement) or float(measurement) < 0:
            print('')

            if not is_number(measurement) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(measurement) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            measurement = (input(f'What is the side length of the '
                              f'square? '))
    measurement = float(measurement)


    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Square area selected: ')
    print('')
    
    square_area = measurement * 2
    square_area_rounded = round(square_area, 3)
    return square_area_rounded, square_num, units_square
def calc_circle_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲')
    print(' ')
    
    print('\033[1m' + 'Circle area selected: ')
    print('')  
    print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')
    
    print(' ')
    circle_num = input('\033[0m' + f'What number circle are you calculating '
                       f'the area of? ') 
    while not is_number(circle_num) or float(circle_num) < 0:
            print('')

            if not is_number(circle_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(circle_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            circle_num = (input(f'What number circle are you calculating '
                       f'the area of? '))
    circle_num = float(circle_num)     
    print(' ')              
    units_circle = input(f"What units (metres, centimetres, etc) are you're " 
                      f"measurements in? ")
    while units_circle.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_circle = input(f'What units are your measurements in? ')
    print(' ')
    radius = (input(f'\033[0m' + f'What is the radius of the circle? '))
    while not is_number(radius) or float(radius) < 0:
            print('')

            if not is_number(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            radius = (input(f'What is the radius of the circle? '))
    radius = float(radius)
    print(' ')

    print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Circle area selected: ')
    print(' ')
    
    circle_area = math.pi * (radius ** 2)
    circle_area_rounded = round(circle_area, 3)
    return circle_area_rounded, circle_num, units_circle
def calc_cylinder_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲')
    print(' ')       
    print('\033[1m' + 'Cylinder (Surface Area) selected: ')
    print('')  
    print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')
    
    print(' ')
    cylinder_num = input('\033[0m' + f'What number cylinder are '
                         f'you calculating the area of? ')    
    while not is_number(cylinder_num) or float(cylinder_num) < 0:
            print('')

            if not is_number(cylinder_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(cylinder_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            cylinder_num = (input(f'What number cylinder are '
                         f'you calculating the area of? '))
    cylinder_num = float(cylinder_num)
    print(' ')              
    units_cylinder = input(f"What units (metres, centimetres, etc) are you're "          
                      f"measurements in? ")

    while units_cylinder.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cylinder = input(f'What units are your measurements in? ')
    print(' ')
    radius = (input('\033[0m' + f'What is the radius of the cylinder? '))
    while not is_number(radius) or float(radius) < 0:
            print('')

            if not is_number(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            radius = (input(f'What is the radius of the cylinder? '))
    radius = float(radius) 
    print(' ')

    height = (input('What is the height of the cylinder? '))
    while not is_number(height) or float(height) < 0:
            print('')

            if not is_number(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            height = (input('What is the height of the cylinder? '))
    height = float(height) 
    print(' ')

    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Cylinder (Surface Area) selected: ')
    print(' ')
    
    cylinder_area = (2 * math.pi * radius*height) + (2 * math.pi *(radius **2))
    cylinder_area_rounded = round(cylinder_area, 3)
    return cylinder_area_rounded, cylinder_num, units_cylinder
def calc_triangle_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Triangle area selected: ')
    print('')  
    print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')

    print(' ')
    triangle_num = input('\033[0m' + f'What number triangle are you '
                         f'calculating the area of? ')      
    
    while not is_number(triangle_num) or float(triangle_num) < 0:
            print('')

            if not is_number(triangle_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(triangle_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            triangle_num = (input(f'What number triangle are you '
                         f'calculating the area of? '))
    triangle_num = float(triangle_num) 
    print(' ')              
    units_triangle = input(f"What units (metres, centimetres, etc) are you're "
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")

    while units_triangle.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_triangle = input(f'What units are your measurements in? ')
    print(' ')
    height = (input('\033[0m' +'What is the height of the triangle? '))
    while not is_number(height) or float(height) < 0:
            print('')

            if not is_number(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            height = (input(f'What is the height of the triangle? '))
    height = float(height)
    print(' ')

    base = (input("What is the length of the triangle's base? "))
    while not is_number(base) or float(base) < 0:
            print('')

            if not is_number(base) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(base) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            base = (input("What is the length of the triangle's base? "))
    base = float(base)
    while base < 0:
            invalid_negetive()
            base = float(input(f"What is the length of the triagle's base? "))
            print(' ')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Triangle area selected: ')
    print(' ')
    
    triangle_area = (height * base)/2
    triangle_area_rounded = round(triangle_area, 3)
    return triangle_area_rounded, triangle_num, units_triangle

#VOLUMEEE
def calc_cuboid_volume():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cuboid volume selected: ')
      print('')  
      print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')
      cubiod_num = input(f'\033[0m' + f'What number cuboid are you '
                         f'calculating the volume of? ') 
      while not is_number(cubiod_num) or float(cubiod_num) < 0:
            print('')

            if not is_number(cubiod_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(cubiod_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            cubiod_num = (input(f'What number cuboid are you '
                         f'calculating the volume of? '))
      cubiod_num = float(cubiod_num)
      print(' ')              
      units_cuboid = input(f"What units (metres, centimetres, etc) are you're "          
                      f"measurements in? ")
      while units_cuboid.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cuboid = input(f'What units are your measurements in? ')
      print(' ')
      height = (input(f'\033[0m' + f'What is the height of the '
                              f'cuboid? ')) 

      while not is_number(height) or float(height) < 0:
            print('')

            if not is_number(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print('')
            height = (input(f'What is the height of the '
                              f'cuboid? '))
      height = float(height)

      print(' ')
      width = (input('What is the width of the cuboid? '))
      while not is_number(width) or float(width) < 0:
            print(' ')

            if not is_number(width) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(width) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            width = (input('What is the width of the cuboid? '))
      width = float(width)
      print(' ')
      depth = float(input('What is the depth of the cuboid? '))
      while not is_number(depth) or float(depth) < 0:
            print(' ')

            if not is_number(depth) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(depth) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            depth = (input('What is the depth of the cuboid? '))
      depth = float(depth)
      print(' ')

      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cuboid volume selected: ')
      print(' ')

      cuboid_volume = height * width * depth
      cuboid_volume_rounded = round(cuboid_volume, 3)
      return cuboid_volume_rounded, cubiod_num, units_cuboid
def calc_cube_volume():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cube volume selected: ')
      print('')  
      print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')

      print(' ')
      cube_num = input(f'\033[0m' + f'What number cube are you '
                       f'calculating the volume of? ')      
      while not is_number(cube_num) or float(cube_num) < 0:
            print(' ')

            if not is_number(cube_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(cube_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            cube_num = (input(f'What number cube are you '
                       f'calculating the volume of? '))
      cube_num = float(cube_num)
      print(' ')              
      units_cube = input(f"What units (metres, centimetres, etc) are you're "          
                      f"measurements in? ")

      while units_cube.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cube = input(f'What units are your measurements in? ')
      print(' ')
      measurement = (input(f'\033[0m' + f'What is the side length'
                              f' of the cube? '))
      while not is_number(measurement) or float(measurement) < 0:
            print(' ')

            if not is_number(measurement) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(measurement) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            measurement = (input(f'What is the side length'
                              f' of the cube? '))
      measurement = float(measurement)
      print(' ')
      '''
      while measurement < 0:
            invalid_negetive()
            measurement = float(input(f'What is the side length'
                              f' of the cube? '))
            print(' ')'''

      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cube volume selected: ')
      print(' ')

      cube_volume = measurement * 3
      cube_volume_rounded = round(cube_volume, 3)
      return cube_volume_rounded, cube_num, units_cube
def calc_cylinder_volume():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cylinder volume selected: ')
      print('')  
      print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')

      print(' ')
      cylinder_num = input(f'\033[0m' + f'What number cylinder are '
                           f'you calculating the volume of? ') 
      while not is_number(cylinder_num) or float(cylinder_num) < 0:
            print(' ')

            if not is_number(cylinder_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(cylinder_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            cylinder_num = (input(f'What number cylinder are '
                           f'you calculating the volume of? '))
      cylinder_num = float(cylinder_num)
      print(' ')              
      units_cylinder = input(f"What units (metres, centimetres, etc) are "
                             f"you're "          
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
      while units_cylinder.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cylinder = input(f'What units are your measurements in? ')
      print(' ')
      height = (input(f'\033[0m' + f'What is the height of the '
                              f'cylinder? '))
      while not is_number(height) or float(height) < 0:
            print(' ')

            if not is_number(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            height = (input(f'What is the height of the '
                              f'cylinder? '))
      height = float(height)
      print(' ')
      radius = (input('What is the radius of the cylinder? '))
      while not is_number(radius) or float(radius) < 0:
            print(' ')

            if not is_number(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            radius = (input('What is the radius of the cylinder? '))
      radius = float(radius)
      print(' ')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cylinder volume selected: ')
      print(' ')

      cylinder_volume = math.pi * (radius ** 2) * height
      cylinder_volume_rounded = round(cylinder_volume, 3)  
      return cylinder_volume_rounded, cylinder_num, units_cylinder
def calc_cone_volume():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')       
      print('\033[1m' + 'Cone volume selected: ')
      print('')  
      print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')
      
      print(' ')
      cone_num = input(f'\033[0m' + f'What number cone are you '
                       f'calculating the volume of? ')      
      while not is_number(cone_num) or float(cone_num) < 0:
            print(' ')

            if not is_number(cone_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(cone_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            cone_num = (input(f'What number cone are you '
                       f'calculating the volume of? '))
      cone_num = float(cone_num)
      print(' ')              
      units_cone = input(f"What units (metres, centimetres, etc) are you're "          
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
      while units_cone.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cone = input(f'What units are your measurements in? ')
      print(' ')
      height = (input(f'\033[0m' + f'What is the height of the '
                              f'cone? '))
      
      while not is_number(height) or float(height) < 0:
            print(' ')

            if not is_number(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(height) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            height = (input(f'What is the height of the '
                              f'cone? '))
      height = float(height)
      print(' ')
      radius = (input('What is the radius of the cone? '))
      while not is_number(radius) or float(radius) < 0:
            print(' ')

            if not is_number(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            radius = (input('What is the radius of the cone? '))
      radius = float(radius)
      print(' ')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cone volume selected: ')
      print(' ')

      cone_volume = math.pi * (radius ** 2) * (height/3)
      cone_volume_rounded = round(cone_volume, 3)
      return cone_volume_rounded, cone_num, units_cone
def calc_sphere_volume():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Sphere volume selected: ')
      print('')  
      print(f'Please remember:'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')
      print(' ')
      sphere_num = input(f'\033[0m' + f'What number sphere are you '
                         f'calculating the volume of? ')  
      while not is_number(sphere_num) or float(sphere_num) < 0:
            print(' ')

            if not is_number(sphere_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(sphere_num) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            sphere_num = (input(f'What number sphere are you '
                         f'calculating the volume of? '))
      sphere_num = float(sphere_num)
      print(' ')              
      units_sphere = input(f"What units (metres, centimetres, etc) are you're "          
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
      while units_sphere.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_sphere = input(f'What units are your measurements in? ')
      print(' ')
      radius = (input('\033[0m' + 'What is the radius of the sphere? '))
      while not is_number(radius) or float(radius) < 0:
            print(' ')

            if not is_number(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            elif float(radius) < 0:
                  print(f'Invalid input, please input a '
                        f'positive integer value.. ')

            print(' ')
            radius = (input('What is the radius of the sphere? '))
      radius = float(radius)
      print(' ')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Sphere volume selected: ')
      print(' ')

      sphere_volume = (4/3) * math.pi * (radius ** 3)
      sphere_volume_rounded = round(sphere_volume, 3)
      return sphere_volume_rounded, sphere_num, units_sphere

#WHAT SHAPE INVAILD
def what_shape_invalid():
      print(' ')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲')
      print(' ')
      print(f'Invalid input, try a number between 1 and 6 from the list '
      f'(above)')
      print(' ')
      what_shape = input(f"What shape's operation would you like to calculate "
                        f"from the list? ")
      while not what_shape.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a '
                        f'positive integer value between.. ')
            print(' ')
            what_shape = input(f"What shape's operation would "
                               f"you like to calculate "
                              f"from the list? ")
      what_shape = int(what_shape)
      return what_shape


#exit/goodbye ("6. Exit")
def goodbye_exit_screen():
    os.system('cls')
    print(f'\n★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ '
          f'　° :. ★　 * • ○ ° ★ .'
          f'　.　. ° 　. ● . ★ ° . *　　　°　.　°☆')
    print(' ')
    print('You will be missed..')
    print(' ')
    print('    ／＞　  　フ')   #Cat and stars from "fonts" mobile app
    print('    | 　_　 _ |')
    print('   ／` ミ＿xノ')
    print('  /　　　 　 |')
    print(' /　 ヽ　　 ﾉ')
    print('│　　| | |')
    print(' ')
    print(' ')
    print('All of the calculation results you recieved are below!!')
    print('---------------------------------------')
    for operation in finalreport:
      print(operation, 'is', finalreport[operation])            
      print(' ')
    print(f'\nThank you for using ConCalc!! Goodluck on your project/s and '
          f'return soon!')
    print(' ')
    
      
    print(f'★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ 　° :. '
          f'★　 * • ○ ° ★ .　 '
          f'* 　.　. ° 　. ● . ★ ° . *　　　°　.　°☆')

def another_calc_Ld_is_letter():
     another_calc_Ld = (input(f"Would you like to complete "
                                  f"another calculation? (input '1' or '2') "))
     while not another_calc_Ld.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a '
                        f'positive integer value.. ')
            print(' ')
            another_calc_Ld = another_calc_Ld_is_letter()

     return another_calc_Ld

#making (now empty) dictionary 
finalreport = {}

desired_calculation = main_program_1st_display()


#invalid ans(desired_calculation)       
while (desired_calculation < 1) or (desired_calculation >= 6): 
      desired_calculation = desired_calculation_invalid()  
      
while desired_calculation != 5:     #as long as it isn't '6' it does this
    print(' ')
    os.system('cls')

    if desired_calculation == 1:  #linear decking
      os.system('cls')
      quantity_linear_m_rounded, deck_num = linear_metres_decking_required()

      #adding 1st one to dictionary
      finalreport[f"The linear "
                  f"metres of "
                  f"decking required "
                  f"for deck {deck_num}"] = f"{quantity_linear_m_rounded}"

      print(f'------------------------------------------------------------'
            f'----------')
      print(' ')
      print('Next options:')
      print(' ')
      print(f'1. Calculate another amount of linear metres of decking '
            f'required (just like you did)')
      print('2. Back to main menu')
      print(' ')
      another_calc_Ld = (input(f"Would you like to complete another "
                                  f"calculation? (input '1' or '2') "))

      while not another_calc_Ld.isdigit() or (int(another_calc_Ld) < 1 or 
                                              int(another_calc_Ld) > 2):   
            print(' ')
            print("Invalid input, please input either '1' or '2'..")
            print(' ')
            another_calc_Ld = (input(f"Would you like to complete "
                                    f"another calculation? "
                                    f"(input '1' or '2'): "))
      another_calc_Ld = int(another_calc_Ld)
  
           
           
      while another_calc_Ld == 1:
            os.system('cls')
            (quantity_linear_m_rounded, 
             deck_num) = linear_metres_decking_required()
            finalreport[f"The linear metres of decking required for "
                        f"deck {deck_num}"] = f"{quantity_linear_m_rounded}"
            
            another_calc_Ld = another_calc_linear_decking()
      if another_calc_Ld == 2:
            os.system('cls')
            desired_calculation = main_program_1st_display() 
                          

    elif desired_calculation == 2:  #stud length

      os.system('cls')
      (calculated_stud_length, what_number_stud, 
       spacing_along_top_plate, FIRST_SHORTEST_stud_length, 
       overall_wall_height, units) = stud_length()
      #adding to 'final report dictionary'
      finalreport[f"The very first stud length at the lowest point of the "
                  f"wall"] = f"{FIRST_SHORTEST_stud_length} {units} long"
      
      finalreport[f"Stud length ({what_number_stud})"] = (f""
                                    f"{calculated_stud_length} {units} long")
      
      finalreport[f"Stud {what_number_stud} (above)"] = (f""
                                          f"{spacing_along_top_plate} {units} "
                                          f"along the top plate and at this "
                                          f"point/stud the total wall "
                                          f"height is {overall_wall_height} "
                                          f"{units} tall")
      
      another_calc =  another_calc_stud()
           
      while another_calc == 1:
            os.system('cls')
            (calculated_stud_length, what_number_stud, units, 
             spacing_along_top_plate, FIRST_SHORTEST_stud_length, 
             overall_wall_height) = stud_length()

            finalreport[f"Stud length ({what_number_stud})"] = (f""
                                    f"{calculated_stud_length} {units} long")

            finalreport[f"Stud {what_number_stud} (above)"] = (f""
                                          f"{spacing_along_top_plate} {units} "
                                          f"along the top plate and at this "
                                          f"point/stud the total wall "
                                          f"height is {overall_wall_height} "
                                          f"{units} tall")
            another_calc = another_calc_stud()
      if another_calc == 2:
            os.system('cls')
            desired_calculation = main_program_1st_display() 

    elif desired_calculation == 3:        #Area!        
        os.system('cls')
        #display/list of operations
        print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲')
        print(' ')

        print('\033[1m' + 'Shape areas avaliable: ')
        print(' ')

        print('\033[0m' + '1. Rectangle')
        print('2. Square')
        print('3. Circle')
        print('4. Cylinder (Surface Area)')
        print('5. Triangle')
        print('6. Back to main menu')
        print(' ')

        what_shape = input(f"What shape's area would you like to calculate "
                           f"from the list? ")
        
        while not what_shape.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            what_shape = (input(f"What shape's area would you like to "
                                f"calculate from"
                           f" the list (between or equal to 1 & 6)? "))
      
        what_shape = int(what_shape)

        #invalid ans                                                            
        while (what_shape < 1) or (what_shape >= 7):
            what_shape = what_shape_invalid()


        #needed math imports:
        math.pi == math.pi

        #while loop for 'area' option (SUB OPTIONS OF MAIN WHILE)
        while what_shape <= 6 and what_shape >= 1:
            #rectangle                                    
            if what_shape == 1:
                os.system('cls')
                (rectangle_area_rounded, rectangle_num, 
                 units_rec) = calc_rectangle_area()
                finalreport[f"Rectangle area "
                            f"({rectangle_num})"] = f"{rectangle_area_rounded}"
                f"{units_rec} squared"
                print(f'\033[0m' + "Your rectangle's area is: " + '\033[1m' +
                      f'{rectangle_area_rounded} {units_rec} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
                print('\033[0m')
                os.system('cls')
            #square                           
            elif what_shape == 2:
                os.system('cls')
                (square_area_rounded, square_num, 
                 units_square) = calc_square_area()
                finalreport[f"Square area "
                            f"({square_num})"] = f"{square_area_rounded} "
                f"{units_square} squared"
                print(f'\033[0m' + "Your cube's volume is: " + '\033[1m' +
                      f'{square_area_rounded} {units_square} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #circle    
            elif what_shape == 3:
                os.system('cls')
                (circle_area_rounded, circle_num, 
                 units_circle) = calc_circle_area()
                finalreport[f"Circle area "
                            f"({circle_num})"] = f"{circle_area_rounded} "
                f"{units_circle} squared"
                print(f'\033[0m' + "Your circle's area is: " + '\033[1m' +
                      f'{circle_area_rounded} {units_circle} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #cylinder    
            elif what_shape == 4:
                os.system('cls')
                (cylinder_area_rounded, cylinder_num,
                  units_cylinder) = calc_cylinder_area()
                finalreport[f"Cylinder area "
                            f"({cylinder_num})"] = f"{cylinder_area_rounded} "
                f"{units_cylinder} squared"
                print(f'\033[0m'+"Your cylinder's surface area is: "+'\033[1m'+ 
                      f'{cylinder_area_rounded} {units_cylinder} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #triagle    
            elif what_shape == 5:
                os.system('cls')
                (triangle_area_rounded, triangle_num, 
                 units_triangle) = calc_triangle_area()
                finalreport[f"Triangle area "
                            f"({triangle_num})"] = f"{triangle_area_rounded} "
                f"{units_triangle} squared"
                print(f'\033[0m' + "Your triangle's area is: " + '\033[1m' + 
                      f'{triangle_area_rounded} {units_triangle} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")           
            #exit
            elif what_shape == 6:
                  os.system('cls')
                  desired_calculation = main_program_1st_display() #(1)
                  break
            break


    elif desired_calculation == 4:        #Volume!         
        os.system('cls')
        #display/list of operations
        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
        print(' ')
        #Lists avaliable volumes
        print('\033[1m' + 'Shape volumes avaliable: ')
        print(' ')

        print('\033[0m' + '1. Cuboid')
        print('2. Cube')
        print('3. Cylinder')
        print('4. Cone')
        print('5. Sphere')
        print('6. Back to main menu')
        print(' ')

        what_shape = input(f"What shape's volume would you like to calculate "
                           f"from the list? ")
        what_shape = int(what_shape)

        #invalid ans        WORKS
        while (what_shape < 1) or (what_shape >= 7):
            what_shape = what_shape_invalid()


        #needed math imports:
        math.pi == math.pi

        #while loop for 'volume' option (SUB OPTIONS OF MAIN WHILE)
        while what_shape <= 6 and what_shape >= 1:
            #CUBOID                                                             
            if what_shape == 1:
                os.system('cls')
                (cuboid_volume_rounded, cubiod_num, 
                 units_cuboid) = calc_cuboid_volume()
                finalreport[f"Cuboid volume "
                            f"({cubiod_num})"] = f"{cuboid_volume_rounded} "
                f"{units_cuboid} cubed"
                print(f'\033[0m' + "Your cuboid's volume is: "+'\033[1m'+
                      f'{cuboid_volume_rounded} {units_cuboid} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
                print('\033[0m')
                os.system('cls')
            #CUBE                           
            elif what_shape == 2:
                os.system('cls')
                (cube_volume_rounded, cube_num, 
                 units_cube) = calc_cube_volume()
                finalreport[f"Cube volume "
                            f"({cube_num})"] = f"{cube_volume_rounded} "
                f"{units_cube} cubed"
                print(f'\033[0m' + "Your cube's volume is: "+'\033[1m'+
                      f'{cube_volume_rounded} {units_cube} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #CYLINDER    
            elif what_shape == 3:                                                   
                os.system('cls')
                (cylinder_volume_rounded, cylinder_num, 
                 units_cylinder) = calc_cylinder_volume()
                finalreport[f"Cylinder volume "
                            f"({cylinder_num})"] = f"{cylinder_volume_rounded}"
                f"{units_cylinder} cubed"
                print(f'\033[0m' + "Your cylinder's volume is: " + '\033[1m' +
                      f'{cylinder_volume_rounded} {units_cylinder} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #CONE    
            elif what_shape == 4:              
                os.system('cls')
                (cone_volume_rounded, cone_num, 
                 units_cone) = calc_cone_volume()
                finalreport[f"Cone volume "
                            f"({cone_num})"] = f"{cone_volume_rounded} "
                f"{units_cone} cubed"
                print(f'\033[0m'+"Your cone's volume is: "+'\033[1m'+ 
                      f'{cone_volume_rounded} {units_cone} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #SPHERE    
            elif what_shape == 5: 
                os.system('cls')
                (sphere_volume_rounded, sphere_num, 
                 units_sphere) = calc_sphere_volume()
                finalreport[f"Sphere volume "
                            f"({sphere_num})"] = f"{sphere_volume_rounded} "
                f"{units_sphere} cubed"
                print(f'\033[0m' + "Your sphere's volume is: " + '\033[1m' + 
                      f'{sphere_volume_rounded} {units_sphere} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")           
            #exit
            elif what_shape == 6:
                  desired_calculation = main_program_1st_display()
                  break
            break


while desired_calculation == 5: #EXIT 
    goodbye_exit_screen()
    
    break
