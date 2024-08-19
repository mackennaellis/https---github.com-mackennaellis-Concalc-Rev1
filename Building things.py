#RECTANGLE VOLUME WITH FUCTIONS (could use in program)
def cube_or_rectangle(x, y, z):
    a = int(x)
    b = int(y)
    c = int(z)
    global shapevolume
    shapevolume = a*b*c


#next class: try get this seperating string thing into a function
#variables = input('What is the length, width, and depth of the rectangular shape?: ')
a = ''
b = ''
c = ''
def split_input3(x, y, z):
    variableSplit = variables.split(' ')
    variableslist = []
    variableslist.append(variableSplit[0])
    variableslist.append(variableSplit[1])
    variableslist.append(variableSplit[2])
    global a        #allows access from outside the function of full 'method' works
    global b
    global c
    a = variableslist[0]
    b = variableslist[1]
    c = variableslist[2]
    return(a, b, c)


def split_input2(x, y):
    variableSplit = variables.split(' ')
    variableslist = []
    variableslist.append(variableSplit[0])
    variableslist.append(variableSplit[1])
    global a        #allows access from outside the function of full 'method' works
    global b
    a = variableslist[0]
    b = variableslist[1]
    return(a, b)


#split_input3(a, b, c)
#cube_or_rectangle(a, b, c)
#print(f'The volume of that 3d rectangular shape is: {shapevolume}')





#can also be used for cube:
#print(f'The volume of that cube is: {shapevolume}')

#triangles!!!!!!!!!!!!
#AREA
variables = input('What is the width, and height of the triangle?: ')
def triangle_area(width, height):
    a = int(width)
    b = int(height)
    global trianglearea
    trianglearea = a*b*0.5

split_input2(a, b)
triangle_area(a, b)
print(trianglearea)