# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *

def myMaterial():
    """
    定义我的材料并创建Section
    """
    mdb.models['Model-1'].Material(name='Panel-2024-T3')
    mdb.models['Model-1'].materials['Panel-2024-T3'].Density(table=((2.83e-09, ), 
        ))
    mdb.models['Model-1'].materials['Panel-2024-T3'].Elastic(table=((72400.0, 
        0.33), ))
    mdb.models['Model-1'].materials['Panel-2024-T3'].Plastic(table=((310.0, 0.0), (
        321.9604284, 0.005), (343.8581277, 0.008), (354.7698431, 0.01), (
        375.4909483, 0.015), (390.9227051, 0.02), (439.4344605, 0.04), (
        469.6486495, 0.06), (492.3376299, 0.08), (510.6887287, 0.1), (1034.0, 
        0.2), (1034.0, 0.3), (1034.0, 0.5)))
    
    mdb.models['Model-1'].Material(name='Rivet-2117-T4')
    mdb.models['Model-1'].materials['Rivet-2117-T4'].Density(table=((2.69e-09, ), 
        ))
    mdb.models['Model-1'].materials['Rivet-2117-T4'].Elastic(table=((71700.0, 
        0.33), ))
    mdb.models['Model-1'].materials['Rivet-2117-T4'].Plastic(table=((172.0, 0.0), (
        221.2258124, 0.02), (259.4613645, 0.04), (284.822102, 0.06), (
        304.3053563, 0.08), (320.3309485, 0.1), (400.8932886, 0.12), (
        414.5388972, 0.15), (432.8187817, 0.2), (459.9597053, 0.3), (
        480.2425071, 0.4), (496.5890049, 0.5), (510.3572474, 0.6), (522.295525, 
        0.7), (532.862425, 0.8)))

    mdb.models['Model-1'].HomogeneousSolidSection(name='PanelSection', 
        material='Panel-2024-T3', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='RivetSection', 
        material='Rivet-2117-T4', thickness=None)


def assignPanelSectionForPanelUpper(panelUpper):
    """
    将PanelSection赋予上板
    """
    p = panelUpper
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#fffff ]', ), )
    region = p.Set(cells=cells, name='Panel_Upper')
    p.SectionAssignment(region=region, sectionName='PanelSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def assignPanelSectionForPanelLower(panelLower):
    """
    将PanelSection赋予下板
    """
    p = panelLower
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#f ]', ), )
    region = p.Set(cells=cells, name='Panel_Lower')
    p.SectionAssignment(region=region, sectionName='PanelSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def assignRivetSectionForRivet(rivet):
    """
    将RivetSection赋予无头铆钉
    """
    p = rivet
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Rivet')
    p.SectionAssignment(region=region, sectionName='RivetSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def assignPanelSectionForDieUpper():
    """
    将PanelSection赋予上铆模
    """
    p = mdb.models['Model-1'].parts['Die_Upper']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    region = p.Set(cells=cells, name='DieUpper')
    p.SectionAssignment(region=region, sectionName='PanelSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def assignPanelSectionForDieLower():
    """
    将PanelSection赋予下铆模
    """
    p = mdb.models['Model-1'].parts['Die_Lower']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    region = p.Set(cells=cells, name='DieLower')
    p.SectionAssignment(region=region, sectionName='PanelSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def assignPanelSectionForClampUpper():
    """
    将PanelSection赋予上压脚
    """
    p = mdb.models['Model-1'].parts['Clamp_Upper']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='ClampUpper')
    p.SectionAssignment(region=region, sectionName='PanelSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def assignPanelSectionForClampLower():
    """
    将PanelSection赋予下压脚
    """
    p = mdb.models['Model-1'].parts['Clamp_Lower']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='ClampLower')
    p.SectionAssignment(region=region, sectionName='PanelSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)