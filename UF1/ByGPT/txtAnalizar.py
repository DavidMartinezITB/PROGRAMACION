"""
David Martinez
ASIXc1A
"""

PROHIBIT_CHARS = '.,?¿!¡"\''

text        = 'Python es un lenguaje de programación versátil y fácil de aprender. Python es ampliamente utilizado en desarrollo web, inteligencia artificial y análisis de datos. Aprender Python puede abrir muchas puertas en tu carrera profesional.'
longest     = ''
palabras    = 0

vecesPalabras   = {}
freqPalabras    = {}

def tratarTexto(text):
    for i in PROHIBIT_CHARS:
        text = text.replace(i, '')
    return text.lower().strip()


for l in text.split():
    palabras += 1
    l = tratarTexto(l)
    if len(l) > len(longest):
        longest = l
    
    if l not in vecesPalabras:
        vecesPalabras[l] = 1
    else:
        vecesPalabras[l] += 1
    
    if len(l) not in freqPalabras:
        freqPalabras[len(l)] = 1
    else:
        freqPalabras[len(l)] += 1

print(f'Cantidad total de palabras: {palabras}\n')
print(f'Frecuencia de cada palabra: ')

for i in vecesPalabras:
    if len(i) <= 4:
        print(f'- {i}:\t\t\t{vecesPalabras[i]}')
    else:
        print(f'- {i}:\t\t{vecesPalabras[i]}')

print(f'\nPalabra mas larga: {longest}\n')

print(f'Frecuencia de longitud de palabras:')

sortedFreq = sorted(freqPalabras.keys())

for i in sortedFreq:
    if i == 1:
        if freqPalabras[i] == 1:
            print(f'- {i} letra:\t{freqPalabras[i]} palabra')
        else:
            print(f'- {i} letra:\t{freqPalabras[i]} palabras')
    else:
        if freqPalabras[i] == 1:
            print(f'- {i} letras:\t{freqPalabras[i]} palabra')
        else:
            print(f'- {i} letras:\t{freqPalabras[i]} palabras')