package nclab.game;

import javax.swing.*;
import javax.swing.border.LineBorder;
import java.awt.*;
import java.util.HashMap;

/**
 * The Cell in the Game Board
 * Created by LIAO on 2016/9/17.
 */
public class NCCell extends JLabel{

    public static final int[] digitSizes = {0, 200, 150, 110, 80, 60};   // font size depend on length of digit
    public static final HashMap<Integer, Color> cellColors = new HashMap(); // cell color map

    {
        cellColors.put(0, this.getBackground());
        cellColors.put(2, new Color(230, 126, 34));
        cellColors.put(4, new Color(211, 84, 0));
        cellColors.put(8, new Color(231, 76, 60));
        cellColors.put(16, new Color(192, 57, 43));
        cellColors.put(32, new Color(46, 204, 113));
        cellColors.put(64, new Color(39, 174, 96));
        cellColors.put(128, new Color(52, 152, 219));
        cellColors.put(256, new Color(41, 128, 185));
        cellColors.put(512, new Color(155, 89, 182));
        cellColors.put(1024, new Color(142, 68, 173));
        cellColors.put(2048, new Color(52, 73, 94));
        cellColors.put(4096, new Color(44, 62, 80));
        cellColors.put(8192, new Color(254, 12, 22));
        cellColors.put(16384, new Color(236, 240, 241));
        cellColors.put(32768, new Color(149, 165, 166));
        cellColors.put(65536, new Color(127, 140, 141));
    }

    private int digit;

    public NCCell(){
        this.setBorder(new LineBorder(Color.BLACK, 2));
        this.setOpaque(true);   // background color is enable only set opaque
        this.setHorizontalAlignment(JLabel.CENTER); // text display in center of label
        digit = 0;
    }

    public int getDigit() {
        return digit;
    }

    public boolean isEmpty() {
        return digit == 0;
    }

    public void setDigit(int digit) {
        this.digit = digit;
        Color c = cellColors.get(digit);
        if (null == c) // Error
            JOptionPane.showMessageDialog(null, "Error", "Oh, it is impossible!", JOptionPane.ERROR_MESSAGE);
        this.setBackground(c);
        this.setText(""+digit);
        if (digit == 0) this.setText("");   // do not display zero
        this.setFont(new Font(Font.SANS_SERIF, Font.BOLD, digitSizes[String.valueOf(digit).length()]));
    }
}
