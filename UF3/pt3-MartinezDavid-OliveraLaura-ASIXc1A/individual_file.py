import config, mix_content

def get_data():
    return mix_content.mix_file_content(config.INPUT_FILE, config.INPUT_FILE)