#face recognision using haar-cascade
import pygame,math,sys
imagePath="faces\\0.jpg"
haarNumbers=[6,3,9,8,5,0,7]

pygame.init()
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
            
            
            
#open image and haar as array
image=loadImage(imagePath)
pygameImage=pygame.image.load(imagePath)
haars=[loadHaar("haars\\"+str(i)+".txt") for i in haarNumbers]

Hwidth=len(haars[0][2][0])
Hheight=len(haars[0][2])
width=len(image[0])-Hwidth
height=len(image)-Hheight


screen = pygame.display.set_mode((width,height))
best=pow(10,10)
bestX=[]
bestY=[]

for x in range(width):
    n=20*x/width
    if n==int(n):
        print(str(int(5*n))+"%")
    for y in range(height):
        h=0
        for haar in haars:
            if abs(haardifference(image,haar[2],x,y)-haar[0])>2*haar[1]:
                break
            else:
                (R,G,B,A)=screen.get_at((x,y))
                screen.set_at((x,y),(R+(255/len(haarNumbers)),G+(255/len(haarNumbers)),B+(255/len(haarNumbers)),A))
            h+=1
            if h==len(haarNumbers):
                screen.blit(pygameImage, (0, 0), (x, y, Hwidth, Hheight))
                pygame.display.flip()
            
    pygame.event.get()
    pygame.display.flip()
pygame.display.flip()
