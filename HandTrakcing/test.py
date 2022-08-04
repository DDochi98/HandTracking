import cv2 as cv
import numpy as np
import time
import os

wCam, hCam = 640, 480

cap = cv.VideoCapture(1)
cap.set(3,wCam)
cap.set(5,hCam)

while True:
    _, img = cap.read()
    #cv.imshow('video',img)
    #cv.waitKey(1)
    hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([0, 48, 80], dtype="uint8")
    upper = np.array([20, 255, 255], dtype="uint8")
    skinRegionHSV = cv.inRange(hsvim, lower, upper)
    blurred = cv.blur(skinRegionHSV, (2, 2))
    ret, thresh = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY)
    cv.imshow('thresh', thresh)
    cv.waitKey(0)

img_path = "D:\python\HandTrakcing\hand5.jpeg"
img = cv.imread(img_path)
cv.imshow('five',img)
cv.waitKey(0)

hsvim = cv.cvtColor(img,cv.COLOR_BGR2HSV)
lower = np.array([0,48,80],dtype = "uint8")
upper = np.array([20,255,255],dtype="uint8")
skinRegionHSV = cv.inRange(hsvim, lower, upper)
blurred = cv.blur(skinRegionHSV,(2,2))
ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
cv.waitKey(0)