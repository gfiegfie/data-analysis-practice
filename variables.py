# 年龄
age = 25
print(age)
print(type(age))
print()
# 姓
__name__ = "Li"
print(__name__)
print(type(__name__))
print()
# 名字
first_name = "Alice"
print(first_name)
print(type(first_name))
print()
# 不合法变量名，变量不能以数字开头
# 2var = 10
# 合法变量名
vars = 10
print(vars)
print(type(vars))
print()
# 大小写敏感，变量名区分大小写
Name = "Bob"
name = "bob"
print(Name, name)  # 输出结果：Bob bob (不同变量)
print(type(Name))
print(type(name))
print()
"""
 规则总结：变量名必须以字母或下划线开头
 后续可以包含字母、数字和下划线；变量名区分大小写；
 变量名不能是 Python 的保留字（如 if、for、while 等）书
"""
# 字符串基本操作，字符串定义
s1 = "python"  # 单引号
s2 = "python"  # 双引号
s3 = "It's okay"  # 双引号内可包含单引号
print(s1, s2, s3)
print(type(s1))
print(type(s2))
print(type(s3))
print()
# .upper() / .lower() / .title()
# 姓名
name = "alice li"
print(name.upper())  # 输出结果：ALICE LI (全部大写)
print(name.lower())  # 输出结果：alice li (全部小写)
print(name.title())  # 输出结果：Alice Li (每个单词首字母大写)
# .upper() 将所有字母转为大写，.title() 将每个单词首字母大写。
print()
# 字符串拼接
# 名字
first = "John"
# 姓氏
last = "Doe"
# 完整的全名姓名
full = first + " " + last
print(full)  # 输出结果：John Doe
print(type(first))
print(type(last))
print(type(full))
# type() 类型转换显示类型
# f-string() 格式化字符串
# 年龄
age = 25
# 消息 本行生成一个包含名字和年龄的完整句子
message = f"{first} is {age} years old."
print(message)
print(type(message))  # f 前缀表示字符串内｛变量名｝会被替换为变量的值
print()
# 数字类型  整型与浮点数
x = 5  # int
y = 3.14  # Float
print(type(x), type(y))
print()
# 下划线表示大数
# 宇宙的年龄
universe_age = 13_800_000_000  # 整数  下划线仅为视觉分割，不影响数值
print(type(universe_age))
print(universe_age)
print()
# 多变量赋值
a, b, c = 1, 2, 3
print(a, b, c)
print(type(a), type(b), type(c))
print()
x = y = z = 0
print(x, y, z)
print(type(x), type(y), type(z))
print()
# 简单打印消息
# 消息       Python的优势之一是其多样化的社区
message = "One of Python's strengths is its diverse community."
print(message)
print(type(message))
print()
# 调整名字大小写
# 名字：阿尔伯特.爱因斯坦
name = "albert einstein"
print(name.lower())  # 全部小写 albert einstein
print(name.upper())  # 全部大写 ALABERT EINSTEIN
print(name.title())  # 首字母大写 Alabert Einstein
print(name)
print(type(name))
print()
# 剔除人名中的空白
# 姓名
name = "\t Albert\n "
print(f"---{name}---")  # 原始字符串
print(f"---{name.lstrip()}---")  # 删除左边空白
print(f"---{name.rstrip()}---")  # 删除右边空白
print(f"---{name.strip()}---")  # 删除两边空白
print(name)
print(type(name))
print()
