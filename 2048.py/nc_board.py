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
        self.occur_new_digit()

    def occur_new_digit(self):
        """ Occur a new digit in current board, the digit is 2 or 4,
        the position is randomly selected """
        empty_cells = []
        for i in range(0, self.NC_NUM_CELL_ROW):
            for j in range(0, self.NC_NUM_CELL_COL):
                if self.nc_cells[i][j].nc_digit == 0:
                    empty_cells.append(self.nc_cells[i][j])
        if len(empty_cells) == 0:   # no empty space
            return False
        sel = random.randint(0, len(empty_cells)-1)
        empty_cells[sel].change_digit(self.tur, random.randint(1, 2) * 2)
        del empty_cells
        return True

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
        """ Press the Up Key Move All Can Move to Up """
        all_moved = False   # flag mark if there exists cell moved
        for col in range(0, self.NC_NUM_CELL_COL):
            while True:
                moved = False
                for i in range(0, self.NC_NUM_CELL_ROW):
                    if self.nc_cells[i][col].nc_digit != 0:
                        moved = self.moved_to_direction(i, col, 1)
                if not moved:
                    break
                else:
                    all_moved = True
        if all_moved:   # if exists moved, occurred a new cell randomly
            res = self.occur_new_digit()
            if not res: # Game Over
                raise BaseException("Game Over!")

    def moved_to_direction(self, i, j, direction):
        """ Move cell to certain direction, merge or replace empty place """
        digit = self.nc_cells[i][j].nc_digit    # my digit

        if direction == 0:  # move right
            pass
        elif direction == 1:    # move up
            find_row = -1
            for row in range(i-1, -1, -1):
                if self.nc_cells[row][j].nc_digit == 0: # find empty place
                    find_row = row
                elif self.nc_cells[row][j].nc_digit == digit:   # find can merge
                    find_row = row
                    # merge digit
                    self.nc_cells[i][j].remove_color(self.tur)
                    self.nc_cells[row][j].change_digit(self.tur, digit*2)
                else:   # find can not merge
                    break
            if find_row == -1:  # can not find an empty place or not merge
                return False
            elif find_row != self.nc_cells[i][j].nc_digit:  # empty place
                self.nc_cells[i][j].remove_color(self.tur)
                self.nc_cells[find_row][j].change_digit(self.tur, digit)
            return True
        elif direction == 2:    # move left
            pass
        elif direction == 3:    # move down
            pass
        else:
            raise ValueError("Unknown direction!")

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
