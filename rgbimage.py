import cv2
import matplotlib
import numpy as np
import datetime
from datetime import datetime, timedelta

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

dts = [dt.strftime('%Y%m%d%H%M%S_0.jpg ') for dt in 
       datetime_range(datetime(2018, 4, 10, 0, 0), datetime(2018, 4, 10,0, 11), 
       timedelta(minutes=1))]

calculation_time=(np.asarray(dts))

# image=np.zeros[11,1]

# for n in range (len(dts)):
#     image=cv2.imread(dts[n],1)
image=cv2.imread('20180410000000_0.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
a=image[:,:,0]
b=image[:,:,1]
c=image[:,:,2]
# a=print(image[2])
   
# for i in range(10):
#     red_channel=image1[:,:,2]
# #     # green_channel[n]=image[n][:,:,1]
# #     # blue_channel[n]=imagen[n][:,:,0]

# image=cv2.imread(dts[5])
cv2.imshow('image',np.hstack([a,b,c]))
cv2.waitKey(0)
cv2.destroyAllWindows()


# for n in calculation_time:
#     image[n]=cv2.imread('dts[n]')
