from view import View
from model import Model
from controller import Controller
from graphics import GraphWin

class App:
    def __init__(self):
        print("CONSTRUCTING APP")
        self.win = GraphWin("FROGS", 700, 700)
        self.view = View(self)
        self.model = Model(self)
        self.controller = Controller(self)
        self.isPlaying = True
        
        self.launch()

    def finalize(self):
        print("Finalize APP")
        self.model.finalize()
        self.view.finalize()
        self.controller.finalize()

    def initialize(self):
        print("INITIALIZING APP")
        self.model.initialize()
        self.view.initialize()
        self.controller.initialize()               

    def launch(self):
        print("LAUNCHING")
        self.initialize()
        self.run()
        self.finalize()
        
    def run(self):
        print("RUNNING APP")
        while(self.isPlaying == True):
            self.model.run()
            self.view.run()
            self.controller.run()