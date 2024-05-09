import string

def cesar():
    text, n = getInput()
    print(encrypt_text(text, n))
    input('ENTER per continuar')

def getInput():
    text    = input('Introdueix a continuacio el text a xifrar:\n')
    n       = input('Introdueix el numero de lletres que se desplazaran: ')
    while not isinstance(n, int):
        try:
            n = int(n)
        except:
            n = input('Introdueix el numero de lletres que se desplazaran: ')
    
    return (text, n)


def encrypt_text(text, n):
    CHARS = string.ascii_letters
    result = ''
    for i in range(len(text)):
        ch = text[i]
        
        if ch not in CHARS:
            result += ch
        elif ch.isupper():
            result += chr((ord(ch) + n-65) % 26 + 65)
        else:
            result += chr((ord(ch) + n-97) % 26 + 97)
    
    return result