import collections
import random
import os

def Guess(correct_word, wrong):
    arr = list(correct_word)
    dict = {}
    guesses = 0
    corr = 0
    while guesses < wrong:
        if corr == len(arr):
            print("You have won!!!!")
            break
        else:
            if wrong - guesses > 1:
                print("You have " + str(wrong - guesses) + " guesses left!")
            else:
                print("You have 1 guess left!")
        x = input("Guess: ")
        if x in arr:
            index = arr.index(x)
            dict[index] = x
            od = collections.OrderedDict(sorted(dict.items()))
            print("Guessed correctly!") 
            for k,v in od.items():
                print(str(k) + ": " +str(v))
            corr +=1
        elif len(list(x)) > 1:
            print("Guess can't be more than one letter, guess again")
        else:
            print("Wrong guess!")
            guesses+=1
    if guesses == wrong:
        print("You lost, you suck")

def tic():
    table = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    def go(z,lst):
        for i in range(0,2):
            if i == 0:
                print("-"*225)
                print("")
                print("                                   "*3, end="")
                print("x: ")
                print("")
            elif i == 1:
                print("-"*225)
                print("                                   "*3, end="")
                print("y: ")
            ele = int(input(""))

            print("-"*225)
            lst.append(ele)

    def printBoard():
        os.system('clear')
        print("-"*225)
        print("")
        print("")
        print("                                   "*3, end="")
        print(table[0])
        print("                                   "*3, end="")
        print(table[1])
        print("                                   "*3, end="")
        print(table[2])
        print("")
        print("")
        print("-"*225)
        print("")
        print("")

    def checkWin():
        if table[0][0] == table[0][1] == table[0][2] != "0":
            return True
        elif table[0][0] == table[1][1] == table[2][2] !="0":
            return True
        elif table[0][2] == table[1][1] == table[2][0] !="0":
            return True
        elif table[1][0] == table[1][1] == table[1][2] !="0":
            return True
        elif table[2][0] == table[2][1] == table[2][2] !="0":
            return True
        elif table[0][0] == table[1][0] == table[2][0] !="0":
            return True
        elif table[0][1] == table[1][1] == table[2][1] !="0":
            return True
        elif table[0][2] == table[1][2] == table[2][2] !="0":
            return True
        else:
            return False



    def AI(i,o):
        
        def AITurn(i,o):

            arr1 = [
                [0,1],
                [1,0],
                [1,2],
                [2,1]
            ]
            arr2 = [
                [0,0],
                [0,2],
                [2,0],
                [2,2]
            ]
            n = 0
            m = 0
            
                   

            if i == 0:
                table[random.randint(0,2)][random.rand(0,2)] = "o"
            
            elif i == o+1:
                
                
                running = True
                while running:
                    cool = False 
                    while n < 2:
                        while m < 2:
                            if table[n][m] == table[n][m-1] != "0" and table[n][0] == "0":
                                if m == 1:
                                    table[n][0] = 'o'
                                    cool = True
                                    printBoard()
                                    o+=1
                                    break
                                else:
                                    table[n][m+1] = 'o'
                                    cool = True
                                    printBoard()
                                    o+=1
                                    break
                            elif table[n][m] == table[n-1][m] !="0" and table[0][m] =="0":
                                if n == 1:
                                    table[0][m] = 'o'
                                    cool = True
                                    printBoard()
                                    o+=1
                                    break
                                else:
                                    table[n+1][m] = 'o'
                                    cool = True
                                    printBoard()
                                    o+=1
                                    break
                            m +=1
                        if cool:
                            running = False
                            break
                        n +=1
                    if random.randint(0,10) > 6:
                        if table[0][0] == table[2][2] !="0" and table[2][0] =="0":
                            table[2][0] = 'o'
                            printBoard()
                            o+=1
                            break
                        elif table[0][0] == table[2][2] !="0" and table[2][0] !="0" and table[0][2] == "0":
                            table[0][2] = 'o'
                            printBoard()
                            o+=1
                            break
                    else:
                        l = 0
                        som = False
                        while l <2:
                            if table[0][l] == table[2][l] !="0" and table[1][l] =="0":
                                table[1][l] = 'o'
                                som = True
                                printBoard()
                                o+=1
                                break
                            elif table[l][0] == table[l][2] != "0" and table[l][1] == "0":
                                table[l][1] = 'o'
                                som = True
                                printBoard()
                                o+=1
                                break
                            elif table[0][0] == table[2][2] !="0" and table[1][1] == "0" or table[0][2] == table[2][0] !="0" and table[1][1] == "0":
                                table[1][1] = 'o'
                                som =True
                                printBoard()
                                o+=1
                                break
                            l+=1

                        if som:
                            break

                     

                    m = random.randint(0,1)
                    n = random.randint(0,3)
                    z = arr1[n]
                    if table[z[0]][z[1]] == "0":
                        table[z[0]][z[1]] = 'o'
                        printBoard()
                        o +=1
                        break
                    else: 
                        y = arr2[n]
                        if table[y[0]][y[1]] == "0":
                            table[y[0]][y[1]] = 'o'
                            printBoard()
                            o+=1
                            break 

        while True:
            if checkWin():
                if i == o+1:
                    print("You won!")
                    break
                elif i == o:
                    print("The computer won")
                    break
                else:
                    print("Somethings not working")
            elif not checkWin() and i == 5:
                print("draw")
            if i == o:
                print("x's go: ")
                lst = []
                go(x,lst)
                if table[lst[0]][lst[1]] == "0":
                    table[lst[0]][lst[1]] = "x"
                    o+=1
                    break
                else:
                    print(str(table[lst[0]][lst[1]]) + " is already in the spot! Go again...")
            if i == o + 1:
                AITurn(i,o)
                o+=1

    x = 0
    o = 0
    running = True
    printBoard()
    while running:
        if checkWin():
            if x == o:
                print("                                   "*3, end="")
                print("o won!")
            else:
                print("                                   "*3, end="")
                print("x won!")
            break
        

        if x == 5:
            break

        if x == o:
            print("                                   "*3, end="")
            print("x's go: ")
            lst= []
            go(x,lst)
            table[lst[0]][lst[1]] = "x"
            x+=1
        elif not checkWin() and x == 5:
            print("                                   "*3, end="")
            print("draw")
        elif x == o + 1:
            print("                                   "*3, end="")
            print("o's go: ")
            lst = []
            go(o,lst) 
            table[lst[0]][lst[1]] = "o"
            o +=1
            #AI(x,o)
        else:
            print("                                   "*3, end="")
            print("Somethings gone wrong...")
        printBoard()



if __name__ == '__main__':
    tic()
