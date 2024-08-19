import os


def volume_shape_selection():
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
    print(' ')
    return

display_volume_selction = volume_shape_selection()