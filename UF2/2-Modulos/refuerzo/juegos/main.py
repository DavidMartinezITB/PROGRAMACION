import utils

def main():
    opt = ''
    while opt != '5':
        opt = utils.menu()
        utils.whatToPlay(opt)
        input()

if __name__ == '__main__':
    main()