from time import sleep

h, m, s = 0,0,0
try:
    targetH, targetM, targetS = int(input('Horas: ')), int(input('Minuts: ')), int(input('Segons: '))

    if targetH in range(24):
        if targetM in range(60):
            if targetS in range(60):
                while h != targetH or m != targetM or s != targetS + 1:
                    # Formateamos para que siempre sean dos digitos
                    sH, sM, sS = h, m, s
                    if len(str(h)) == 1: sH = '0' + str(h)
                    if len(str(m)) == 1: sM = '0' + str(m)
                    if len(str(s)) == 1: sS = '0' + str(s)
                    
                    # Hacemos el print de hh:mm:ss
                    print("\033c") # Para limpiar terminal
                    print(f'{sH}:{sM}:{sS}')
                    
                    s += 1 # Incrementsmos el segundero

                    # Logica para saltar al siguiente minuto y a la siguiente hora 
                    if s >= 60:
                        s = 0
                        m += 1
                        if m >= 60:
                            s = 0
                            m = 0
                            h += 1
                    
                    # Una vez acabe toda la logica del while, esperamos un segundo
                    sleep(1)
            else: print('Segundos mal')
        else: print('Minutos mal')
    else: print('Horas mal')
except ValueError:
    print('NO SON ENTEROS!')