# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *

def myAssembly(dieUpper, dieLower, clampUpper, clampLower, panelUpper, panelLower, rivet):
    """
    装配部件
    """
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    #载入需要的部件
    a.Instance(name='Panel_Lower-1', part=panelLower, dependent=ON)
    a.Instance(name='Panel_Upper-1', part=panelUpper, dependent=ON)
    a.Instance(name='Die_Upper-1', part=dieUpper, dependent=ON)
    a.Instance(name='Die_Lower-1', part=dieLower, dependent=ON)
    a.Instance(name='Clamp_Upper-1', part=clampUpper, dependent=ON)
    a.Instance(name='Clamp_Lower-1', part=clampLower, dependent=ON)
    a.Instance(name='Rivet-1', part=rivet, dependent=ON)
    
    #以Panel_Lower-1为基底，完全约束Panel_Upper-1
    f1 = a.instances['Panel_Upper-1'].faces
    f2 = a.instances['Panel_Lower-1'].faces
    a.FaceToFace(movablePlane=f1[67], fixedPlane=f2[19], flip=ON, clearance=0.0)
    e1 = a.instances['Panel_Upper-1'].edges
    e2 = a.instances['Panel_Lower-1'].edges
    a.ParallelEdge(movableAxis=e1[14], fixedAxis=e2[20], flip=OFF)
    f1 = a.instances['Panel_Upper-1'].faces
    f2 = a.instances['Panel_Lower-1'].faces
    a.Coaxial(movableAxis=f1[82], fixedAxis=f2[17], flip=ON)    
    
    #完全约束Clamp_Upper-1
    f1 = a.instances['Clamp_Upper-1'].faces
    f2 = a.instances['Panel_Upper-1'].faces
    a.FaceToFace(movablePlane=f1[3], fixedPlane=f2[84], flip=ON, clearance=0.0)
    e1 = a.instances['Clamp_Upper-1'].edges
    e2 = a.instances['Panel_Upper-1'].edges
    a.ParallelEdge(movableAxis=e1[6], fixedAxis=e2[126], flip=OFF)
    f1 = a.instances['Clamp_Upper-1'].faces
    f2 = a.instances['Panel_Lower-1'].faces
    a.Coaxial(movableAxis=f1[0], fixedAxis=f2[17], flip=ON)

	#完全约束Clamp_Lower-1
    f1 = a.instances['Clamp_Lower-1'].faces
    f2 = a.instances['Panel_Lower-1'].faces
    a.FaceToFace(movablePlane=f1[3], fixedPlane=f2[6], flip=ON, clearance=0.0)
    e1 = a.instances['Clamp_Lower-1'].edges
    e2 = a.instances['Panel_Lower-1'].edges
    a.ParallelEdge(movableAxis=e1[11], fixedAxis=e2[20], flip=OFF)
    f1 = a.instances['Clamp_Lower-1'].faces
    f2 = a.instances['Panel_Lower-1'].faces
    a.Coaxial(movableAxis=f1[0], fixedAxis=f2[17], flip=OFF)
    
    #完全约束Rivet-1
    f1 = a.instances['Rivet-1'].faces
    f2 = a.instances['Panel_Upper-1'].faces
    a.FaceToFace(movablePlane=f1[2], fixedPlane=f2[84], flip=OFF, clearance=4.94)
    e1 = a.instances['Rivet-1'].edges
    e2 = a.instances['Panel_Upper-1'].edges
    a.ParallelEdge(movableAxis=e1[7], fixedAxis=e2[14], flip=OFF)
    f1 = a.instances['Rivet-1'].faces
    f2 = a.instances['Panel_Lower-1'].faces
    a.Coaxial(movableAxis=f1[1], fixedAxis=f2[17], flip=OFF)
    
    #完全约束Die_Upper-1
    f1 = a.instances['Die_Upper-1'].faces
    f2 = a.instances['Rivet-1'].faces
    a.FaceToFace(movablePlane=f1[8], fixedPlane=f2[2], flip=ON, clearance=0.0)
    e1 = a.instances['Die_Upper-1'].edges
    e2 = a.instances['Rivet-1'].edges
    a.ParallelEdge(movableAxis=e1[5], fixedAxis=e2[7], flip=ON)
    f1 = a.instances['Die_Upper-1'].faces
    f2 = a.instances['Rivet-1'].faces
    a.Coaxial(movableAxis=f1[5], fixedAxis=f2[1], flip=ON)

    #完全约束Die_Lower-1
    f1 = a.instances['Die_Lower-1'].faces
    f2 = a.instances['Rivet-1'].faces
    a.FaceToFace(movablePlane=f1[8], fixedPlane=f2[0], flip=ON, clearance=0.0)
    e1 = a.instances['Die_Lower-1'].edges
    e2 = a.instances['Rivet-1'].edges
    a.ParallelEdge(movableAxis=e1[19], fixedAxis=e2[2], flip=OFF)
    f1 = a.instances['Die_Lower-1'].faces
    f2 = a.instances['Rivet-1'].faces
    a.Coaxial(movableAxis=f1[3], fixedAxis=f2[1], flip=OFF)
    
    #设置之后要用到的Sets
    e1 = a.instances['Panel_Lower-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#0 #1 ]', ), )
    e2 = a.instances['Panel_Upper-1'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#8000 #100000 #400 #8000010 ]', ), )
    a.Set(edges=edges1+edges2, name='path_x')

    e1 = a.instances['Panel_Lower-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#800 ]', ), )
    e2 = a.instances['Panel_Upper-1'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#40000 #10000000 #2000 #10020000 ]', ), 
        )
    a.Set(edges=edges1+edges2, name='path_y')

    f1 = a.instances['Panel_Upper-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#604400 #1204400 #400010 ]', ), )
    f2 = a.instances['Panel_Lower-1'].faces
    faces2 = f2.getSequenceFromMask(mask=('[#8020 ]', ), )
    a.Set(faces=faces1+faces2, name='fix_x')

    f1 = a.instances['Panel_Lower-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#4800 ]', ), )
    f2 = a.instances['Panel_Upper-1'].faces
    faces2 = f2.getSequenceFromMask(mask=('[#810a000 #880a000 #200800 ]', ), )
    a.Set(faces=faces1+faces2, name='fix_y')

    e1 = a.instances['Panel_Upper-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#10000000 #2001008 ]', ), )
    e2 = a.instances['Panel_Lower-1'].edges
    edges2 = e2.getSequenceFromMask(mask=('[#804c000 ]', ), )
    a.Set(edges=edges1+edges2, name='fix_z')

    f1 = a.instances['Rivet-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
    f2 = a.instances['Panel_Lower-1'].faces
    faces2 = f2.getSequenceFromMask(mask=('[#12000 ]', ), )
    f3 = a.instances['Panel_Upper-1'].faces
    faces3 = f3.getSequenceFromMask(mask=('[#1800090 #500090 #801000 ]', ), )
    a.Set(faces=faces1+faces2+faces3, name='symmetry_y')

    f1 = a.instances['Rivet-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#8 ]', ), )
    f2 = a.instances['Panel_Lower-1'].faces
    faces2 = f2.getSequenceFromMask(mask=('[#40008 ]', ), )
    f3 = a.instances['Panel_Upper-1'].faces
    faces3 = f3.getSequenceFromMask(mask=('[#30000220 #30000120 #80004 ]', ), )
    a.Set(faces=faces1+faces2+faces3, name='symmetry_x')