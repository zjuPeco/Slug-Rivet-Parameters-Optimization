# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *
import mesh

def meshForClampLower(seedSize):
    """
    给下压脚划分网格
    """
    p = mdb.models['Model-1'].parts['Clamp_Lower']
    p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p.generateMesh()


def meshForClampUpper(seedSize):
    """
    给上压脚划分网格
    """
    p = mdb.models['Model-1'].parts['Clamp_Upper']
    p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p.generateMesh()

def meshForDieLower(seedSize):
    """
    给下铆模划分网格
    """
    p = mdb.models['Model-1'].parts['Die_Lower']
    p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p.generateMesh()


def meshForDieUpper(seedSize):
    """
    给上铆模划分网格
    """
    p = mdb.models['Model-1'].parts['Die_Upper']
    p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p.generateMesh()


def meshForPanelLower(seedSize1, seedSize2, seedSize3, seedSize4):
    """
    给下板划分网格，其中seedSize1表示沿孔厚度的种子，seedSize2表示沿孔边的种子，
    seedSize3表示孔附近的种子，seedSize4表示其余的种子
    """
    p = mdb.models['Model-1'].parts['Panel_Lower']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#800 #1 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=seedSize1, deviationFactor=0.1, 
        constraint=FINER)
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#200000 #8 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=seedSize2, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Panel_Lower']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#80101400 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=seedSize3, deviationFactor=0.1, 
        constraint=FINER)
    p.seedPart(size=seedSize4, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#f ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p.generateMesh()


def meshForPanelUpper(seedSize1, seedSize2, seedSize3, seedSize4):
    """
    给上板划分网格，其中seedSize1表示沿孔厚度的种子，seedSize2表示沿孔边的种子，
    seedSize3表示孔附近的种子，seedSize4表示其余的种子
    """
    p = mdb.models['Model-1'].parts['Panel_Upper']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#48000 #10100000 #2400 #18020010 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=seedSize1, deviationFactor=0.1, 
        constraint=FINER)
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#800 #40 #8000004 #20800000 ]', ), 
        )
    p.seedEdgeBySize(edges=pickedEdges, size=seedSize2, deviationFactor=0.1, 
        constraint=FINER)
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#25400 #8000080 #10001008 #40410000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=seedSize3, deviationFactor=0.1, 
        constraint=FINER)
    p.seedPart(size=seedSize4, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fffff ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p.generateMesh()


def meshForRivet(seedSize):
    """
    给无头铆钉划分网格
    """
    p = mdb.models['Model-1'].parts['Rivet']
    p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p.generateMesh()