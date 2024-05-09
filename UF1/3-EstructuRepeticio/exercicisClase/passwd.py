"""
    # David Martinez - ASIXc1A
    # 13/11/2023
    # M03 UF1 - Estructures de repeticio
    # Descripcion: 

    Pide contraseña (o contraseña SAT) y si se introduce acaba programa y te dice que has desbloqueado
    Si se pasa de los intentos, dice que se bloquea y acaba programa
"""

PWD = "asd"
SAT_PWD = '1234'
MAX_INTENTOS = 3

intentos = 0
clave = ''

if MAX_INTENTOS >= 1:
    while clave != PWD and clave != SAT_PWD and intentos < MAX_INTENTOS:
        clave = input('Dime la clave: ')
        if intentos >= MAX_INTENTOS:
            print(f'Lo has bloqueado - {MAX_INTENTOS}/{MAX_INTENTOS} intentos')
        elif clave == PWD or clave == SAT_PWD:
            print('Bienvenido!!!')
        else:
            print(f'Contraseña incorrecta - {intentos+1}/{MAX_INTENTOS} intentos')
        intentos += 1
else:
    print('El numero maximo de intentos debe ser mayor o igual a 1.')

print('Programa terminado')