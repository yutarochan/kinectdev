'''
Harris Corner Detection Algorithm
Detects all relevant vertecies from camera.

TODO: Map this together with depth map.
'''
import cv2
import freenect
import numpy as np

fgbg = cv2.BackgroundSubtractorMOG()

def getDepth():
	depth, timestamp = freenect.sync_get_depth()
	return depth

def getVideo():
	image, timestamp = freenect.sync_get_video()
	return image

while True:
	img = getVideo()
	g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	gray = np.float32(g_img)
	dst = cv2.cornerHarris(gray, 2, 1, 0.01)
	'''
	Corner Harris Parameters:
	- image (8bit input img)
	- block size
	- apeture size
	- haris detect param

	adjust and play around with parameters accordingly...
	more info: http://docs.opencv.org/modules/imgproc/doc/feature_detection.html?highlight=cornerharris#cv.CornerHarris
	'''

	dst = cv2.dilate(dst, None)
	img[dst > 0.01 * dst.max()] = [0, 0, 255]

	cv2.imshow('image', img)

	#window exit
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
