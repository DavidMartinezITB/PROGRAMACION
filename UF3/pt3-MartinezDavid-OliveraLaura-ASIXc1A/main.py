"""
David Martinez y Laura Olivera 
ASIXc1A
UF3 Projecte Paraules Boges
R3
- Procesa el contenido de un archivo de entrada
- Procesa el contenido de n archivos en un directorio (recursivo)
- Mide el tiempo de ejecucion de inicio a fin
"""

import utils, data_source, write_words, logger, config, time, individual_file, crazy_words

def main():
    start=time.time()
    logger.iniLog()
    puede_empezar= utils.check_folders(config.LOG_DIRECTORY, config.DIRECTORI_ENTRADA, config.DIRECTORI_SORTIDA)
    
    contingut_fitxer = individual_file.get_data()

    if contingut_fitxer:
        write_words.write_output(crazy_words.crazy_text(contingut_fitxer))
    else:
        logger.error(f"CAN'T START INDIVIDUAL FILE PROCESS: Not able to read {config.INPUT_FILE} content")
    
    if puede_empezar:
        contingut_directori = data_source.get_dir_content(config.DIRECTORI_ENTRADA)

        if contingut_directori:
            write_words.write_mixed_content(contingut_directori)
        else:
            logger.error("Not able to read directory content")
    logger.info(f'Program ended. TIME ELAPSED: {utils.calculate_time(start)} ({round((time.time() - start) * 1000)}ms)')

if __name__ == '__main__':

    main()
