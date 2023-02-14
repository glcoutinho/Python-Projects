import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from score import Score


def color_line(y):
    if y == 8 or y == 7:
        score.yellow_points()
    if y == 6 or y == 5:
        score.green_points()
    if y == 4 or y == 3:
        score.orange_points()
    if y == 2 or y == 1:
        score.red_points()


def rules_wall(y):
    if ball.distance(wall.the_wall[11 * y - 11]) < 50:  # Use distance function  if near any block and y
        wall.breaking_the_wall(11 * y - 11)  # send block to far away the screen
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 10]) < 50:
        wall.breaking_the_wall(11 * y - 10)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 9]) < 50:
        wall.breaking_the_wall(11 * y - 9)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 8]) < 50:
        wall.breaking_the_wall(11 * y - 8)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 7]) < 50:
        wall.breaking_the_wall(11 * y - 7)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 6]) < 50:
        wall.breaking_the_wall(11 * y - 6)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 5]) < 50:
        wall.breaking_the_wall(11 * y - 5)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 4]) < 50:
        wall.breaking_the_wall(11 * y - 4)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 3]) < 50:
        wall.breaking_the_wall(11 * y - 3)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 2]) < 50:
        wall.breaking_the_wall(11 * y - 2)
        ball.y_bounce()
        color_line(y)

    elif ball.distance(wall.the_wall[11 * y - 1]) < 50:
        wall.breaking_the_wall(11 * y - 1)
        ball.y_bounce()
        color_line(y)


screen = Screen()  # import screen method in turtle
screen.setup(width=600, height=600)  # adjust size, color and title
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)  # remove turtle animations

paddle = Paddle()  # Create object paddle
paddle.pos_paddle()  # go to position
screen.listen()

screen.onkey(paddle.go_right, "Right")  # Create function that activates by pressing certain key
screen.onkey(paddle.go_left, "Left")

ball = Ball()

wall = Wall()

score = Score()

no_end_game = True
while no_end_game:  # Need to create while loop to make paddle change positions
    screen.update()  # refresh screen very important to display changes
    time.sleep(0.1)  # IMPORTANT: import time module and slow down by 0.1 TO SEE THE BALL MOVEMENT
    ball.movement()
    if ball.ycor() > 280:
        ball.y_bounce()

    if ball.ycor() < -280:  # if goes out of field call loss live and rest ball
        score.lost_lives()
        ball.reset_ball()

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.x_bounce()

    if ball.distance(paddle) < 50:  # Usefully in-boot function allows to determine the distance between objects window
        # print("yes i touch the paddle")
        ball.y_bounce()

    if 280 > ball.ycor() > 250:
        rules_wall(1)

    if 250 > ball.ycor() > 220:
        rules_wall(2)

    if 220 > ball.ycor() > 190:
        rules_wall(3)

    if 190 > ball.ycor() > 160:
        rules_wall(4)

    if 160 > ball.ycor() > 130:
        rules_wall(5)  # find y line (correspondent colour 8) to send to function to determine block

    if 130 > ball.ycor() > 100:
        rules_wall(6)

    if 100 > ball.ycor() > 70:
        rules_wall(7)

    if 70 > ball.ycor() > 40:
        rules_wall(8)

    if score.score > 100 or score.lives == 0:
        score.game_over()
        no_end_game = False

    screen.update()
screen.exitonclick()
