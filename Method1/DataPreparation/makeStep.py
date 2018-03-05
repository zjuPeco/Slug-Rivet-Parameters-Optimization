# -*- coding: UTF-8 -*-

from abaqus import *
from abaqusConstants import *


def myStep(pushForce, fixForce):
    """
    创建分析步
    """
    #建立Step-1和Step-2
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
        timePeriod=0.001)
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-2', previous='Step-1', 
        timePeriod=0.001)
    #设置接触
    mdb.models['Model-1'].ContactProperty('IntProp-1')
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.2, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    mdb.models['Model-1'].ContactExp(name='Int-1', createStepName='Initial')
    mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
        stepName='Initial', useAllstar=ON)
    mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
        stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))
    #设置边界条件
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.instances['Die_Upper-1'].referencePoints
    refPoints1=(r1[2], )
    region = a.Set(referencePoints=refPoints1, name='DU')
    mdb.models['Model-1'].DisplacementBC(name='fixDU', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.instances['Die_Lower-1'].referencePoints
    refPoints1=(r1[2], )
    region = a.Set(referencePoints=refPoints1, name='DL')
    mdb.models['Model-1'].DisplacementBC(name='fixDL', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    r1 = a.instances['Clamp_Upper-1'].referencePoints
    refPoints1=(r1[2], )
    region = a.Set(referencePoints=refPoints1, name='CU')
    mdb.models['Model-1'].DisplacementBC(name='fixCU', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    r1 = a.instances['Clamp_Lower-1'].referencePoints
    refPoints1=(r1[2], )
    region = a.Set(referencePoints=refPoints1, name='CL')
    mdb.models['Model-1'].DisplacementBC(name='fixCL', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['fix_x']
    mdb.models['Model-1'].DisplacementBC(name='fix_x', createStepName='Step-1', 
        region=region, u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
        fieldName='', localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['fix_y']
    mdb.models['Model-1'].DisplacementBC(name='fix_y', createStepName='Step-1', 
        region=region, u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
        fieldName='', localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['fix_z']
    mdb.models['Model-1'].DisplacementBC(name='fix_z', createStepName='Step-1', 
        region=region, u1=UNSET, u2=UNSET, u3=0.0, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
        fieldName='', localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['symmetry_x']
    mdb.models['Model-1'].XsymmBC(name='fix_symmetry_x', createStepName='Step-1', 
        region=region, localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['symmetry_y']
    mdb.models['Model-1'].YsymmBC(name='symmetry_y', createStepName='Step-1', 
        region=region, localCsys=None)
    #设置Amplitude
    mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (0.001, 1.0)))
    #Step-2中边界条件的更改
    mdb.models['Model-1'].boundaryConditions['fixDL'].setValuesInStep(
        stepName='Step-2', u3=-0.3, amplitude='Amp-1')
    mdb.models['Model-1'].boundaryConditions['fixDU'].setValuesInStep(
        stepName='Step-2', u3=0.3, amplitude='Amp-1')
    #设置载荷
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['DU']
    mdb.models['Model-1'].ConcentratedForce(name='DULoad', createStepName='Step-1', 
        region=region, cf3=-pushForce, amplitude='Amp-1', 
        distributionType=UNIFORM, field='', localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['DL']
    mdb.models['Model-1'].ConcentratedForce(name='DLLoad', createStepName='Step-1', 
        region=region, cf3=pushForce, amplitude='Amp-1', 
        distributionType=UNIFORM, field='', localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['CU']
    mdb.models['Model-1'].ConcentratedForce(name='CULoad', createStepName='Step-1', 
        region=region, cf3=-fixForce, amplitude='Amp-1', distributionType=UNIFORM, 
        field='', localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['CL']
    mdb.models['Model-1'].ConcentratedForce(name='CLLoad', createStepName='Step-1', 
        region=region, cf3=fixForce, amplitude='Amp-1', distributionType=UNIFORM, 
        field='', localCsys=None)
    #更改Step-2中的载荷
    mdb.models['Model-1'].loads['DLLoad'].deactivate('Step-2')
    mdb.models['Model-1'].loads['DULoad'].deactivate('Step-2')