from turtle import Turtle
import nc_cell
import random


class NCBoard:

    """ Author: LIAO
    Date: 2016.9.16
    NCLAB Copyright 2016 All right reserved
    Game Board of row * col, but for turtle, x is the horizontal direction,
    from left to right; y is the vertical direction, from bottom to up. The origin
    point is in the center of screen.
    """
    NC_NUM_CELL_ROW = 4  # Number of cells per row
    NC_NUM_CELL_COL = 4  # Number of cells per column
    NC_CELL_SIZE = 150  # Length/Width of per cell

    def __init__(self, win):

        random.seed()
        self.win = win
        self.win.bgcolor("black")

        # Listen Direction Key
        self.win.onkey(self.on_key_up, "Up")
        self.win.onkey(self.on_key_down, "Down")
        self.win.onkey(self.on_key_left, "Left")
        self.win.onkey(self.on_key_right, "Right")

        # Listen Game Control Key
        self.win.onkey(self.on_key_Q, "Q")
        self.win.onkey(self.on_key_r, "r")  # lowercase

        self.win.listen()

        # Draw the Board
        self.tur = Turtle()
        self.tur.color("white")
        self.tur.speed(10)
        self.tur.hideturtle()
        self.tur.pensize(3)
        self.draw_board()

        # Build Board Cells
        self.nc_cells = [[nc_cell.NCCell for col in range(self.NC_NUM_CELL_COL)] for row in range(self.NC_NUM_CELL_ROW)]
        for i in range(0, self.NC_NUM_CELL_ROW):
            for j in range(0, self.NC_NUM_CELL_COL):
                self.nc_cells[i][j] = nc_cell.NCCell((-self.NC_NUM_CELL_COL/2+j)*self.NC_CELL_SIZE,
                                                     (self.NC_NUM_CELL_ROW/2-i)*self.NC_CELL_SIZE,
                                                     i,
                                                     j,
                                                     0)

        # Random Select One Cell Set to 2/4
        row = random.randint(0, self.NC_NUM_CELL_COL-1)
        col = random.randint(0, self.NC_NUM_CELL_ROW-1)
#        self.nc_cells[row][col].change_digit(self.tur, random.randint(1, 2)*2)
        self.nc_cells[row][col].change_digit(self.tur, 65536)

    def draw_board(self):
        for i in range(-self.NC_NUM_CELL_COL / 2, self.NC_NUM_CELL_COL / 2 + 1):
            # draw columns
            self.tur.penup()
            self.tur.setpos(i * self.NC_CELL_SIZE, -self.NC_NUM_CELL_ROW * self.NC_CELL_SIZE / 2)
            self.tur.pendown()
            self.tur.setheading(90)
            self.tur.forward(self.NC_NUM_CELL_ROW * self.NC_CELL_SIZE)
            # draw rows
            self.tur.penup()
            self.tur.setpos(-self.NC_NUM_CELL_COL * self.NC_CELL_SIZE / 2, i * self.NC_CELL_SIZE)
            self.tur.pendown()
            self.tur.setheading(0)
            self.tur.forward(self.NC_NUM_CELL_COL * self.NC_CELL_SIZE)

    def on_key_up(self):
        pass

    def on_key_down(self):
        pass

    def on_key_left(self):
        pass

    def on_key_right(self):
        pass

    def on_key_Q(self):
        self.win.bye()

    def on_key_r(self):
        pass

    def draw_square(self, tur):
        for i in range(0, 4):  # Turn 4 Directions
            tur.forward(self.NC_CELL_SIZE)
            tur.left(90)
