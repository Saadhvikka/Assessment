
import cv2
import numpy as np

img = cv2.imread( '/Users/venkatachalam/Desktop/25.jpg' )
x, y, z = img.shape


lower = np.array([0,0,0])  
upper = np.array([220,220,220])  
mask = cv2.inRange(img, lower, upper)
res = cv2.bitwise_and(img, img, mask= mask)  
cv2.imshow('Result',res)
bgr = [40, 158, 16]
thresh = 40
 
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
 
maskBGR = cv2.inRange(img,minBGR,maxBGR)
resultBGR = cv2.bitwise_and(img, img, mask = maskBGR)
cv2.imshow("Result BGR", resultBGR)
