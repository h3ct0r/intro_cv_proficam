#! /usr/local/python

import cv2
import numpy as np
import matplotlib.pyplot as plt

print "OpenCV version:", cv2.__version__


img = cv2.imread('mine_worker.jpg')

print "shape tuple RGB:", img.shape
print "height:", img.shape[0], "width:", img.shape[1], "channels:", img.shape[2]

#cv2.imshow('image', img)
#cv2.waitKey(0)


img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print "shape tuple GRAY:", img_gray.shape
print "height:", img_gray.shape[0], "width:", img_gray.shape[1]

# cv2.imshow('image_gray', img_gray)
# cv2.waitKey(0)

img_crop = img_gray[170:320, 260:410]
print "shape tuple img_crop:", img_crop.shape
# cv2.imshow('image_gray', img_crop)
# cv2.waitKey(0)

img_roi = img.copy()
cv2.rectangle(img_roi, (110,170), (540, 610), (255, 0, 0), 4)
cv2.rectangle(img_roi, (420, 250), (550, 450), (0, 0, 198), 4)
cv2.imshow('img_roi', img_roi)
cv2.waitKey(0)