from ultralytics import YOLO
import cv2
#testing commit to git
model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("Images/Cars.jpg", show=True)
cv2.waitKey(0)