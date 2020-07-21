import rhinoscriptsyntax as rs
import random


def addArc(startPt, endPt, vecDir):
    vecBase = rs.PointSubtract(endPt, startPt)
    if rs.VectorLength(vecBase) == 0.0:
        return
    if rs.IsVectorParallelTo(vecBase, vecDir):
        return

    vecBase = rs.VectorUnitize(vecBase)
    vecDir = rs.VectorUnitize(vecDir)

    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)

    midlength = (0.5*rs.Distance(startPt, endPt)) / (rs.VectorDotProduct(vecBisector, vecDir))

    vecBisector = rs.VectorScale(vecBisector, midlength)
    return rs.AddArc3Pt(startPt, endPt, rs.PointAdd(startPt, vecBisector))


def drawBranch(origin, dir, minDistance, maxDistance, maxAngle):
    vecTwig = rs.VectorUnitize(dir)
    vecTwig = rs.VectorScale(vecTwig, minDistance+random.random()*(maxDistance-minDistance))
    mutationPlane = rs.PlaneFromNormal((0, 0, 0), vecTwig)
    vecTwig = rs.VectorRotate(vecTwig, random.random()*maxAngle, mutationPlane[1])
    vecTwig = rs.VectorRotate(vecTwig, random.random()*360, dir)
    return rs.PointAdd(origin, vecTwig)


def drawTree(startPt, vecDir, (minTwigCount, maxTwigCount, maxGenerations, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation), g):
    if g > maxGenerations:
        return
    newProps = minTwigCount, maxTwigCount, maxGenerations, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation
    maxTwigLength *= lengthMutation
    maxTwigAngle *= angleMutation
    if maxTwigAngle > 90:
        maxTwigAngle = 90
    newProps = minTwigCount, maxTwigCount, maxGenerations, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation
    maxN = int(minTwigCount+random.random()*(maxTwigCount-minTwigCount))
    for n in range(1, maxN):
        ptGrow = drawBranch(startPt, vecDir, 0.25*maxTwigLength, maxTwigLength, maxTwigAngle)
        newTwig = addArc(startPt, ptGrow, vecDir)
        if newTwig:
            vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain(newTwig)[1])
            drawTree(ptGrow, vecGrow, newProps, g+1)


drawTree((0, 0, 0), (0, 0, 1), (5, 7, 6, 8, 0.7, 3, 6), 0)
