# -*- coding: UTF-8 -*-

from abaqus import *
from abaqusConstants import *
from odbAccess import *
import time
import math

import makeParts
import makePartition
import defineMaterial
import makeAssembly
import makeMesh
import makeStep
import makeRigid

if __name__ == '__main__':
    #创建存储结果的文件
    with open('result.csv', 'w') as f:
        f.write('startTime: ' + time.asctime( time.localtime(time.time()) ))
    print 'startTime: ' + str(time.asctime( time.localtime(time.time())))
    
    #设置上铆模的参数
    theta_upper = 59.0
    h_upper = 1.0
    #设置下铆模的参数
    theta_lower = 66.0
    h_lower = 2.0
    #设置步长
    mystep = 1.0
    #设置上限
    myLimit = 91.0
    #设置需要修改的参数
    parameterName = "theta_upper"
    #循环次数记录
    loopNums = 1
    while 1:
        if parameterName == "theta_upper":
            theta_upper += mystep
            if theta_upper > myLimit:
                break
        elif parameterName == "h_upper":
            h_upper += mystep
            if h_upper > myLimit:
                break
        elif parameterName == "theta_lower":
            theta_lower += mystep
            if theta_lower > myLimit:
                break
        elif parameterName == "h_lower":
            h_lower += mystep
            if h_lower > myLimit:
                break
        else:
            print 'No such parameter'
            break
        #输入属性到文件
        if loopNums == 1:
            with open('result.csv', 'a') as f:
                    f.write('\n上铆模角度,' + str(theta_upper) + '度')
                    f.write('\n上铆模深度,' + str(h_upper) + '毫米')
                    f.write('\n下铆模角度,' + str(theta_lower) + '度')
                    f.write('\n下铆模深度,' + str(h_lower) + '毫米')
        else:
            with open('result.csv', 'r') as f:
                lines = f.readlines()
            with open('result.csv', 'w') as f:
                lines[1] = lines[1][0:-1] + ',,,,,上铆模角度,' + str(theta_upper) + '度\n'
                lines[2] = lines[2][0:-1] + ',,,,,上铆模深度,' + str(h_upper) + '毫米\n'
                lines[3] = lines[3][0:-1] + ',,,,,下铆模角度,' + str(theta_lower) + '度\n'
                lines[4] = lines[4][0:-1] + ',,,,,下铆模深度,' + str(h_lower) + '毫米\n'
                f.writelines(lines)
        # 为循环做准备，每次改变distance值重建Model时需要删除原来的model
        # models中至少要有一个model，故引入Model-2
        try:
            mdb.Model(name='Model-2', modelType=STANDARD_EXPLICIT)
            del mdb.models['Model-1']
            mdb.Model(name='Model-1', modelType=STANDARD_EXPLICIT)
        except:
            del mdb.models['Model-1']
            mdb.Model(name='Model-1', modelType=STANDARD_EXPLICIT)
        #建立上铆模的模型
        dieUpper = makeParts.myDieUpper(theta_upper / 2.0, h_upper)
        #建立下铆模的模型
        dieLower = makeParts.myDieLower(theta_lower / 2.0, h_lower)
        #建立上压脚模型
        clampUpper = makeParts.myClampUpper(15.0, 20.0, 1.0)
        #建立下压脚模型
        clampLower = makeParts.myClampLower(5.0, 7.45, 1.0)
        #下板的模型建立
        panelLower = makeParts.myPanelLower(25.0, 2.455, 3.0)
        #上板的模型建立
        panelUpper = makeParts.myPanelUpper()
        #无头铆钉模型的建立
        rivet = makeParts.myRivet(2.38, 15.88)

        #给上板做分割
        makePartition.makePartitionForPanelUpper(panelUpper)
        #给下板做分割
        makePartition.makePartitionForPanelLower(panelLower)
        #给上铆模做分割
        makePartition.makePartitionForDieUpper()
        #给下铆模做分割
        makePartition.makePartitionForDieLower()

        #定义材料和Section
        defineMaterial.myMaterial()
        #将Section赋予模型
        defineMaterial.assignPanelSectionForPanelUpper(panelUpper)
        defineMaterial.assignPanelSectionForPanelLower(panelLower)
        defineMaterial.assignRivetSectionForRivet(rivet)
        defineMaterial.assignPanelSectionForDieUpper()
        defineMaterial.assignPanelSectionForDieLower()
        defineMaterial.assignPanelSectionForClampUpper()
        defineMaterial.assignPanelSectionForClampLower()

        #装配部件
        makeAssembly.myAssembly(dieUpper, dieLower, clampUpper, clampLower, panelUpper, panelLower, rivet)

        #划分网格
        makeMesh.meshForClampLower(0.5)
        makeMesh.meshForClampUpper(0.5)
        makeMesh.meshForDieLower(0.3)
        makeMesh.meshForDieUpper(0.3)
        makeMesh.meshForPanelLower(0.1, 0.2, 0.3, 1.5)
        makeMesh.meshForPanelUpper(0.1, 0.2, 0.3, 1.5)
        makeMesh.meshForRivet(0.2)

        #设置刚体
        makeRigid.makeDURigid()
        makeRigid.makeDLRigid()
        makeRigid.makeCURigid()
        makeRigid.makeCLRigid()

        #创建分析步
        makeStep.myStep(10000.0, 125.0)

        #创建Job
        mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
            memoryUnits=PERCENTAGE, explicitPrecision=SINGLE,
            nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF,
            contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='',
            resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1,
            activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)

        #提交
        mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
        
        #等待分析作业完成
        mdb.jobs['Job-1'].waitForCompletion()
        
        #处理结果
        myodb = openOdb('Job-1.odb')
        nodeRegion1 = myodb.rootAssembly.nodeSets['PATH_X']
        nodeRegion2 = myodb.rootAssembly.nodeSets['PATH_Y']
        displacements = myodb.steps['Step-2'].frames[-1].fieldOutputs['U']
        sets1 = displacements.getSubset(region = nodeRegion1).values
        sets2 = displacements.getSubset(region = nodeRegion2).values
        pathx_data = map(lambda x:[x.nodeLabel, x.data[0], x.data[1], x.data[2]], sets1)
        pathy_data = map(lambda x:[x.nodeLabel, x.data[0], x.data[1], x.data[2]], sets2)
        if loopNums == 1:
            with open('result.csv', 'a') as f:
                f.write('\n\nnodeLabel,pathx_data')
            sum1 = 0
            for data in pathx_data:
                with open('result.csv', 'a') as f:
                    f.write('\n' + str(data[0]) + ',' + str(data[1]))
                print "nodeLabel:%s, x = %s" % (data[0], data[1])
                sum1 += abs(data[1])
            
            average1 = sum1 / len(pathx_data)
            res1 = round(average1 * 100 / 4.76, 2)
            
            with open('result.csv', 'a') as f:
                f.write('\n\naverage1,' + str(res1) + '%\n ')
            print "\n"
        else:
            with open('result.csv', 'r') as f:
                lines = f.readlines()
            with open('result.csv', 'w') as f:
                lines[6] = lines[6][0:-1] + ',,nodeLabel,pathx_data\n'
                f.writelines(lines)
            sum1 = 0
            count = 0   
            for data in pathx_data:
                with open('result.csv', 'r') as f:
                    lines = f.readlines()
                with open('result.csv', 'w') as f:
                    lines[count + 7] = lines[count + 7][0:-1] + ',,' + str(data[0]) + ',' + str(data[1]) + '\n'
                    f.writelines(lines)
                print "nodeLabel:%s, y = %s" % (data[0], data[1])
                sum1 += abs(data[1])
                count += 1
            average1 = sum1 / len(pathx_data)
            res1 = round(average1 * 100 / 4.76, 2)
            
            with open('result.csv', 'r') as f:
                lines = f.readlines()
            with open('result.csv', 'w') as f:
                lines[-2] = lines[-2][0:-1] + ',,average1,' + str(res1) + '%\n'
                f.writelines(lines)
            print "\n"

        with open('result.csv', 'r') as f:
            lines = f.readlines()
        with open('result.csv', 'w') as f:
            lines[6] = lines[6][0:-1] + ',,nodeLabel,pathy_data\n'
            f.writelines(lines)

        sum2 = 0
        count = 0   
        for data in pathy_data:
            with open('result.csv', 'r') as f:
                lines = f.readlines()
            with open('result.csv', 'w') as f:
                lines[count + 7] = lines[count + 7][0:-1] + ',,' + str(data[0]) + ',' + str(data[2]) + '\n'
                f.writelines(lines)
            print "nodeLabel:%s, y = %s" % (data[0], data[2])
            sum2 += abs(data[2])
            count += 1
        
        average2 = sum2 / len(pathy_data)
        res2 = round(average2 * 100 / 4.76, 2)
        
        with open('result.csv', 'r') as f:
            lines = f.readlines()
        with open('result.csv', 'w') as f:
            lines[-2] = lines[-2][0:-1] + ',,average2,' + str(res2) + '%\n'
            f.writelines(lines)
        print "\n"
        
        average = (sum1 + sum2) / (len(pathx_data) + len(pathy_data))
        res = round(average * 100 / 4.76, 2)
        if loopNums == 1:
            with open('result.csv', 'r') as f:
                lines = f.readlines()
            with open('result.csv', 'w') as f:
                lines[-1] = lines[-1][0:-1] + ',,,average,' + str(res) + '%\n'
                f.writelines(lines)
        else:
            with open('result.csv', 'r') as f:
                lines = f.readlines()
            with open('result.csv', 'w') as f:
                lines[-1] = lines[-1][0:-1] + ',,,,,average,' + str(res) + '%\n'
                f.writelines(lines)
        print "result = %s%%" % res
        
        del mdb.jobs['Job-1']
        loopNums += 1
    
    with open('result.csv', 'a') as f:
            f.write('\nendTime: ' + time.asctime( time.localtime(time.time()) ))
    print 'endTime: ' + str(time.asctime( time.localtime(time.time())))