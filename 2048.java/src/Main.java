import nclab.game.NCBoard;

import javax.swing.*;

public class Main {

    // icon
    //public static ImageIcon icon = new ImageIcon(Main.class.getResource("/icon.png"));
    public static ImageIcon icon = new ImageIcon("icon.png");

    public static void main(String[] args) {
        JFrame.setDefaultLookAndFeelDecorated(true);
        try {
            // UIManager.setLookAndFeel( UIManager.getSystemLookAndFeelClassName());
            UIManager.setLookAndFeel("com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel");
        } catch (ClassNotFoundException e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        } catch (InstantiationException e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        } catch (IllegalAccessException e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        } catch (UnsupportedLookAndFeelException e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
        new NCBoard(icon).setVisible(true);
    }
}
