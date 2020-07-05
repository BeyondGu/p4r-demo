import rhinoscriptsyntax as rs
import random, math

def mapFromAtoB(inA,A,B):
    (startA,endA) = A
    (startB,endB) = B
    inB = ((inA-startA)*(endB-startB)) / (endA-startA) + startB
    return inB

def getPointByParameter(line,t):
    (p0,p1) = line
    x = p0[0]+(p1[0]-p0[0])*t
    y = p0[1]+(p1[1]-p0[1])*t
    p = ( x, y, 0 )
    return p


def getrandom(offset):
    return random.uniform(-1.5*offset,1.5*offset)
#    return 0.0
    
def drawLerpLines(line0,line1,num):
    for i in range(num):
        t0 = mapFromAtoB(i,(0,num-1),(0,1))
        p0 = getPointByParameter(line0, t0)
        t1 = mapFromAtoB(i,(0,num-1),(0,1))
        p1 = getPointByParameter(line1, t1)
        rs.AddLine(p0,p1)
        
width = 1000
height = 150
numlines =20

xstep = float(width/ (numlines-1))
ystep = 150
groupstep = 400

xoffset = xstep /3.0
yoffset = ystep /3.0

mylines=[]
i =0

for k in range(3):
    for j in range(numlines):
#        rs.AddTextDot(str(j)+','+str(k),(xstep*j,ystep*i+k*groupstep))        
        p0 = (xstep*j+ getrandom(xoffset),
                ystep*i +getrandom(yoffset)+ k*groupstep,
                0)
        p1 = (xstep*j+ getrandom(xoffset),
                ystep*(i+1) + getrandom(yoffset)+ k*groupstep,
                0)
        mylines.append((p0,p1))

#for line in mylines:
#    rs.AddLine(line[0],line[1])

for k in range(3):
    for j in range(numlines):
        if j !=0:
            line0= mylines[k*(numlines)+j-1]
#            print(line0)
            line1 = mylines[k*(numlines)+j]
#            print(line1)
            drawLerpLines(line0,line1,numlines+1)
