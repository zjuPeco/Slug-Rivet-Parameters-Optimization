# -*- coding: UTF-8 -*-

from abaqus import *
from abaqusConstants import *
import regionToolset

def makeDURigid():
    """
    使上铆模成为刚体
    """
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Die_Upper-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    region2=a.Set(cells=cells1, name='DU_rigd')
    r1 = a.instances['Die_Upper-1'].referencePoints
    refPoints1=(r1[2], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='DU_rigid', refPointRegion=region1, 
        bodyRegion=region2)


def makeDLRigid():
    """
    使下铆模成为刚体
    """
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Die_Lower-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    region2=a.Set(cells=cells1, name='DL_rigd')
    r1 = a.instances['Die_Lower-1'].referencePoints
    refPoints1=(r1[2], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='DL_rigid', refPointRegion=region1, 
        bodyRegion=region2)


def makeCURigid():
    """
    使上压脚成为刚体
    """
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Clamp_Upper-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=a.Set(cells=cells1, name='CU_rigid')
    r1 = a.instances['Clamp_Upper-1'].referencePoints
    refPoints1=(r1[2], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='CU_rigid', refPointRegion=region1, 
        bodyRegion=region2)


def makeCLRigid():
    """
    使下压脚成为刚体
    """
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Clamp_Lower-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=a.Set(cells=cells1, name='CL_rigid')
    r1 = a.instances['Clamp_Lower-1'].referencePoints
    refPoints1=(r1[2], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='CL_rigid', refPointRegion=region1, 
        bodyRegion=region2)