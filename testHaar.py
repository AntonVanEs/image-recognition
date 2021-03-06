import pygame,math,sys
pygame.init()
#SETTINGS:
startFace=0
numberOfFaces=21
haarPath="haars\\0.txt"


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
    return [[image.get_at((x,y))[0:3] for x in range(width)] for y in range(height)]
  
def loadHaar(path):
    file=open(path, "r")
    average=float(file.readline())
    sDev=float(file.readline())
    ar=file.readline()[2:-2].split('], [')
    file.close()
    
    haar=[[int(i) for i in st.split(',')] for st in ar]
    return (average,sDev,haar)

def haardifference(image,haar,X,Y):
    ret=[]
    width=len(haar[0])
    height=len(haar)
    imagePart=[[image[y][x] for x in range(X,X+width)] for y in range(Y,Y+height)]

    for x in range(width):
        for y in range(height):
            (r,g,b)=imagePart[y][x]
            ret.append((r+b+g)*haar[y][x])
    return mean(ret)
#open haar
(average,sDev,haar)=loadHaar(haarPath)
Hwidth=len(haar[0])
Hheight=len(haar)

for im in range(numberOfFaces):
    pygameImage=pygame.image.load("faces/"+str(im)+".jpg")
    image=loadImage("faces//"+str(im)+".jpg")
    (average,sDev,haar)=loadHaar(haarPath)

    width=len(image[0])-len(haar[0])
    height=len(image)-len(haar)

    best=pow(10,10)
    bestX=[]
    bestY=[]
    
    for x in range(width):
        for y in range(height):
            dif = abs(haardifference(image,haar,x,y)-average)

            if dif==best:
                bestY.append(x)
                bestY.append(y)
            elif dif<best:
                bestX=[x]
                bestY=[y]
                best=dif
    
    for i in range(len(bestX)):
        cropped = pygame.Surface((Hwidth, Hheight))
        cropped.blit(pygameImage, (0, 0), (bestX[i], bestY[i], Hwidth, Hheight))
        if i==0:
            pygame.image.save(cropped,"results\\"+str(im)+".png")
        else:
            pygame.image.save(cropped,"results\\"+str(im)+"."+str(i)+".png")
