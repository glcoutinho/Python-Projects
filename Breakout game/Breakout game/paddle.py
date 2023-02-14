from turtle import Turtle


class Paddle(Turtle):  # Create a class with a self.innit method for object construction
    def __init__(self):
        super().__init__()
        self.shape("square")  # define shape, size and color
        self.shapesize(1, 5)
        self.color("light blue")
        self.penup()

    def pos_paddle(self):
        self.goto(0, -280)  # and setle position

    def go_right(self):
        new_x = self.xcor() + 30  # The key function takes the current value and adds 20 in the x coordinate
        self.goto(new_x, self.ycor())  # send paddle to the new position

    def go_left(self):
        new_x = self.xcor() - 30  # same but subtract
        self.goto(new_x, self.ycor())