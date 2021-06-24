from graphics import *

class App:
    def __init__(self):
        self.win = GraphWin("TRT", 100, 100)
        self.isPlaying = True

        self.Launch()

    def Launch(self):
        self.initilize()
        self.run()
        self.finialize()

    def initilize(self):
        frog = Image(Point(50, 50), "frog.png")
        frog.draw(self.win)

    def run(self):
        self.isPlaying = True
        while(self.isPlaying == True):
            click = self.win.getMouse()
            if(click.y > click.x):
                positive = True
            elif(click.y < click.x):
                positive = False
            if(click.y > -click.x + 100):
                negitive = True
            elif(click.y < -click.x + 100):
                negitive = False
            if(
                (positive == True)
                    and
                (negitive == True)
            ):
                print("down")
            elif(
                (positive == False)
                    and
                (negitive == False)
            ):
                print("up")
            elif(
                (positive == True)
                    and
                (negitive == False)
            ):
                print("left")
            elif(
                (positive == False)
                    and
                (negitive == True)
            ):
                print("right")

    def finialize(self):
        print("Finalize APP")