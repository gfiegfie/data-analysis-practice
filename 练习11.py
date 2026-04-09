"""
众数

手工计算

数据集：[1, 2, 2, 3] → 出现最多次的是 2（2次） → 众数 = 2
"""

"""
翻译：从 scipy 库中导入 stats 模块。
解释：scipy 是一个科学计算库，stats 模块提供了统计相关的函数
（如计算众数、均值、分布等）。这里只导入 stats，而不是整个 scipy
"""
from scipy import stats


# 翻译：创建一个名为 data 的列表，包含四个整数：1, 2, 2, 3。
# 解释：这是一个普通 Python 列表，用于存放数据样本
data = [1, 2, 2, 3]

"""
翻译：调用 stats.mode() 函数，计算 data 列表的众数，并将返回的结果赋值给变量 mode_result。
解释：众数是一组数据中出现次数最多的数值。这里 data 中 2 出现两次，
1 和 3 各出现一次，所以众数是 2。返回的结果是一个 ModeResult 对象，包含众数值和出现次数
"""
mode_result = stats.mode(data)
"""
翻译：将变量 mode_result 的内容输出到控制台。
解释：打印的结果通常类似于 ModeResult(mode=array([2]), 
count=array([2]))，表示众数为 2，出现次数为 2。

注意：较新版本的 scipy 中，stats.mode 返回的是一个对象，
包含 mode 和 count 属性。如果想只打印众数，
可以写 print(mode_result.mode[0])

"""

print(mode_result)
"""
mode 返回一个对象， mode_result.mode 是众数值,
mode_result.count 是出现次数
"""
