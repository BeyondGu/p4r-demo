import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
import math


def draw_result(ps, ks, pts, kts):
    surfaces = []
    tri_points = []
    mid_points = []
    cen_points = []
    lines = []


    for x in range(ps.BranchCount-1):
        for y in range(ps.Branch(x).Count-2):            
            if x >= 0 and y >= 0 and y%2 ==0:
                y = int(y)
                m = x
                n = y

                p0 = ps.Branch(x)[y]
                p1 = ps.Branch(x+1)[y]
                p2 = pts.Branch(m)[n+1]
                p3 = ps.Branch(x)[y+2]
                p4 = ps.Branch(x+1)[y+2]
                p5 = pts.Branch(m+1)[n+1]

                pline0 = rs.AddLine(p0, p1)
                pline1 = rs.AddLine(p1, p2)
                pline2 = rs.AddLine(p2, p0)
                
                lines.append(pline0)
                lines.append(pline1)
                lines.append(pline1)

                pline3 = rs.AddLine(p2, p3)
                pline4 = rs.AddLine(p3, p4)
                pline5 = rs.AddLine(p4, p2)

                lines.append(pline3)
                lines.append(pline4)
                lines.append(pline5)

                lines.append(rs.AddLine(p2, p5))
                lines.append(rs.AddLine(p5, p1))
                lines.append(rs.AddLine(p4, p5))

                m01 = (p1+p0) / 2.0
                m12 = (p1+p2) / 2.0
                m20 = (p2+p0) / 2.0
                m24 = (p2+p4) / 2.0
                m34 = (p3+p4) / 2.0
                m23 = (p2+p3) / 2.0

                m15 = (p1+p5) / 2.0
                m25 = (p2+p5) / 2.0
                m45 = (p4+p5) / 2.0

                cen_point0 = (p0+p1+p2) / 3.0
                cen_point1 = (p2+p3+p4) / 3.0
                cen_point2 = (p1+p2+p5) / 3.0
                cen_point3 = (p2+p4+p5) / 3.0

                dist = rs.Distance(p1, p0)

                tri_points.append([p0, p1, p2])
                tri_points.append([p2, p3, p4])
                tri_points.append([p1, p2, p5])
                tri_points.append([p2, p4, p5])

                x_mid01_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) * (dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point0, m01))
                x_mid01_point = rs.PointAdd(m01, x_mid01_vector)

                y_mid12_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) * (dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point0, m12))
                y_mid12_point = rs.PointAdd(m12, y_mid12_vector)

                y_mid20_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) * (dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point0, m20))
                y_mid20_point = rs.PointAdd(m20, y_mid20_vector)

                y_mid23_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) * (dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point1, m23))
                y_mid23_point = rs.PointAdd(m23, y_mid23_vector)

                x_mid34_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) *(dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point1, m34))
                x_mid34_point = rs.PointAdd(m34, x_mid34_vector)

                y_mid24_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) *(dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point1, m24))
                y_mid24_point = rs.PointAdd(m24, y_mid24_vector)

                y_mid21_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) *(dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point2, m12))
                y_mid21_point = rs.PointAdd(m12, y_mid21_vector)

                x_mid25_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) *(dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point2, m25))
                x_mid25_point = rs.PointAdd(m25, x_mid25_vector)

                y_mid15_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) *(dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point2, m15))
                y_mid15_point = rs.PointAdd(m15, y_mid15_vector)

                x_mid52_vector = (1+math.sin( (x/(ps.BranchCount)) * 2*math.pi)) *(dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point3, m25))
                x_mid52_point = rs.PointAdd(m25, x_mid52_vector)

                y_mid42_vector = (1+math.sin((x/(ps.BranchCount)) * 2*math.pi)) *(dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point3, m24))
                y_mid42_point = rs.PointAdd(m24, y_mid42_vector)

                y_mid45_vector = (1+math.sin((x/(ps.BranchCount)) * 2*math.pi)) *(dist/5.0)*rs.VectorUnitize(rs.VectorCreate(cen_point3, m45))
                y_mid45_point = rs.PointAdd(m45, y_mid45_vector)

                mid_points.append([(m01, x_mid01_point), (m12, y_mid12_point), (m20, y_mid20_point),
                                (m23, y_mid23_point), (m34, x_mid34_point), (m24, y_mid24_point),
                                (m12, y_mid21_point), (m25, x_mid25_point), (m15, y_mid15_point),
                                (m24, y_mid42_point), (m25, x_mid52_point), (m45, y_mid45_point)                                  
                                ])
                
                x_axis = rs.VectorCreate(p1, p0)
                y_axis = rs.VectorCreate(p2, m01)
                z_axis = (dist/10.0)*rs.VectorUnitize(rs.VectorCrossProduct(y_axis, x_axis))

                cen_above_point0 = rs.PointAdd(cen_point0, z_axis)
                cen_above_point1 = rs.PointAdd(cen_point1, z_axis)
                cen_above_point2 = rs.PointAdd(cen_point2, z_axis)
                cen_above_point3 = rs.PointAdd(cen_point3, z_axis)

                cen_points.append([cen_point0, cen_above_point0])
                cen_points.append([cen_point1, cen_above_point1])
                cen_points.append([cen_point2, cen_above_point2])
                cen_points.append([cen_point3, cen_above_point3])


                surf = []
                surf.append(rs.AddSrfPt((p0, cen_above_point0, x_mid01_point)))
                surf.append(rs.AddSrfPt((p1, cen_above_point0, x_mid01_point)))
                surf.append(rs.AddSrfPt((p1, cen_above_point0, y_mid12_point)))
                surf.append(rs.AddSrfPt((p2, cen_above_point0, y_mid12_point)))
                surf.append(rs.AddSrfPt((p2, cen_above_point0, y_mid20_point)))
                surf.append(rs.AddSrfPt((p0, cen_above_point0, y_mid20_point)))

                surf.append(rs.AddSrfPt((p2, cen_above_point1, y_mid23_point)))
                surf.append(rs.AddSrfPt((p3, cen_above_point1, y_mid23_point)))
                surf.append(rs.AddSrfPt((p3, cen_above_point1, x_mid34_point)))
                surf.append(rs.AddSrfPt((p4, cen_above_point1, x_mid34_point)))
                surf.append(rs.AddSrfPt((p4, cen_above_point1, y_mid24_point)))
                surf.append(rs.AddSrfPt((p2, cen_above_point1, y_mid24_point)))

                surf.append(rs.AddSrfPt((p1, cen_above_point2, y_mid21_point)))
                surf.append(rs.AddSrfPt((p2, cen_above_point2, y_mid21_point)))
                surf.append(rs.AddSrfPt((p2, cen_above_point2, x_mid25_point)))
                surf.append(rs.AddSrfPt((p5, cen_above_point2, x_mid25_point)))
                surf.append(rs.AddSrfPt((p5, cen_above_point2, y_mid15_point)))
                surf.append(rs.AddSrfPt((p1, cen_above_point2, y_mid15_point)))

                surf.append(rs.AddSrfPt((p2, cen_above_point3, x_mid52_point)))
                surf.append(rs.AddSrfPt((p5, cen_above_point3, x_mid52_point)))
                surf.append(rs.AddSrfPt((p5, cen_above_point3, y_mid45_point)))
                surf.append(rs.AddSrfPt((p4, cen_above_point3, y_mid45_point)))
                surf.append(rs.AddSrfPt((p4, cen_above_point3, y_mid42_point)))
                surf.append(rs.AddSrfPt((p2, cen_above_point3, y_mid42_point)))

                surfaces.append(surf)


    return(surfaces, tri_points, mid_points, cen_points, lines)


surfaces, tri_points, mid_points, cen_points, lines = draw_result(p, k, pt, kt)

surface = th.list_to_tree(surfaces, source=[0,0])
point = th.list_to_tree(tri_points, source=[0,0])
middle = th.list_to_tree(mid_points, source=[0,0])
center = th.list_to_tree(cen_points, source=[0,0])
line = th.list_to_tree(lines, source=[0,0])

