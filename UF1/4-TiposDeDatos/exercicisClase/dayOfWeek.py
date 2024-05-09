"""
David Martinez
ASIXc1A
Programacio

Donat un enter, mostrar el dia de la setmana amb text (dilluns, dimarts, dimecres…), tenint en compte que dilluns és el 1. Els dies de la setmana es guarden en una llista.

Fer el control d'errors

Input
7 

Output
diumenge
"""

DIAS = (
    ('dilluns', 'dimarts', 'dimecres', 'dijous', 'divendres', 'dissabte', 'diumenje'),
    ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'),
    ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
)

try:
    dia = int(input()) - 1

    if dia in range(7):
        for lang in DIAS:
            print(lang[dia].capitalize())
    else:
        print(f'[!] No existe el dia de la semana numero {dia + 1}!')
except ValueError:
    print('[!] Debe ser un entero!')