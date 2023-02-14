from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):  # 1 Creating a init object
    def __init__(self):
        super().__init__()
        self.score = 0  # 0 create Variable
        self.lives = 3
        self.color("white")  # 2 Object defenition
        self.penup()
        self.goto(0, -20)
        self.hideturtle()
        self.update()

    def update(self):  # Turtle to write
        self.clear()
        self.write(f"Lives: {self.lives} Score: {self.score}", align=ALIGNMENT, font=FONT)

    def yellow_points(self):  # 3 yellow points
        points = 1
        self.score += points  # add the fix points
        self.update()

    def green_points(self):  # 3 yellow points
        points = 3
        self.score += points  # add the fix points
        self.update()

    def orange_points(self):  # 3 yellow points
        points = 5
        self.score += points  # add the fix points
        self.update()

    def red_points(self):  # 3 yellow points
        points = 7
        self.score += points  # add the fix points
        self.update()

    def lost_lives(self): # Fazer a vidas
        self.lives -= 1
        self.update()

    def game_over(self):  # a function
        self.clear()
        self.write("Game Over", align=ALIGNMENT, font=FONT)


