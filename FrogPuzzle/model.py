from frog import Frogs
from text import Texts

class Model:
    def __init__(self, app):
        print("CONSTRUCTING MODEL")
        self.app = app
        self.frogs = []
        for row in range(5):
            cols = []
            for col in range(5):
                cols.append(Frogs(col, row, app.win, "frog.png", 100))
            self.frogs.append(cols)
        self.numFrogDraw = []
        for row in range(5):
            cols = []
            for col in range(5):
                cols.append(Texts(col, row, app.win))
            self.numFrogDraw.append(cols)
        self.numFrog = []
        for row in range(5):
            cols = []
            for col in range(5):
                cols.append(1)
            self.numFrog.append(cols)
        self.frogMove = []
        for row in range(5):
            cols = []
            for col in range(5):
                cols.append(False)
            self.frogMove.append(cols)
    def finalize(self):
        print("Finalize MODEL")

    def initialize(self):
        print("INITIALIZING MODEL")

    def run(self):
        #print("RUNNING MODEL")
        return
        