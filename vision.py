import cv2
import numpy as np
from Take_Image import take_image
from Resize import resized,setside
from wrap_image import wrap_image
import Color as col
from Process import process
cap = take_image()
rimg = resized(cap,600)
img = wrap_image(rimg)

# img = cv2.imread('image01_r.jpg')

image = setside(img,'1')
# cv2.imshow('side',image)

blurr = cv2.GaussianBlur(image,(5,5),0)
# detect color
# lower = np.array([10,40,80])
# upper = np.array([150,255,255])

lower = np.array([10,40,80])
upper = np.array([100,250,250])


mask = cv2.inRange(blurr,lower,upper)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv = cv2.bitwise_and(gray,mask)
cv2.imshow('maks',mask)
t1,th1 = cv2.threshold(gray,110,255, cv2.THRESH_BINARY_INV)

t,thresh = cv2.threshold(mask,110,255,cv2.THRESH_BINARY)

cnts,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image,cnts,-1,(0,255,0),1)




# for cnt in cnts:
# 	print(cnt)
# 	cntarea = cv2.contourArea(cnt)
# 	if cntarea > 0 :
# 		print(cntarea)
# 		cv2.drawContours(image,cnt,-1,(0,255,0),1)
	
process(cnts)

cv2.imshow('Res',image)


cv2.waitKey(0)