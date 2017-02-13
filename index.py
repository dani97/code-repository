import cv2
import numpy as np
im1 = cv2.imread("sad1.jpg")
cv2.imshow("Original Image",im1)
rm = np.random.randn(5,5)
rm = np.ones((5,5))/20
print rm
im2 = cv2.filter2D(im1, -1, rm)
cv2.imshow("Gaussain ",im2)
cv2.waitKey()
