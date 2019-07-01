import cv2
#starting camera 
cap=cv2.VideoCapture(0)
#  first camera
# to check camera started or not
#adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
#saving video
output=cv2.VideoWriter('class.mp4',plugin,10,(640,480))



while cap.isOpened() :
    status,frame=cap.read()
   
    output.write(frame)

    cv2.imshow('live',frame)
    


    #cv2.imshow('live2',graying)
    if cv2.waitKey(10) & 0xff == ord('q') :
       break
cv2.destroyAllWindows()
cap.release()


