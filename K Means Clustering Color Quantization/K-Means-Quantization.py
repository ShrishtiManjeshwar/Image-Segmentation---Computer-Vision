import cv2
from matplotlib import pyplot as plt
import numpy as np
import random

#init Mu
def initMu(K,img):
    l=[]
    for i in range(0,K):
        l.append((np.random.randint(255,size=3)).tolist())
    #np.random.shuffle(img)
    return l

#Euclidean distances and classify
def minDistClass(M,imD):

    minl=[]
    N=len(imD)
    for i in range(0,N):
        p=np.sqrt(np.sum(np.square(M-imD[i]),axis=1))
        minl.append(p)
    minA=np.argmin(minl,axis=1)
    #minA=np.argmin(minl)
    #print("minA:")
    #print(minA)
    #print("counts:")
    #print(l0,l1,l2)
    
    classL=[[]*len(imD) for i in range(len(Mu))]
    #print(minA)
    for i in range(0,N):
        ind=minA[i]
        classL[ind].append(imD[i])
        
    

    return minA,classL

	#Mean and New Mu

def MuMean(classLl):
    aR=[]
    aG=[]
    aB=[]
    newMu=[]
    for i in classLl:
        if(len(i)==0):
            sx=0
            sy=0
            sz=0
            aR.append(sx)
            aG.append(sy)
            aB.append(sz)
        else:
            sx=0
            sy=0
            sz=0
            for j in i:
                sx=sx+j[0]
                sy=sy+j[1]
                sz=sz+j[2]
            aR.append(sx/len(i))
            aG.append(sy/len(i))
            aB.append(sz/len(i))
            
    for i in range(0,len(aR)):
        x=np.around(aR[i],4)
        y=np.around(aG[i],4)
        z=np.around(aB[i],4)
        newMu.append([x,y,z])
    print(newMu)
    
    return newMu



def IterMu(Mu,imD):
    M=Mu
    itr=5
    i=0
    while(i<itr):
        minA,cL=minDistClass(M,imD)
        UpdatedMu=MuMean(cL)
        M=UpdatedMu
        i=i+1
    
    return M,minA

	
def drawBaboon(I,UpMu,minN,fname):
    l=0
    for i in range(0,h):
        for j in range(0,w):
            I[i][j]=UpMu[minN[l]]
            l=l+1
    cv2.imwrite(fname,I)

img=cv2.imread("baboon.jpg")
w,h,d=img.shape
imD=np.reshape(img,(w*h,d))

K=[3,5,10,20]
Kname=["task3_baboon_3.jpg","task3_baboon_5.jpg","task3_baboon_10.jpg","task3_baboon_20.jpg"]

Mu=initMu(3,imD)
minV,cL=minDistClass(Mu,imD)
UpdatedMu=MuMean(cL)
mu,minAr=IterMu(UpdatedMu,imD)
drawBaboon(img,mu,minAr,"baboon_3.jpg")

Mu=initMu(5,imD)
minV,cL=minDistClass(Mu,imD)
UpdatedMu=MuMean(cL)
mu,minAr=IterMu(UpdatedMu,imD)
drawBaboon(img,mu,minAr,"baboon_5.jpg")

Mu=initMu(10,imD)
minV,cL=minDistClass(Mu,imD)
UpdatedMu=MuMean(cL)
mu,minAr=IterMu(UpdatedMu,imD)
drawBaboon(img,mu,minAr,,"baboon_10.jpg")


Mu=initMu(20,imD)
minV,cL=minDistClass(Mu,imD)
UpdatedMu=MuMean(cL)
mu,minAr=IterMu(UpdatedMu,imD)
drawBaboon(img,mu,minAr,"baboon_20.jpg")




    

