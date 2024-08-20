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
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
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
      print(f"Please also note that when the units say 'millimetres' "
            f"decimal values are invalid as they're not required, input "
            f"whole numbers here.")
      print(' ')
      deck_num = input(f'What number deck are you calculating '
                       f'the linear metres of decking required for? ')

          #checking is a number
      while not deck_num.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            deck_num = (input(f'What number deck are you calculating '
                       f'the linear metres of decking required for? '))
      deck_num = float(deck_num)

      print(' ')
      width = (input(f"What is the width of the decking boards "
                        f"you're going to be using (units: millimetres)? "))
      #checking is a number
      while not width.isdigit():
            print(' ')
            print('Invalid input, please input a whole positive integer value.. ')
            print(' ')
            width = (input(f"What is the width of the decking boards "
                        f"you're going to be using (units: millimetres)? "))
      width = float(width)
      print(' ')

      gap = (input(f'What is the width of the gap between the '
                        f'decking boards horizontally (units: '
                        f'millimetres)? '))
      
      #checking is a number
      while not gap.isdigit():
            print(' ')
            print('Invalid input, please input a whole positive integer value.. ')
            print(' ')
            gap = (input(f'What is the width of the gap between the '
                        f'decking boards horizontally (units: '
                        f'millimetres)? '))
      gap = float(gap)

      print(' ')

      deck_width = (input(f'What is the width of the overall '
                              f'(whole) deck (units: metres)? '))
      
      #checking is a number
      while not is_number(deck_width):
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            deck_width = (input(f'What is the width of the overall '
                              f'(whole) deck (units: metres)? '))
      deck_width = float(deck_width)
      print(' ')

      deck_length = (input(f'What is the length of the overall '
                              f'(whole) deck (units: metres)? '))

      #checking is a number
      while not is_number(deck_length):
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            deck_length = (input(f'What is the length of the overall '
                              f'(whole) deck (units: metres)? '))
      deck_length = float(deck_length)
      print(' ')

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
                                    f"(units: whole number (/percentage without '%' sign))? "))
      #checking is a number
      while not waste_percentage_num.isdigit():
            print(' ')
            print(f'Invalid input, please input a whole positve integer '
                  f'value.. ')
            print(' ')
            waste_percentage_num = (input(f"What is the waste percentage "
                                    f"number you would like to allow "
                                    f"(units: whole number (/percentage "
                                    f"without '%' sign))? "))
      waste_percentage_num = float(waste_percentage_num)
      while waste_percentage_num <= 0:
                  invalid_negetive()
                  waste_percentage_num = float(input(f"What is the waste "
                                                     f"percentage "
                                    f"number you would like to allow "
                                    f"(units: whole number (/percentage "
                                    f"without '%' sign))? "))

      os.system('cls')

      decking_area = deck_width * deck_length
      decking_area_rounded = round(decking_area, 3)

      waste_percentage = (waste_percentage_num / 100) + 1

      #Amount in m^2 one linear metre (board??) takes up
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
      
      #checking desired_calculation is a number
      while not another_calc_Ld.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            another_calc_Ld = (input(f"Would you like to complete another "
                                  f"calculation? (input '1' or '2') "))
      another_calc_Ld = int(another_calc_Ld)
      while (another_calc_Ld < 1) or (another_calc_Ld > 2):
           print(' ')
           print("Invalid input, please input either '1' or '2'..")
           print(' ')
           another_calc_Ld = int(input(f"Would you like to complete "
                                  f"another calculation? (input '1' or '2') "))


      return another_calc_Ld

#for stud bit
def another_calcc():
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
      
           #checking desired_calculation is a number
      while not another_calc.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            another_calc = (input(f"Would you like to complete another "
                                  f"calculation? (input '1' or '2') "))
      another_calc = int(another_calc)
      while (another_calc < 1) or (another_calc > 2):
           print(' ')
           print("Invalid input, please input either '1' or '2'..")
           print(' ')
           another_calc = int(input(f"Would you like to complete "
                                  f"another calculation? (input '1' or '2') "))


      
      return another_calc
#STUD OPTION (2)
def stud_length():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲')
      print(' ')

      print('\033[1m' + 'Stud Length (/Raked Wall) selected: ' + '\033[0m')
      print(' ')
      print(f'Please remember: The answers will be in millimetres, so please '
            f'input your values as this measurement value. Thus decimal '
            f'places are not required, please only input whole numbers.'
            f' Unless stated otherwise the units will remain the same across '
            f'all inputs (you do not have to include the units in your input, '
            f'simply input the integer value) otherwise the result/s will be '
            f'incorrect.')
      print(' ')
    #  units = input(f'What units are your measurements in '
    #                f'(this will be the same units '
      #            f'in the results, all units must be the same unless stated '
      #            f'otherwise)? ')
      #while units == int:
      #  invalid_negetive()
      #   units = input('What units are your measurements in? ')
   #   print(' ')
      print(f'--------------------------------------'
            f'---------------------------------')
      print(' ')

      height_outside_edge_lowest_wall = (input(f'What is the height '
                                                    f'of the '
                                          f'lowest wall on the outside '
                                          f'edge? '))


      while not height_outside_edge_lowest_wall.isdigit():
            print(' ')
            print('Invalid input, please input a whole positive integer value.. ')
            print(' ')
            height_outside_edge_lowest_wall = (input(f'What is the height '
                                                    f'of the '
                                          f'lowest wall on the '
                                          f'outside edge? '))
      height_outside_edge_lowest_wall = float(height_outside_edge_lowest_wall)

      while height_outside_edge_lowest_wall < 0:
            invalid_negetive()
            height_outside_edge_lowest_wall = float(input(f'What is the '
                                                          f'height of the'
                                          f' lowest wall on the '
                                          f'outside edge? '))
      print(' ')

      top_plate_thickness = (input(f'What is the top plates thickness? '))
      while not top_plate_thickness.isdigit():
            print(' ')
            print('Invalid input, please input a whole positive integer value.. ')
            print(' ')
            top_plate_thickness = (input(f'What is the top plates '
                                         f'thickness? '))
      top_plate_thickness = float(top_plate_thickness)

 #     while top_plate_thickness < 0:
  #          invalid_negetive()
   #         top_plate_thickness = float(input(f'What is '
  #                                            f'the top plates thickness? '))
      print(' ')

      wall_angle = (input(f'What is the angle of the wall '
                               f'(in degrees (unit))? '))
      while not wall_angle.isdigit():
            print(' ')
            print('Invalid input, please input a whole positive integer value.. ')
            print(' ')
            wall_angle = (input(f'What is the angle of the wall '
                               f'(in degrees (unit))? '))
      wall_angle = float(wall_angle)
      print(' ')


      #plumb_cut = top_plate_thickness / (math.degrees(math.cos(wall_angle)))
      plumb_cut = (top_plate_thickness/math.sin((90-wall_angle)*(math.pi/180)))
      plumb_cut = round(plumb_cut, 3)


      bottom_plate_thickness = (input(f'What is the bottom '
                                           f'plate thickness? '))
      while not bottom_plate_thickness.isdigit():
            print(' ')
            print('Invalid input, please input a whole positive integer value.. ')
            print(' ')
            bottom_plate_thickness = (input(f'What is the bottom '
                                           f'plate thickness? '))
      bottom_plate_thickness = float(bottom_plate_thickness)

    #  while bottom_plate_thickness < 0:
   #         invalid_negetive()
   #         bottom_plate_thickness = float(input(f'What is the bottom plate '
   #                                             f'thickness? '))
      print(' ')

      FIRST_SHORTEST_stud_length = (height_outside_edge_lowest_wall 
                                    - (plumb_cut + bottom_plate_thickness))

      FIRST_SHORTEST_stud_length = round(FIRST_SHORTEST_stud_length, 3)
      os.system('cls')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
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
      continuee=input(f"Press " + '\033[1m' + f"ENTER" + '\033[0m' 
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
            print('Invalid input, please input a whole positive integer value.. ')
            print(' ')
            stud_space_running = (input(f"What is the running stud "
                                             f"spacing (the "
                                    f"distance from the very first "
                                    f"stud at the lowest side of the wall "
                                    f"to the stud you're currently "
                                    f"calculating the length of)? "))
      stud_space_running = float(stud_space_running)

      while stud_space_running < 1:
            invalid_negetive()
            stud_space_running = float(input(f"What is the running stud "
                                             f"spacing (the "
                                    f"distance from the very first "
                                    f"stud at the lowest side of the wall "
                                    f"to the stud you're currently "
                                    f"calculating the length of)? "))
            
      print(' ')
      what_number_stud = (input(f"What number stud along the bottom plate "
                              f"(excluding the very first one on"
                              f" the outside edge, so the miniumum "
                              f"input here is "
                              f"'2') is the one you're calculating "
                              f"the height of? "))
      while not what_number_stud.isdigit():
            print(' ')
            print('Invalid input, please input a whole2 positive integer value.. ')
            print(' ')
            what_number_stud = (input(f"What number stud along the bottom "
                                        f"plate "
                              f"(excluding the very first one on"
                              f" the outside edge, so the miniumum "
                              f"input here is "
                              f"'2') is the one you're calculating "
                              f"the height of? "))
      what_number_stud = float(what_number_stud)

      while what_number_stud <= 1:
            invalid_negetive()
            what_number_stud = float(input(f"What number stud along the "
                                         f"bottom plate "
                              f"(excluding the very first one on"
                              f" the outside edge, so the miniumum "
                              f"input here is "
                              f"'2') is the one you're calculating the "
                              f"height of? "))

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
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
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
              overall_wall_height)

#DONE ABOVE TO HERE... (invalidation etc...)

#desired_calculation = 3 ('what shape' calculation functions) TESTED AND WORK
def calc_rectangle_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Rectangle area selected: ')
    print('')  
    rectangle_num = input('\033[0m' + 'What number rectangle are you calculating the area of? ')      ##
    print(' ')              
    units_rec = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
    print(' ')
    width = float(input('\033[0m' + 'What is the width of the rectangle? '))
    print('')
    while width < 0:
            invalid_negetive()
            width = float(input('What is the width of the rectangle? '))
            print(' ')
    length = float(input('What is the length of the rectangle? '))
    while length < 0:
            invalid_negetive()
            length = float(input('What is the length of the rectangle? '))
            print(' ')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Rectangle volume selected: ')
    print('')
    
    rectangle_area = width * length
    rectangle_area_rounded = round(rectangle_area, 3)
    return rectangle_area_rounded, rectangle_num, units_rec
def calc_square_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('') 
    print('\033[1m' + 'Square area selected: ')
    print('') 
    square_num = input('\033[0m' + 'What number square are you calculating the area of? ')      ##
    print(' ')              
    units_square = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
    print(' ')
    measurement = float(input('\033[0m' + 'What is the side length of the '
                              f'square? '))
    while measurement < 0:
            invalid_negetive()
            measurement = float(input(f'What is the side length of the '
                              f'square?  '))
            print(' ')

    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Square area selected: ')
    print('')
    
    square_area = measurement * 2
    square_area_rounded = round(square_area, 3)
    return square_area_rounded, square_num, units_square
def calc_circle_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    
    print('\033[1m' + 'Circle area selected: ')
    print(' ')
    circle_num = input('\033[0m' + 'What number circle are you calculating the area of? ')      ##
    print(' ')              
    units_circle = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
    print(' ')
    radius = float(input(f'\033[0m' + 'What is the radius of the circle? '))
    print(' ')
    while radius < 0:
            invalid_negetive()
            radius = float(input(f'What is the radius of the circle? '))
            print(' ')
    print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Circle area selected: ')
    print(' ')
    
    circle_area = math.pi * (radius ** 2)
    circle_area_rounded = round(circle_area, 3)
    return circle_area_rounded, circle_num, units_circle
def calc_cylinder_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')       
    print('\033[1m' + 'Cylinder (Surface Area) selected: ')
    print(' ')
    cylinder_num = input('\033[0m' + 'What number cylinder are you calculating the area of? ')      ##
    print(' ')              
    units_cylinder = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
    print(' ')
    radius = float(input('\033[0m' + 'What is the radius of the cylinder? ')) 
    print(' ')
    while radius < 0:
            invalid_negetive()
            radius = float(input(f'What is the radius of the cylinder? '))
            print(' ')
    height = float(input('What is the height of the cylinder? '))
    while height < 0:
            invalid_negetive()
            radius = float(input(f'What is the height of the cylinder? '))
            print(' ')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Cylinder (Surface Area) selected: ')
    print(' ')
    
    cylinder_area = (2 * math.pi * radius*height) + (2 * math.pi *(radius **2))
    cylinder_area_rounded = round(cylinder_area, 3)
    return cylinder_area_rounded, cylinder_num, units_cylinder
def calc_triangle_area():
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Triangle area selected: ')
    print(' ')
    triangle_num = input('\033[0m' + 'What number triangle are you calculating the area of? ')      ##
    print(' ')              
    units_triangle = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
    print(' ')
    height = float(input('\033[0m' +'What is the height of the triangle? '))
    print(' ')
    while height < 0:
            invalid_negetive()
            radius = float(input(f'What is the height of the triangle? '))
            print(' ')
    base = float(input("What is the length of the triangle's base? "))
    while base < 0:
            invalid_negetive()
            base = float(input(f"What is the length of the triagle's base? "))
            print(' ')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
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
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cuboid volume selected: ')
      print(' ')
      cubiod_num = input(f'\033[0m' + f'What number cuboid are you '
                         f'calculating the volume of? ')      ##
      print(' ')              
      units_cuboid = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
      print(' ')
      height = float(input(f'\033[0m' + 'What is the height of the '
                              f'cuboid? ')) 
      while height < 0:
            invalid_negetive()
            height = float(input(f'What is the height of the cuboid? '))
            print(' ')
      #'float' allows for decimals as builders work to decimals 

      print(' ')
      width = float(input('What is the width of the cuboid? '))
      print(' ')
      while width < 0:
            invalid_negetive()
            width = float(input(f'What is the width of the cuboid? '))
            print(' ')
      depth = float(input('What is the depth of the cuboid? '))
      print(' ')
      while depth < 0:
            invalid_negetive()
            depth = float(input(f'What is the depth of the cuboid? '))
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
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
      print(' ')
      print('\033[1m' + 'Cube volume selected: ')
      print(' ')
      cube_num = input(f'\033[0m' + f'What number cube are you '
                       f'calculating the volume of? ')      ##
      print(' ')              
      units_cube = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
      print(' ')
      measurement = float(input(f'\033[0m' + 'What is the side length'
                              f' of the cube? '))
      print(' ')
      while measurement < 0:
            invalid_negetive()
            measurement = float(input(f'What is the side length'
                              f' of the cube? '))
            print(' ')

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
      print(' ')
      cylinder_num = input(f'\033[0m' + f'What number cylinder are '
                           f'you calculating the volume of? ')      ##
      print(' ')              
      units_cylinder = input(f"What units (metres, centimetres, etc) are "
                             f"you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
      print(' ')
      height = float(input(f'\033[0m' + 'What is the height of the '
                              f'cylinder? '))
      print(' ')
      while height < 0:
            invalid_negetive()
            height = float(input(f'What is the height of the cylinder? '))
            print(' ')
      radius = float(input('What is the radius of the cylinder? '))
      print(' ')
      while radius < 0:
            invalid_negetive()
            radius = float(input(f'What is the radius of the cylinder? '))
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
      print(' ')
      cone_num = input(f'\033[0m' + f'What number cone are you '
                       f'calculating the volume of? ')      ##
      print(' ')              
      units_cone = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
      print(' ')
      height = float(input(f'\033[0m' + 'What is the height of the '
                              f'cone? '))
      print(' ')
      while height < 0:
            invalid_negetive()
            height = float(input(f'What is the height of the cone? '))
            print(' ')
      radius = float(input('What is the radius of the cone? '))
      print(' ')
      while radius < 0:
            invalid_negetive()
            radius = float(input(f'What is the radius of the cone? '))
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
      print(' ')
      sphere_num = input(f'\033[0m' + f'What number sphere are you '
                         f'calculating the volume of? ')      ##
      print(' ')              
      units_sphere = input(f"What units (metres, centimetres, etc) are you're "          ##
                      f"measurements in (please keep them the same for "
                      f"each input unless asked for differently)? ")
      print(' ')
      radius = float(input('\033[0m' + 'What is the radius of the sphere? '))
      print(' ')
      while radius < 0:
            invalid_negetive()
            radius = float(input(f'What is the radius of the sphere? '))
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
      what_shape = int(what_shape)
      return what_shape


#exit/goodbye ("6. Exit")
def goodbye_exit_screen():
    os.system('cls')
    print(f'\n★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ 　° :. ★　 * • ○ ° ★ .'
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
    
      
    print(f'★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ 　° :. ★　 * • ○ ° ★ .　 '
          f'* 　.　. ° 　. ● . ★ ° . *　　　°　.　°☆')

#additional linear decking function
def another_calc_Ld_is_letter():
     another_calc_Ld = (input(f"Would you like to complete "
                                  f"another calculation? (input '1' or '2') "))
     while not another_calc_Ld.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
           # another_calc_Ld = (input(f"Would you like to complete another "
                                #  f"calculation? (input '1' or '2') "))
            another_calc_Ld = another_calc_Ld_is_letter()

           # if another_calc_Ld != another_calc_Ld.isdigit():
         #         another_calc_Ld = float(another_calc_Ld)
      
     return another_calc_Ld

#making (now empty) dictionary 
finalreport = {}

desired_calculation = main_program_1st_display()


#invalid ans        works
while (desired_calculation < 1) or (desired_calculation >= 6): 
      desired_calculation = desired_calculation_invalid()  
      
while desired_calculation != 5:     #as long as it isn't '6' it does this
    print(' ')
    os.system('cls')

    if desired_calculation == 1:  #linear decking
      os.system('cls')
      #decking_result = calc_decking()
      quantity_linear_m_rounded, deck_num = linear_metres_decking_required()

      #adding 1st one to dic
      finalreport[f"The linear metres of decking required for deck {deck_num}"] = f"{quantity_linear_m_rounded}"

      print('-----------------------------------------------------------------------')
      print(' ')
      print('Next options:')
      print(' ')
      print(f'1. Calculate another amount of linear metres of decking '
            f'required (just like you did)')
      print('2. Back to main menu')
      print(' ')
      another_calc_Ld = (input(f"Would you like to complete another "
                                  f"calculation? (input '1' or '2') "))
                                                                                    #this doesn't work (keeps reasking even if '1' or '2' is inputted)
      
      while not another_calc_Ld.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            another_calc_Ld = (input(f"Would you like to complete another "
                                  f"calculation? (input '1' or '2') "))
      another_calc_Ld = int(another_calc_Ld)
      while (another_calc_Ld < 1) or (another_calc_Ld > 2):
           print(' ')
           print("Invalid input, please input either '1' or '2'..")
           print(' ')
           another_calc_Ld = int(input(f"Would you like to complete "
                                  f"another calculation? (input '1' or '2') "))
           
  
           
           
      while another_calc_Ld == 1:
            os.system('cls')
            quantity_linear_m_rounded, deck_num = linear_metres_decking_required()
            finalreport[f"The linear metres of decking required for deck {deck_num}"] = f"{quantity_linear_m_rounded}"
            
            another_calc_Ld = another_calc_linear_decking()
      if another_calc_Ld == 2:
            os.system('cls')
            desired_calculation = main_program_1st_display() #(1)
      #cont=input("Press ENTER to continue")                               

    elif desired_calculation == 2:  #stud length

      os.system('cls')
      #  stud_result = stud_length()
      (calculated_stud_length, what_number_stud, 
       spacing_along_top_plate, FIRST_SHORTEST_stud_length, 
       overall_wall_height) = stud_length()
      
      finalreport[f"The very first stud length at the lowest point of the "
                  f"wall"] = f"{FIRST_SHORTEST_stud_length} mm long"
      
      finalreport[f"Stud length ({what_number_stud})"] = (f""
                                    f"{calculated_stud_length} mm long")
      
      finalreport[f"Stud {what_number_stud} (above)"] = (f""
                                          f"{spacing_along_top_plate} mm "
                                          f"along the top plate and at this "
                                          f"point/stud the total wall "
                                          f"height is {overall_wall_height} "
                                          f"mm tall")
      print(f'--------------------------------'
            f'---------------------------------------')
      print(' ')
      print('Next options:')
      print(' ')
      print('1. Calulate another stud length (just like you did)')
      print('2. Back to main menu')
      print(' ')
      another_calc = (input("Would you like to complete another "
                               f"calculation? (input '1' or '2') "))
      
      while not another_calc.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            another_calc = (input(f"Would you like to complete another "
                                  f"calculation? (input '1' or '2') "))
      another_calc = int(another_calc)
      while (another_calc < 1) or (another_calc > 2):
           print(' ')
           print("Invalid input, please input either '1' or '2'..")
           print(' ')
           another_calc = int(input(f"Would you like to complete "
                                  f"another calculation? (input '1' or '2') "))
           
      while another_calc == 1:
            os.system('cls')
            calculated_stud_length, what_number_stud, units, spacing_along_top_plate, FIRST_SHORTEST_stud_length, overall_wall_height = stud_length()

            finalreport[f"Stud length ({what_number_stud})"] = f"{calculated_stud_length} {units} long"

            finalreport[f"Stud {what_number_stud} (above)"] = f"{spacing_along_top_plate} {units} along the top plate and at this point/stud the total wall height is {overall_wall_height} {units} tall"  ##
            
            another_calc = another_calcc()
      if another_calc == 2:
            os.system('cls')
            desired_calculation = main_program_1st_display() #(1)

    elif desired_calculation == 3:        #Area!          WORKS!! DONE  W DICTIONARY APPEND ALSO DONE
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

        what_shape = input(f"What shape's area would you like to calculate from"
                           f" the list? ")
        
        while not what_shape.isdigit():
            print(' ')
            print('Invalid input, please input a positive integer value.. ')
            print(' ')
            what_shape = (input(f"What shape's area would you like to calculate from"
                           f" the list (between or equal to 1 & 6)? "))
      
        what_shape = int(what_shape)

        #invalid ans                                                            
        while (what_shape < 1) or (what_shape >= 7):
            what_shape = what_shape_invalid()


        #needed math imports:
        math.pi == math.pi

        #while loop for 'area' option (SUB OPTIONS OF MAIN WHILE) (nested?!?!)
        while what_shape <= 6 and what_shape >= 1:
            #rectangle                                    
            if what_shape == 1:
                os.system('cls')
                rectangle_area_rounded, rectangle_num, units_rec = calc_rectangle_area()
                finalreport[f"Rectangle area ({rectangle_num})"] = f"{rectangle_area_rounded} {units_rec} squared"
                print(f'\033[0m' + "Your rectangle's area is: " + '\033[1m' +
                      f'{rectangle_area_rounded} {units_rec} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
                print('\033[0m')
                os.system('cls')
            #square                           
            elif what_shape == 2:
                os.system('cls')
                square_area_rounded, square_num, units_square = calc_square_area()
                finalreport[f"Square area ({square_num})"] = f"{square_area_rounded} {units_square} squared"
                print(f'\033[0m' + "Your cube's volume is: " + '\033[1m' +
                      f'{square_area_rounded} {units_square} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #circle    
            elif what_shape == 3:
                os.system('cls')
                circle_area_rounded, circle_num, units_circle = calc_circle_area()
                finalreport[f"Circle area ({circle_num})"] = f"{circle_area_rounded} {units_circle} squared"
                print(f'\033[0m' + "Your circle's area is: " + '\033[1m' +
                      f'{circle_area_rounded} {units_circle} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #cylinder    
            elif what_shape == 4:
                os.system('cls')
                cylinder_area_rounded, cylinder_num, units_cylinder = calc_cylinder_area()
                finalreport[f"Cylinder area ({cylinder_num})"] = f"{cylinder_area_rounded} {units_cylinder} squared"
                print(f'\033[0m'+"Your cylinder's surface area is: "+'\033[1m'+ 
                      f'{cylinder_area_rounded} {units_cylinder} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #triagle    
            elif what_shape == 5:
                os.system('cls')
                triangle_area_rounded, triangle_num, units_triangle = calc_triangle_area()
                finalreport[f"Triangle area ({triangle_num})"] = f"{triangle_area_rounded} {units_triangle} squared"
                print(f'\033[0m' + "Your triangle's area is: " + '\033[1m' + 
                      f'{triangle_area_rounded} {units_triangle} squared')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")           
            #exit
            elif what_shape == 6:
                  os.system('cls')
                  desired_calculation = main_program_1st_display() #(1)
                  break
            break


      #desired_calculation = main_program_1st_display()    
            #works but the desired calculation goes to 'what_shape' and keeps 
            #within this loop, need to fix somehow..


    elif desired_calculation == 4:        #Volume!          WORKS!! DONE  W DICTIONARY APPEND ALSO DONE
        os.system('cls')
        #display/list of operations
        print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
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

        #while loop for 'volume' option (SUB OPTIONS OF MAIN WHILE) (nested?!?!)
        while what_shape <= 6 and what_shape >= 1:
            #CUBOID                                                             
            if what_shape == 1:
                os.system('cls')
                cuboid_volume_rounded, cubiod_num, units_cuboid = calc_cuboid_volume()
                finalreport[f"Cuboid volume ({cubiod_num})"] = f"{cuboid_volume_rounded} {units_cuboid} cubed"
                print(f'\033[0m' + "Your cuboid's volume is: "+'\033[1m'+
                      f'{cuboid_volume_rounded} {units_cuboid} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
                print('\033[0m')
                os.system('cls')
            #CUBE                           
            elif what_shape == 2:
                os.system('cls')
                cube_volume_rounded, cube_num, units_cube = calc_cube_volume()
                finalreport[f"Cube volume ({cube_num})"] = f"{cube_volume_rounded} {units_cube} cubed"
                print(f'\033[0m' + "Your cube's volume is: "+'\033[1m'+
                      f'{cube_volume_rounded} {units_cube} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #CYLINDER    
            elif what_shape == 3:                                                   
                os.system('cls')
                cylinder_volume_rounded, cylinder_num, units_cylinder = calc_cylinder_volume()
                finalreport[f"Cylinder volume ({cylinder_num})"] = f"{cylinder_volume_rounded} {units_cylinder} cubed"
                print(f'\033[0m' + "Your cylinder's volume is: " + '\033[1m' +
                      f'{cylinder_volume_rounded} {units_cylinder} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #CONE    
            elif what_shape == 4:              
                os.system('cls')
                cone_volume_rounded, cone_num, units_cone = calc_cone_volume()
                finalreport[f"Cone volume ({cone_num})"] = f"{cone_volume_rounded} {units_cone} cubed"
                print(f'\033[0m'+"Your cone's volume is: "+'\033[1m'+ 
                      f'{cone_volume_rounded} {units_cone} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")
            #SPHERE    
            elif what_shape == 5: 
                os.system('cls')
                sphere_volume_rounded, sphere_num, units_sphere = calc_sphere_volume()
                finalreport[f"Sphere volume ({sphere_num})"] = f"{sphere_volume_rounded} {units_sphere} cubed"
                print(f'\033[0m' + "Your sphere's volume is: " + '\033[1m' + 
                      f'{sphere_volume_rounded} {units_sphere} cubed')
                print(' ')
                print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                cont=input("Press ENTER to continue back to main screen")           
            #exit
            elif what_shape == 6:
                  desired_calculation = main_program_1st_display() #(1)
                  break
            break


while desired_calculation == 5: #EXIT works
    goodbye_exit_screen()
    
    break
