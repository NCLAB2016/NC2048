package nclab.game;

import javax.swing.*;
import java.awt.Color;
import java.awt.GridLayout;
import java.util.ArrayList;

/**
 * Game board which size is Height x Width
 * Created by LIAO on 2016/9/17.
 */
public class NCBoard extends JFrame {

    public static final int NC_NUM_ROW = 4; // number of rows of board
    public static final int NC_NUM_COL = 4; // number of columns of board
    public static final int NC_WINDOW_WIDTH = 800;
    public static final int NC_WINDOW_HEIGHT = 800;
    public static final int INF = 1000000;

    private NCCell[][] cells;

    public NCBoard() {

        this.setSize(NC_WINDOW_WIDTH, NC_WINDOW_HEIGHT);  // set window size
        this.setLocationRelativeTo(null);  // set position on center of screen
        this.setTitle("2048.java - NCLAB");
        this.setLayout(new GridLayout(NC_NUM_ROW, NC_NUM_COL));
        this.setResizable(false);
        this.setBackground(new Color(189, 195, 199));

        // construct cells
        cells = new NCCell[NC_NUM_ROW][NC_NUM_COL];
        for (int i = 0; i < NC_NUM_ROW; ++i)
            for (int j = 0; j < NC_NUM_COL; ++j) {
                cells[i][j] = new NCCell();
                this.add(cells[i][j]);
            }

        // random select one cell to occur digit 2/4
        occurDigit();

    }

    private void occurDigit() {

        // put all empty cell to list
        ArrayList<NCCell> list = new ArrayList<NCCell>();
        list.clear();
        for (int i = 0; i < NC_NUM_ROW; ++i)
            for (int j = 0; j < NC_NUM_COL; ++j)
                if (cells[i][j].isEmpty()) list.add(cells[i][j]);
        if (list.isEmpty())
            JOptionPane.showMessageDialog(null, "Error", "Oh, it is impossible!", JOptionPane.ERROR_MESSAGE);

        // randomly select an empty cell
        int sel = (int)(Math.random() * INF) % (list.size());
        int rndDig = Math.random() > 0.5 ? 2 : 4;

        // set select digit
        int now = 0;
        Outer: for (int i = 0; i < NC_NUM_ROW; ++i)
            for (int j = 0; j < NC_NUM_COL; ++j) {
                if (cells[i][j].isEmpty()) ++now;
                if (now == sel){
                    cells[i][j].setDigit(rndDig);
                    break Outer;
                }
            }
    }

}
