from turtle import Turtle
import random
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.res=[]
        self.speed=5
    def createcar(self):
        if random.randint(1,6)==1:
            turtle=Turtle()
            turtle.shape("square")
            turtle.shapesize(stretch_wid=1,stretch_len=2)
            turtle.penup()
            turtle.color(random.choice(COLORS))
            turtle.goto(280,random.randint(-250,250))
            self.res.append(turtle)

    def movecars(self):
        for i in self.res:
            i.backward(self.speed)
    
    def increaseSpeed(self):
        self.speed+=3

