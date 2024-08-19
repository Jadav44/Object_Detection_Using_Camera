from ultralytics import YOLO
import cv2
import cvzone
import math
import time

cap = cv2.VideoCapture(0)  # For Webcam
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img=cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)
