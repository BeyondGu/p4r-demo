import Rhino
import rhinoscriptsyntax as rs

p0 = Rhino.Geometry.Point3d(0, 0, 0)
p1 = Rhino.Geometry.Point3d(10, 0, 0)
p3 = rs.PointAdd(p0, rs.VectorRotate(p1-p0, -60, (0, 0, 1)))


def draw(p0, p1, n=1):
    if n == 0:
        rs.AddLine(p0, p1)
    elif n >= 1:
        p01 = rs.PointAdd(p0, (p1-p0)/3)
        p10 = rs.PointAdd(p0, (p1-p0)*2/3)
        p2 = rs.PointAdd(p01, rs.VectorRotate(p10 - p01, 60, (0, 0, 1)))
        draw(p0, p01, n-1)
        draw(p01, p2, n-1)
        draw(p2, p10, n-1)
        draw(p10, p1, n-1)


pts = [p0, p1, p3]

for i in range(len(pts)):
    j = i + 1
    if i + 1 == len(pts):
        j = 0

    draw(pts[i], pts[j], 4)
