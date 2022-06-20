import cv2
import numpy as np

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim=(width, height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    frame=rescale_frame(frame,percent=47)
    cv2.rectangle(frame,(0,0),(150,30),(255,255,255),-1)
    frame=cv2.putText(frame,"Original Image",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_blue=np.array([90,170,160])
    upper_blue=np.array([130,255,255])
    mask_blue=cv2.inRange(hsv,lower_blue,upper_blue)
    res_blue=cv2.bitwise_and(frame,frame,mask=mask_blue)
    cv2.rectangle(res_blue,(0,0),(150,30),(255,255,255),-1)
    res_blue=cv2.putText(res_blue,"Blue Color",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)

    lower_green=np.array([60,170,160])
    upper_green=np.array([80,255,255])
    mask_green=cv2.inRange(hsv,lower_green,upper_green)
    res_green=cv2.bitwise_and(frame,frame,mask=mask_green)
    cv2.rectangle(res_green,(0,0),(150,30),(255,255,255),-1)
    res_green=cv2.putText(res_green,"Green Color",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)

    lower_red=np.array([0,35,210])
    upper_red=np.array([10,255,255])
    mask_red=cv2.inRange(hsv,lower_red,upper_red)
    res_red=cv2.bitwise_and(frame,frame,mask=mask_red)
    cv2.rectangle(res_red,(0,0),(150,30),(255,255,255),-1)
    res_red=cv2.putText(res_red,"Red Color",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    
    lower_yellow=np.array([20,0,240])
    upper_yellow=np.array([80,255,255])
    mask_yellow=cv2.inRange(hsv,lower_yellow,upper_yellow)
    res_yellow=cv2.bitwise_and(frame,frame,mask=mask_yellow)
    cv2.rectangle(res_yellow,(0,0),(150,30),(255,255,255),-1)
    res_yellow=cv2.putText(res_yellow,"Yellow Color",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)

    lower_purple=np.array([140,20,160])
    upper_purple=np.array([160,255,255])
    mask_purple=cv2.inRange(hsv,lower_purple,upper_purple)
    res_purple=cv2.bitwise_and(frame,frame,mask=mask_purple)
    cv2.rectangle(res_purple,(0,0),(150,30),(255,255,255),-1)
    res_purple=cv2.putText(res_purple,"Purple Color",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    
    hor1=cv2.hconcat([frame,res_blue])
    hor2=cv2.hconcat([res_green,res_red])
    hor3=cv2.hconcat([res_yellow,res_purple])
    concat=cv2.vconcat([hor1,hor2,hor3])
    
    cv2.imshow('Color Segmentation',concat)
    
    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()
