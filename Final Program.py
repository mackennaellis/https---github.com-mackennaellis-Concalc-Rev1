# The program's first version was completed on the 6/09/24.

# Imports required throughout the program
import math
import os

#Checks if input is a number
def is_number(input_str):
     '''Checks if user input is a digit in a way that accepts decimal and 
     negative values as well
     '''
     try:
          float(input_str)
          return True
     except ValueError:
          return False

# Invalid negative input
def invalid_negetive():
      '''Invalid negative - Checks if a digit is negative
      
      This function is what is printed when a users input is negative and
      therefore is invalid
      '''
      print(' ')
      print(f'Invalid input, please input a more ' + '\033[1m' + f'positive' +
            '\033[0m' + f' number')
      print(' ')

# Main Program (The opening welcome screen)
def main_program_1st_display():
      '''Prints the users welcome screen, and then asks the user which 
      calculation from the list they'd like the calculate.
      Once the user has inputted their value it tests if the value is invalid.
      Invalid in this function means that the input is not a number'''

      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲')
      print(' ')

      print('Welcome to the program!!')
      print(' ')

      print(f'How to use the program: You’ll notice that all items in the '
            f'lists shown are numbered, when asked for what you’d like to '
            f'complete please enter the corresponding number to the '
            f'operation you’d like.')
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
      
      # Checking desired_calculation is a number
      while not desired_calculation.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            desired_calculation = (input(f'What calculation would you like to '
                                          f'complete from the list/s? '))
      desired_calculation = int(desired_calculation)

      return desired_calculation

# Desired_calculation invalid
def desired_calculation_invalid():
      '''The printed text that appears when the user's input for 
      desired_calculation is invalid (less then 1 or greater then 
      6 or a decimal). It then asks for another input that fits the conditions.
      '''
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

# Decking option (1)
def linear_metres_decking_required():
      '''This function contains the calculations required to find the 
      linear-metres of decking required. The code specificies how units work
      throughout this operation, asks for several different inputs, and for 
      each input tests if it is a digit of not - with decimals accepted but 
      not negatives. It also explains some terminology where it may be needed.

      Then the code calculates the amount of linear-metres of decking required 
      for the user's deck.'''
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
      # Input validation for deck_num
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
      # Input validation for width
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
      # Input validation for gap
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
      # Input validation for deck_width
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
      # Input validation for deck_length
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
      # Explains what a waste percentage is
      print(f'**A waste percentage is how much waste (extra) '
            f'are you allowing for. Between 5 - 15% is '
            f'recommended with 10% usually being a great allowance. '
            f'At least greater then zero**')
      print(' ')
      waste_percentage_num = (input(f"What is the waste percentage "
                                    f"number you would like to allow "
                                    f"(units: whole number (/percentage "
                                    f"without '%' sign))? "))
      # Input validation for waste_percentage_num
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

      # Calculations start here
      decking_area = deck_width * deck_length
      decking_area_rounded = round(decking_area, 3)

      waste_percentage = (waste_percentage_num / 100) + 1

      # Amount in m^2 one linear metre (board) takes up
      decking_area_in_m2 = (gap + width) / 1000

      # How much liner-metres of decking is actually required
      quantity_linear_m = (((decking_area) / decking_area_in_m2) 
                           * waste_percentage)
      quantity_linear_m_rounded = round(quantity_linear_m, 3)

      # Prints the amount of liner-metres of decking required for the user 
      # to see
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

# If the user wants to calculate another amount of liner-metres of decking
def another_calc_linear_decking():   
      '''This function asks the user if they'd like to complete another
      calculation of the amount of liner-metres of decking required, it provides
      them with a list of options to choose from as explained on the 
      welcome/home screen. 
      The code checks if the user's input is valid by 
      seeing if it is a '1' or '2', if it is the test is finished and the 
      value is valid. If not the code checks why it is invalid by seeing if it's
      a digit (decimals and negatives are also invalid) and if the input is 
      invalid asks the user for another.
      '''         
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
      
      # Checks another_calc_Ld isn't decimal, or letter or anything other then
      # a 1 or 2.
      while True:
            if ((another_calc_Ld) == '1' or (another_calc_Ld) == '2'):
               another_calc_Ld = int(another_calc_Ld)
               break # A valid input breaks the loop here
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

# If the user wants to calculate another stud length
def another_calc_stud():
      '''This function asks the user if they'd like to complete another
      stud length calculation, it provides them with a list of options 
      to choose from as explained on the welcome/home screen. 
      The code checks if the user's input is valid by 
      seeing if it is a '1' or '2' via the boundries of < 1 and > 2,
      if the input is invalid it asks the user for another.
      '''  
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

# Stud option (2)
def stud_length():
      '''This function includes all the calculations for the 'Stud Length'
      operation. It asks the user for certain values and specifies a
      difference in units when needed. 
      If the value is invalid the code says so; it can tell by testing if it's
      a digit or not with decimals allowed.
      It then calculates the answers and prints them for the user to see.
      '''
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
      # Input validation for units
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
      # Input validation for height_outside_edge_lowest_wall
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
      # Input validation for top_plate_thickness
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
      # Input validation for wall_angle
      while not wall_angle.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a whole '
                        f'positive integer value.. ')
            print(' ')
            wall_angle = (input(f'What is the angle of the wall '
                               f'(in degrees (unit))? '))
      wall_angle = float(wall_angle)
      print(' ')

      # Calculating plub cut
      plumb_cut = (top_plate_thickness / math.sin((90 - wall_angle) 
                                                  * (math.pi / 180)))
      plumb_cut = round(plumb_cut, 3)


      bottom_plate_thickness = (input(f'What is the bottom '
                                           f'plate thickness? '))
      # Input validation for bottom_plate_thickness
      while not bottom_plate_thickness.isdigit():                                           
            print(' ')
            print(f'Invalid input, please input a whole '
                        f'positive integer value.. ')
            print(' ')
            bottom_plate_thickness = (input(f'What is the bottom '
                                           f'plate thickness? '))
      bottom_plate_thickness = float(bottom_plate_thickness)
      print(' ')

      # Calculating the very first stud's length
      FIRST_SHORTEST_stud_length = (height_outside_edge_lowest_wall 
                                    - (plumb_cut + bottom_plate_thickness))
      FIRST_SHORTEST_stud_length = round(FIRST_SHORTEST_stud_length, 3)

      os.system('cls')
      # Printing answers (set '1')
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
      # So that screen doesn't clear too early
      continue_stud=input(f"Press " + '\033[1m' + f"ENTER" + '\033[0m' 
                      + f" to continue")
      os.system('cls')
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      # Next 'set' of questions
      stud_space_running = (input(f"What is the running stud "
                                             f"spacing (the "
                                    f"distance from the very first "
                                    f"stud at the lowest side of the wall "
                                    f"to the stud you're currently "
                                    f"calculating the length of)? "))
      # Input validation for stud_space_running
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
      # Input validation for what_number_stud
      while not what_number_stud.isdigit() or float(what_number_stud) <= 1:
            print(' ')
            print(f"Invalid input, please input a whole "
                  f"positive integer value greater then (1).. ")
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
      
      # All other calculations start here (as of variables)      
      rise_of_stud = (math.tan(wall_angle * math.pi / 180) 
                      * stud_space_running)
      rise_of_stud = round(rise_of_stud, 3)

      spacing_along_top_plate = math.sqrt((stud_space_running ** 2) 
                                          + (rise_of_stud ** 2))
      
      spacing_along_top_plate = round(spacing_along_top_plate, 3)

      calculated_stud_length = FIRST_SHORTEST_stud_length + rise_of_stud
      calculated_stud_length = round(calculated_stud_length, 3)

      overall_wall_height = (calculated_stud_length + top_plate_thickness 
                             + plumb_cut)
      overall_wall_height =  round(overall_wall_height, 3)

      os.system('cls')
      # Prints all answers calculated
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

# Area option calculations (3)
# Rectangle
def calc_rectangle_area():
      '''This function calculates the area of a rectangle. It asks the user 
      for the required measurements and what units they want to use, it makes 
      sure to validate each input and then asks the user for another if it's 
      invalid. Then the rectangle's area is calculated from those variables.
      '''
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲')
      print('')
      print('\033[1m' + 'Rectangle area selected: ')
      print(' ')
      print(f'Please remember: Unless stated otherwise the units will remain '
            f'the same across all inputs (you do not have to include the '
            f'units in your input, simply input the integer value) otherwise '
            f'the result/s will be incorrect.')     
      print(' ')

      rectangle_num = input('\033[0m' + f'What number rectangle are you '
                              f'calculating the area of? ')      
      # Input validation for rectangle_num   
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
      # Input validation for units_rec (this one wants a non-digit input)
      while units_rec.isdigit():
                  print(' ')
                  print(f'Invalid units, try units without only '
                        f'numerical values in them..')
                  print(' ')
                  units_rec = input(f'What units are your measurements in? ')
      print(' ')

      width = (input('\033[0m' + 'What is the width of the rectangle? '))
      # Input validation for width
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
      # Input validation for length
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

      # Prints start of answers screen
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

      # Calculation and rounding (Rectangle area)
      rectangle_area = width * length
      rectangle_area_rounded = round(rectangle_area, 3)

      return rectangle_area_rounded, rectangle_num, units_rec
# Square
def calc_square_area():
      '''This function calculates the area of a square. It asks the user for
      the required measurements and what units they want to use, it makes sure 
      to validate each input and then asks the user for another if it's 
      invalid. Then the square's area is calculated from those variables.
      '''
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲')
      print('') 
      print('\033[1m' + 'Square area selected: ')
      print('')  
      print(f'Please remember: Unless stated otherwise the units will remain '
            f'the same across all inputs (you do not have to include the '
            f'units in your input, simply input the integer value) otherwise '
            f'the result/s will be incorrect.')
      print(' ')

      square_num = input('\033[0m' + f'What number square are you '
                        f'calculating the area of? ')  
      # Input validation for square_num   
      while not is_number(square_num) or float(square_num) < 0:
                  print('')

                  if not is_number(square_num) < 0:
                        print(f'Invalid input, please input a '
                              f'positive integer value.. ')

                  elif float(square_num) < 0:
                        print(f'Invalid input, please input a '
                              f'positive integer value.. ')

                  print('')
                  square_num = (input(f'What number rectangle are you '
                              f'calculating the area of? '))
      square_num = float(square_num)    
      print(' ') 

      units_square = input(f"What units (metres, centimetres, etc) are you're "       
                        f"measurements in (please keep them the same for "
                        f"each input unless asked for differently)? ")
      # Input validation for units_square (this one wants a non-digit input)
      while units_square.isdigit():
                  print(' ')
                  print(f'Invalid units, try units without only '
                        f'numerical values in them..')
                  print(' ')
                  units_square = input(f'What units are your measurements '
                                       f'in? ')
      print(' ')

      measurement = (input('\033[0m' + f'What is the side length of the '
                                    f'square? '))
      # Input validation for measurement
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

      # Prints start of answers screen
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

      # Calculation and rounding (Square area)
      square_area = measurement * 2
      square_area_rounded = round(square_area, 3)

      return square_area_rounded, square_num, units_square
# Circle
def calc_circle_area():
      '''This function calculates the area of a circle. It asks the user for
      the required measurements and what units they want to use, it makes sure 
      to validate each input and then asks the user for another if it's 
      invalid. Then the circle's area is calculated from those variables.
      '''
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲')
      print(' ')
      
      print('\033[1m' + 'Circle area selected: ')
      print('')  
      print(f'Please remember: Unless stated otherwise the units will remain '
            f'the same across all inputs (you do not have to include the '
            f'units in your input, simply input the integer value) otherwise '
            f'the result/s will be incorrect.') 
      print(' ')
      
      circle_num = input('\033[0m' + f'What number circle are you calculating '
                        f'the area of? ') 
      # Input validation for circle_num
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
      # Input validation for units_circle (this one wants a non-digit input)
      while units_circle.isdigit():
                  print(' ')
                  print(f'Invalid units, try units without only '
                        f'numerical values in them..')
                  print(' ')
                  units_circle = input(f'What units are your measurements in? ')
      print(' ')

      radius = (input(f'\033[0m' + f'What is the radius of the circle? '))
      # Input validation for radius
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

      # Prints start of answers screen
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲')
      os.system('cls')
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Circle area selected: ')
      print(' ')
      
      # Calculation and rounding (Circle area)
      circle_area = math.pi * (radius ** 2)
      circle_area_rounded = round(circle_area, 3)

      return circle_area_rounded, circle_num, units_circle
# Cylinder
def calc_cylinder_area():
      '''This function calculates the area of a cylinder. It asks the user for
      the required measurements and what units they want to use, it makes sure 
      to validate each input and then asks the user for another if it's 
      invalid. Then the cylinder's area is calculated from those variables.
      '''
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲')
      print(' ')       
      print('\033[1m' + 'Cylinder (Surface Area) selected: ')
      print('')  
      print(f'Please remember: Unless stated otherwise the units will remain '
            f'the same across all inputs (you do not have to include the '
            f'units in your input, simply input the integer value) '
            f'otherwise the result/s will be incorrect.')
      print(' ')

      cylinder_num = input('\033[0m' + f'What number cylinder are '
                              f'you calculating the area of? ')    
      # Input validation for cylinder_num
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

      units_cylinder = input(f"What units (metres, centimetres, etc) are "
                             f"you're measurements in? ")
      # Input validation for units_cylinder (this one wants a non-digit input)
      while units_cylinder.isdigit():
                  print(' ')
                  print(f'Invalid units, try units without only '
                        f'numerical values in them..')
                  print(' ')
                  units_cylinder = input(f'What units are your measurements '
                                         f'in? ')
      print(' ')

      radius = (input('\033[0m' + f'What is the radius of the cylinder? '))
      # Input validation for radius
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
      # Input validation for height
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

      # Prints start of answers screen
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲')
      os.system('cls')
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cylinder (Surface Area) selected: ')
      print(' ')
      
      # Calculation and rounding (Cylinder area)
      cylinder_area = (2 * math.pi * radius * height) + (2 * math.pi 
                                                            * (radius ** 2))
      cylinder_area_rounded = round(cylinder_area, 3)

      return cylinder_area_rounded, cylinder_num, units_cylinder
# Triangle
def calc_triangle_area():
      '''This function calculates the area of a triangle. It asks the user for
      the required measurements and what units they want to use, it makes sure 
      to validate each input and then asks the user for another if it's 
      invalid. Then the triangle's area is calculated from those variables.
      '''
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Triangle area selected: ')
      print('')  
      print(f'Please remember: Unless stated otherwise the units will '
            f'remain the same across all inputs (you do not have to include '
            f'the units in your input, simply input the integer value) '
            f'otherwise the result/s will be incorrect.')
      print(' ')

      triangle_num = input('\033[0m' + f'What number triangle are you '
                              f'calculating the area of? ')      
      # Input validation for triangle_num
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

      units_triangle = input(f"What units (metres, centimetres, etc) are "
                             f"you're measurements in (please keep them the "
                             f"same for each input unless asked for "
                             f"differently)? ")
      # Input validation for units_triangle (this one wants a non-digit input)
      while units_triangle.isdigit():
                  print(' ')
                  print(f'Invalid units, try units without only '
                        f'numerical values in them..')
                  print(' ')
                  units_triangle = input(f'What units are your measurements in? ')
      print(' ')

      height = (input('\033[0m' +'What is the height of the triangle? '))
      # Input validation for height
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
      # Input validation for base
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
      # Input validation for base (specifically for if it's a negative value)
      while base < 0:
                  invalid_negetive()
                  base = float(input(f"What is the length of the triagle's "
                                     f"base? "))
                  print(' ')
      
      # Prints start of answers screen
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲')
      os.system('cls')
      print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Triangle area selected: ')
      print(' ')
      
      # Calculation and rounding (Triangle area)
      triangle_area = (height * base) / 2
      triangle_area_rounded = round(triangle_area, 3)

      return triangle_area_rounded, triangle_num, units_triangle

# Volume option calculations (4)
# Cuboid
def calc_cuboid_volume():
      '''This function calculates the volume of a cuboid. It asks the user for
      the required measurements and what units they want to use, it makes sure 
      to validate each input and then asks the user for another if it's 
      invalid. Then the cuboids's volume is calculated from those variables.
      '''
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
      print(' ')

      cubiod_num = input(f'\033[0m' + f'What number cuboid are you '
                         f'calculating the volume of? ') 
      # Input validation for cuboid_num 
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
      # Input validation for units_cuboid (this one wants a non-digit input)
      while units_cuboid.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cuboid = input(f'What units are your measurements in? ')
      print(' ')

      height = (input(f'\033[0m' + f'What is the height of the '
                              f'cuboid? ')) 
      # Input validation for height 
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
      # Input validation for width 
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
      # Input validation for depth 
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

      # Prints start of answers screen
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cuboid volume selected: ')
      print(' ')

      # Calculation and rounding (Cubiod volume)
      cuboid_volume = height * width * depth
      cuboid_volume_rounded = round(cuboid_volume, 3)

      return cuboid_volume_rounded, cubiod_num, units_cuboid
# Cube
def calc_cube_volume():
      '''This function calculates the volume of a cube. It asks the user for
      the required measurements and what units they want to use, it makes sure 
      to validate each input and then asks the user for another if it's 
      invalid. Then the cube's volume is calculated from those variables.
      '''
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
      # Input validation for cube_num    
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
      # Input validation for units_cube (this one wants a non-digit input)
      while units_cube.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cube = input(f'What units are your measurements in? ')
      print(' ')

      measurement = (input(f'\033[0m' + f'What is the side length'
                              f' of the cube? '))
      # Input validation for measurement 
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
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')

      # Prints start of answers screen
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cube volume selected: ')
      print(' ')

      # Calculation and rounding (Cube volume)
      cube_volume = measurement * 3
      cube_volume_rounded = round(cube_volume, 3)

      return cube_volume_rounded, cube_num, units_cube
# Cylinder
def calc_cylinder_volume():
      '''This function calculates the volume of a cylinder. It asks the user 
      for the required measurements and what units they want to use, it 
      makes sure to validate each input and then asks the user for another 
      if it's invalid. Then the cylinder's volume is calculated from those 
      variables.
      '''
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
      # Input validation for cylinder_num 
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
      # Input validation for units_cylinder (this one wants a non-digit input)
      while units_cylinder.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cylinder = input(f'What units are your measurements in? ')
      print(' ')

      height = (input(f'\033[0m' + f'What is the height of the '
                              f'cylinder? '))
      # Input validation for height 
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
      # Input validation for radius 
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

      # Prints start of answers screen
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cylinder volume selected: ')
      print(' ')

      # Calculation and rounding (Cylinder volume)
      cylinder_volume = math.pi * (radius ** 2) * height
      cylinder_volume_rounded = round(cylinder_volume, 3) 

      return cylinder_volume_rounded, cylinder_num, units_cylinder
# Cone
def calc_cone_volume():
      '''This function calculates the volume of a cone. It asks the user 
      for the required measurements and what units they want to use, it 
      makes sure to validate each input and then asks the user for another 
      if it's invalid. Then the cone's volume is calculated from those 
      variables.
      '''
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
      # Input validation for cone_num    
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
      # Input validation for units_cone (this one wants a non-digit input)
      while units_cone.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_cone = input(f'What units are your measurements in? ')
      print(' ')

      height = (input(f'\033[0m' + f'What is the height of the '
                              f'cone? '))
      # Input validation for height 
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
      # Input validation for radius 
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

      # Prints start of answers screen
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cone volume selected: ')
      print(' ')

      # Calculation and rounding (Cone volume)
      cone_volume = math.pi * (radius ** 2) * (height / 3)
      cone_volume_rounded = round(cone_volume, 3)

      return cone_volume_rounded, cone_num, units_cone
# Sphere
def calc_sphere_volume():
      '''This function calculates the volume of a sphere. It asks the user 
      for the required measurements and what units they want to use, it 
      makes sure to validate each input and then asks the user for another 
      if it's invalid. Then the sphere's volume is calculated from those 
      variables.
      '''
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
      # Input validation for sphere_num 
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
      # Input validation for units_sphere (this one wants a non-digit input)
      while units_sphere.isdigit():
            print(' ')
            print(f'Invalid units, try units without only '
                  f'numerical values in them..')
            print(' ')
            units_sphere = input(f'What units are your measurements in? ')
      print(' ')

      radius = (input('\033[0m' + 'What is the radius of the sphere? '))
      # Input validation for radius 
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

      # Prints start of answers screen
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
      f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Sphere volume selected: ')
      print(' ')

      # Calculation and rounding (Sphere volume)
      sphere_volume = (4 / 3) * math.pi * (radius ** 3)
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

# Final Goodbye/Exit screen option (5)
def goodbye_exit_screen():
      '''In this function the text is printed to farewell the user and their
      'final report' is displayed with includes all of their calculation 
      results from there session using the program. It does this by printing 
      the 'finalreport' dictionary.
      '''
      os.system('cls')

      # Credits: Cat and stars from "Fonts" mobile app
      print(f'\n★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ '
            f'　° :. ★　 * • ○ ° ★ .'
            f'　.　. ° 　. ● . ★ ° . *　　　°　.　°☆')
      print(' ')
      print('You will be missed..')
      print(' ')
      print('    ／＞　  　フ') 
      print('    | 　_　 _ |')
      print('   ／` ミ＿xノ')
      print('  /　　　 　 |')
      print(' /　 ヽ　　 ﾉ')
      print('│　　| | |')
      print(' ')
      print(' ')
      print('All of the calculation results you recieved are below!!')
      print('---------------------------------------')

      # Prints the final report
      for operation in finalreport:
            print(operation, 'is', finalreport[operation])            
            print(' ')

      print(f'\nThank you for using ConCalc!! Goodluck on your project/s and '
            f'return soon!')
      print(' ')


      print(f'★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ 　° :. '
            f'★　 * • ○ ° ★ .　 '
            f'* 　.　. ° 　. ● . ★ ° . *　　　°　.　°☆')

# Another_calc_linear_decking is 'invalid'
def another_calc_Ld_is_letter():
      '''This function checks if specifically the 
      'another_calc_linear_decking' function's input is a digit or not after 
      asking for another if the orginal one in the 
      'another_calc_linear_decking' function is invalid. In this function, 'Ld'
      stands for 'linear decking'
      '''
      another_calc_Ld = (input(f"Would you like to complete "
                               f"another calculation? (input '1' or '2') "))
      # Input validation for another_calc_Ld
      while not another_calc_Ld.isdigit():
            print(' ')
            print(f'Invalid input, please input a '
                        f'positive integer value.. ')
            print(' ')
            another_calc_Ld = another_calc_Ld_is_letter()

      return another_calc_Ld

# The 'finalreport' dictionary is created (empty) 
finalreport = {}

# Prints the welcome/main screen
desired_calculation = main_program_1st_display()

# Input validation for desired_calculation       
while (desired_calculation < 1) or (desired_calculation >= 6): 
      desired_calculation = desired_calculation_invalid()  

# If the user's input is valid and not '5' this while statement runs and takes
# the user to their inputted number's represented operation  
while desired_calculation != 5: 
      
      print(' ')
      os.system('cls')

      # If the user selects to calculate the linear-metres of decking required
      # (1)
      if desired_calculation == 1:  
            os.system('cls')
            (quantity_linear_m_rounded, 
             deck_num) = linear_metres_decking_required()

            # Adds the first amount required to 'finalreport'
            finalreport[f"The linear  of decking required for "
                        f"deck {deck_num}"] = f"{quantity_linear_m_rounded}"

            # Asks the user if they want to calculate another amount of
            # linear-metres of decking
            print(f'---------------------------------------------------------'
                  f'-------------')
            print(' ')
            print('Next options:')
            print(' ')
            print(f'1. Calculate another amount of linear metres of decking '
                  f'required (just like you did)')
            print('2. Back to main menu')
            print(' ')
            another_calc_Ld = (input(f"Would you like to complete another "
                                          f"calculation? (input '1' or '2') "))
            # Input validation another_calc_Ld
            while not another_calc_Ld.isdigit() or (int(another_calc_Ld) < 1 or 
                                                      (int(another_calc_Ld) 
                                                       > 2)):   
                  print(' ')
                  print("Invalid input, please input either '1' or '2'..")
                  print(' ')
                  another_calc_Ld = (input(f"Would you like to complete "
                                          f"another calculation? "
                                          f"(input '1' or '2'): "))
            another_calc_Ld = int(another_calc_Ld)

            # Yes they want to complete another:
            while another_calc_Ld == 1:
                  os.system('cls')
                  (quantity_linear_m_rounded, 
                        deck_num) = linear_metres_decking_required()
                  finalreport[f"The linear metres of decking required for "
                              f"deck "
                              f"{deck_num}"] = f"{quantity_linear_m_rounded}"
                  another_calc_Ld = another_calc_linear_decking()
            # No they don't want to complete another:
            if another_calc_Ld == 2:
                  os.system('cls')
                  desired_calculation = main_program_1st_display() 
                          
      # If the user selects to calculate a stud length (2)
      elif desired_calculation == 2: 
            os.system('cls')
            (calculated_stud_length, what_number_stud, 
            spacing_along_top_plate, FIRST_SHORTEST_stud_length, 
            overall_wall_height, units) = stud_length()

            # Adds the first stud length to 'finalreport'
            finalreport[f"The very first stud length at the lowest point of "
                        f"the "
                        f"wall"] = f"{FIRST_SHORTEST_stud_length} {units} long"
            
            # Adds the calculated stud length to 'finalreport'
            finalreport[f"Stud length "
                        f"({what_number_stud})"] = (f"{calculated_stud_length}"
                                                    f"{units} long")
            
            # Adds how far along the top_plate the stud is to 'finalreport'
            finalreport[f"Stud {what_number_stud} (above)"] = (f""
                                          f"{spacing_along_top_plate} {units} "
                                          f"along the top plate and at this "
                                          f"point/stud the total wall "
                                          f"height is {overall_wall_height} "
                                          f"{units} tall")
            
            # Asks if the user wants to calculate another stud length
            another_calc =  another_calc_stud()
            
            # Yes they want to calculate another:
            while another_calc == 1:
                  os.system('cls')
                  (calculated_stud_length, what_number_stud, units, 
                  spacing_along_top_plate, FIRST_SHORTEST_stud_length, 
                  overall_wall_height) = stud_length()

                  # Adds the calculated stud length to 'finalreport'
                  finalreport[f"Stud length ({what_number_stud})"] = (f""
                                    f"{calculated_stud_length} {units} long")
                  
                  # Adds how far along the top_plate the stud is to 
                  # 'finalreport'
                  finalreport[f"Stud {what_number_stud} (above)"] = (f""
                                          f"{spacing_along_top_plate} {units} "
                                          f"along the top plate and at this "
                                          f"point/stud the total wall "
                                          f"height is {overall_wall_height} "
                                          f"{units} tall")
                  another_calc = another_calc_stud()

            # No they don't want to calculate another"
            if another_calc == 2:
                  os.system('cls')
                  desired_calculation = main_program_1st_display() 

      # If the user selects to calculate a shapes area (3)
      elif desired_calculation == 3:  
            os.system('cls')

            # Displays the list of area calculations avaliable
            print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲')
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

            what_shape = input(f"What shape's area would you like to "
                               f"calculate from the list? ")
            # Input validation what_shape
            while not what_shape.isdigit():
                  print(' ')
                  print(f'Invalid input, please input a positive integer '
                        f'value.. ')
                  print(' ')
                  what_shape = (input(f"What shape's area would you like to "
                                    f"calculate from"
                              f" the list (between or equal to 1 & 6)? "))
            what_shape = int(what_shape)

            # Input valid                                                          
            while (what_shape < 1) or (what_shape >= 7):
                  what_shape = what_shape_invalid()

            # Required 'math' imports:
            math.pi == math.pi

            # While loop for which 'area' option the user wants to calculate
            # if valid input (<= 6 and >=1)
            while what_shape <= 6 and what_shape >= 1:
                  # Rectangle                                   
                  if what_shape == 1:
                        os.system('cls')
                        (rectangle_area_rounded, rectangle_num, 
                        units_rec) = calc_rectangle_area()

                        # Adds the rectangle area and what number rectangle
                        # to 'finalreport'
                        finalreport[f"Rectangle area "
                                    f"({rectangle_num}"
                                    f")"] = f"{rectangle_area_rounded} "
                        f"{units_rec} squared"

                        # Prints the rectangle's area answer for the user to 
                        # see
                        print(f'\033[0m' + "Your rectangle's area is: " 
                              + '\033[1m' +
                              f'{rectangle_area_rounded} {units_rec} squared')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to "
                                   f"main screen" + '\033[0m')
                        os.system('cls')

                  # Square                           
                  elif what_shape == 2:
                        os.system('cls')
                        (square_area_rounded, square_num, 
                        units_square) = calc_square_area()

                        # Adds the square's area and what number square
                        # to 'finalreport'
                        finalreport[f"Square area "
                                    f"({square_num}"
                                    f")"] = f"{square_area_rounded} "
                        f"{units_square} squared"

                        # Prints the square area answer for the user to see
                        print(f'\033[0m' + "Your cube's volume is: " 
                              + '\033[1m' +
                              f'{square_area_rounded} {units_square} squared')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                   f"screen")
                        os.system('cls')
                        
                  # Circle    
                  elif what_shape == 3:
                        os.system('cls')
                        (circle_area_rounded, circle_num, 
                        units_circle) = calc_circle_area()

                        # Adds the circle's area and what number circle
                        # to 'finalreport'
                        finalreport[f"Circle area "
                                    f"({circle_num}"
                                    f")"] = f"{circle_area_rounded} "
                        f"{units_circle} squared"

                        # Prints the circle area answer for the user to see
                        print(f'\033[0m' + "Your circle's area is: " 
                              + '\033[1m' +
                              f'{circle_area_rounded} {units_circle} squared')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                   f"screen")
                        os.system('cls')
                        
                  # Cylinder    
                  elif what_shape == 4:
                        os.system('cls')
                        (cylinder_area_rounded, cylinder_num,
                              units_cylinder) = calc_cylinder_area()
                        
                        # Adds the cylinder's area and what number cylinder
                        # to 'finalreport'
                        finalreport[f"Cylinder area "
                                    f"({cylinder_num}"
                                    f")"] = f"{cylinder_area_rounded} "
                        f"{units_cylinder} squared"

                        # Prints the cylinder area answer for the user to see
                        print(f'\033[0m' + "Your cylinder's surface area is: "
                              + '\033[1m' + f'{cylinder_area_rounded} '
                              f'{units_cylinder} squared')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                   f"screen")
                        os.system('cls')

                  # Triangle    
                  elif what_shape == 5:
                        os.system('cls')
                        (triangle_area_rounded, triangle_num, 
                        units_triangle) = calc_triangle_area()

                        # Adds the triangle's area and what number triangle
                        # to 'finalreport'
                        finalreport[f"Triangle area "
                                    f"({triangle_num}"
                                    f")"] = f"{triangle_area_rounded} "
                        f"{units_triangle} squared"

                        # Prints the triangle area answer for the user to see
                        print(f'\033[0m' + "Your triangle's area is: " 
                              + '\033[1m' + f'{triangle_area_rounded} '
                              f'{units_triangle} squared')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                   f"screen")
                        os.system('cls')           
                       
                  # If the user no longer wants to calculate a shapes area     
                  elif what_shape == 6:
                        os.system('cls')
                        desired_calculation = main_program_1st_display()
                        break
                  break

      # If the user selects to calculate a shapes volume (4)
      elif desired_calculation == 4:     
            os.system('cls')

            # Displays the list of area calculations avaliable
            print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                        f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                        f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
            print(' ')
            print('\033[1m' + 'Shape volumes avaliable: ')
            print(' ')
            print('\033[0m' + '1. Cuboid')
            print('2. Cube')
            print('3. Cylinder')
            print('4. Cone')
            print('5. Sphere')
            print('6. Back to main menu')
            print(' ')

            what_shape = input(f"What shape's volume would you like to "
                               f"calculate from the list? ")
            what_shape = int(what_shape)

            # Input validation what_shape
            while (what_shape < 1) or (what_shape >= 7):
                  what_shape = what_shape_invalid()

            # Required 'math' imports:
            math.pi == math.pi

            # While loop for which 'volume' option the user wants to calculate
            # if valid input (<= 6 and >=1)
            while what_shape <= 6 and what_shape >= 1:
                  # Cuboid                                                             
                  if what_shape == 1:
                        os.system('cls')
                        (cuboid_volume_rounded, cubiod_num, 
                        units_cuboid) = calc_cuboid_volume()

                        # Adds the cuboid's volume and what number cuboid
                        # to 'finalreport'
                        finalreport[f"Cuboid volume "
                                    f"({cubiod_num}"
                                    f")"] = f"{cuboid_volume_rounded} "
                        f"{units_cuboid} cubed"

                        # Prints the cuboid volume answer for the user to see
                        print(f'\033[0m' + "Your cuboid's volume is: " 
                              + '\033[1m' + f'{cuboid_volume_rounded} '
                              f'{units_cuboid} cubed')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                   f"screen")
                        print('\033[0m')
                        os.system('cls')
                  # Cube                          
                  elif what_shape == 2:
                        os.system('cls')
                        (cube_volume_rounded, cube_num, 
                        units_cube) = calc_cube_volume()

                        # Adds the cube's volume and what number cube
                        # to 'finalreport'
                        finalreport[f"Cube volume "
                                    f"({cube_num}"
                                    f")"] = f"{cube_volume_rounded} "
                        f"{units_cube} cubed"

                        # Prints the cube volume answer for the user to see
                        print(f'\033[0m' + "Your cube's volume is: " 
                              + '\033[1m' + f'{cube_volume_rounded} '
                              f'{units_cube} cubed')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                   f"screen")
                        os.system('cls')
                  # Cylinder    
                  elif what_shape == 3:                                                   
                        os.system('cls')
                        (cylinder_volume_rounded, cylinder_num, 
                        units_cylinder) = calc_cylinder_volume()

                        # Adds the cylinders's volume and what number cylinder
                        # to 'finalreport'
                        finalreport[f"Cylinder volume "
                                    f"({cylinder_num}"
                                    f")"] = f"{cylinder_volume_rounded}"
                        f"{units_cylinder} cubed"

                        # Prints the cylinder volume answer for the user to see
                        print(f'\033[0m' + "Your cylinder's volume is: " 
                              + '\033[1m' + f'{cylinder_volume_rounded} '
                              f'{units_cylinder} cubed')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                   f"screen")
                        os.system('cls')
                  # Cone    
                  elif what_shape == 4:              
                        os.system('cls')
                        (cone_volume_rounded, cone_num, 
                        units_cone) = calc_cone_volume()

                        # Adds the cone's volume and what number cone
                        # to 'finalreport'
                        finalreport[f"Cone volume "
                                    f"({cone_num}"
                                    f")"] = f"{cone_volume_rounded} "
                        f"{units_cone} cubed"

                        # Prints the cone volume answer for the user to see
                        print(f'\033[0m' + "Your cone's volume is: " 
                              + '\033[1m' + f'{cone_volume_rounded} '
                              f'{units_cone} cubed')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                     f"screen")
                        os.system('cls')
                  # Sphere    
                  elif what_shape == 5: 
                        os.system('cls')
                        (sphere_volume_rounded, sphere_num, 
                        units_sphere) = calc_sphere_volume()

                        # Adds the sphere's volume and what number sphere
                        # to 'finalreport'
                        finalreport[f"Sphere volume "
                                    f"({sphere_num}"
                                    f")"] = f"{sphere_volume_rounded} "
                        f"{units_sphere} cubed"

                        # Prints the cone volume answer for the user to see
                        print(f'\033[0m' + "Your sphere's volume is: " 
                              + '\033[1m' + f'{sphere_volume_rounded} '
                              f'{units_sphere} cubed')
                        print(' ')
                        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                              f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                        print(' ')
                        cont = input(f"Press ENTER to continue back to main "
                                     f"screen")
                        os.system('cls')        
                  # If the user no longer wants to calculate a shapes volume
                  elif what_shape == 6:
                        desired_calculation = main_program_1st_display()
                        break
                  break

# If the user no longer wants to calculate calculations and wants to exit
# the program (5)
while desired_calculation == 5: #EXIT 
    goodbye_exit_screen()
    
    break
