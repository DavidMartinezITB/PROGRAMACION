def palindrom():
    w = getInput()
    if w == w[::-1]:
        print('Es palindrom!')
    else:
        print('No es palindrom!')
    input('ENTER per continuar')

def getInput():
    BADCHARS = ' .,\'\"/!@#$%^&*()\{\}\\'
    w = input()
    for char in BADCHARS:
        w = w.replace(char, '')
    return w