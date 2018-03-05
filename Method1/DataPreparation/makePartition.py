# -*- coding: UTF-8 -*-

from abaqus import *
from abaqusConstants import *

def makePartitionForPanelUpper(panelUpper):
    """
    给上板做分割
    """
    p = panelUpper
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    e, v1, d1 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(normal=e[21], cells=pickedCells, 
        point=p.InterestingPoint(edge=e[21], rule=MIDDLE))

    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    e1, v2, d2 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(normal=e1[18], cells=pickedCells, 
        point=p.InterestingPoint(edge=e1[18], rule=MIDDLE))

    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#f ]', ), )
    e, v1, d1 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(point=v1[26], normal=e[5], cells=pickedCells)

    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#aa ]', ), )
    e1, v2, d2 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(point=v2[33], normal=e1[38], 
        cells=pickedCells)

    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#aa0 ]', ), )
    e, v1, d1 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(point=v1[41], normal=e[62], 
        cells=pickedCells)

    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#a00c ]', ), )
    e1, v2, d2 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(point=v2[51], normal=e1[37], 
        cells=pickedCells)


def makePartitionForPanelLower(panelLower):
    """
    给下板做分割
    """
    p = panelLower
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    e, v1, d1 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(normal=e[0], cells=pickedCells, 
        point=p.InterestingPoint(edge=e[0], rule=MIDDLE))

    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    e1, v2, d2 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(normal=e1[12], cells=pickedCells, 
        point=p.InterestingPoint(edge=e1[12], rule=MIDDLE))


def makePartitionForDieUpper():
    """
    给上铆模做分割
    """
    p = mdb.models['Model-1'].parts['Die_Lower']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    e, v, d = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(normal=e[3], cells=pickedCells, 
        point=p.InterestingPoint(edge=e[10], rule=MIDDLE))


def makePartitionForDieLower():
    """
    给下铆模做分割
    """
    p = mdb.models['Model-1'].parts['Die_Upper']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    e1, v1, d1 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlanePointNormal(normal=e1[3], cells=pickedCells, 
        point=p.InterestingPoint(edge=e1[10], rule=MIDDLE))