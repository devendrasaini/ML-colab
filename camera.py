import cv2
#starting camera 
cap=cv2.VideoCapture(0)
#  first camera
# to check camera started or not
if cap.isOpened() :
        print("camera is readuy to take picture")
else :
        print("check your drivers")
#now we can take read input from camera
status,img=cap.read()
status1,img1=cap.read()
cv2.imshow('liveimage',img)
cv2.imshow('liveimage1',img1)
cv2.waitKey(0)
#to close camera
cap.release()

