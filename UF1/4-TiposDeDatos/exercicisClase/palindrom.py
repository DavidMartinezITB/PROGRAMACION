"""
David Martinez
ASIXc1A - M03
Tipus de dades secuencials - Exercicis de classe
"""
# Definim input en minuscules i eliminant els espais entre paraules, els punts i les comes
w = input().replace(' ', '').replace('.', '').replace(',', '').replace('’', '').lower()

if w == w[::-1]:
    print('Es palindrom!')
else:
    print('No es palindrom!')