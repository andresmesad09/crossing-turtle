from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("black")
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
