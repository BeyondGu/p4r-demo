import rhinoscriptsyntax as rs


def fibo(n):
    if n == 1 or n == 0:
        return n 
    elif n > 1:
        return fibo(n-1)+fibo(n-2)


def drawArc(dir, Pt, radius):
        if dir[0] == 0 and dir[1] == -1:
            nextPt = (Pt[0]+radius, Pt[1]-radius, 0)
            nextDir = (1, 0)
        elif dir[0] == 1 and dir[1] == 0:
            nextPt = (Pt[0]+radius, Pt[1]+radius, 0)
            nextDir = (0, 1)
        elif dir[0] == 0 and dir[1] == 1:
            nextPt = (Pt[0]-radius, Pt[1]+radius, 0)
            nextDir = (-1, 0)
        elif dir[0] == -1 and dir[1] == 0:
            nextPt = (Pt[0]-radius, Pt[1]-radius, 0)
            nextDir = (0, -1)

        rs.AddArcPtTanPt(Pt, dir, nextPt)
        return (nextDir, nextPt, radius)


def drawFiboArc(startDir, startPt, j, radiusList):  
    j += 1   
    if j < len(radiusList):
        radius = radiusList[j]
        nextDir, nextPt, nextradius = drawArc(
            startDir, startPt, radius)
        drawFiboArc(nextDir, nextPt, j, radiusList)
    
    

radiusList = [fibo(i) for i in range(1,20)]
print(radiusList)

drawFiboArc((0, -1), (0, 0, 0), -1, radiusList)
