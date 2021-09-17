# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:00:56 2021

@author: MOONKNIGHT
"""
import numpy as np
import cv2
import sys
import urllib
import urllib.request

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier(r'C:\Users\kesha\Desktop\People-Counting-in-Real-Time\Face_Detection\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5
        ,     
        minSize=(20, 20)
    )
    i=0
    for (x,y,w,h) in faces:
    #for face in faces:
        #x, y = face.left(), face.top()
        #x1, y1 = face.right(), face.bottom()
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        i+=1
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if(x<=320 and y>240 and (x+w)<=320 and (y+h)>240):
            cv2.putText(img, 'face num'+str(i)+'-Q1',(x-10, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
            print("Q1")
        elif(x<320 and y<240 and (x+w)<320 and (y+h)<240):
            cv2.putText(img, 'face num'+str(i)+'-Q2',(x-10, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
            print("Q2")
        elif(x>320 and y<=240 and (x+w)>320 and (y+h)<=240):
            cv2.putText(img, 'face num'+str(i)+'-Q3',(x-10, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
            print("Q3")
        elif(x>320 and y>240 and (x+w)>320 and (y+h)>240):
            cv2.putText(img, 'face num'+str(i)+'-Q4',(x-10, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
            print("Q4")
        else:
            cv2.putText(img, 'face num'+str(i)+'-None',(x-10, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
            print("None")
    if(i>0):
        print(i)
        r=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=6L6YWQQ9TTQQP2YG&field1='+str(i))
    #print(x,y,(x+w),(y+h))
        
    cv2.imshow('video',img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()