import rhinoscriptsyntax as rs 
import math,random
import util

rows=10
columns=10
levels=30
side=10

shiftfactor=1/1000
rotatefactor=1/70

def getrotate(total,rotatefactor): 
    return random.uniform(-total,total)*rotatefactor

def getshift(k,total,shiftfactor): 
    shiftIntensity = (k**3)* (math.log(total+1))*shiftfactor
    return random.uniform(-shiftIntensity,shiftIntensity)
    
for k in range(levels):
    for j in range(columns):
        for i in range(rows):
            total = i*j*k 
                         
            x = side * j + getshift(k, total, shiftfactor)
            y = side * i + getshift(k, total, shiftfactor)
            z = side * k + getshift(k, total, shiftfactor)

            util.drawBox(side/2,(x,y,-z),
            getrotate(total,rotatefactor),
            getrotate(total,rotatefactor))
