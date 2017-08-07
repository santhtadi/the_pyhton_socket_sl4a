# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 18:58:25 2017

@author: santh
"""
import cv2
import numpy as np
img=cv2.imread("cable.jpg")
img_str = cv2.imencode('.jpg', img)[1].tostring()
print type(img_str)
nparr = np.fromstring(img_str, np.uint8)
img2=img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
