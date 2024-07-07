import time
import cv2
import urllib.request
import numpy as np
import imutils


cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

cascade_src1 = 'ambulance.xml'
car_cascade1 = cv2.CascadeClassifier(cascade_src1)

ip_cam=["100.83.81.182:8080"]


try:
    while True:
        detected = [0]
        for ip in range(len(ip_cam)):
            url="http://"+ip_cam[ip]+"/shot.jpg"
            imgPath=urllib.request.urlopen(url)
            imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
            img=cv2.imdecode(imgNp,-1)
            img=imutils.resize(img,width=500)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            amb = car_cascade1.detectMultiScale(gray, 1.1, 1)
            
            for (x,y,w,h) in cars:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

            for (x1,y1,w1,h1) in amb:
                cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)
                
                print("Ambulance detected..!!")
                
            cv2.imshow(str(ip), img)                      
            b=str(len(cars))
            a= int(b)
                      
          #  print("Number of Vehicles")            
           # print ("%d" % int(a))
            
           # time.sleep(0)
            
            if cv2.waitKey(1):
                break
                
except KeyboardInterrupt:            
    cv2.destroyAllWindows()


