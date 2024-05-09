import colors

def getInputFromKeyboard():
    data = input().split()
    if data == []:
        return []
    
    if len(data) != 3 and data[0] != ';Q':
        return []
    elif data[0] == ';Q':
        return 'e'
    
    if not data[1].isdigit() and not data[2].isdigit():
        return []
    
    try:
        data[1] = int(data[1])
        data[2] = int(data[2])
    except Exception as e:
        #print('[!] Error: {}'.format(e))
        return []
    
    return tuple(data)

def displayRectangle(color, rows, columns): 
    match str(color.lower().strip()):
        case 'red':
            color = colors.CRED
        case 'green':
            color = colors.CGREEN
        case 'blue':
            color = colors.CBLUE
        case _:
            return
    
    print(color)

    for i in range(rows):
        for j in range(columns):
            print('X', end="")
        print()