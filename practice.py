import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
img = cv2.imread('cell-count-data/test0/img0.jpg')

result = model(img)
print(result)