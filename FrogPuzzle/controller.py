from math import floor
class Controller:
    def __init__(self, app):
        print("CONSTRUCTING CONTROLLER")
        self.app = app

    def detectClick(self):
        click = self.app.win.getMouse()
        row = self.getRow(click.y)
        col = self.getCol(click.x)
        #print(row)
        #print(col)
        if(  
            click.y - (row * 100) 
                <=
            click.x - (col * 100) 
        ):
            positive = 1
        elif(  
            click.y - (row * 100) 
                >=
            click.x - (col * 100)
        ):
            positive = 0
        else:
            positive = 2
        if( 
            click.y - ( (row + 1) * 100 )
                <= -(  
            click.x - ( col * 100 )  
                ) 
         ):
            negitive =  1
        elif(  
            click.y - ( (row + 1) * 100 ) 
                >= -(  
            click.x - ( col * 100 )  
                ) 
        ):
            negitive = 0
        else:
            negitive = 2
        print(positive)
        print(negitive)
        frog = self.app.model.frogs[row][col]
        numFrogDraw = self.app.model.numFrogDraw
        numFrogs = self.app.model.numFrog
        if(
            (positive == 1)
                and
            (negitive == 1)
        ):
            print("up")
            if (self.cant(row, col, -1 ,0) == False):
                return
            frog.move(-1, 0)
            numFrogs[row - 1][col] += 1
            numFrogDraw[row - 1][col].setText(numFrogs[row - 1][col])

        elif(
            (positive == 0)
                and
            (negitive == 0)
        ):
            print("down")
            if (self.cant(row, col, 1 ,0) == False):
                return
            frog.move(1, 0)
            numFrogs[row + 1][col] += 1
            numFrogDraw[row + 1][col].setText(numFrogs[row + 1][col])

        elif(
            (positive == 1)
                and
            (negitive == 0)
        ):
            print("right")
            if (self.cant(row, col, 0 ,1) == False):
                return
            frog.move(0, 1)
            numFrogs[row][col + 1] += 1
            numFrogDraw[row][col + 1].setText(numFrogs[row][col + 1])

        elif(
            (positive == 0)
                and
            (negitive == 1)
        ):
            print("left")
            if (self.cant(row, col, 0, -1) == False):
                return
            frog.move(0, -1)
            numFrogs[row][col - 1] += 1
            numFrogDraw[row][col - 1].setText(numFrogs[row][col - 1])
        numFrogs[row][col] -= 1
        numFrogDraw[row][col].setText(numFrogs[row][col])
        self.app.model.frogMove[row][col] = True
        return

    def getRow(self, pointy):
        return floor(pointy / (self.app.win.height / 5))

    def getCol(self, pointx):
        return floor(pointx / (self.app.win.width / 5))

    def cant(self, row, col, moveRow, moveCol):
        numFrogs = self.app.model.numFrog
        if (
                (
                    row == 0 
                        and
                    moveRow == -1
                )
                    or
                (   
                    row == 4
                        and
                    moveRow == 1
                )
                    or
                (
                    col == 0
                        and
                    moveCol == -1
                )
                    or
                (
                    col == 4
                        and 
                    moveCol == 1
                )
                    or 
                (
                    numFrogs[row][col] == 0
                )
                    or
                (
                    self.app.model.frogMove[row][col] == True
                )
            ):
            return False
        else:
            return True

    def finalize(self):
        print("Finalize CONTROLLER")

    def initialize(self):
        print("INITIALIZING CONTROLLER")

    def run(self):
        #print("RUNNING CONTROLLER")
        self.detectClick()