import numpy as np
import cv2 

thresh = 110

def process(conts):
	# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# ret, threshed_img = cv2.threshold(gray,thresh, 255, cv2.THRESH_BINARY_INV)

	# imag, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	# cv2.drawContours(img,contours,-1,(0,255,0),1)


	# cv2.imshow('s',img)
	x=[]
	y=[]
	xM =[]
	yM=[]

	for indx,i in enumerate(conts):
	    x.append([])
	    y.append([])     
	    xM.append([])     
	    yM.append([])     
	    for j in i:
	        x[indx].append(j[0][0])
	        y[indx].append(j[0][1])

	ob = len(conts)

	ex = 50
	ey = 90
	emid = [ex/2,ey/2]

	# equal to eraser 
	for j in range(len(x)):
		for i in range(len(x[j])):
			xmin = min(x[j])
			xmax = max(x[j])
			ymin = min(y[j])
			ymax = max(y[j])
			dx = xmax-xmin
			dy = ymax-ymin
			if ex >= dx:
				if ey >= dy:
					print('X',int((xmax+xmin)/2),'Y',int((ymin+ymax)/2))
					break
				elif ey <= dy:
					print('Y1',ymin,'Y2',ymax)
					break

			elif ex <= dx:
				if ey >= dy:
					print('X1',xmin,'X2',xmax)
					break
				if ey <= dy:
					print('X',x[j][i],'Y',y[j][i])
					
		print('Compled Object',j+1)
