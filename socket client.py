
import androidhelper
import cv
import socket
droid=androidhelper.Android()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('enter your own same as in server',5005))
while True:
    flag=s.recv(4096)
    if flag=='ok':
        droid.cameraCapturePicture('/sdcard/caps/cap.jpg')
        img=cv.imread('/sdcard/caps/cap.jpg')
        img=cv.resize(img,(200,200))
        img_str = cv.imencode('.jpg', img)[1].tostring()
        print len(img_str)
        s.send(img_str)
        flag2=s.recv(4096)
s.close()
