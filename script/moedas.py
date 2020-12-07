#! /usr/local/python

import cv2
import numpy as np
import matplotlib.pyplot as plt

print "OpenCV version:", cv2.__version__


img = cv2.imread('../img/moedas.png')

print "shape tuple RGB:", img.shape
print "height:", img.shape[0], "width:", img.shape[1], "channels:", img.shape[2]

cv2.imshow('img_gray', img)
cv2.waitKey(0)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask1 = cv2.inRange(imgHSV, (15, 10, 10), (36, 250, 200))
mask2 = cv2.inRange(imgHSV, (0, 100, 10), (20, 150, 100))

mask = cv2.bitwise_or(mask1, mask2)

cv2.imshow('mask', mask)
cv2.waitKey(0)

kernel = np.ones((3, 3),np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

cv2.imshow('opening', opening)
cv2.waitKey(0)

dilation = cv2.dilate(opening, kernel,iterations=7)
cv2.imshow('dilation', dilation)
cv2.waitKey(0)

im, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw contours:
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow('target', img)
cv2.waitKey(0)