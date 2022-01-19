import random
lists = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

m1 = 'X'
m2 = 'O'

def winCheck():
    '''
    The function checks if A player win in a row/column/hypotenuse
    :return: We Have A Winner
    '''
    for row in lists:
        if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
            return print('We Have A Winner')
    if lists[0][0] == lists[1][0] == lists[2][0] == m1:
        return print('We Have A Winner')
    elif lists[0][0] == lists[1][0] == lists[2][0] == m2:
        return print('We Have A Winner')
    elif lists[0][1] == lists[1][1] == lists[2][1] == m1:
        return print('We Have A Winner')
    elif lists[0][1] == lists[1][1] == lists[2][1] == m2:
        return print('We Have A Winner')
    elif lists[0][2] == lists[1][2] == lists[2][2] == m1:
        return print('We Have A Winner')
    elif lists[0][2] == lists[1][2] == lists[2][2] == m2:
        return print('We Have A Winner')
    elif lists[0][0] == lists[1][1] == lists[2][2] == m1:
        return print('We Have A Winner')
    elif lists[0][0] == lists[1][1] == lists[2][2] == m2:
        return print('We Have A Winner')
    elif lists[0][2] == lists[1][1] == lists[2][0] == m1:
        return print('We Have A Winner')
    elif lists[0][2] == lists[1][1] == lists[2][0] == m2:
        return print('We Have A Winner')
    return

while True:
    x = int(input('Please enter row number: ').upper())
    y = int(input('Please enter Ta number: ').upper())

    if 0 <= x <= 2 and 0 <= y <= 2:  #checks if input in range
        if lists[x][y] == 'X' and 'O':
            print('Place Occupied...')
        else:
            z = input('Choose X or O: ').upper()
            if z != 'X' and z != 'O':
                print('Wrong matrix')
            else:
                lists[x][y] = z
    else:
        print('Invalid position')
#robot
    rd1 = random.randint(0, 2)
    rd2 = random.randint(0, 2)
    x = rd1
    y = rd2
    while True:
        if lists[x][y] == 'X' and 'O':
            continue
        else:
            lists[x][y] = 'O'
            break
    for i in lists:
        print(i)
    winCheck()
