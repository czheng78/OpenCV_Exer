# Copyright 2017 Chuan Xing Zheng czheng78@bu.edu

import cv2

Lenna = cv2.imread('Lenna.jpg')
cv2.imwrite('original.jpg',Lenna)

grayscaled = cv2.cvtColor(Lenna,cv2.COLOR_BGR2GRAY)

[retval,threshold] = cv2.threshold(grayscaled, 128, 255,2)
cv2.imshow('Thresholded',threshold)
cv2.imwrite('Thresholded.jpg',threshold)
[retval, thresh1] = cv2.threshold(grayscaled, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold',thresh1)
cv2.imwrite('Binary_Threshold.jpg',thresh1)

[retval,thresh2] = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY_INV)
[retval, thresh3] = cv2.threshold(grayscaled, 27, 255, cv2.THRESH_BINARY)

bandThresh = cv2.bitwise_and(thresh2,thresh3)
cv2.imshow('Banded Threshold',bandThresh)
cv2.imwrite('Banded_Threshold.jpg',bandThresh)

[retval,thresh4] = cv2.threshold(grayscaled,128,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
semiThresh = cv2.bitwise_and(grayscaled,thresh4)
cv2.imshow('Semi-Thresholded',semiThresh)
cv2.imwrite('Semi-Threshold.jpg',semiThresh)

thresh5 = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
cv2.imshow('Adaptive Threshold', thresh5)
cv2.imwrite('Adaptive_Threshold.jpg',thresh5)

cv2.waitKey(0)