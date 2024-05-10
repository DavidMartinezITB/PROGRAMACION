import logging

def debug(msg=''):
    logging.debug(msg)

def info(msg=''):
    logging.info(msg)

def error(msg='Error generico'):
    logging.error(msg)

def warning(msg='Warning generico'):
    logging.warning(msg)

def init(format, logFileName, mode):
    # if config.LOG_DIRECTORY not in os.listdir('.'):
    #     os.mkdir(config.LOG_DIRECTORY)
    logging.basicConfig(level=logging.DEBUG,format=format,filename=logFileName,filemode=mode)
    info('=========================== PROGRAM STARTED ===========================')