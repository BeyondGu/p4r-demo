import rhinoscriptsyntax as rs
import math


p0 = (0, 0, 0)
pts = []


def drawLine(p0, steps):
    for t in range(steps):
        x = -(t**3) * math.cos(t * (math.pi / 6))
        y = (t**3) * math.sin(t * (math.pi / 6))
        Pt = (x, y, 0)
        pts.append(Pt)
    return pts


drawLine(p0, 22)
for i in range(len(pts)):
    j = i + 1
    if i + 1 == len(pts):
        break
    rs.AddLine(pts[i], pts[j])
