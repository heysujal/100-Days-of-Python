from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color('white')
        self.sety(275)
        # self.write(f"Score is {self.score_count} High Score is {self.high_score}", False, "center",
        #            font=("Arial", 15, "normal"))
        self.ht()
        self.update_scoreboard()

    def increase_score(self):
        self.score_count += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # if self.score_count > self.high_score:
        #     self.high_score = self.score_count
        #     with open("data.txt","w") as file:
        #         file.write(f"{self.high_score}")

        self.write(f"Score is {self.score_count} High Score is {self.high_score}", False, "center",
                   font=("Arial", 15, "normal"))

    def reset_game(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")

        self.score_count = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",False,"center",font=("Arial", 15, "normal"))
