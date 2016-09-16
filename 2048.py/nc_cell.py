#import nc_board as nb


class NCCell:

    """ Author: LIAO
    Date: 2016.9.16
    NCLAB Copyright 2016 All right reserved
    A cell in 2048 board, actually it is a top-left vertex of a cell. """

#    NC_X_OFFSET = nb.NCBoard.NC_CELL_SIZE / 6  # x offset of digit in cell relative to top-left point in cell
#    NC_Y_OFFSET = nb.NCBoard.NC_CELL_SIZE / 6  # y offset of digit in cell relative to top-left point in cell

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

    def change_digit(self, tur, digit):
        self.nc_digit = digit
        x = tur.xcor()
        y = tur.ycor()
        print("POS: (" + str(self.nc_row) + ", " + str(self.nc_col) + ") : " + str(self.nc_digit))
   #     tur.write(str(digit), True)
