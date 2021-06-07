#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


file_list = os.listdir('./')
img_files = [file for file in file_list if file.endswith('.jpg')]
imgsLen = len(img_files) + 1



def changeColor(val):
    pass
#---------------------------------------------------  

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.createTrackbar("mosaic", "frame", 0, imgsLen, changeColor)
cv2.setTrackbarPos("mosaic", "frame", 0)

#---------------------------------------------------  

    
while(1):
    
    _, frame= cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    imgSize = np.shape(frame)

    button = cv2.getTrackbarPos("mosaic", "frame")
    
#---------------------------------------------------
    if button == 1 :
        all_img = cv2.resize(frame, (imgSize[1]//15, imgSize[0]//15))
        all_img = cv2.resize(all_img, (imgSize[1], imgSize[0]), interpolation=cv2.INTER_AREA)
    elif button == 0 :
        all_img = frame
    else :
        img = cv2.imread(img_files[button-2])
        all_img = cv2.resize(img, (imgSize[1], imgSize[0]))
#---------------------------------------------------        
    for (x,y,w,h) in faces:
        roi = frame[y:y+h, x:x+w]
        all_img[y:y+h, x:x+h] = roi

#-----------------------------------        
        
    cv2.putText(all_img, "The 0th is original", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(all_img, "The 1st is mosaic.", (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(all_img, "from 2nd is photograph", (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(all_img, "Exit is key 'esc'", (imgSize[1]-150,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(all_img, "Please save the background picture as a jpg file .", (10,imgSize[0]-35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(all_img, "in the folder where the ipnd file is located.", (10,imgSize[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    
    
#---------------------------------------------------
    cv2.imshow('frame',all_img)
    
    k = cv2.waitKey(5) & 0xFF
    k2 = cv2.waitKey(5)
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




