import cv2
import numpy as np

def rectify(h):
	h = h.reshape((4,2))
	hnew = np.zeros((4,2),dtype = np.float32)
	add = h.sum(1)
	hnew[0] = h[np.argmin(add)]
	hnew[2] = h[np.argmax(add)]
	diff = np.diff(h,axis = 1)
	hnew[1] = h[np.argmin(diff)]
	hnew[3] = h[np.argmin(diff)]
	return hnew

def wrap_image(img):

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	#  noise removal and thresholding
	gray = cv2.GaussianBlur(gray,(5,5),0)
	thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

	# find the contours
	contous, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	biggest = None
	max_area = 0
	for i in contous:
		area = cv2.contourArea(i)
		if area > 100:
			peri = cv2.arcLength(i,True)
			approx = cv2.approxPolyDP(i,0.02*peri,True)
			if area > max_area and len(approx)==4:
				biggest = approx
				max_area = area
	x1 = biggest[0]
	x2 = biggest[1]
	x3 = biggest[2]
	x4 = biggest[3]

	w = np.float32([x1,x4,x2,x3])

	h = np.float32([[0,0],[img.shape[1],0],[0,img.shape[0]],[img.shape[1],img.shape[0]]])
		
	retval = cv2.getPerspectiveTransform(w,h)
	warp = cv2.warpPerspective(img,retval,(img.shape[1],img.shape[0]))

	return warp


