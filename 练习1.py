# 变量定义
name = "张三"  # name: 表示名称
age = 25  # age: 表示年龄
score = 89.5  # score: 表示浮点数
is_pass = True  # is_pass: 表示是否通过

# 打印
print(name, age, score, is_pass)

# 类型转换
# num 表示 "number" 意为数字， str 表示"string" 意为字符串
# 因此，num_str 可以翻译为 “number string”，即数字字符串。在代码中，num_str 被赋值为 "123"，这是一个包含数字的字符串。
"""
is_pass： 
前缀 is_：在命名布尔变量时，使用 is_ 或 has_ 前缀是一个常见的约定。这提高了代码的可读性，
明确表示该变量是一个布尔值，通常用于表示某种状态或条件是否满足。
pass：表示“通过”的意思。因此，is_pass 表示“是否通过”。
num_int： 
num：表示“number”，意为数字。这表明该变量与数字有关。
int：表示“integer”，意为整数。这表明该变量的具体类型是整数。
组合 num_int：num_int 表示“数字整数”，即一个将字符串转换后的整数。
user_input： 
user：表示用户。
input：表示输入的内容。
组合 user_input：user_input 表示“用户输入的内容”，即从用户那里获取的输入。

"""
num_str = "123"  # num_str: 表示字符串数字
num_int = int(num_str)  # num_int: 表示将字符串转换后的整数
print(num_int + 10)

# 用户输入
user_input = input("请输入您的姓名：")  # user_input: 表示用户输入的姓名
print("您好," + user_input)  # 表示用户输入的姓名

# 将 age 转换为字符串后拼接输出
print("年龄" + str(age))  # 使用 str() 函数将 age 转为字符串
