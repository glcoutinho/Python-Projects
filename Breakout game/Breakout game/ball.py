from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # shaped circle and color white
        self.color("white")
        self.penup()  # no tracer
        self.y_move = 1
        self.x_move = 1

    def movement(self):  # start move down
        new_y = self.ycor() - 20 * self.y_move
        new_x = self.xcor() - 25 * self.x_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1  # limit bounce

    def x_bounce(self):
        self.x_move *= -1  # limit bounce

    def reset_ball(self):
        self.goto(0, 0)