#learning
import pygame,math,sys
import random as rnd

numberOfTruePicturs=40
numberOfFalsePicturs=62
width=40
height=20
atempts=5000

def mean(array):
    return sum(array)/len(array)

def standardDeviation(array):
    average=mean(array)
    diffSum=0
    for e in array:
        diffSum+=(e-average)**2
    return math.sqrt(diffSum/len(array))

def normCdf(mean,sDev,low,high):
    return ((1+math.erf((high-mean)/(sDev*math.sqrt(2))))-(1+math.erf((low-mean)/(sDev*math.sqrt(2)))))/2
    
def loadImage(path):
    image=pygame.image.load(path)
    width=image.get_rect()[2]
    height=image.get_rect()[3]
    return [[image.get_at((x,y))[0:3] for x in range(40)] for y in range(20)]
  
def haardifference(image,haar):
    ret=[]
    width=len(haar[0])
    height=len(haar)
    black=[]
    for x in range(width):
        for y in range(height):
            (r,g,b)=image[y][x]
            ret.append((r+b+g)*haar[y][x])
    return mean(ret)

def test(haar):

    true=[]
    false=[]
    for image in trueImages:
        true.append(haardifference(image,haar))
    average=mean(true)
    sDev=standardDeviation(true)
    for i in range(numberOfFalsePicturs):
        false.append(haardifference(falseImages[i],haar))
        

    return 1/normCdf(mean(false),standardDeviation(false),average-2*sDev,average+2*sDev)
     
pygame.init()


trueImages=[loadImage("examplesTRUE\\"+str(i)+".png") for i in range(numberOfTruePicturs)]
falseImages=[loadImage("examplesFALSE\\"+str(i)+".png") for i in range(numberOfFalsePicturs)]
for j in range(1,6):
    haar=[[0 for i in range(width)] for i in range(height)]
    lastHaar=[[0 for i in range(width)] for i in range(height)]
    maxHaar=[[0 for i in range(width)] for i in range(height)]
    score=1
    maxScore=1
    for i in range(atempts):
        n=20*i/atempts
        if n==int(n):
            print(str(int(5*n))+"%")
            print(score,"max:",maxScore,"(",100/maxScore,"%)")
        
        
        x=rnd.randint(0,39)
        y=rnd.randint(0,19)
        haar[y][x]+=1
        
        x=rnd.randint(0,39)
        y=rnd.randint(0,19)
        haar[y][x]-=1
        
        score=test(haar)
        
        if score<=0.8*maxScore:
            haar=[[lastHaar[y][x] for x in range(width)] for y in range(height)]
        if score>=0.9*maxScore:
            lastHaar=[[haar[y][x] for x in range(width)] for y in range(height)]
        if score>maxScore:
            lastHaar=[[haar[y][x] for x in range(width)] for y in range(height)]
            maxHaar=[[haar[y][x] for x in range(width)] for y in range(height)]
            maxScore=test(maxHaar)
    print("100%")
                      
    print()
    
    true=[]
    for image in trueImages:
        true.append(haardifference(image,maxHaar))
    average=mean(true)
    sDev=standardDeviation(true)

    print("mean:",average,"sDev:",sDev)
    file = open("haars\\"+str(j)+".txt", "w")
    file.write(str(average)+"\n")
    file.write(str(sDev)+"\n")
    file.write(str(maxHaar))
    file.close()


    
