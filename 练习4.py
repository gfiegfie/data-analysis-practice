print("This is a string")  # 这是一个字符串
print("This is also a string.")  # 这也是一个字符串
print('I told my friend, "Python is my favorite language!"')
# 我告诉朋友：Python是我最喜欢的语言！
print("The language  'Python' is named after Monty Python, not the snake.")
# 语言'Python'是取自Monty Python，而不是蛇。
print("One of Python's streng is its diverse and supportive community.")
# Python的一个优点是它拥有多样而支持的社区
print()
name = "ada lovelace"
print(name.title())  # title()方法将字符串的每个单词的首字母大写
print(type(name))
print()
name = "Ada Lovelace"
print(name.upper())  # upper()方法将字符串的所有字母转换为大写
print(name.lower())  # lower()方法将字符串的所有字母转换为小写
print()
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"  # f-string 是一种格式化字符串的方法，允许在字符串中直接嵌入变量
print(full_name)
print()
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
print()
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"hello,{full_name.title()}"
print(message)
print()
print("Python")
print("\tPython")  # \t 表示制表符，通常用于对齐文本
print("python\tJava")
print()
print("python\nJava")
print("Languages:\nPython\nC\nJavaScript")  # \n 表示换行符，用于在字符串中创建新行
print("python'sbook")  # \  转义符，用于插入特殊字符
print()
# 第一个示例：定义名字和年龄，打印相关信息
name = "Edward"
age = 10
age = 10.5  # 年龄从整数变为浮点数
print(f"{name} is {age} years old.")  # 打印 Edward is 10.5 years old.
print()
# 第二个示例：定义名字和年龄，打印相关信息，并展示名字的大写形式
name = "Edward"
age = 10
print(f"{name} is {age} years old.")  # 打印 Edward 的年龄
print(f"{name.upper()} is {age} years old.")
print()
# 第三个示例：定义名字和年龄，打印相关信息，并展示名字的小写形式
name = "Edward"
age = 10
print(f"{name} is {age} years old.")  # 打印 Edward 的年龄
print(f"{name.upper()} is {age} years old.")  # 打印 Edward 的名字大写形式和年龄
print(f"{name.lower()} is {age} years old.")  # 打印 Edward 的名字小写形式和年龄
print()
print("Languages:\nPython\nC\nJavaScript")
print()
favortite_language = "Python "
print(favortite_language.rstrip())  # rstrip()方法用于去除字符串末尾的空格
print(favortite_language)  # 原字符串未改变
print(favortite_language.lstrip())  # lstrip()方法用于去除字符串开头的空格
print(favortite_language)  # 原字符串未改变
print(favortite_language.strip())  # strip()方法用于去除字符串两端的空格
favortite_language = "Python"
favortite_language = favortite_language.strip()
print(favortite_language)  # 原字符串已被修改
favortite_language = "Python "
print(favortite_language.strip())  # strip()方法去除两端的空格
print(favortite_language.lstrip())  # 原字符串未改变
print(favortite_language.rstrip())  # 原字符串未改变
print()
nostarch_url = "https://nostarch.com"
print(
    nostarch_url.removeprefix("https://")
)  # removeprefix()方法用于去除字符串开头的指定前缀
print(nostarch_url.removesuffix("/"))  # removesuffix()方法用于去除字符串结尾的指定后缀
print()
"""
lstrip()：左去除 – 只删除字符串开头（左侧）的指定字符。

rstrip()：右去除 – 只删除字符串结尾（右侧）的指定字符。

strip()：两端去除 – 同时删除开头和结尾的指定字符。

注意：这三个方法都只会删除字符串中出现的指定字符，不会影响字符串的其他部分。
"""
