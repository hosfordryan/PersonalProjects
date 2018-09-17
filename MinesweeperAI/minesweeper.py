from random import randint
import os
import time
import msvcrt



BOARDSIZE = 30
NUM_BOMBS = 150
win = False
lose = False

AISolve = False
AiFirstMoves = True

attempt = 0

xLoc = 0
yLoc = 0

startTime = 0

class Square:
    bomb = False
    count = 0
    hidden = True
    flag = False
    selected = False
    checked = False

    def __init__(self):
        self.bomb = False
    def display(self):
        if self.selected == True:
            return "+"
        elif self.flag == True:
            return "F"
        elif self.hidden == True:
            return " "
        elif self.bomb == True:
            return "*"
        else:
            return "{}".format(self.count)

    def toggleFlag(self):
        if self.flag == False:
            self.flag = True
        else:
            self.flag = False


def buildBoard(size):
    board = [[Square() for x in range(size)] for x in range(size)]
    return board


def displayBoard(gameBoard):
    os.system('cls')
    for i in range(len(gameBoard)):
        toPrint = ""
        for j in range(len(gameBoard[i])):
            toPrint += gameBoard[i][j].display() + "|"
        print(toPrint)


def checkBomb(x,y,gameBoard):
    if gameBoard[y][x].bomb == True:
        return True


def placeBombs(numBombs, gameBoard):
    for i in range(numBombs):
        randX = randint(0,len(gameBoard) -1 )
        randY = randint(0,len(gameBoard) -1 )
        while checkBomb(randX,randY,gameBoard) is True:
            randX = randint(0,len(gameBoard) -1 )
            randY = randint(0,len(gameBoard) -1 )
        gameBoard[randY][randX].bomb = True
        gameBoard[randY][randX].hidden = True                  # Temporary. For debugging
        #gameBoard[randY][randX].flag = True


def getBombCount(y,x,gameBoard):
    count = 0
    if y > 0:
        if gameBoard[y-1][x].bomb == True:
            count+=1
    if y < BOARDSIZE -1:
        if gameBoard[y+1][x].bomb == True:
            count+=1
    if x >0:
        if gameBoard[y][x-1].bomb == True:
            count+=1
    if x < BOARDSIZE-1:
        if gameBoard[y][x+1].bomb == True:
            count+=1
    if y > 0 and x > 0:
        if gameBoard[y-1][x-1].bomb == True:
            count+=1
    if y > 0 and x < BOARDSIZE-1:
        if gameBoard[y-1][x+1].bomb == True:
            count+=1
    if y < BOARDSIZE-1 and x > 0:
        if gameBoard[y+1][x-1].bomb == True:
            count+=1
    if y < BOARDSIZE -1 and x < BOARDSIZE-1:
        if gameBoard[y+1][x+1].bomb == True:
            count+=1
    return count


def placeCounts(gameBoard):
    for y in range(len(gameBoard)):
        for x in range(len(gameBoard[y])):
            gameBoard[y][x].count = getBombCount(y,x,gameBoard)


def setup():
    print("Setup...")
    board = buildBoard(BOARDSIZE)
    displayBoard(board)
    print("\n\n")
    placeBombs(NUM_BOMBS,board)
    placeCounts(board)
    displayBoard(board)
    board[yLoc][xLoc].selected = True
    print("Done setting up...\n")
    return board


def checkNeighbor(gameBoard,y,x):
    if gameBoard[y][x].count != 0 or gameBoard[y][x].bomb== True or gameBoard[y][x].flag==True or gameBoard[y][x].checked==True:
        if gameBoard[y][x].count != 0:
            gameBoard[y][x].hidden = False
        return
    else:
        gameBoard[y][x].hidden = False
        gameBoard[y][x].checked = True
        if(y>0):
            checkNeighbor(gameBoard,y-1,x)
        if(y<BOARDSIZE-1):
            checkNeighbor(gameBoard,y+1,x)
        if(x<BOARDSIZE-1):
            checkNeighbor(gameBoard,y,x+1)
        if(x>0):
            checkNeighbor(gameBoard,y,x-1)
        if y>0 and x < BOARDSIZE-1:
            checkNeighbor(gameBoard,y-1,x+1)
        if y>0 and x>0:
            checkNeighbor(gameBoard,y-1,x-1)
        if y<BOARDSIZE-1 and x < BOARDSIZE-1:
            checkNeighbor(gameBoard,y+1,x+1)
        if y<BOARDSIZE-1 and x > 0:
            checkNeighbor(gameBoard,y+1,x-1)



def pick(y,x,gameBoard):
    global startTime
    if gameBoard[y][x].bomb == True:
        timeTaken = time.clock() - startTime
        if timeTaken > 1.5:
            os.system('cls')
            print("Bomb hit. You lose.")
            print("Time taken: {0:.2f} seconds.".format(timeTaken))
            input("Press enter to quit.")
            quit()
        else:
            main()
    else:
        gameBoard[y][x].hidden= False
        checkNeighbor(gameBoard,y,x)


def checkwin(gameBoard):
    for y in range(len(gameBoard)):
        for x in range(len(gameBoard[y])):
            if gameBoard[y][x].bomb== False and gameBoard[y][x].hidden == True:
                return False
    return True


def play(gameBoard):
    global xLoc, yLoc, win
    displayBoard(gameBoard)
    print("Move-wasd\tselect-space\tflag-f\tquit-q")
    direction = msvcrt.getch().decode()
    if direction.upper() == 'F':
        gameBoard[yLoc][xLoc].toggleFlag()
    elif direction.upper() == 'W':
        if yLoc > 0:
            gameBoard[yLoc][xLoc].selected=False
            yLoc-= 1
            gameBoard[yLoc][xLoc].selected=True
    elif direction.upper() == 'S':
        if yLoc < BOARDSIZE-1:
            gameBoard[yLoc][xLoc].selected=False
            yLoc+= 1
            gameBoard[yLoc][xLoc].selected = True
    elif direction.upper() == 'A':
        if xLoc > 0:
            gameBoard[yLoc][xLoc].selected=False
            xLoc -= 1
            gameBoard[yLoc][xLoc].selected = True
    elif direction.upper() == 'D':
        if xLoc < BOARDSIZE-1:
            gameBoard[yLoc][xLoc].selected=False
            xLoc += 1
            gameBoard[yLoc][xLoc].selected = True
    elif direction.upper() == ' ':
        pick(yLoc,xLoc,gameBoard)
    elif direction.upper() == 'Q':
        exit()
    return gameBoard

def isFirstMove(gameBoard):
    global AiFirstMoves
    revealedCount = 0
    for y in range(len(gameBoard)):
        for x in range(len(gameBoard[y])):
            if gameBoard[y][x].hidden == False:
                revealedCount += 1

    if revealedCount > 20:
        AiFirstMoves = False


def getNumHiddenNeighbors(y,x,gameBoard):
    count = 0
    if(y>0):
        if gameBoard[y-1][x].hidden == True:
            count += 1
    if(y<BOARDSIZE-1):
        if gameBoard[y+1][x].hidden == True:
            count += 1
    if(x<BOARDSIZE-1):
        if gameBoard[y][x+1].hidden == True:
            count += 1
    if(x>0):
        if gameBoard[y][x-1].hidden == True:
            count += 1
    if y>0 and x < BOARDSIZE-1:
        if gameBoard[y-1][x+1].hidden == True:
            count += 1
    if y>0 and x>0:
        if gameBoard[y-1][x-1].hidden == True:
            count += 1
    if y<BOARDSIZE-1 and x < BOARDSIZE-1:
        if gameBoard[y+1][x+1].hidden == True:
            count += 1
    if y<BOARDSIZE-1 and x > 0:
        if gameBoard[y+1][x-1].hidden == True:
            count += 1
    return count


def pickHiddenNeighbors(y,x,gameBoard):
    curx = y
    cury = x
    if(y>0):
        if gameBoard[y-1][x].hidden == True and gameBoard[y-1][x].flag == False:
            print("up")
            gameBoard[cury][curx].selected = False
            cury=y-1
            curx=x
            gameBoard[cury][curx].selected = True
            pick(y-1,x,gameBoard)
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if(y<BOARDSIZE-1):
        if gameBoard[y+1][x].hidden == True and gameBoard[y+1][x].flag == False:
            print("down")
            gameBoard[cury][curx].selected = False
            cury = y+1
            curx=x
            gameBoard[cury][curx].selected = True
            pick(y+1,x,gameBoard)
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if(x<BOARDSIZE-1):
        if gameBoard[y][x+1].hidden == True and gameBoard[y][x+1].flag == False:
            print("right")
            gameBoard[cury][curx].selected = False
            cury = y
            curx=x+1
            gameBoard[cury][curx].selected = True
            pick(y,x+1,gameBoard)
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if(x>0):
        if gameBoard[y][x-1].hidden == True and gameBoard[y][x-1].flag == False:
            print("left")
            gameBoard[cury][curx].selected = False
            cury = y
            curx=x-1
            gameBoard[cury][curx].selected = True
            pick(y,x-1,gameBoard)
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if y>0 and x < BOARDSIZE-1:
        if gameBoard[y-1][x+1].hidden == True and gameBoard[y-1][x+1].flag == False:
            print("top right")
            gameBoard[cury][curx].selected = False
            cury = y-1
            curx=x+1
            gameBoard[cury][curx].selected = True
            pick(y-1,x+1,gameBoard)
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if y>0 and x>0:
        if gameBoard[y-1][x-1].hidden == True and gameBoard[y-1][x-1].flag == False:
            print("top left")
            gameBoard[cury][curx].selected = False
            cury = y-1
            curx=x-1
            gameBoard[cury][curx].selected = True
            pick(y-1,x-1,gameBoard)
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if y<BOARDSIZE-1 and x < BOARDSIZE-1:
        if gameBoard[y+1][x+1].hidden == True and gameBoard[y+1][x+1].flag == False:
            print("bottom right")
            gameBoard[cury][curx].selected = False
            cury = y+1
            curx=x+1
            gameBoard[cury][curx].selected = True
            pick(y+1,x+1,gameBoard)
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if y<BOARDSIZE-1 and x > 0:
        if gameBoard[y+1][x-1].hidden == True and gameBoard[y+1][x-1].flag == False:
            print("bottom left")
            gameBoard[cury][curx].selected = False
            cury = y+1
            curx=x-1
            gameBoard[cury][curx].selected = True
            pick(y+1,x-1,gameBoard)
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    gameBoard[cury][curx].selected = False



def flagHiddenNeighbors(y,x,gameBoard):
    if(y>0):
        if gameBoard[y-1][x].hidden == True and gameBoard[y-1][x].flag == False:
            gameBoard[y-1][x].flag=True
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if(y<BOARDSIZE-1):
        if gameBoard[y+1][x].hidden == True and gameBoard[y+1][x].flag == False:
            gameBoard[y+1][x].flag=True
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if(x<BOARDSIZE-1):
        if gameBoard[y][x+1].hidden == True and gameBoard[y][x+1].flag == False:
            gameBoard[y][x+1].flag=True
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if(x>0):
        if gameBoard[y][x-1].hidden == True and gameBoard[y][x-1].flag == False:
            gameBoard[y][x-1].flag=True
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if y>0 and x < BOARDSIZE-1:
        if gameBoard[y-1][x+1].hidden == True and gameBoard[y-1][x+1].flag == False:
            gameBoard[y-1][x+1].flag=True
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if y>0 and x>0:
        if gameBoard[y-1][x-1].hidden == True and gameBoard[y-1][x-1].flag == False:
            gameBoard[y-1][x-1].flag=True
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if y<BOARDSIZE-1 and x < BOARDSIZE-1:
        if gameBoard[y+1][x+1].hidden == True and gameBoard[y+1][x+1].flag == False:
            gameBoard[y+1][x+1].flag=True
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")
    if y<BOARDSIZE-1 and x > 0:
        if gameBoard[y+1][x-1].hidden == True and gameBoard[y+1][x-1].flag == False:
            gameBoard[y+1][x-1].flag=True
            displayBoard(gameBoard)
            #time.sleep(0.3)     # So you can see what AI is doing
            #input("Enter to continue")


def getNumFlagNeighbors(y,x,gameBoard):
    count = 0
    if(y>0):
        if gameBoard[y-1][x].flag == True:
            count += 1
    if(y<BOARDSIZE-1):
        if gameBoard[y+1][x].flag == True:
            count += 1
    if(x<BOARDSIZE-1):
        if gameBoard[y][x+1].flag == True:
            count += 1
    if(x>0):
        if gameBoard[y][x-1].flag == True:
            count += 1
    if y>0 and x < BOARDSIZE-1:
        if gameBoard[y-1][x+1].flag == True:
            count += 1
    if y>0 and x>0:
        if gameBoard[y-1][x-1].flag == True:
            count += 1
    if y<BOARDSIZE-1 and x < BOARDSIZE-1:
        if gameBoard[y+1][x+1].flag == True:
            count += 1
    if y<BOARDSIZE-1 and x > 0:
        if gameBoard[y+1][x-1].flag == True:
            count += 1
    return count


def flagRandom(y,x,gameBoard,numHidden):
    options =  [Square() for i in range(numHidden)]
    randNum = randint(1,numHidden)
    print("")
    count = 0
    if(y>0):
        if gameBoard[y-1][x].hidden == True and gameBoard[y-1][x].flag == False:
            options[count]=gameBoard[y-1][x]
            count+=1
    if(y<BOARDSIZE-1):
        if gameBoard[y+1][x].hidden == True and gameBoard[y+1][x].flag == False:
            options[count]=gameBoard[y+1][x]
            count+=1
    if(x<BOARDSIZE-1):
        if gameBoard[y][x+1].hidden == True and gameBoard[y][x+1].flag == False:
            options[count]=gameBoard[y][x+1]
            count+=1
    if(x>0):
        if gameBoard[y][x-1].hidden == True and gameBoard[y][x-1].flag == False:
            options[count]=gameBoard[y][x-1]
            count+=1
    if y>0 and x < BOARDSIZE-1:
        if gameBoard[y-1][x+1].hidden == True and gameBoard[y-1][x+1].flag == False:
            options[count]=gameBoard[y-1][x+1]
            count+=1
    if y>0 and x>0:
        if gameBoard[y-1][x-1].hidden == True and gameBoard[y-1][x-1].flag == False:
            options[count]=gameBoard[y-1][x-1]
            count+=1
    if y<BOARDSIZE-1 and x < BOARDSIZE-1:
        if gameBoard[y+1][x+1].hidden == True and gameBoard[y+1][x+1].flag == False:
            options[count]=gameBoard[y+1][x+1]
            count+=1
    if y<BOARDSIZE-1 and x > 0:
        if gameBoard[y+1][x-1].hidden == True and gameBoard[y+1][x-1].flag == False:
            options[count]=gameBoard[y+1][x-1]
            count+=1

    options[randNum-1].flag = True
    displayBoard(gameBoard)



def AIPlay(gameBoard):
    global xLoc, yLoc, AiFirstMoves, attempt
    displayBoard(gameBoard)

    # Check if this is first move. If so, pick random value in the middle for best chances
    if AiFirstMoves == True:
        isFirstMove(gameBoard)
        lowerBound = 0
        upperBound = BOARDSIZE-1
        randX = randint(lowerBound,upperBound)
        randY = randint(lowerBound,upperBound)
        pick(randY,randX,gameBoard)
    else:
        for y in range(len(gameBoard)):
            for x in range(len(gameBoard[y])):
                if gameBoard[y][x].hidden == False:
                    #print("y: {} x: {}".format(y,x))
                    #print("count: {} numHidden: {}".format(gameBoard[y][x].count,getNumHiddenNeighbors(y,x,gameBoard)))
                    if gameBoard[y][x].count == getNumFlagNeighbors(y,x,gameBoard) and gameBoard[y][x].count != 0 and getNumHiddenNeighbors(y,x,gameBoard) > getNumFlagNeighbors(y,x,gameBoard):
                        pickHiddenNeighbors(y,x,gameBoard)
                        attempt = 0
                        #return gameBoard
                    if gameBoard[y][x].count == getNumHiddenNeighbors(y,x,gameBoard) and gameBoard[y][x].count != 0 and gameBoard[y][x].count != getNumFlagNeighbors(y,x,gameBoard):
                        flagHiddenNeighbors(y,x,gameBoard)
                        attempt = 0
                        #return gameBoard
                    elif gameBoard[y][x].count > getNumFlagNeighbors(y,x,gameBoard) and (gameBoard[y][x].count - getNumFlagNeighbors(y,x,gameBoard)) < getNumHiddenNeighbors(y,x,gameBoard) and attempt > 4:
                        numHidden = getNumHiddenNeighbors(y,x,gameBoard)
                        print("Guessing!")
                        time.sleep(10)
                        flagRandom(y,x,gameBoard,numHidden)
                        #time.sleep(1)
                        attempt = 0
                        #return gameBoard
        attempt += 1






    return gameBoard

def main():
    global win, lose, startTime, AISolve, AiFirstMoves, attempt,xLoc,yLoc
    win = False
    lose = False

    AISolve = False
    AiFirstMoves = True

    attempt = 0

    xLoc = 0
    yLoc = 0
    AiString = input("AI Solve? (Y/N)")
    if AiString.upper() == "Y":
        AISolve = True
    startTime = time.clock()
    board = setup()
    count = 0
    while win == False and lose == False:
        print("Game loop")
        if AISolve == False:
            board = play(board)
        else:
            board = AIPlay(board)
            print("Made it through a loop")
        if checkwin(board) == True:
            os.system('cls')
            print("Winner!")
            timeTaken = time.clock() - startTime
            print("Time taken: {0:.2f} seconds.".format(timeTaken))
            input("Press enter to exit.")
            win = True
        print(str(count))
        count += 1
        #time.sleep(1)


if __name__ == "__main__":
    main()
