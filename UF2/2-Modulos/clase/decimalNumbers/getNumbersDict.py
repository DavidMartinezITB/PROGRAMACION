
def printNumbers(numbers):
    RAW = """  
   ###       #      #####    #####   #     #  #######   #####   #######   #####    #####           
  #   #     ##     #     #  #     #  #     #  #        #             #   #     #  #     #          
 #     #     #           #       ##  #     #  #####    #####        #     #####    ######  ####### 
 #     #     #      #####         #  #######       #   #     #     #     #     #        #          
  #   #      #     #        #     #        #  #     #  #     #    #      #     #  #     #          
   ###    #######  #######   #####         #   #####    #####     #       #####    #####           """
    

    NUM_LEN = 9

    print(RAW)

    # for num in numbers:
    #     pos = [0, 0]
    #     pos[0] = int(int(num) * NUM_LEN) - 1
    #     pos[1] = int(pos[0] + 9) - 1
    #     print(pos[0], pos[1])
    #     print(RAW[pos[0]:pos[1]], end='a\n')
        # for i in RAW.split('\n')[1:]:
            # print()
            # print(i[pos[0], pos[1]])

    # for i in RAW.split('\n')[1:]:
        # i = RAW.split('\n')[-1]
        # print(len(i))
        # for j in range(0, len(i), NUM_LEN):
        #     # print(j)
        #     print(i[j:j+NUM_LEN], end='')
        # print()

printNumbers('1234')