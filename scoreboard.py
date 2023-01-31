from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("white")
        with open("high_score.txt", "r") as score:
            self.high_score = score.read()
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.goto(0, 250)
        self.write(arg=f"Score: {self.score}   Level: {self.level}   High Score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT)

    def game_over(self, outcome):
        self.goto(0, 0)
        if outcome == "Win":
            message = "YOU WIN"
        elif outcome == "Lose":
            message = "GAME OVER"
        self.write(arg=f"{message}", align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        with open("high_score.txt", "w") as score:
            score.write(f"{self.score}")
