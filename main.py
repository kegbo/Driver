from __future__ import print_function
from pynput.keyboard import Key, Listener
#from PiVideoStream import PiVideoStream
#from imutils.video import FPS
#from picamera.array import PiYUVArray
#from picamera import PiCamera
import argparse
import imutils
import time
import cv2
#import socket
import drive
import time
import csv

#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#IP = '192.168.8.2'
#PORT = 5000
#server_address = (IP,PORT)
#sock.connect(server_address)
#sock.sendall('connected')



Forward = [8,11,13,18]
Reverse = [7,10,16,19]

Left = [8,18]
Right = [11,13]


F_Left = [8,18,13]
F_Right = [11,13,18]

R_Left = [10,7,16]
R_Right = [10,7,19]

Spin_F_Left = [8,18,10,19] 
Spin_F_Right = [11,13,7,16]

Spin_R_Left = [7,16,11,13] 
Spin_R_Right = [10,19,8,18]

Spot_F_Left = [8,18,13,10]
Spot_F_Right = [11,13,18,7]

Spot_R_Left = [10,7,16,19]
Spot_R_Right = [10,7,19,16]


L_M1 = [10, 11]
R_M1 = [8, 7]
L_M2 =[15,19]
R_M2 = [16,18]


def printtofile(image,direction):
        with open('dataset.csv', 'a+') as fp:
                a = csv.writer(fp, delimiter=',')
                data = [[image,direction]]
                a.writerows(data)
def on_press(key):       
                #frame = vs.read()
                frame = 'Evangelion'                            
                if key == Key.esc:
                        drive.stop()
                        cv2.destroyAllWindows()
                        #vs.stop()
                        return False
                if key == Key.up:
                        drive.move(Forward)
                        print('foward')
                        printtofile(frame,'forward')
                if key == Key.down:
                        drive.move(Reverse)
                        print('reverse')
                        printtofile(frame,'reverse')
                if key == Key.left:
                        drive.move(Left)
                        print('left')
                        printtofile(frame,'left')
                if key == Key.right:
                        drive.move(Right)
                        print('right')
                        printtofile(frame,'right')
                if key == Key.page_up:
                        drive.move(F_Right)
                        print('f_right')
                        printtofile(frame,'f_right')
                if key == Key.home:
                        drive.move(F_Left)
                        print('f_left')
                        printtofile(frame,'f_left')
                if key == Key.page_down:
                        drive.move(R_Right)
                        print('r_right')
                        printtofile(frame,'r_right')
                if key == Key.end:
                        drive.move(R_Left)
                        print('r_left')
                        printtofile(frame,'r_left')                
                if key == Key.f1:
                        drive.move(Spin_F_Left)
                        print('spot_f_left')
                        printtofile(frame,'spin_f_left')
                if key == Key.f2:
                        drive.move(Spin_F_Right)
                        print('spin_f_right')
                        printtofile(frame,'spin_f_left')
                if key == Key.f3:
                        drive.move(Spin_R_Left)
                        print('spin_r_left')
                        printtofile(frame,'spin_r_left')
                if key == Key.f4:
                        drive.move(Spin_R_Right)
                        print('spin_r_right')
                        printtofile(frame,'spin_r_right')
                if key == Key.f5:
                        drive.move(Spot_F_Right)
                        print('spot_f_right')
                        printtofile(frame,'r_left')
                if key == Key.f6:
                        drive.move(Spot_F_Left)
                        print('spot_f_left')
                        printtofile(frame,'spot_f_left')
                if key == Key.f7:
                        drive.move(Spot_R_Right)
                        print('spot_r_right')
                        printtofile(frame,'spo_r_left')
                if key == Key.f8:
                        drive.move(Spot_R_Left)
                        print('spot_r_left')
                        printtofile(frame,'r_left')
                #if key == Key.enter:
                #        drive.stop()
                #        print('stop')
                #        printtofile(frame,'stop')
                if key == Key.delete:
                        drive.stop()
                        drive.cleanup()
                        print('STOP AND CLEANUP')

print("[INFO] sampling THREADED frames from `picamera` module...")
#vs = PiVideoStream().start()
#time.sleep(2.0)
drive.setup()

with Listener(on_press=on_press) as listener:
	listener.join()
	
