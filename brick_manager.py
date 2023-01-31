from turtle import Turtle

START_X = -350
START_Y = -50
BRICK_COLORS = ["green", "blue", "red", "purple", "orange", "yellow"]


class Brick:
    def __init__(self):
        self.start_x = START_X
        self.all_bricks = []
        self.row_level = 4

    def build_bricks(self):
        start_y = START_Y
        color_num = 0
        row = 0

        build = True
        while build:
            for _ in range(10):
                brick = Turtle()
                brick.shape("square")
                brick.setheading(180)
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.goto(self.start_x, start_y)
                brick.color(BRICK_COLORS[color_num])
                self.all_bricks.append(brick)
                self.start_x += 75

            color_num += 1
            start_y += 50
            self.start_x = START_X
            row += 1

            if row == self.row_level:
                build = False
