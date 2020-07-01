import rhinoscriptsyntax as rs
import math,random
import util

rows = 10
columns = 10
levels = 30
side = 10

shiftfactor = 1/1000
rotationfactor = 1/70

for i in range(levels*rows*columns):

    lvl = math.floor(i/(rows*columns))          
    totalPlane = i % (columns*rows)
    row = math.floor(totalPlane / columns)
    col = totalPlane % columns
            
    shiftIntensity = math.pow(lvl,3)*math.log(i+1)*shiftfactor
    shiftX = random.uniform(-shiftIntensity,shiftIntensity)
    shiftY = random.uniform(-shiftIntensity,shiftIntensity)
    shiftZ = random.uniform(-shiftIntensity,shiftIntensity)
    sx = side * col + shiftX
    sy = side * row + shiftY
    sz = side * lvl + shiftZ

    rotationAdd = random.uniform(-i, i)*rotationfactor
        
    util.drawBox(side/2,(sx,sy,-sz),rotationAdd,rotationAdd)
            
