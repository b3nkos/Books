import javax.swing.*;
import java.awt.*;

/**
 * A program for viewing images
 * @version 1.1 2025-12-24
 * @author Cristian Martinez
 */
public class ImageViewer {
    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            var frame = new ImageViewerFrame();
            frame.setTitle("Image Viewer");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);
        });
    }
}
