from Graphics import *


class Blade(object):
    """creates a blade for the lightsaber"""

    def __init__(self, x, y, color, width, height, win):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def drawBlade(x, y = 250, color = "red", width = 200, height = 30):
        blade = Rectangle(Point(x, y), Point(x + width, y + height))
        blade.setFill(color)
        blade.setOutline("white")
        blade.draw(win)


    def main(win):
        """Runs the main code"""
        Blade.drawBlade(200)
        Blade.drawBlade(625)




        win.getMouse()
        win.close()



win = GraphWin("Lightsaber", 1000, 650)
win.setBackground("black")

Blade.main(win)

class Handle(Blade):
    def __init__(self, x, y, color, win):
        super(Handle,self).__init__(x, y, color, win)
        self.drawHandle(win)
        self.drawButton(win)

    def drawHandle(self, win):
        hand = Rectangle(Point(self.x + 45, self.y - 25), Point(self.x + 225, self.y))
        hand.setFill(self.color)
        hand.draw(win)
        line = Line(Point(self.x + 30, self.y - 45), Point(self.x + 150, self.y - 65))
        line.setWidth(25)
        hand.draw(win)

    def drawButton(self, win):
        button = Circle(Point(x+255, y+ 485), 25)
        button.draw(win)
#def main():
