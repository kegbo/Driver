# import the necessary packages
from __future__ import print_function
#from imutils.video.pivideostream import PiVideoStream
from PiVideoStream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiYUVArray
from picamera import PiCamera
import argparse
import imutils
import time
import cv2
 



print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream().start()
time.sleep(2.0)


while True:	
	frame = vs.read()
	print(frame)
	#frame = imutils.resize(frame, width=400)
	#frame = frame[:, :, 0]
	#cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

my_file.close()
cv2.destroyAllWindows()
vs.stop()

