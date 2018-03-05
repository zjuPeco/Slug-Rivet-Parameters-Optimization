# -*- coding: UTF-8 -*-

from abaqus import *
from abaqusConstants import *
import math

def myDieLower(theta, h):
    """
    Die_Lower的模型建立
    """
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=60.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -30.0), point2=(0.0, 30.0))
    s.FixedConstraint(entity=g[2])
    s.Line(point1=(0.0, 0.0), point2=(2.38, 0.0))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    s.Line(point1=(2.38, 0.0), point2=(6.0, -h))
    s.AngularDimension(line1=g[4], line2=g[3], textPoint=(1.59237098693848, 
        -1.89099597930908), value= 90.0 + theta)
    s.Line(point1=(0.0, 0.0), point2=(0.0, h))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[5], addUndoState=False)
    s.Line(point1=(0.0, h), point2=(4.5, h))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(4.5, h), point2=(4.5, -h))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(4.5, -h), point2=(0.0, -h))
    s.HorizontalConstraint(entity=g[8], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
    s.autoTrimCurve(curve1=g[8], point1=(1.0, -h))
    s.autoTrimCurve(curve1=g[4], point1=(2.38 + (h + 0.1) * tan(theta * pi / 180.0), -(h + 0.1)))
    p = mdb.models['Model-1'].Part(name='Die_Lower', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Die_Lower']
    p.BaseSolidRevolve(sketch=s, angle=90.0, flipRevolveDirection=OFF)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Die_Lower']
    v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
    p.ReferencePoint(point=v[0])
    return p


def myDieUpper(theta, h):
    """
    Die_Upper的模型建立
    """
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=20.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -10.0), point2=(0.0, 10.0))
    s.FixedConstraint(entity=g[2])
    s.Line(point1=(0.0, 0.0), point2=(0.0, h))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.Line(point1=(0.0, h), point2=(4.5, h))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(4.5, h), point2=(4.5, -h))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(4.5, -h), point2=(0.0, -h))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
    s.Line(point1=(0.0, 0.0), point2=(2.38, 0.0))
    s.HorizontalConstraint(entity=g[7], addUndoState=False)
    s.Line(point1=(2.38, 0.0), point2=(6.0, -h))
    s.AngularDimension(line1=g[8], line2=g[7], textPoint=(2.10657835006714, 
        -0.829383850097656), value=90.0 + theta)
    s.autoTrimCurve(curve1=g[6], point1=(1.0, -h))
    s.autoTrimCurve(curve1=g[8], point1=(2.38 + (h + 0.1) * tan(theta * pi / 180.0), -(h + 0.1)))
    p = mdb.models['Model-1'].Part(name='Die_Upper', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Die_Upper']
    p.BaseSolidRevolve(sketch=s, angle=90.0, flipRevolveDirection=OFF)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Die_Upper']
    v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
    p.ReferencePoint(point=v[0])
    return p


def myClampUpper(r1, r2, h):
    """
    上压脚的模型建立
    """
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=60.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -30.0), point2=(0.0, 30.0))
    s.FixedConstraint(entity=g[2])
    s.rectangle(point1=(r1, 0.0), point2=(r2, h))
    p = mdb.models['Model-1'].Part(name='Clamp_Upper', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Clamp_Upper']
    p.BaseSolidRevolve(sketch=s, angle=90.0, flipRevolveDirection=OFF)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Clamp_Upper']
    v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
    p.ReferencePoint(point=p.InterestingPoint(edge=e[3], rule=CENTER))
    return p


def myClampLower(r1, r2, h):
    """
    下压脚的模型建立
    """
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=60.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -30.0), point2=(0.0, 30.0))
    s.FixedConstraint(entity=g[2])
    s.rectangle(point1=(r1, 0.0), point2=(r2, h))
    p = mdb.models['Model-1'].Part(name='Clamp_Lower', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Clamp_Lower']
    p.BaseSolidRevolve(sketch=s, angle=90.0, flipRevolveDirection=OFF)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Clamp_Lower']
    v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
    p.ReferencePoint(point=p.InterestingPoint(edge=e[3], rule=CENTER))
    return p


def myPanelLower(length, r, depth):
    """
    下板的模型建立
    """
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=100.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(length, length))
    s.ArcByCenterEnds(center=(0.0, 0.0), point1=(r, 0.0), point2=(0.0, r), 
        direction=COUNTERCLOCKWISE)
    s.CoincidentConstraint(entity1=v[5], entity2=g[2], addUndoState=False)
    s.autoTrimCurve(curve1=g[5], point1=(r / 2, 0.0))
    s.autoTrimCurve(curve1=g[2], point1=(0.0, r / 2))
    p = mdb.models['Model-1'].Part(name='Panel_Lower', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Panel_Lower']
    p.BaseSolidExtrude(sketch=s, depth=depth)
    del mdb.models['Model-1'].sketches['__profile__']
    return p


def myPanelUpper():
    """
    上板的模型建立
    """
    #创建基体
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=100.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(25.0, 25.0))
    p = mdb.models['Model-1'].Part(name='Panel_Upper2', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Panel_Upper2']
    p.BaseSolidExtrude(sketch=s, depth=3.0)
    del mdb.models['Model-1'].sketches['__profile__']
    #创建剪切部分
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=50.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -25.0), point2=(0.0, 25.0))
    s1.FixedConstraint(entity=g[2])
    s1.Line(point1=(0.0, 0.0), point2=(2.455, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.Line(point1=(2.455, 0.0), point2=(2.455, 1.5))
    s1.VerticalConstraint(entity=g[4], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s1.Line(point1=(2.455, 1.5), point2=(2.455 + 2, 1.5 + 2.0 / tan(41 * pi / 180.0)))
    s1.Line(point1=(0.0, 0.0), point2=(0.0, 3.0))
    s1.VerticalConstraint(entity=g[6], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[3], entity2=g[6], addUndoState=False)
    s1.Line(point1=(0.0, 3.0), point2=(3.4, 3.0))
    s1.HorizontalConstraint(entity=g[7], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s1.Line(point1=(3.4, 3.0), point2=(3.4 - 0.5, 3 - 0.5 / tan(15 * pi / 180)))
    s1.autoTrimCurve(curve1=g[8], point1=(3.12491416931152, 1.72794055938721))
    s1.autoTrimCurve(curve1=g[5], point1=(3.78666305541992, 2.97794055938721))
    p = mdb.models['Model-1'].Part(name='PartToBeCut', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['PartToBeCut']
    p.BaseSolidRevolve(sketch=s1, angle=360.0, flipRevolveDirection=OFF)
    del mdb.models['Model-1'].sketches['__profile__']
    #倒角
    p = mdb.models['Model-1'].parts['PartToBeCut']
    e = p.edges
    p.Round(radius=0.25, edgeList=(e[4], ))
    p = mdb.models['Model-1'].parts['PartToBeCut']
    e1 = p.edges
    p.Round(radius=1.3, edgeList=(e1[3], ))
    #装配后进行布尔运算
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Panel_Upper2']
    a.Instance(name='Panel_Upper2-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['PartToBeCut']
    a.Instance(name='PartToBeCut-1', part=p, dependent=ON)
    f1 = a.instances['PartToBeCut-1'].faces
    f2 = a.instances['Panel_Upper2-1'].faces
    a.FaceToFace(movablePlane=f1[5], fixedPlane=f2[4], flip=OFF, clearance=0.0)
    e1 = a.instances['PartToBeCut-1'].edges
    v11 = a.instances['Panel_Upper2-1'].vertices
    a.CoincidentPoint(fixedPoint=v11[0], 
        movablePoint=a.instances['PartToBeCut-1'].InterestingPoint(edge=e1[5], 
        rule=CENTER))
    a.InstanceFromBooleanCut(name='Panel_Upper', 
        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Panel_Upper2-1'], 
        cuttingInstances=(a.instances['PartToBeCut-1'], ), 
        originalInstances=DELETE)
    #清除多余的模型
    del mdb.models['Model-1'].parts['Panel_Upper2']
    del mdb.models['Model-1'].parts['PartToBeCut']
    del a.features['Panel_Upper-1']
    del a.features['Datum csys-1']
    p = mdb.models['Model-1'].parts['Panel_Upper']
    return p


def myRivet(r, h):
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=50.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -25.0), point2=(0.0, 25.0))
    s.FixedConstraint(entity=g[2])
    s.rectangle(point1=(0.0, 0.0), point2=(r, h))
    p = mdb.models['Model-1'].Part(name='Rivet', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Rivet']
    p.BaseSolidRevolve(sketch=s, angle=90.0, flipRevolveDirection=OFF)
    del mdb.models['Model-1'].sketches['__profile__']
    return p