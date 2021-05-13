import time
from turtle import Screen

from food import Food
from scoreboard import Score
from snake import Snake

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)



snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        score.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 250 or snake.head.ycor() < -270:
        game_is_on = False
        score.game_over()

    for segment in snake.all_turtles[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
