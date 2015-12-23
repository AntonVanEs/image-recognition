#this doesnt work at all
import pygame,math,sys
import random as rnd

numberOfTruePicturs=40
numberOfFalsePicturs=42
width=40
height=20
atempts=100
populationSize=100

populationSize-=populationSize%4

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
    return (1/normCdf(mean(false),standardDeviation(false),average-2*sDev,average+2*sDev),average,sDev)

def breed(father,mother):
    parents=[father[3],mother[3]]
    return([[parents[rnd.randint(0,1)][y][x] for x in range(width)] for y in range(height)])

def breedPopulation(population):
    nextGeneration=[]
    for i in range(int(populationSize/2)):
        nextGeneration.append(breed(population[rnd.randint(0,populationSize/4)],population[rnd.randint(0,populationSize/4)]))
    for i in range(int(populationSize/2)):
        nextGeneration.append(breed(population[rnd.randint(0,populationSize/2)],population[rnd.randint(0,populationSize/2)]))
    return nextGeneration
  
pygame.init()

trueImages=[loadImage("examplesTRUE\\"+str(i)+".png") for i in range(numberOfTruePicturs)]
falseImages=[loadImage("examplesFALSE\\"+str(i)+".png") for i in range(numberOfFalsePicturs)]
for j in range(1,2):
    population=[[[0 for i in range(40)] for i in range(20)]]*populationSize
    #(score, mean, standard deviation, array)
    for i in range(atempts):
        
        
        parents=[]
        for individual in population:
            haar=individual
            x=rnd.randint(0,width-1)
            y=rnd.randint(0,height-1)
            haar[y][x]+=1
            x=rnd.randint(0,width-1)
            y=rnd.randint(0,height-1)
            haar[y][x]-=1
            (score,average,sDev)=test(haar)
            parents.append((score,average,sDev,haar))
        parents.sort()
        population=breedPopulation(parents)

        n=20*i/atempts
        if n==int(n):
            print(str(int(5*n))+"%")
            print("score:",parents[0][0],"%")
            
    lastGeneration=[]
    for individual in population:
        haar=individual[3]
        x=rnd.randint(0,width-1)
        y=rnd.randint(0,height-1)
        haar[y][x]+=1
        x=rnd.randint(0,width-1)
        y=rnd.randint(0,height-1)
        haar[y][x]-=1
        lastGeneration.append((test(haar),mean(haar),sDev(haar),haar))
    lastGeneration.sort()
    average=lastGeneration[0][1]
    sDev=lastGeneration[0][2]
    print("mean:",average,"sDev:",sDev)
    file = open("haars\\"+str(j)+".txt", "w")
    file.write(str(average)+"\n")
    file.write(str(sDev)+"\n")
    file.write(str(maxhaar))
    file.close()
