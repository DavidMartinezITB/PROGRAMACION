import RGBRectangles

def main():
    data = []
    input = RGBRectangles.getInputFromKeyboard()
    while input != 'e':
        if input != []:
            data.append(input)
        input = RGBRectangles.getInputFromKeyboard()
    for i in data:
        RGBRectangles.displayRectangle(i[0], i[1], i[2])

if __name__ == '__main__':
    main()