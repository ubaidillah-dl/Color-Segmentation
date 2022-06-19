import cv2
import numpy as np

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim=(width, height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

camera=cv2.VideoCapture(0)

while True:
    _,frame=camera.read()
    image=rescale_frame(frame,percent=70)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv=rescale_frame(hsv,percent=50)
    frame2=rescale_frame(frame,percent=50)
    
    #Blue
    lower_blue=np.array([90,50,70])
    upper_blue=np.array([128,255,255])
    mask_blue=cv2.inRange(hsv,lower_blue,upper_blue)
    mask_blue=cv2.cvtColor(mask_blue,cv2.COLOR_GRAY2BGR)
    
    #Green
    lower_green=np.array([60,50,70])
    upper_green=np.array([89,255,255])
    mask_green=cv2.inRange(hsv,lower_green,upper_green)
    mask_green=cv2.cvtColor(mask_green,cv2.COLOR_GRAY2BGR)
    
    #Yellow
    lower_yellow=np.array([20,100,120])
    upper_yellow=np.array([50,255,255])
    mask_yellow=cv2.inRange(hsv,lower_yellow,upper_yellow)
    mask_yellow=cv2.cvtColor(mask_yellow,cv2.COLOR_GRAY2BGR)
    
    #Red
    lower_red=np.array([0,30,40])
    upper_red=np.array([10,255,255])
    mask_red=cv2.inRange(hsv,lower_red,upper_red)
    mask_red=cv2.cvtColor(mask_red,cv2.COLOR_GRAY2BGR)

    cv2.rectangle(image,(0,0),(150,30),(255,255,255),-1)
    cv2.rectangle(mask_blue,(0,0),(150,30),(255,255,255),-1)
    cv2.rectangle(mask_green,(0,0),(150,30),(255,255,255),-1)
    cv2.rectangle(mask_yellow,(0,0),(150,30),(255,255,255),-1)
    cv2.rectangle(mask_red,(0,0),(150,30),(255,255,255),-1)
    
    image=cv2.putText(image,"Original Image",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    mask_blue=cv2.putText(mask_blue,"Blue",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    mask_green=cv2.putText(mask_green,"Green",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    mask_yellow=cv2.putText(mask_yellow,"Yellow",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    mask_red=cv2.putText(mask_red,"Red",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    
    hor1=np.hstack((mask_blue,mask_green))
    hor2=np.hstack((mask_yellow,mask_red))
    hor1n2=np.vstack((hor1,hor2))
    
    stacked=np.vstack((image,hor1n2))
    cv2.imshow('Color Segmentation',stacked)
    
    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()