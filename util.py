#coding=utf-8
'''
Copyright
create on 2020.05.19
@author mahaidong
https://github.com/mahaidong
Description: Python4Rhino tutorial
'''
import rhinoscriptsyntax as rs 

def drawRect( side, location, angle_degrees ):
    """画一个2D方块
    参数:
      side(double): 方块的长度, double 
      locaiton(tuple(double, double,double)): 方块中心的位置
      angle_degrees(double): 旋转角度degree
    Returns:
      guid
    """

    p0 = (-side/2,-side/2,0)
    p1 = (side/2,-side/2,0)
    p2 = (side/2,side/2,0)
    p3 = (-side/2,side/2,0)

    obj = rs.AddPolyline([p0,p1,p2,p3,p0])

   
    xform = rs.XformRotation2(angle_degrees, (0,0,1), (0,0,0))
    obj = rs.TransformObject( obj, xform, False )

    xform = rs.XformTranslation( location)
    obj = rs.TransformObject( obj, xform, False )

    return obj

def drawBox( side, location, angle_degrees1, angle_degrees2):
    """画一个2D方块
    参数:
      side(double): 方块的长度, double 
      locaiton(tuple(double, double,double)): 方块中心的位置
      angle_degrees1(double): xy平面旋转角度degree1
      angle_degrees2(double): 到达位置后继续朝z轴方向旋转角度degree2
    Returns:
      guid
    """
    corners = []
    corners.append((-side/2,-side/2,0))
    corners.append(( side/2,-side/2,0))
    corners.append((side/2,side/2,0))
    corners.append((-side/2,side/2,0)) 
    corners.append((-side/2,-side/2,side))
    corners.append((side/2,-side/2,side))
    corners.append((side/2,side/2,side))
    corners.append((-side/2,side/2,side))
    obj = rs.AddBox(corners)

    xform = rs.XformRotation2(angle_degrees1, (0,0,1), (0,0,0))
    obj = rs.TransformObject( obj, xform, False )
    vectorR1 = rs.VectorRotate( (1,0,0), angle_degrees1, (0,0,0))
    vectorR2 = rs.VectorCrossProduct(vectorR1, (0,0,1))
    xform = rs.XformRotation2(angle_degrees1, vectorR2, (0,0,0))
    obj = rs.TransformObject( obj, xform, False )
    xform = rs.XformTranslation( location)
    obj = rs.TransformObject( obj, xform, False )

    return obj 