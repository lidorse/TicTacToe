lists = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

m1 = 'X'
m2 = 'O'
m3 = 'X' or 'O'

def winCheck():
    '''
    The function checks if A player win in a row/column/hypotenuse
    :return: We Have A Winner
    '''
    for row in lists: #checks win in row
        if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
            return True
    if lists[0][0] == lists[1][0] == lists[2][0] == m1: #checks win in column
        return True
    elif lists[0][0] == lists[1][0] == lists[2][0] == m2:
        return True
    elif lists[0][1] == lists[1][1] == lists[2][1] == m1:
        return True
    elif lists[0][1] == lists[1][1] == lists[2][1] == m2:
        return True
    elif lists[0][2] == lists[1][2] == lists[2][2] == m1:
        return True
    elif lists[0][2] == lists[1][2] == lists[2][2] == m2:
        return True
    elif lists[0][0] == lists[1][1] == lists[2][2] == m1: #checks win in hypotenuse
        return True
    elif lists[0][0] == lists[1][1] == lists[2][2] == m2:
        return True
    elif lists[0][2] == lists[1][1] == lists[2][0] == m1:
        return True
    elif lists[0][2] == lists[1][1] == lists[2][0] == m2:
        return True
'''def boardIsFull():
    for row in lists:
        if row[0] == m3 and row[1] == m3 and row[2] == m3:
            return True'''

while True:
    try:
        x = int(input('Please enter row number: ').upper())
        y = int(input('Please enter Ta number: ').upper())

        if 0 <= x <= 2 and 0 <= y <= 2:  #checks if input in range
            if lists[x][y] == 'X' and 'O': #checks if place occupied
                print('Place Occupied...')
            else:
                z = input('Choose X or O: ').upper() #checks if metrix is correct
                if z != 'X' and z != 'O':
                    print('Wrong matrix')
                else:
                    lists[x][y] = z
        else:
            print('Invalid position')
    except:
        print('Error Value, Please try again')

    for i in lists:
        print(i)
    winCheck()
    if winCheck() == True:
        print('We Have A Winner!')
        break
    '''boardIsFull()
    if boardIsFull() == True:
        print('Its a Tie!')
        lists.clear()'''
