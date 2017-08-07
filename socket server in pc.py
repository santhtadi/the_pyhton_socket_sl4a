# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 17:35:04 2017

@author: santh
"""

import cv2
import socket
import numpy as np
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("enter your own", 5005))
server_socket.listen(1)
client_socket, address = server_socket.accept()
print "android connected"
while True:
    flag=raw_input("enter ok if you want to recieve another picture: ")
    if flag=='ok':
        try:
            client_socket.send('ok')
            img_str=client_socket.recv(4096000)
            client_socket.send("ko")
            nparr = np.fromstring(img_str, np.uint8)
            img2=cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
            cv2.imwrite("x.jpg",img2)
            cv2.imshow("captured",img2)
            cv2.waitKey(0)
        except:
            pass
    else:
        client_socket.send('no')
        break
client_socket.close()
server_socket.close()
cv2.destroyAllWindows()    