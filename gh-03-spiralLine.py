import rhinoscriptsyntax as rs
import math

pts = []


def drawLine(p0, steps):
    for t in range(steps):
        x = (t**b) * math.cos((t/c)*(math.pi/6)+t/c)
        y = -(t**b) * math.sin((t/c)*(math.pi/6)+t/c)
        p1 = (x, y, 0)
        pts.append(p1)
    return pts


def drawLineByPts(result, pts):
    for i in range(len(pts)):
        j = i + 1
        if i + 1 == len(pts):
            break
        result.append(rs.AddLine(pts[i], pts[j]))
    return result


a = []
drawLine(p0, steps)
drawLineByPts(a, pts)
