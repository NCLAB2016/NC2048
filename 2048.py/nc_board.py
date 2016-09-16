from turtle import Turtle

class NCBoard(object):
    NC_NUM_CELL_ROW = 4  # Number of cells per row
    NC_NUM_CELL_COL = 4  # Number of cells per column
    NC_CELL_SIZE = 150  # Length/Width of per cell

    def __init__(self, win):

        # Board Cells
        self.nc_cells = [[0] * self.NC_NUM_CELL_COL] * self.NC_NUM_CELL_ROW
        # Board Turtles
        self.nc_turtles = [[0] * self.NC_NUM_CELL_COL] * self.NC_NUM_CELL_ROW

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
        for i in range(-self.NC_NUM_CELL_ROW / 2, self.NC_NUM_CELL_ROW / 2):
            for j in range(-self.NC_NUM_CELL_COL / 2, self.NC_NUM_CELL_COL / 2):
                self.nc_turtles[i][j] = Turtle()
                self.nc_turtles[i][j].setpos(i * self.NC_CELL_SIZE,
                                             j * self.NC_CELL_SIZE)
                self.nc_turtles[i][j].setheading(0)
                self.nc_turtles[i][j].color("white")
                self.nc_turtles[i][j].speed(10)
                self.nc_turtles[i][j].shape("turtle")
                self.nc_turtles[i][j].pensize(3)
                self.draw_square(self.nc_turtles[i][j])

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
