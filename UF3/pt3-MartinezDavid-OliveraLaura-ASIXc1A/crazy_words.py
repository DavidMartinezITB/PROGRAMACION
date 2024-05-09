#region ############ IMPORTS & CONSTANTS ############
import random, string, utils

# Alphabet letters plus some special chars and numbers
LETTERS = string.ascii_letters + 'àèìòùÀÈÌÒÙâêîôûÂÊÎÔÛäëïöüÄËÏÖÜçÇáéíóúÁÉÍÓÚñÑ1234567890'
#endregion

#region ################ FUNCTIONS ##################
def randomize_string(text):
    """
    Returns a randomized version of a string (shuffled)\n
    randomize_string(string) -> string
    """
    char_list = list(text)
    random.shuffle(char_list)
    return "".join(char_list)

def get_positions(text):
    """
    If a string starts or ends with a bad chars sequence, returns the indexes where the non-containing badchars string starts and ends\n
    get_positions(string) -> tuple(2)\n

    Ej: ..potato..
        Returns 2 and 8 inside a tuple
    """
    # Position of the first and last char of the word
    positions = [0, len(text) - 1]
    
    # Iterathe through the string to find the bad chars amount at the beginning and end
    while text[positions[0]] not in LETTERS:
        positions[0] += 1

    while text[positions[1]] not in LETTERS:
        positions[1] -= 1
    
    # Correct the second position to point the char that ends the cleaned word
    positions[1] += 1

    return tuple(positions)

def crazy_text(text):
    """
    Returns a crazy version of the text: each word has all his chars shuffled excluding the first and the last\n
    crazy_text(string) -> string
    """
    
    crazy_words = ''
    for line in text.split('\n'):
        for word in line.split():
            try:
                positions = get_positions(word)
            except:
                positions = (0, len(word))
            # Get a cleaned version of the word to operate with
            cleaned_string = word[positions[0]:positions[1]]
            if len(cleaned_string) > 1 and not utils.is_mail(word) and not utils.has_number(cleaned_string) and not utils.is_url_or_filename(cleaned_string):
                # Randomize middle chars
                randomized = randomize_string(cleaned_string[1:-1])
                # Append the generated word to the finale string (beginning bad chars + first char + randomized + last char + end bad chars)
                crazy_words += f'{word[:positions[0]]}{cleaned_string[0]}{randomized}{cleaned_string[-1]}{word[positions[1]:]} '
            else:
                # Just ap   pend the word to finale text, if lenght is less than 4
                crazy_words += '{} '.format(word)
        crazy_words += '\n'
    return crazy_words[:-1]
#endregion