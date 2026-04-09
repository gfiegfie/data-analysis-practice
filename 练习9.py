"""
统计学

手工计算均值

数据集：[2, 4, 6, 8]

公式：均值 = (2+4+6+8) / 4 = 20 / 4 = 5
"""

# 导入 numpy 库，并为其指定别名 np
import numpy as np

# 创建一个名为 data 的列表，包含四个整数元素：2、4、6、
data = [2, 4, 6, 8]
# 调用 numpy 库中的 mean 函数，计算 data 列表中所有元素的算术平均值，
# 并将结果赋值给变量 mean_val
mean_val = np.mean(data)
# 将变量 mean_val 的值输出到控制台
print(mean_val)
"""
import numpy as np: 导入NumPy 库并简写为Np
np.mean(data): 调用 NumPy 的 mean 函数计算均值
"""
