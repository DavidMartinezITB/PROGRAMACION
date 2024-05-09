import kernel

if __name__ == '__main__':
    try:
        print(kernel.readIntListFromKeyboard())
    except Exception as e:
        print('Error: {}'.format(e))