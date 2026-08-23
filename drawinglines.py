import cv2
import numpy as np

# Canvas layer to hold drawn strokes
canvas = None
drawing = False
last_pt = None

def draw_brush(event, x, y, flags, param):
    global drawing, last_pt, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_pt = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        if last_pt is not None:
            # Draw continuous line segments as mouse moves (Red, thickness 4)
            cv2.line(canvas, last_pt, (x, y), (0, 0, 255), 4)
            last_pt = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        last_pt = None

cap = cv2.VideoCapture(0)
cv2.namedWindow('Freehand Line Drawing')
cv2.setMouseCallback('Freehand Line Drawing', draw_brush)

print("Controls:\n - Click & Drag to draw\n - Press 'c' to clear\n - Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Combine video frame with freehand drawings
    output = cv2.add(frame, canvas)

    cv2.imshow('Freehand Line Drawing', output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)  # Clear screen

cap.release()
cv2.destroyAllWindows()