import logging, config, os

def debug(msg=''):
    logging.debug(msg)
def info(msg=''):
    logging.info(msg)

def error(msg='Error generico'):
    logging.error(msg)

def warning(msg='Warning generico'):
    logging.warning(msg)

def iniLog():
    if config.LOG_DIRECTORY not in os.listdir('.'):
        os.mkdir(config.LOG_DIRECTORY)
    logging.basicConfig(level=logging.DEBUG,format=config.LOG_FORMAT,filename=config.LOG_PATH,filemode=config.LOG_MODE)
    info('======================================================')