from graphics import *
class Frogs:
    def __init__(self, col, row, win, pic, size):
        self.row = row
        self.col = col
        self.win = win
        self.pic = pic
        self.size = size
        self.image = Image(
            Point(
                (col + 0.5) * size,
                (row + 0.5) * size,
            ),
            pic
        )

        self.image.draw(self.win)

    def move(self, dRow, dCol):
        self.row += dRow
        self.col += dCol
        self.image.move(dCol * self.size, dRow * self.size)
