chart = [ [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0] ]
rows_r = 5
cols_r = 6

def desplay():
    for row in chart:
        for i in row:
            print(i, end = ' ')
        print()
    print("- - - - - - -")
    print("1 2 3 4 5 6 7")

def getRow(colum):
    if chart[5][colum] == 0:
        return 5
    elif chart[4][colum] == 0:
        return 4
    elif chart[3][colum] == 0:
        return 3
    elif chart[2][colum] == 0:
        return 2
    elif chart[1][colum] == 0:
        return 1
    elif chart[0][colum] == 0:
        return 0
    else:
        return -1

def checkWinHor():
    row_num = -1
    for row in chart:
        row_num = row_num + 1
        #print(row_num)
        old_num = 3
        count = 0
        for num in row:
            #print(num)
            if num == old_num and old_num != 0: 
                count += 1
                print("one")
                if count == 3:
                    print(str(num) + " wins!")
                    return True
            else:
                old_num = num
                count = 0
                #print("no")

#def checkWinVer():
    #row_num = -1
    #old_num = "#"
    
    #for row in chart:
     #   row_num = row_num + 1
        #print(row_num)
      #  count = 0
       # num = chart[row[0]]
        #if num == old_num and old_num != 0: 
         #   count += 1
          #  print("one")
           # if count == 3:
            #    print(str(num) + " wins!")
             #   return True
        #else:
         #   old_num = num
          #  count = 0
            #print("no")
def checkWinVer(sym):
        for i in range(cols_r):
            for r in range(rows_r):
                if r > 2 and r < 4:
                    e = 3
                elif r > 3 and r < 5:
                    e = 4
                elif r > 4 and r < 6:
                    e = 5
                else:
                    e = 0
                if r < 2:
                    continue
                elif chart[e - 1[i]] == sym and chart[e - 2[i]] == sym and chart[e - 3[i]] == sym:
                    return True

def checkWinDi():
    col = 1
    row = 1
    count = 0
    
def checkWin():
    if checkWinHor() or checkWinVer("#") or checkWinVer("!"):
        return True

def move(color):
    desplay()
    if checkWin():
        print("hi")
        return
    colum = (int(input("What is your colum " + color + " ?")) - 1)
    #colum = int(colum) - 1
    row = getRow(colum)
    if row == -1:
        print("ILLEGAL MOVE! TRY AGAIN")
        return move(color)
    else:
        chart[row][colum] = color
        move("#" if (color == "!") else "!")

move("#")