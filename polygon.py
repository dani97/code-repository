# count polygon and angle in a given image


# coding: utf-8

# ## Mini Project 2 - Identifiy Contours by Shape

# In[3]:

import numpy as np
import cv2
import math
import sys

def get_contour_areas(contours):
    # returns the areas of all contours as list
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>25:
			all_areas.append(cnt)
    return all_areas

def calculateAngles(points):
	z=[]
	t=[]
	flag=False
	#arccos formula 
	for i in range(len(points)):
		pa=points[i][0]
		pb=points[(i+1)%len(points)][0]
		pc=points[(i+2)%len(points)][0]
		lab = ((pa[0]-pb[0])**2+(pa[1]-pb[1])**2)**0.5
		lbc = ((pb[0]-pc[0])**2+(pb[1]-pc[1])**2)**0.5
		lca = ((pc[0]-pa[0])**2+(pc[1]-pa[1])**2)**0.5
		val = (lab**2+lbc**2-lca**2)/(2*lca*lab)
		f=True
		#cos range checking[-1,1]
		if abs(val)>1:
			val=(lbc**2+lca**2-lab**2)/(2*lbc*lab)
			f=False
			if abs(val)>1:
				f=False
				val=(lca**2+lab**2-lbc)/(2*lca*lbc)
		angle = math.degrees(math.acos(val))
		if not f:
			angle=90-angle
		z.append(int(round(angle)))
		t.append(int(round(lab)))
	z.sort()
	z=z[::-1]
	k=z[0]
	for i in z:
		if i!=k:
			break
	else:
		flag=True
	k=t[0]
	for i in t:
		if i!=k:
			break
	else:
		flag=True and flag
			
	for i in z:
		print i,
	if flag:
		print "Y"
	else:
		print "N"
	return
	
		
# Load and then gray scale image
inputFile=sys.argv[1]
image = cv2.imread(inputFile)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Identifying Shapes',gray)
cv2.waitKey(0)
ret, thresh = cv2.threshold(gray, 245,255,1)
#cv2.imshow('thresh',thresh)
# Extract Contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours=get_contour_areas(contours)
#print len(contours)
image1=image.copy()
#cv2.drawContours(image1,contours,-1,(0,255,0),3)
contours = sorted(contours,key=cv2.contourArea,reverse=True)


for cnt in contours:
    # Get approximate polygons
    #print cnt
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)
    print len(approx),
    cv2.drawContours(gray,[cnt],0,(0,255,0),-1)
    calculateAngles(approx)

    
cv2.destroyAllWindows()

