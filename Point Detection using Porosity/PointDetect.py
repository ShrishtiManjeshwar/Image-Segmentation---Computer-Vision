import cv2
import numpy as np
import time
img = cv2.imread("point.jpg", 0)
ele=np.full((3,3),-1)
ele[1][1]=8
e_r=ele.shape[1]
e_c=ele.shape[0]
r=len(img)
c=len(img[0])
pad_0=[[0]*(c+2) for i in range(0,r+2)]

for i in range(1,r):
    for j in range(1,c):
        pad_0[i][j]=img[i-1][j-1]
        
im=np.asarray(pad_0)

thres=823
conv=[[0] * c for i in range(r)]
conI=[[0] * c for i in range(r)]

for x in range(1,r-1):
    for y in range(1,c-1):
        sum1=0
        for k in range(3):
            for l in range(3):
                sum1+=im[x+k-1][y+l-1]*ele[k][l]        
        conI[x-1][y-1]=sum1

        if(abs(sum1)>thres):
            conv[x-1][y-1]=255
            print("The x coordinate is",y-1)
            print("The y coordinate is",x-1)
            print(x-1,y-1)

ab=cv2.rectangle(convI, (500,200),(400,300),(255,0,0),3)
convI=np.asarray(conI)
cv2.imwrite('task2Im1.jpg',convI)
cI=np.asarray(conv)
cv2.imwrite('task2Im2.jpg',cI)
cv2.imwrite('task2Im3.jpg',ab)

