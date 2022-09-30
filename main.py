import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
car=CarManager()
player=Player()
score=Scoreboard()
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.createcar()
    car.movecars()
    screen.update()
    for eachcar in car.res:
        if player.distance(eachcar)<20:
            game_is_on=False
            score.gameOver()
        if player.ycor()>280:
            car.increaseSpeed()
            score.updateScore()
            player.finish()
screen.exitonclick()
