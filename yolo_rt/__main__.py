import cv2
import numpy as np

from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('videoplayback.webm')
# Loop over frames from the video capture device
while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()

    
    res = model(frame)
        
    res_plotted = res[0].plot()
    cv2.imshow("result", res_plotted)

    cv2.imshow('Real-time object detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the video capture device and close the window
cap.release()
cv2.destroyAllWindows()