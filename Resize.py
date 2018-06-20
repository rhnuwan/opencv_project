import cv2

def scale_image(img,scale_percent):
	scale_percent = 20 # percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	return resized

def resized(img,width):

	width = width
	height = int(img.shape[0]/(img.shape[1]/width))
	dim = (width, height)
	resized = cv2.resize(img,dim,interpolation =cv2.INTER_AREA)
	return resized

def setside(img,side):
	hight, width = img.shape[:2]
	r = 15
	# yStrat y end xStrat x end
	crop = img[r:hight-r,r:width-r]

	h,w = crop.shape[:2]
	print(w,h)
	centerX = int(w/2)
	centerY = int(h/2)
	
	if side == '1':
		crop2 = crop[0:centerY, 0:centerX]
	elif side == '2':
		crop2 = crop[0:centerY, centerX:w]
	elif side == '3':
		crop2 = crop[centerY:h, 0:centerX]
	elif side == '4':
		crop2 = crop[centerY:h, centerX:w]
	
	image = cv2.resize(crop2,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
	
	return image


