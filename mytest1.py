# -*- coding: utf-8 -*-
# Filename : mytest1.py

import numpy as np 
from numpy import *
import matplotlib.pyplot as plt 

# 测试数据集
dataSet = [[-0.017612, 14.053064],[-1.395634,2],[-0.752157,6.538620],[-1.322371,7.152853],
[0.423363,11.054677],[0.406704,7.067335],[0.667394,12.741452],[-2.460150,6.866805],
[0.569411,9.548755],[-0.026632,10.427743],[0.850433,6.920334],[1.347183,13.175500],
[1.176813,3.167020],[-1.781871,9.097953]]

# 将数据集转换为numpy矩阵，并转置
dataMat = mat(dataSet).T

# 绘制数据集散点图
plt.scatter(dataMat[0],dataMat[1],c='red',marker='o')

# 绘制直线图形
# 产生直线数据集
X = np.linspace(-2,2,100)
# 建立线性方程
Y = 2.8 * X + 9
# 绘制直线图
plt.plot(X,Y)
# 显示绘制后的结果
plt.show()