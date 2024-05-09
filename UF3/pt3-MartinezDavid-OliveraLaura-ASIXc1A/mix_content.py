import os, crazy_words

def mix_file_content(ruta_fitxer_entrada, fitxer):
    # No se llega a ejecutar en segundo directorio
    # Solo pilla el primer directorio recursivo
    if os.path.isfile(ruta_fitxer_entrada) and fitxer.endswith('.txt'):
        with open(ruta_fitxer_entrada, mode='rt', encoding='utf-8') as f:
            contingut_boig=[]
            contingut_fitxer= f.readlines()

            for line in contingut_fitxer:
                linea_boja=crazy_words.crazy_text(line)
                contingut_boig.append(linea_boja)

            contingut_exit="".join([str(elem) for elem in contingut_boig])
            return contingut_exit
