from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_left(self):
        if self.xcor() > -335:
            new_x = self.xcor() - 50
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 335:
            new_x = self.xcor() + 50
            self.goto(new_x, self.ycor())
