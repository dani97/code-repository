#count number of circles in a given image
#usage circleCount.py filename


import cv2
import numpy as np
import cv2.cv as cv
import sys

def countCircle(output_img):
	output_img = cv2.cvtColor(output_img,cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(output_img, 30,255,1)
	contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	all_areas = []
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area>30:
			all_areas.append(cnt)
	contours=all_areas
	image1=image.copy()
	count=0
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)
		if(len(approx))>=10:
			count+=1
	return count


Input = sys.argv[1]
image = cv2.imread(Input)
img_hsv=cv2.cvtColor(image.copy(), cv2.COLOR_BGR2HSV)
#blue color
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask0 = cv2.inRange(img_hsv, lower_blue, upper_blue)
output_img = image.copy()
output_img[np.where(mask0==0)] = 0
blue=countCircle(output_img)
#red color
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
output_img = image.copy()
output_img[np.where(mask1==0)] = 0
red=countCircle(output_img)

#green color
lower_green =np.array([50,100,100])
upper_green=np.array([70,255,255])
mask2 = cv2.inRange(img_hsv, lower_green, upper_green)
output_img = image.copy()
output_img[np.where(mask2==0)] = 0
green=countCircle(output_img)

print red,green,blue



