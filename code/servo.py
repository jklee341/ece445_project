from picamera2 import Picamera2
import cv2
from ultralytics import YOLO

# Initialize PiCamera2
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'BGR888', "size": (640, 480)}))
picam2.start()

model = YOLO("yolov8n.pt")

# Main streaming loop
while True:
    # Capture frame from PiCamera2
    frame = picam2.capture_array()

    # Display frame
    frame_resize = cv2.resize(frame, (640, 480))

    model.predict(frame_resize, show = True)
    

# Clean up
picam2.stop()
#cv2.destroyAllWindows()
