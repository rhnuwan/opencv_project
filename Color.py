import cv2
import numpy as np

# Red
r_lower = np.array([10,40,60])
r_upper = np.array([100,255,255])

#Blue
b_lower = np.array([20,100,100])
b_upper = np.array([170,255,255])

#Green
g_lower = np.array([10,40,60])
g_upper = np.array([100,255,255])


def setColor(img, color):
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	if(color == 'red'):
		mask = cv2.inRange(img, r_lower, r_upper)
	elif(color == 'blue'):
		mask = cv2.inRange(hsv,b_lower,b_upper)
	elif(color == 'green'):
		mask = cv2.inRange(img, g_lower,g_upper)
	else:
		print("Not Color Range")

	image = cv2.bitwise_and(img,img,mask = mask)

	return mask, image

def getColor_Mask(img, color):
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	if(color == 'red'):
		mask = cv2.inRange(img, r_lower, r_upper)
	elif(color == 'blue'):
		mask = cv2.inRange(hsv,b_lower,b_upper)
	elif(color == 'green'):
		mask = cv2.inRange(img, g_lower,g_upper)
	else:
		print("Not Color Range")

	return mask