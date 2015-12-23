#visualise
import pygame,math,sys
path="haars//0.txt"

file=open(path, "r")
average=float(file.readline())
sDev=float(file.readline())
ar=file.readline()[2:-2].split('], [')
file.close()

haar=[[int(i) for i in st.split(',')] for st in ar]
width=len(haar[0])
height=len(haar)

visual=pygame.Surface((width,height))
high=0
for x in range(width):
    for y in range(height):
        n=abs(haar[y][x])
        if n>high:
            high=n
            
for x in range(width):
    for y in range(height):
        value=haar[y][x]
        if value>0:
            visual.set_at((x,y),(int(255*value/high),0,0))
        else:
            visual.set_at((x,y),(0,int(255*abs(value)/high),0))

pygame.image.save(visual,path[:-3]+"png")
