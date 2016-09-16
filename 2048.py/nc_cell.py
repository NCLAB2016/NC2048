import nc_board


class NCCell:

    """ Author: LIAO
    Date: 2016.9.16
    NCLAB Copyright 2016 All right reserved
    A cell in 2048 board, actually it is a top-left vertex of a cell. """

    # backgroud color of this cell in different with digit
    BG_COLORS = {2: '#f1c40f', 4: '#f39c12', 8: '#e67e22', 16: '#d35400',
                 32: '#e74c3c', 64: '#16a085', 128: '#3498db', 256: '#8e44ad',
                 512: '#34495e', 1024: '#8b0000', 2048: '#191970', 4096: '#00000f',
                 8192: '#00000f', 16384: '#00000f', 32768: '#00000f', 65536: '#00000f'}

    # size of digit in different with length of digit
    SIZE_PER_LEN = {1: 100, 2: 90, 3: 70, 4: 50, 5: 40}

    def __init__(self, x, y, row, col, digit):
        # type: (int, int, int, int, int) -> NCCell
        """

        :rtype: NCCell
        """
        self.nc_x = x   # x position of this cell
        self.nc_y = y   # y position of this cell
        self.nc_row = row   # row of this cell
        self.nc_col = col   # column of this cell
        self.nc_digit = digit   # digit in this cell, e.g. 2/4/8/16... 0 for no digit
        self.nc_label = None    # label in frame to show digit
        self.nc_x_offset = nc_board.NCBoard.NC_CELL_SIZE / 2  # x offset of digit relative to top-left point in cell
        self.nc_y_offset = -nc_board.NCBoard.NC_CELL_SIZE   # y offset of digit relative to top-left point in cell

    def change_digit(self, tur, digit):
        """ Change the digit in this cell, draw on cell and fill color in the same time """
        self.nc_digit = digit
        print("POS: (" + str(self.nc_row) + ", " + str(self.nc_col) + ") : " + str(self.nc_digit))
        print(str(self.nc_x) + ", " + str(self.nc_y))
        # fill color in cell
        self.fill_color(tur)
        # write digit to cell
        tur.penup()
        tur.setpos(self.nc_x+self.nc_x_offset, self.nc_y+self.nc_y_offset)
        tur.pendown()
        tur.write(str(digit), align="center", font=("Arial", self.SIZE_PER_LEN[len(str(digit))], "normal"))

    def fill_color(self, tur):
        """ Fill color on current cell, the color filled was depended on the digit
        in this cell, see BG_COLORS """
        tur.fillcolor(self.BG_COLORS[self.nc_digit])
        tur.penup()
        tur.setheading(0)
        tur.setpos(self.nc_x, self.nc_y)
        tur.begin_fill()
        for i in range(0, 4):
            tur.forward(nc_board.NCBoard.NC_CELL_SIZE)
            tur.right(90)
        tur.end_fill()
        tur.pendown()

