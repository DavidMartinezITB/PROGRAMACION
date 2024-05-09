def main():
    try:
        with open('Dragon.in', 'r') as inp:
            data = inp.read().replace('0', 'x')
    except:
        print('ERROR')

if __name__ == '__main__':
    main()