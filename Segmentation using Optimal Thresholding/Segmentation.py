import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("segment.jpg",0)
[rows,cols] = img.shape
hist=np.zeros((255))
print(rows,cols)
for i in range(rows):
    for j in range(cols):
        v=img[i,j]
        hist[v]=hist[v]+1
plt.bar(np.arange(len(hist)-1),hist[1:])
plt.show()
arm=np.argsort(hist)
t=len(arm)-2
thres=arm[t]
print(thres)
r=len(img)
c=len(img[0])
plI=[[0]*(c) for i in range(0,r)]
li=[]
for i in range(r):
    for j in range(c):
        if(img[i][j]>(thres+15)):
            plI[i][j]=255
            li.append([i,j])
B=np.asarray(plI)
cv2.imwrite('bone.jpg',B)
l = img[:,0:210]
m = img[:,213:313]
n = img[:,309:389]
o = img[:,393:718]
def draw(a,a1,a2,z,eximg):
    rx=a.shape[0]
    ry=a.shape[1]
    xpt = []
    ypt = []
    for i in range(rx):
        for j in range(ry):
            if (a[i][j]>thres+10):
                xpt.append(i)
                ypt.append(j)
    x_max1 = max(xpt)+a2
    x_min1 = min(xpt)-20
    y_max1 = max(ypt)+a1
    y_min1 = min(ypt)+a1+z  
    bIm=cv2.rectangle(eximg,(y_min1,x_max1),(y_max1,x_min1),(255,0,0),3)
    cv2.imwrite("im1.jpg",bIm)
    return bIm

imgRGB = cv2.imread("segment.jpg")
al=draw(l,0,20,0,imgRGB)
am=draw(m,224,20,0,al)
an=draw(n,305,20,-8,am)
ao=draw(o,390,50,-5,an)
