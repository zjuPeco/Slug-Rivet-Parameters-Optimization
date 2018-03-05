# 铆钉铆接参数优化
在铆钉的铆接过程中，涉及的参数较多，如何选择最优的参数组合成了一个难题。这里提供了两种思路，详情请参见[这里](http://47.100.104.7/2/)。

## 运行环境
有限元仿真软件：abaqus 6.14

语言：python2.7

## 方案一：回归+遗传算法
1. 设置Method1/DataPreparation/demo.py中的参数并在Abaqus环境下运行，获取数据。

2. 依次运行Method1/Regression&Optimization下的collect data.ipynb和locally weighted linear regression.ipynb

## 方案二：只用遗传算法
1. 设置Method2/geneticOptimize.py中的参数并载Abaqus环境下运行。