from turtle import Screen
import time
from brick_manager import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Initial game set-up
brick = Brick()
paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()

# Build screen
screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.setup(width=800, height=600)
screen.tracer(0)

# Screen listeners
screen.listen()
screen.onkeypress(fun=paddle.move_left, key="Left")
screen.onkeypress(fun=paddle.move_right, key="Right")

# Build bricks
brick.build_bricks()

# Game variables
bricks_broken = 0


# Game functions
def check_score():
    if scoreboard.score > int(scoreboard.high_score):
        scoreboard.update_high_score()


on = True
while on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    # Detect collision with paddle
    if ball.distance(paddle) < 50:
        ball.bounce_y()

    # Used to check is game is working properly (other than paddle)
    # if ball.ycor() < -240:
    #     ball.bounce_y()

    # Detect collision with wall or ceiling
    if ball.xcor() > 335 or ball.xcor() < -335:
        ball.bounce_x()
    elif ball.ycor() > 240:
        ball.bounce_y()

    # Speed up ball
    if bricks_broken % 10 == 0:
        ball.speed_up()

    # Detect collision with brick
    for b in brick.all_bricks:
        if b.distance(ball) < 30:
            brick.all_bricks.remove(b)
            b.hideturtle()
            ball.bounce_y()
            bricks_broken += 1
            scoreboard.increase_score()
            scoreboard.update_score()

    # Next level
    if not brick.all_bricks:
        scoreboard.level += 1
        brick.row_level += 1
        brick.build_bricks()
        ball.ball_restart()

    # End game (Lose)
    if ball.ycor() < -260:
        scoreboard.game_over(outcome="Lose")
        check_score()
        on = False

    # End game (Win)
    if not brick.all_bricks and scoreboard.level < 3:
        scoreboard.game_over(outcome="Win")
        check_score()
        on = False

screen.exitonclick()
