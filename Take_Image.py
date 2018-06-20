import cv2

def take_image():
	camera_port = 1
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
	cv2.imshow('Im',camera_capture)

	return camera_capture