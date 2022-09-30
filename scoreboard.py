from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level=0
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.updateScore()
    
    def updateScore(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)
    
    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)

