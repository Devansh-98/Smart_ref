from process_img import *
import cv2
from datetime import date
from datetime import datetime
import time


num = 1


cam=cv2.VideoCapture(1);

while(True):
    today = date.today()
    now = datetime.now().time()
    now = str(now)
    qw = now.replace(":","-")
    ret,img = cam.read()
    img_name="Data/" + str(num) + "_" + str(today) + "_" + qw + ".jpg"
    detect_labels_cloud_storage("C:/Users/HP/Desktop/Fridge/" + img_name)
    time.sleep(2)
    num=num+1
    if(num>5):
        break;

cam.release()
cv2.destroyAllWindows()
