from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.startPosition()

    def move(self):
        self.forward(20)
    
    def finish(self):
        self.startPosition()
    def startPosition(self):
        self.goto(0,-280)
