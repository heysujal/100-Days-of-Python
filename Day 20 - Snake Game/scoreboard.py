from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.penup()
        self.color('white')
        self.sety(275)
        self.write(f"Score is {self.score_count}",False,"center", font=("Arial", 15, "normal"))
        self.ht()

    def update_score(self):
        self.score_count += 1
        self.clear()
        self.write(f"Score is {self.score_count}", False, "center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"center",font=("Arial", 15, "normal"))