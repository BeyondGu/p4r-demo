import rhinoscriptsyntax as rs
import math
startPt = (0, 0, 0)
pts = []


def drawLine(startPt, steps):
    for t in range(steps):
        x = -(t**3) * math.cos(t * (math.pi / 6))
        y = (t**3) * math.sin(t * (math.pi / 6))
        Pt = (x, y, 0)
        pts.append(Pt)
    return pts


def draw(p0, p1, n=4):
    if n == 0:
        rs.AddLine(p0, p1)
    elif n >= 1:
        p01 = rs.PointAdd(p0, rs.PointScale(rs.PointSubtract(p1, p0), 1/3))
        p10 = rs.PointAdd(p0, rs.PointScale(rs.PointSubtract(p1, p0), 2/3))
        p2 = rs.PointAdd(p01, rs.VectorRotate(rs.PointSubtract(p10, p01), 60, (0, 0, 1)))
        draw(p0, p01, n-1)
        draw(p01, p2, n-1)
        draw(p2, p10, n-1)
        draw(p10, p1, n-1)


def drawResult(startPt, steps):
    drawLine(startPt, steps)
    for i in range(len(pts)):
        j = i + 1
        if i + 1 == len(pts):
            break
#        rs.AddLine(pts[i], pts[j])
        p0 = pts[i]
        p1 = pts[j]
#        print(p0)
#        print(p1)
        draw(p0, p1)


drawResult(startPt, 22)
