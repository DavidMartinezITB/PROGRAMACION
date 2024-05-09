"""
David Martinez
ASIXc1A - M03
UF2 - A1
Basket
"""
from time import sleep

# CONSTANTES #
DEFAULT_TEAM_1      = 'Local'
DEFAULT_TEAM_2      = 'Visitante'

VALID_POINTS        = [1, 2, 3]
COMMENT_SENTENCES   = [
    "El partido ha comenzado! $team1$ vs $team2$", # Inicio de partido
    "El equipo $team$ ha marcado en tiro libre!",  # Tiro libre
    "El equipo $team$ ha marcado canasta!",        # Canasta
    "El equipo $team$ ha marcado un triple!"       # Triple
] # $team$ -> Equipo que marca; $team1$ -> Equipo 1; $team2$ -> Equipo 2

# FUNCTIONS #
# XOR
def xor(a, b):
    return bool(a) ^ bool(b)

# Display de errores
def displayError(*e):
    RED = '\033[31m'
    WHITE = '\033[0m'

    if e:
        print(RED + '[!] Error: ' + e + '!' + WHITE)
    else:
        print(RED + '[!] Error no especificado!' + WHITE)

# Obtener equipos
def getTeams():
    # Obtenemos inputs
    t1 = input()
    t2 = input()

    # Si el usuario añade una cadena vacia como nombre de equipo (o espacios)
    if t1.strip() == '':
        print('[i] Equipo 1: {}'.format(DEFAULT_TEAM_1))
        t1 = DEFAULT_TEAM_1
    if t2.strip() == '':
        print('[i] Equipo 2: {}'.format(DEFAULT_TEAM_2))
        t2 = DEFAULT_TEAM_2

    # Si los equipos se llaman igual (not case-sensitive)
    if t1.lower() == t2.lower():
        print('[!] Los nombres de los equipos no pueden ser iguales!\n    Equipos {} y {}'.format(DEFAULT_TEAM_1, DEFAULT_TEAM_2))
        return DEFAULT_TEAM_1, DEFAULT_TEAM_2

    return t1, t2

# Obtener puntuaciones
def getPoints():
    points = [(0, 0)] # Lista que va recogiendo cada jugada en tuplas (tupla / jugada)
    on = True # Flag que se encarga de controlar el status de While
    while on:
        try:
            data = [int(x) for x in input().split()]
            if len(data) == 2: # Se han introducido 2 valores separados por espacios
                if data[0] - points[-1][0] <= 3 or data[1] - points[-1][1] <= 3: # Se ha añadido correctamente un valor al marcador (1, 2 o 3)
                    if data[0] > points[-1][0] or data[1] > points[-1][1]:
                        if xor(data[0] == points[-1][0], data[1] == points[-1][1]): # XOR que se asegura que uno de los dos puntajes ha aumentado y no los dos (abajo explicacion de como funciona puerta logica XOR)
                            points.append((data[0], data[1]))
                        else:
                            displayError('Solo puedes incrementar uno de los valores por jugada')
                    else:
                        displayError('El contador debe incrementar')
                else:
                    displayError('Puntuacion ivalida')
            elif len(data) == 1 and data[0] == -1: # Se ha introducido solo un valor -1
                if points[-1][0] != points[-1][1]: # No estan empatados los equipos
                    on = False # Salimos de While
                else:
                    displayError('Empates no admitidos. Se realiza prorroga hasta desempate')
            else:
                displayError('Se esperaban dos valores')
        except ValueError:
            displayError('Solo se admiten numeros enteros')
    return points

# Comentar partido
def commentPlay():
    for k, v in enumerate(points):
        # Obtenemos la diferencia del valor incrementado
        # Que valor ha incrementado?
        if k == 0: # Si es la primera puntuacion
            if v[0] == 0: # Si el valor del primer equipo vale 0, sabemos que ha incrementado el contrario
                inc = 1
            else:
                inc = 0
            inc_value = v[inc]
        else:
            if v[0] == points[k-1][0]: # Si el contador del primer equipo es igual a la anterior jugada, sabemos que ha incrementado el contrario
                inc = 1
            else:
                inc = 0
            inc_value = v[inc] - points[k - 1][inc] # Sabemos que el valor que el valor que se ha incrementado es la resta del valor total y el valor de la jugada anterior
        
        # Evaluamos el valor de 'inc_value' y obtenemos la frase a printar
        match inc_value:
            case 1: sentence = 1
            case 2: sentence = 2
            case 3: sentence = 3
            case _: sentence = 0
        
        # Printamos la frase segun el valor de 'sentence', reemplazando $team$ por el nombre del equipo y $team1$-$team2$ por el nombre de cada equipo
        print(COMMENT_SENTENCES[sentence].replace('$team$', teams[inc]).replace('$team1$', teams[0]).replace('$team2$', teams[1]))
        
        sleep(1)

# Obtener ganador
def getWinner():
    if points[-1][0] > points[-1][1]:
        return 0
    else:
        return 1

# MAIN CODE # 
teams  = getTeams() # Obtenemos equipos
points = getPoints() # Obtenemos puntos
winner = getWinner() # Obtenemos el ganador

# Si algo falla, que muestre un error generico
if len(teams) != 2 or len(points) == 1: displayError()

commentPlay() # Comentamos el partido

# Hacemos el print final con el ganador y sus puntos
print('El equipo {} ha ganado con {} puntos!'.format(teams[winner], points[-1][winner]))

# XOR #
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0
# Como un OR pero solo devuelve verdadero cuando solo uno de los dos valores es verdadero