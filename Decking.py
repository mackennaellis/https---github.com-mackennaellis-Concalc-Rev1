def invalid_negetive():
      print(' ')
      print(f'Invalid input, please input a ' + '\033[1m' + f'positive' +
            '\033[0m' + f' number')
      print(' ')

def another_calc_linear_decking():
      print('-----------------------------------------------------------------------')
      print(' ')
      print('Next options:')
      print(' ')
      print('1. Calulate another amount of linear metres of decking (just like you did)')
      print('2. Back to main menu')
      another_calc_Ld = int(input("Would you like to complete another calculation? (input '1' or '2') "))
      return another_calc_Ld

def linear_metres_decking_required():
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲')
      print(' ')
      print('\033[1m' + 'Linear Metres Of Decking Required Selected: ')
      print('')           
      print(f'\033[0m' + f'Next to the questions, units will be stated. '
            f'Please do not include the units in your input '
            f'it is simply to tell you what units the input '
            f'should be in.')     
      print(' ')
      width = float(input(f"What is the width of the decking boards "
                        f"you're going to be using (units: millimetres)? "))
      print(' ')
      gap = float(input(f'What is the width of the gap between the '
                        f'decking boards horizontally (units: '
                        f'millimetres)? '))
      print('')
      deck_width = float(input(f'What is the width of the overall '
                              f'(whole) deck (units: metres)? '))
      print(' ')
      deck_length = float(input(f'What is the length of the overall '
                              f'(whole) deck (units: metres)? '))
      print(' ')
      print('-----------------------------------------------------------------------')
      print(' ')
      print(f'**A waste percentage is how much waste (extra) '
            f'are you allowing for. Between 5 - 15% is '
            f'recommended with 10% usually being a great allowance. '
            f'At least greater then zero**')
      print(' ')
      waste_percentage_num = float(input(f'What is the waste percentage '
                                    f'number you would like to allow '
                                    f'(units: percentage)? '))
      while waste_percentage_num <= 0:
                  invalid_negetive()
                  waste_percentage_num = float(input(f'What is the waste percentage '
                                    f'number you would like to allow '
                                    f'(units: percentage)? '))
      #not 0
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲')

      os.system('cls')

      decking_area = deck_width * deck_length
      decking_area_rounded = round(decking_area, 3)

      waste_percentage = (waste_percentage_num / 100) + 1

      #Amount in m^2 one linear metre (board??) takes up
      decking_area_in_m2 = (gap + width) / 1000

      quantity_linear_m = ((decking_area**2) / decking_area_in_m2) * waste_percentage
      quantity_linear_m_rounded = round(quantity_linear_m, 3)

      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲')
      print(' ')
      print('\033[1m' + 'Linear Metres Of Decking Required Selected: ')
      print(' ')
      print(f'\033[0m' + f'For this {decking_area} metres-squared deck, ' 
            + '\033[1m' +  f'{quantity_linear_m_rounded} linear-metres ' 
            + '\033[0m' + f'of decking is required')
      print(' ')
      print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲')
      print(' ')
print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
                  f'☲☲')
print(' ')
print('\033[1m' + 'Linear Metres Of Decking Required Selected: ')
print('')           
print(f'\033[0m' + f'Next to the questions, units will be stated. '
      f'Please do not include the units in your input '
      f'it is simply to tell you what units the input '
      f'should be in.')     
print(' ')
width = float(input(f"What is the width of the decking boards "
                  f"you're going to be using (units: millimetres)? "))
print(' ')
gap = float(input(f'What is the width of the gap between the '
                  f'decking boards horizontally (units: '
                  f'millimetres)? '))
print('')
deck_width = float(input(f'What is the width of the overall '
                        f'(whole) deck (units: metres)? '))
print(' ')
deck_length = float(input(f'What is the length of the overall '
                        f'(whole) deck (units: metres)? '))
print(' ')
print('-----------------------------------------------------------------------')
print(' ')
print(f'**A waste percentage is how much waste (extra) '
      f'are you allowing for. Between 5 - 15% is '
      f'recommended with 10% usually being a great allowance. '
      f'At least greater then zero**')
print(' ')
waste_percentage_num = float(input(f'What is the waste percentage '
                              f'number you would like to allow '
                              f'(units: percentage)? '))
while waste_percentage_num <= 0:
            invalid_negetive()
            waste_percentage_num = float(input(f'What is the waste percentage '
                              f'number you would like to allow '
                              f'(units: percentage)? '))
#not 0
print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲')

os.system('cls')

decking_area = deck_width * deck_length
decking_area_rounded = round(decking_area, 3)

waste_percentage = (waste_percentage_num / 100) + 1

#Amount in m^2 one linear metre (board??) takes up
decking_area_in_m2 = (gap + width) / 1000

quantity_linear_m = ((decking_area**2) / decking_area_in_m2) * waste_percentage
quantity_linear_m_rounded = round(quantity_linear_m, 3)

print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲')
print(' ')
print('\033[1m' + 'Linear Metres Of Decking Required Selected: ')
print(' ')
print(f'\033[0m' + f'For this {decking_area} metres-squared deck, ' 
      + '\033[1m' +  f'{quantity_linear_m_rounded} linear-metres ' 
      + '\033[0m' + f'of decking is required')
print(' ')
print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲')
print(' ')
print('-----------------------------------------------------------------------')
print(' ')
print('Next options:')
print(' ')
print('1. Calulate another stud length (just like you did)')
print('2. Exit')
print(' ')
another_calc_Ld = int(input("Would you like to complete another calculation? (input '1' or '2') "))
while another_calc_Ld == 1:
      os.system('cls')
      linear_metres_decking_required()
      another_calc_Ld = another_calc_linear_decking()
if another_calc_Ld == 2:
      os.system('cls')
      desired_calculation = main_program_1st_display() #(1)

