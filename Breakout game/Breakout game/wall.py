import random
from turtle import Turtle

BRICKS_POSITION = {  # 6º Create a dictionary with positon colors and points
    "red": [(250, 280), (200, 280), (150, 280), (100, 280), (50, 280), (0, 280), (-50, 280), (-100, 280), (-150, 280),
            (-200, 280), (-250, 280), (250, 250), (200, 250), (150, 250), (100, 250), (50, 250), (0, 250), (-50, 250),
            (-100, 250), (-150, 250), (-200, 250), (-250, 250)],

    "orange":
        [(250, 220), (200, 220), (150, 220), (100, 220), (50, 220), (0, 220), (-50, 220), (-100, 220), (-150, 220),
         (-200, 220), (-250, 220), (250, 190), (200, 190), (150, 190), (100, 190), (50, 190), (0, 190), (-50, 190),
         (-100, 190), (-150, 190), (-200, 190), (-250, 190)],

    "green": [(250, 160), (200, 160), (150, 160), (100, 160), (50, 160), (0, 160), (-50, 160), (-100, 160), (-150, 160),
              (-200, 160), (-250, 160), (250, 130), (200, 130), (150, 130), (100, 130), (50, 130), (0, 130), (-50, 130),
              (-100, 130), (-150, 130), (-200, 130), (-250, 130)],

    "yellow": [(250, 100), (200, 100), (150, 100), (100, 100), (50, 100), (0, 100), (-50, 100), (-100, 100),
               (-150, 100),
               (-200, 100), (-250, 100), (250, 70), (200, 70), (150, 70), (100, 70), (50, 70), (0, 70), (-50, 70),
               (-100, 70), (-150, 70), (-200, 70), (-250, 70)],
}


class Wall:  # Create a normal class
    def __init__(self):  # init
        self.the_wall = []  # Create a list to put all blocks
        self.building_the_red_wall()  # 5º call functions
        self.building_the_orange_wall()
        self.building_the_green_wall()
        self.building_the_yellow_wall()

        self.MOVEMENT_INCREMENT = 50

    def building_the_red_wall(self):
        red_colour = "red"
        for position in BRICKS_POSITION[red_colour]:  # Loop the list
            self.bricks_in_the_wall(position, red_colour)  # 2º loops and send position

    def building_the_orange_wall(self):
        orange_colour = "orange"
        for position in BRICKS_POSITION[orange_colour]:  # Loop the list
            self.bricks_in_the_wall(position, orange_colour)  # 2º loops and send position

    def building_the_green_wall(self):
        green_colour = "green"
        for position in BRICKS_POSITION[green_colour]:  # Loop the list
            self.bricks_in_the_wall(position, green_colour)  # 2º loops and send position

    def building_the_yellow_wall(self):
        yellow_colour = "yellow"
        for position in BRICKS_POSITION[yellow_colour]:  # Loop the list
            self.bricks_in_the_wall(position, yellow_colour)  # 2º loops and send position

    def bricks_in_the_wall(self, position, colour):  # 3º add vari
        bricks = Turtle("square")  # 4 º Define object
        bricks.shapesize(1, 2)
        bricks.color(colour)
        bricks.penup()
        bricks.goto(position)
        self.the_wall.append(bricks)  # put bricks on the_wall list

    def breaking_the_wall(self, loc):
        wall = self.the_wall[loc]   # mandar o block para fora do mapa 87-0
        wall.goto(600, -600)
