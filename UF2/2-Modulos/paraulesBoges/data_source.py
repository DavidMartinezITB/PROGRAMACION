#region ############ IMPORTS & CONSTANTS ############
import utils, openai, requests, json, config
#endregion

#region ################ FUNCTIONS ##################
def get_data_from_keyboard():
    """
    If the input has more than one word, returns it stripped\n
    get_text() - string
    """
    text = input().strip()
    if text == '':
        utils.displayError('You must specify minimum a word')
    else:
        return text

def get_data_from_server():
    """
    Query data from Quotes - API Ninjas (https://api-ninjas.com/api/quotes)
    """
    response = requests.get('https://api.api-ninjas.com/v1/quotes', headers={'X-Api-Key': config.NINJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        text = json.loads(response.text)
        print("{}: ".format(text[0]['author']), end='')
        return "\"{}\"".format(text[0]['quote'])
    utils.displayError("API Query error:\n    Status code: {}\n    Message: \t {}".format(response.status_code, response.text, response.text))
    return False

def get_data_from_chatGPT(words):
    """
    Return text in Catalan with N words passed as arg.
    get_data_from_chatGPT(string) -> string
    """

    try:
        # Put your API key here
        client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user", "content": "Dame un texto aleatorio en {} con {} palabras y que tenga sentido".format(config.CHATGPT_LANG, words)
            }]
        )
        return chat_completion.choices[0].message.content
    except openai.AuthenticationError:
        utils.displayError('Invalid API Key')
    except:
        utils.displayError('Error trying to query data from ChatGPT')

def get_data_from_file():
    """
    TODO
    """
    utils.displayError('Function not implemented')
    return False

def menu():
    """
    Display a menu and return the chossen option
    menu() -> string
    """
    MENU = 'PARAULES BOGES\n\nCom vols introduir les dades?\n [1] Per teclat\n [2] Des d\'un servidor (API Rest)\n [3] Amb ChatGPT\n [4] Des d\'un fitxer\n'

    print(MENU)
    return input('-> ')

def get_data():
    """
    Function returns data if no error. Otherwise returns False.
    """

    opt = menu()
    match opt:
        case '1':
            return get_data_from_keyboard()
        case '2':
            return get_data_from_server()
        case '3':
            try:
                words = int(input(' (text length) -> '))
                return get_data_from_chatGPT(words)
            except ValueError:
                utils.displayError('Solo numeros enteros')
        case '4':
            return get_data_from_file()
        case _:
            utils.displayError('Invalid option')
#endregion