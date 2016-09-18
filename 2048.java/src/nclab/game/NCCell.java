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

    public static final int[] digitSizes = {0, 90, 80, 50, 40, 30};   // font size depend on length of digit
    public static final HashMap<Integer, Color> cellColors = new HashMap(); // cell color map

    {
        cellColors.put(0, Color.BLACK);
        cellColors.put(2, new Color(255, 251, 9));
        cellColors.put(4, new Color(255, 220, 168));
        cellColors.put(8, new Color(255, 133, 113));
        cellColors.put(16, new Color(253, 162, 180));
        cellColors.put(32, new Color(66, 255, 142));
        cellColors.put(64, new Color(170, 255, 231));
        cellColors.put(128, new Color(35, 152, 255));
        cellColors.put(256, new Color(84, 64, 255));
        cellColors.put(512, new Color(199, 66, 254));
        cellColors.put(1024, new Color(255, 9, 189));
        cellColors.put(2048, new Color(255, 0, 64));
        cellColors.put(4096, new Color(1, 80, 0));
        cellColors.put(8192, new Color(0, 23, 69));
        cellColors.put(16384, new Color(53, 0, 20));
        cellColors.put(32768, new Color(41, 37, 0));
        cellColors.put(65536, new Color(255, 249, 251));
    }

    private int digit;

    public NCCell(){
        this.setBorder(new LineBorder(Color.WHITE, 2));
        this.setBackground(Color.BLACK);
        this.setForeground(Color.WHITE);
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
        this.setFont(new Font(Font.SANS_SERIF, Font.PLAIN, digitSizes[String.valueOf(digit).length()]));
    }
}
