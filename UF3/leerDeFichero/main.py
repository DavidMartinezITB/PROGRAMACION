import config, logger, get_data, write_data

def main():
    cfg = config.getConfigFromJson()
    logger.init(cfg['logs']['logFormat'], cfg['logs']['logFile'], cfg['logs']['logMode'])
    words = get_data.getDataFromFile(cfg['input']['fileName'])
    write_data.writeInFile(cfg['output']['fileName'], words)
    print('cleaned')
    words = get_data.cleanLines(words)
    print(words)
    print('formated')
    words = get_data.formatLines(words)
    print(words)

if __name__ == '__main__':
    main()