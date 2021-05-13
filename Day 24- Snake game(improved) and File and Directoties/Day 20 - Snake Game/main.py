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
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        score.increase_score()
        # score.update_scoreboard()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 250 or snake.head.ycor() < -270:
        # game_is_on = False
        score.reset_game()
        snake.reset_snake()

    for segment in snake.all_turtles[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            snake.reset_snake()
            score.reset_game()
screen.exitonclick()
