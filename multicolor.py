import cv2
import numpy as np


def main():
    # Create a black image
    img = np.zeros((300, 500, 3), dtype=np.uint8)

    # Draw 5 columns of color shades
    for i in range(5):
        # Blue row
        img[0:100, i * 100:(i + 1) * 100] = (255, 0, 255 - i * 50)

        # Green row
        img[100:200, i * 100:(i + 1) * 100] = (0, 255 - i * 50, 0)

        # Red row
        img[200:300, i * 100:(i + 1) * 100] = (0, 0, 255 - i * 50)

    # Show the image
    cv2.imshow("Color Shades Using Pixels", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image
    cv2.imwrite("colorshades.png", img)


if __name__ == "__main__":
    main()