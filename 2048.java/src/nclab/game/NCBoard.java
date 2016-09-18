package nclab.game;

import javax.swing.*;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.ArrayList;

/**
 * Game board which size is Height x Width
 * Created by LIAO on 2016/9/17.
 */
public class NCBoard extends JFrame {

    public static final int NC_NUM_ROW = 4; // number of rows of board
    public static final int NC_NUM_COL = 4; // number of columns of board
    public static final int NC_CELL_SIZE = 100; // size of cell
    public static final int INF = 1000000;

    // Directions
    public static final int RIGHT = 0;
    public static final int UP = 1;
    public static final int LEFT = 2;
    public static final int DOWN = 3;

    // simple lock
    public boolean lock = false;

    private NCCell[][] cells;

    public NCBoard(ImageIcon icon) {

        help();

        this.setIconImage(icon.getImage());
        this.setSize(NC_CELL_SIZE * NC_NUM_ROW, NC_CELL_SIZE * NC_NUM_COL);  // set window size
        this.setLocationRelativeTo(null);  // set position on center of screen
        this.setTitle("2048.java - NCLAB");
        this.setLayout(new GridLayout(NC_NUM_ROW, NC_NUM_COL));
        this.setResizable(false);
        this.setBackground(Color.BLACK);
        this.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);  // set do nothing on close

        // add key listener
        this.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (lock) return;
                lock = true;
                if (e.getKeyCode() == KeyEvent.VK_Q){   // quit
                    quit();
                }
                if (e.getKeyCode() == KeyEvent.VK_R){   // restart
                    restart();
                }
                else if (e.getKeyCode() == KeyEvent.VK_H) { // help
                    help();
                }
                else if (e.getKeyCode() == KeyEvent.VK_UP)  // up
                {
                    moveCells(UP);
                }
                else if (e.getKeyCode() == KeyEvent.VK_DOWN)  // down
                {
                    moveCells(DOWN);
                }
                else if (e.getKeyCode() == KeyEvent.VK_LEFT)  // left
                {
                    moveCells(LEFT);
                }
                else if (e.getKeyCode() == KeyEvent.VK_RIGHT)  // right
                {
                    moveCells(RIGHT);
                }
                lock = false;
            }
        });

        // add window listener
        this.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                quit();
            }
        });

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

    /**
     * Show Help Message
     */
    private  void help() {
        JOptionPane.showMessageDialog(null, "Up/Down/Left/Right - Control Move\n" +
                "Q - Quit\nR - Restart\nH - Help\nhttps://github.com/NCLAB2016/",
                "Help", JOptionPane.INFORMATION_MESSAGE);
    }

    /**
     * Restart the Game
     */
    private void restart() {
        int res = JOptionPane.showConfirmDialog(null, "Sure to Restart? O(^_^)O", "Restart",
                JOptionPane.YES_NO_OPTION);
        if (res == JOptionPane.YES_OPTION) _restart();
    }

    private void _restart() {
        for (int i = 0; i < NC_NUM_ROW; ++i)
            for (int j = 0; j < NC_NUM_COL; ++j)
                cells[i][j].setDigit(0);
        occurDigit();
    }

    private void quit() {
        int res = JOptionPane.showConfirmDialog(null, "Sure to leave me? :(",
                "Quit", JOptionPane.YES_NO_OPTION);
        if (res == JOptionPane.YES_OPTION) System.exit(0);
    }

    private void moveCells(int direction) {
        boolean moved = false, allMoved = false;
        switch (direction){
            case UP:    // direction up
                while (true) {
                    moved = false;
                    for (int col = 0; col < NC_NUM_COL; ++col)
                        for (int i = 0; i < NC_NUM_ROW; ++i)
                            if (!cells[i][col].isEmpty()) {  // not empty cell
                                boolean res = movedACell(i, col, direction);
                                if (res) moved = true;
                            }
                    if (!moved) break;
                    else allMoved = true;
                }
                break;
            case DOWN:    // direction down
                while (true) {
                    moved = false;
                    for (int col = 0; col < NC_NUM_COL; ++col)
                        for (int i = NC_NUM_ROW-1; i >= 0; --i)
                            if (!cells[i][col].isEmpty()) { // not empty cell
                                boolean res = movedACell(i, col, direction);
                                if (res) moved = true;
                            }
                    if (!moved) break;
                    else allMoved = true;
                }
                break;
            case LEFT:    // direction left
                while (true) {
                    moved = false;
                    for (int row = 0; row < NC_NUM_ROW; ++row)
                        for (int j = 0; j < NC_NUM_COL; ++j)
                            if (!cells[row][j].isEmpty()) {  // not empty cell
                                boolean res = movedACell(row, j, direction);
                                if (res) moved = true;
                            }
                    if (!moved) break;
                    else allMoved = true;
                }
                break;
            case RIGHT:    // direction right
                while (true) {
                    moved = false;
                    for (int row = 0; row < NC_NUM_ROW; ++row)
                        for (int j = NC_NUM_COL-1; j >= 0; --j)
                            if (!cells[row][j].isEmpty()) { // not empty cell
                                boolean res = movedACell(row, j, direction);
                                if (res) moved = true;
                            }
                    if (!moved) break;
                    else allMoved = true;
                }
                break;
            default:    // Error
                JOptionPane.showMessageDialog(null, "Oh, it is impossible!", "Error", JOptionPane.ERROR_MESSAGE);
        }
        if (allMoved) occurDigit(); // select new cell to occur digit
        if (isGameOver()) JOptionPane.showMessageDialog(null, "Game Over!", "Thank you",
                JOptionPane.INFORMATION_MESSAGE);
    }

    private boolean isGameOver() {
        for (int i = 0; i < NC_NUM_ROW; ++i)
            for (int j = 0; j < NC_NUM_COL; ++j) {
                if (cells[i][j].isEmpty()) return false;
                int digit = cells[i][j].getDigit();
                if (i > 0 && cells[i-1][j].getDigit() == digit) return false;
                if (i < NC_NUM_ROW-1 && cells[i+1][j].getDigit() == digit) return false;
                if (j > 0 && cells[i][j-1].getDigit() == digit) return false;
                if (j < NC_NUM_COL-1 && cells[i][j+1].getDigit() == digit) return false;
            }
        return true;
    }

    private boolean movedACell(int i, int j, int dir) {
        int emptyPos = -1, digit = cells[i][j].getDigit();
        switch (dir) {
            case UP:
                for (int row = i-1; row >= 0; --row){
                    if (cells[row][j].getDigit() == digit) {  // find can merge
                        cells[i][j].setDigit(0);
                        cells[row][j].setDigit(digit << 1);   // multiply 2
                        if (cells[row][j].getDigit() >= 2048)
                            JOptionPane.showMessageDialog(null, "unbelievable! Go On!", "Ohhhh",
                                    JOptionPane.INFORMATION_MESSAGE);
                        return true;
                    }
                    if (cells[row][j].isEmpty())    // find empty cell
                    {
                        emptyPos = row;
                    }
                    else if (cells[row][j].getDigit() != digit) break;   // different
                }
                if (emptyPos == -1) return false;
                cells[i][j].setDigit(0);            // move cell
                cells[emptyPos][j].setDigit(digit);
                return true;
            case DOWN:
                for (int row = i+1; row < NC_NUM_ROW; ++row){
                    if (cells[row][j].getDigit() == digit) {  // find can merge
                        cells[i][j].setDigit(0);
                        cells[row][j].setDigit(digit << 1);   // multiply 2
                        if (cells[row][j].getDigit() >= 2048)
                            JOptionPane.showMessageDialog(null, "unbelievable! Go On!", "Ohhhh",
                                    JOptionPane.INFORMATION_MESSAGE);
                        return true;
                    }
                    if (cells[row][j].isEmpty())    // find empty cell
                    {
                        emptyPos = row;
                    }
                    else if (cells[row][j].getDigit() != digit) break; // different
                }
                if (emptyPos == -1) return false;
                cells[i][j].setDigit(0);            // move cell
                cells[emptyPos][j].setDigit(digit);
                return true;
            case LEFT:
                for (int col = j-1; col >= 0; --col){
                    if (cells[i][col].getDigit() == digit) {  // find can merge
                        cells[i][j].setDigit(0);
                        cells[i][col].setDigit(digit << 1);   // multiply 2
                        if (cells[i][col].getDigit() >= 2048)
                            JOptionPane.showMessageDialog(null, "unbelievable! Go On!", "Ohhhh",
                                    JOptionPane.INFORMATION_MESSAGE);
                        return true;
                    }
                    if (cells[i][col].isEmpty())    // find empty cell
                    {
                        emptyPos = col;
                    }
                    else if (cells[i][col].getDigit() != digit) break;   // different
                }
                if (emptyPos == -1) return false;
                cells[i][j].setDigit(0);            // move cell
                cells[i][emptyPos].setDigit(digit);
                return true;
            case RIGHT:
                for (int col = j+1; col < NC_NUM_COL; ++col){
                    if (cells[i][col].getDigit() == digit) {  // find can merge
                        cells[i][j].setDigit(0);
                        cells[i][col].setDigit(digit << 1);   // multiply 2
                        if (cells[i][col].getDigit() >= 2048)
                            JOptionPane.showMessageDialog(null, "unbelievable! Go On!", "Ohhhh",
                                    JOptionPane.INFORMATION_MESSAGE);
                        return true;
                    }
                    if (cells[i][col].isEmpty())    // find empty cell
                    {
                        emptyPos = col;
                    }
                    else if (cells[i][col].getDigit() != digit) break; // different
                }
                if (emptyPos == -1) return false;
                cells[i][j].setDigit(0);            // move cell
                cells[i][emptyPos].setDigit(digit);
                return true;
            default:    // Error
                JOptionPane.showMessageDialog(null, "Oh, it is impossible!", "Error", JOptionPane.ERROR_MESSAGE);
        }
        return false;
    }

    private void occurDigit() {

        // put all empty cell to list
        ArrayList<NCCell> list = new ArrayList<NCCell>();
        list.clear();
        for (int i = 0; i < NC_NUM_ROW; ++i)
            for (int j = 0; j < NC_NUM_COL; ++j)
                if (cells[i][j].isEmpty()) list.add(cells[i][j]);
        if (list.isEmpty())
            JOptionPane.showMessageDialog(null, "Oh, it is impossible!", "Error", JOptionPane.ERROR_MESSAGE);

        // randomly select an empty cell
        int sel = (int)(Math.random() * INF) % (list.size());
        int rndDig = Math.random() > 0.5 ? 2 : 4;

        // set select digit
        int now = -1;
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
