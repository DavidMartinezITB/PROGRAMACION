"""
    # David Martinez - ASIXc1A
    # 23/10/2023
    # M03 UF1 - Manipulacion de datos
    # Descripcion: Introduim el mes (1-12) y printem els dies que te (2023)
"""

mes = input()

match mes:
    case "1" | "3" | "5" | "7" | "8" | "10" | "12": print(31)
    case "4" | "6" | "9" | "11": print(30)
    case "2": print(28)
    case _: print("Mes no valid!")