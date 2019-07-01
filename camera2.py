import cv2
#starting camera 
cap=cv2.VideoCapture(0)
#  first camera
# to check camera started or not
while cap.isOpened() :
    status,frame=cap.read()
    graying=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #now we can draw all those pattern
    #line
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
    #rectangle
    cv2.rectangle(frame,(50,50),(150,200),(0,0,255),3)
    cv2.circle(frame,(200,300),100,(0,255,255),3)
    cv2.imshow('live',frame)
    


    #cv2.imshow('live2',graying)
    if cv2.waitKey(10) & 0xff == ord('q') :
       break
cv2.destroyAllWindows()
cap.release()


