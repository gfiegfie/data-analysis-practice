"""
思路
用 input() 获取两个数字（字符串）。

用 int() 将字符串转换为整数。

分别计算和、差、积、商。

输出结果，商使用格式化保留两位小数。
"""

# 获取用户输入
num1_str = input("请输入第一个数字：")  # num1: 表示用户输入的第一个数字
num2_str = input("请输入第二个数字：")  # num2: 表示用户输入的第二个数字

# 转换为整数
num1 = int(num1_str)
# num1: 表示将第一个数字字符串转换后的整数 (num1: 表示用户输入的第一个数字)
num2 = int(num2_str)
# num2: 表示将第二个数字字符串转换后的整数 (num2: 表示用户输入的第二个数字)

#  计算
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
# 除法注意除数不能为零，这里假设输入合法
quot_result = num1 / num2

# 输出结果，商保留两位小数
print("和: ", sum_result)
print("差:", diff_result)
print("积:", prod_result)
print("商: {:.2f}".format(quot_result))  # 或使用 f"{quot_result:.2f}
