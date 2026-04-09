"""
给定身高数据（cm）：[160, 165, 170, 170, 175]

手工计算

均值：(160+165+170+170+175)/5 = 840/5 = 168

中位数：排序后中间是第3个 → 170

众数：170 出现 2 次 → 170

"""

# 导入 numpy 库，并起别名为 np。
# numpy 是数值计算的基础库，后面用 np.mean 计算均值、np.median 计算中位数
import numpy as np

# 从 scipy 库中导入 stats 模块。
# scipy.stats 提供了统计函数，后面用 stats.mode 计算众数。
from scipy import stats

# 创建一个名为 heights 的列表，包含 5 个身高数值（单位假设为厘米）。
# 这是一个样本数据，用于演示均值、中位数、众数的计算
heights = [160, 165, 170, 170, 175]

# 打印字符串 "Mean:" 并接着打印 heights 的算术平均值。
# np.mean(heights) 计算 (160+165+170+170+175)/5 = 168.0，输出 Mean: 168.0
print("Mean:", np.mean(heights))

# 打印字符串 "Median:" 并接着打印 heights 的中位数。
# 排序后为 [160,165,170,170,175]，中位数是第 3 个数（索引 2）：170.0，输出 Median: 170.
print("Median:", np.median(heights))

# 打印字符串 "mode:" 并接着打印 heights 的众数结果。
# stats.mode(heights) 返回一个 ModeResult 对象，包含众数值和出现次数。
# 170 出现 2 次，输出类似 mode: ModeResult(mode=array([170]), count=array([2]))
print("mode:", stats.mode(heights))
