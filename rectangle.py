import cv2
import numpy as np

# Create a white image
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

points = []

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global img, points

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

        # Draw a small circle where clicked
        cv2.circle(img, (x, y), 4, (0, 0, 255), -1)

        # Draw rectangle after two clicks
        if len(points) == 2:
            cv2.rectangle(img, points[0], points[1], (255, 0, 0), 2)
            print("Rectangle Drawn!")

cv2.namedWindow("Rectangle")
cv2.setMouseCallback("Rectangle", draw_rectangle)

while True:
    cv2.imshow("Rectangle", img)

    key = cv2.waitKey(1) & 0xFF

    # Press 'r' to reset
    if key == ord('r'):
        img = np.ones((500, 500, 3), dtype=np.uint8) * 255
        points = []

    # Press ESC to exit
    elif key == 27:
        break

cv2.destroyAllWindows()