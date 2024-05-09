"""
    # David Martinez - ASIXc1A
    # 13/11/2023
    # M03 UF1 - Estructures de repeticio
    # Descripcion: 

    Programa per crear una serp Python a mida.

    Cal demanar quina mida (quantitat de COS) ha de tenir la serp. Tot seguit mostrar-la per pantalla. 

    Es valorarà el fet de que el cos faci siga sagues. Potser, la mida del cos ha de ser mínim 5
"""

"""
╚═(███)═╝

.╚═(███)═╝

..╚═(███)═╝

...╚═(███)═╝

...╚═(███)═╝

..╚═(███)═╝

.╚═(███)═╝

╚═(███)═╝
"""

CAP     = "....\...../...."
ULLS    = "...╚⊙ ⊙╝..."
COS     = "═(███)═"
CUA     = " ═V═ "

try:
    reps = int(input())
    if reps >= 5:
        print(CAP)
        print("  " + ULLS)

        c = 0
        crece = True
        for i in range(1, reps + 1):
            if c == 5:
                crece = False
            elif c == 1:
                crece = True
            
            if crece:
                c +=1
            else:
                c -=1

            print("   " + (" " * c) + COS)

            if i == reps:
                print("    " + (" " * c) + CUA)
    else:
        print('Debe ser igual o superior a 5!')

except:
    print('ERRORRRRRR')