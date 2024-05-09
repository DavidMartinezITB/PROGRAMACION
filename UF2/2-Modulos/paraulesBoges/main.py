"""
David Martinez - Laura Olivera
ASIXc1A - M03 UF2
Projecte - Paraules boges - Release 1
Descripcio:
L'usuari introdueix una frase (minim d'una paraula) i el programa te que retornar la mateixa frase pero
"randomitzant" els caracters de totes les frases exceptuant el primer i l'ultim.

En aquest release l'hem fet modular:
    - crazy_words.py - Funcions de la fase de procesament de dades
    - data_source.py - Funcions de la fase d'obtencio de dades
    - main.py        - Fitxer principal del projecte
    - utils.py       - Funcions varies (validacio de text i errors)

Cal instalar el modul de openai (pip install openai)
Cal afegir les API Key a les constants del fitxer data_source.py
"""
import data_source, crazy_words

def main():
    text = data_source.get_data()

    if text:
        print(crazy_words.crazy_text(text))

if __name__ == '__main__':
    main()  