import cv2
from datetime import datetime

# Open the default camera
camera = cv2.VideoCapture(0)

# Check if camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read frame from camera
    ret, frame = camera.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Get current date and time
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Display time on camera
    cv2.putText(
        frame,
        "Time: " + current_time,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display date on camera
    cv2.putText(
        frame,
        "Date: " + current_date,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Show camera window
    cv2.imshow("Camera - Live Time", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
camera.release()
cv2.destroyAllWindows()