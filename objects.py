import cv2
def take_image():
	camera_port = 0
	#Number of frames to throw away while the camera adjusts to light levels
	ramp_frames = 100
	camera = cv2.VideoCapture(camera_port)
	def get_image():
		retval, im = camera.read()
		return im
	for i in range(ramp_frames):
		temp = get_image()
	print("Taking image...")
	camera_capture = get_image()
	file = "cap_image.jpg"
	cv2.imwrite(file, camera_capture)
	# del(camera)
	cv2.imshow('Tack_image',camera_capture)

	return camera_capture


def resized(img,width):

	width = width
	height = int(img.shape[0]/(img.shape[1]/width))
	dim = (width, height)
	resized = cv2.resize(img,dim,interpolation =cv2.INTER_AREA)
	return resized

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

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)


