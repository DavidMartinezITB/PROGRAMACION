import os, time, logger

#region ######## VALIDATION ########
def is_mail(text):
    """
    Returns True if the string is a mail\n
    is_mail(string) -> bool
    """
    return '@' in text and '.' in text
        
def has_number(text):
    """
    Returns True if the string has a number\n
    word_has_number(string) -> bool
    """
    for char in text:
        if char.isdigit():
            return True

def is_url_or_filename(text):
    """
    Returns True if the string is an URL or filename\n
    is_url(string) -> bool
    """
    return '.' in text or '/' in text or '\\' in text 

#endregion

#region ########## ERRORS ##########

def check_folders(LOG_DIRECTORY, DIRECTORI_ENTRADA, DIRECTORI_SORTIDA):
    directoris= os.listdir('.')
    if DIRECTORI_ENTRADA not in directoris:
        logger.error("CAN'T START DIRECTORY LISTING: Not able to find input directory")
        return
    elif DIRECTORI_SORTIDA not in directoris:
        logger.warning("Not able to find output directory. Creating...")
        os.mkdir(DIRECTORI_SORTIDA)
    return True

start= time.time()
def calculate_time(start):
    elapsed_time = time.time() - start
    days = 0
    if elapsed_time >= 86400:
        days = int(elapsed_time / 86400)
    elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - start))
    total=f"{days}:{elapsed}"

    return total

calculate_time(start)
