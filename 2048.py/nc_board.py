# coding=utf-8
from turtle import Turtle
from tkMessageBox import showinfo
from tkMessageBox import showwarning
from tkMessageBox import showerror
from tkMessageBox import askyesno
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
        self.win.setup(width=800, height=800)   # default size
        self.win.title("2048.py - NCLAB")

        # show help info
        showinfo('Help', u'方向键Up/Down/Left/Right\nR/r - 重新开始\nQ/q - 退出\n'
                         u'H/h - Help\n\nhttps://github.com/NCLAB2016/\n')

        # Listen Direction Key
        self.win.onkey(self.on_key_up, "Up")
        self.win.onkey(self.on_key_down, "Down")
        self.win.onkey(self.on_key_left, "Left")
        self.win.onkey(self.on_key_right, "Right")

        # Listen Game Control Key
        self.win.onkey(self.on_key_q, "Q")  # uppercase
        self.win.onkey(self.on_key_r, "R")
        self.win.onkey(self.on_key_h, "H")
        self.win.onkey(self.on_key_q, "q")  # lowercase
        self.win.onkey(self.on_key_r, "r")
        self.win.onkey(self.on_key_h, "h")

        # simple lock for control key press
        self.lock = False
        self.win.listen()

        # Draw the Board
        self.tur = Turtle()
        self.tur.color("white")
        self.tur.speed("fastest")   # draw speed
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
        sel = random.randint(0, len(empty_cells)-1)  # select one randomly
        empty_cells[sel].change_digit(self.tur, random.randint(1, 2) * 2)
        del empty_cells
        if self.is_game_over():
            showwarning("Thank you", "Game Over!\n")
        return True

    def is_game_over(self):
        """ Check the board state to find if game is over """
        for i in range(0, self.NC_NUM_CELL_ROW):
            for j in range(0, self.NC_NUM_CELL_COL):
                digit = self.nc_cells[i][j].nc_digit
                if digit == 0:   # exist empty place
                    return False
                if i > 0 and digit == self.nc_cells[i-1][j].nc_digit:  # check up
                    return False
                if i < self.NC_NUM_CELL_ROW - 1 and digit == self.nc_cells[i+1][j].nc_digit:    # check down
                    return False
                if j > 0 and digit == self.nc_cells[i][j-1].nc_digit:   # check left
                    return False
                if j < self.NC_NUM_CELL_COL - 1 and digit == self.nc_cells[i][j+1].nc_digit:    # check right
                    return False
        return True

    def draw_board(self):
        """ Draw the game board """
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

    def new_game(self):
        """ Restart a New Game """
        for i in range(0, self.NC_NUM_CELL_ROW):
            for j in range(0, self.NC_NUM_CELL_COL):
                self.nc_cells[i][j].remove_color(self.tur)
        self.occur_new_digit()

    def on_key_up(self):
        """ Press the Up Key Move All Can Move to Up """
        if self.lock:       # wait for the lock
            return
        self.lock = True    # hold the lock
        all_moved = False   # flag mark if there exists cell moved
        for col in range(0, self.NC_NUM_CELL_COL):
            while True:
                moved = False
                for i in range(0, self.NC_NUM_CELL_ROW):
                    if self.nc_cells[i][col].nc_digit != 0:
                        moved = self.moved_to_direction(i, col, 1)  # 1: up
                if not moved:
                    break
                else:
                    all_moved = True
        if all_moved:   # if exists moved, occurred a new cell randomly
            res = self.occur_new_digit()
            if not res:  # Error
                showerror("Error", "It is impossible!")
        self.lock = False   # release the lock

    def on_key_down(self):
        """ Press the Down Key Move All Can Move to Down """
        if self.lock:       # wait for the lock
            return
        self.lock = True    # hold the lock
        all_moved = False   # flag mark if there exists cell moved
        for col in range(0, self.NC_NUM_CELL_COL):
            while True:
                moved = False
                for i in range(self.NC_NUM_CELL_ROW-1, -1, -1):
                    if self.nc_cells[i][col].nc_digit != 0:
                        moved = self.moved_to_direction(i, col, 3)  # 3: down
                if not moved:
                    break
                else:
                    all_moved = True
        if all_moved:   # if exists moved, occurred a new cell randomly
            res = self.occur_new_digit()
            if not res:  # Error
                showerror("Error", "It is impossible!")
        self.lock = False

    def on_key_left(self):
        """ Press the Left Key Move All Can Move to Left """
        if self.lock:       # wait for the lock
            return
        self.lock = True    # hold the lock
        all_moved = False   # flag mark if there exists cell moved
        for row in range(0, self.NC_NUM_CELL_ROW):
            while True:
                moved = False
                for j in range(0, self.NC_NUM_CELL_COL):
                    if self.nc_cells[row][j].nc_digit != 0:
                        moved = self.moved_to_direction(row, j, 2)  # 2: left
                if not moved:
                    break
                else:
                    all_moved = True
        if all_moved:   # if exists moved, occurred a new cell randomly
            res = self.occur_new_digit()
            if not res:  # Error
                showerror("Error", "It is impossible!")
        self.lock = False

    def on_key_right(self):
        """ Press the Right Key Move All Can Move to Right """
        if self.lock:       # wait for the lock
            return
        self.lock = True    # hold the lock
        all_moved = False   # flag mark if there exists cell moved
        for row in range(0, self.NC_NUM_CELL_ROW):
            while True:
                moved = False
                for j in range(self.NC_NUM_CELL_COL-1, -1, -1):
                    if self.nc_cells[row][j].nc_digit != 0:
                        moved = self.moved_to_direction(row, j, 0)  # 0: right
                if not moved:
                    break
                else:
                    all_moved = True
        if all_moved:   # if exists moved, occurred a new cell randomly
            res = self.occur_new_digit()
            if not res:  # Error
                showerror("Error", "It is impossible!")
        self.lock = False

    def moved_to_direction(self, i, j, direction):
        """ Move cell to certain direction, merge or replace empty place """
        digit = self.nc_cells[i][j].nc_digit  # my digit

        if direction == 0:  # move right
            find_col = -1
            for col in range(j + 1, self.NC_NUM_CELL_COL):
                if self.nc_cells[i][col].nc_digit == 0:  # find empty place
                    find_col = col
                elif self.nc_cells[i][col].nc_digit == digit:  # find can merge
                    # merge digit
                    self.nc_cells[i][j].remove_color(self.tur)
                    self.nc_cells[i][col].change_digit(self.tur, digit * 2)
                    return True
                else:  # find can not merge
                    break
            if find_col == -1:  # can not find an empty place or not merge
                return False
            else:  # empty place
                self.nc_cells[i][j].remove_color(self.tur)
                self.nc_cells[i][find_col].change_digit(self.tur, digit)
            return True
        elif direction == 1:  # move up
            find_row = -1
            for row in range(i - 1, -1, -1):
                if self.nc_cells[row][j].nc_digit == 0:  # find empty place
                    find_row = row
                elif self.nc_cells[row][j].nc_digit == digit:  # find can merge
                    # merge digit
                    self.nc_cells[i][j].remove_color(self.tur)
                    self.nc_cells[row][j].change_digit(self.tur, digit * 2)
                    return True
                else:  # find can not merge
                    break
            if find_row == -1:  # can not find an empty place or not merge
                return False
            else:   # empty place
                self.nc_cells[i][j].remove_color(self.tur)
                self.nc_cells[find_row][j].change_digit(self.tur, digit)
            return True
        elif direction == 2:  # move left
            find_col = -1
            for col in range(j-1, -1, -1):
                if self.nc_cells[i][col].nc_digit == 0:  # find empty place
                    find_col = col
                elif self.nc_cells[i][col].nc_digit == digit:  # find can merge
                    # merge digit
                    self.nc_cells[i][j].remove_color(self.tur)
                    self.nc_cells[i][col].change_digit(self.tur, digit * 2)
                    return True
                else:  # find can not merge
                    break
            if find_col == -1:  # can not find an empty place or not merge
                return False
            else:  # empty place
                self.nc_cells[i][j].remove_color(self.tur)
                self.nc_cells[i][find_col].change_digit(self.tur, digit)
            return True
        elif direction == 3:  # move down
            find_row = -1
            for row in range(i + 1, self.NC_NUM_CELL_ROW):
                if self.nc_cells[row][j].nc_digit == 0:  # find empty place
                    find_row = row
                elif self.nc_cells[row][j].nc_digit == digit:  # find can merge
                    # merge digit
                    self.nc_cells[i][j].remove_color(self.tur)
                    self.nc_cells[row][j].change_digit(self.tur, digit * 2)
                    return True
                else:  # find can not merge
                    break
            if find_row == -1:  # can not find an empty place or not merge
                return False
            else:   # empty place
                self.nc_cells[i][j].remove_color(self.tur)
                self.nc_cells[find_row][j].change_digit(self.tur, digit)
            return True
        else:
            showerror("Error", "Unknown direction!")

    def on_key_q(self):
        res = askyesno("Quit", "Sure to leave me? :(")
        if res:
            self.win.bye()

    def on_key_r(self):
        res = askyesno("New", "Sure to restart? O(^_^)O")
        if res:
            self.new_game()

    def on_key_h(self):
        showinfo('Help', u'方向键Up/Down/Left/Right\nR/r - 重新开始\nQ/q - 退出\n'
                         u'H/h - Help\n\nhttps://github.com/NCLAB2016/\n')

    def draw_square(self, tur):
        for i in range(0, 4):  # Turn 4 Directions
            tur.forward(self.NC_CELL_SIZE)
            tur.left(90)
