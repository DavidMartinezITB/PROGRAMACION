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
def displayError(e):
    """
    Display an error\n
    Void string to generic error\n
    displayError(string) -> void\n
    Pass an exception message could break the code, use this func to display custom errors!
    """
    RED = '\033[31m'
    WHITE = '\033[0m'

    if e != '':
        print(RED + '[!] Error: ' + e + '!' + WHITE)
    else:
        print(RED + '[!] Error generic!' + WHITE)
#endregion