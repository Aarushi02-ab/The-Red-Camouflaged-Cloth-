import numpy as np
import cv2
import time
import music

# catching the background frame


cap1=cv2.VideoCapture(0)#Reading web cam

time.sleep(3) #for the system to sleep for 3 second before the webcam starts
for i in range(30):
    retval,back=cap1.read()
back=np.flip(back,axis=1)
cap1=cv2.VideoCapture(0)  

## detecting the red portion In each frame


while (cap1.isOpened()):  ##Read every Frame from the webcam, until the camera is open 
    ret,img=cap1.read()
    if ret:
        img=np.flip(img,axis=1)
        
        ##convert the color space from BGR to HSV
        hsv_color_space=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        
        ##Generat masks to detect red color
        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])
        m1 = cv2.inRange(hsv_color_space,lower_red,upper_red)
        
        lower_red = np.array([170,120,70])
        upper_red = np.array([180,255,255])
        m2 = cv2.inRange(hsv_color_space,lower_red,upper_red)
        m1+=m2
        
        #Replacing the red portion with a mask image in each frame

        m = cv2.morphologyEx(m1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
        img[np.where(m==255)]=back[np.where(m==255)]
        
         #Final output shown on the webcam
        cv2.imshow("Hey watch! The red colour got camoflauged!",img)
        import music
    key = cv2.waitKey(1)
    if key==ord("e"):
        break
cap1.release()
cv2.destroyAllWindows()