VOCALS = ["A", 'E', 'I', 'O', 'U']

letra = ''

def isVocal(letra):
    for i in VOCALS:
            if letra.upper() == i:
                return True

while letra != ' ':
    letra = input()
    if len(letra) == 1 and letra != ' ':
        if isVocal(letra):
            print('VOCAL')
        else:
             print('NO VOCAL')