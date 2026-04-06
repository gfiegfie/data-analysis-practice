print("Hello, world!")  # 你好，世界
print("Hello, Python, World!")  # 你好，Python，世界
message = "Hello Python Crash Course World!"
print(message)
message = "Hello Python Crash Course World!"
print(message)
message = "Hello, Python learner!"  # 你好，Python学习者！
print(message)
message = "First message: Learning python is fun!"  # 第一条消息：学习python很有趣
print(message)
message = "Second message: Practice makes perfect!"  # 第二条消息：世间出真相
print("Hello")
print("你好。")
print("初次见面。")
print("你好。", end=" ")
print("初次见面。")
print("风\n林\n火\n山")
print("风")
print("林")
print("火")
print("山")
print("你好，")
print()
print("初次见面。")
print("Hello!\nGood Bay!")  # 你好，再见！
print()
print("I am studying python")  # 我正在学习Python
print("Life is short, use Python.")  # 生活短暂，使用Python。
print("Life's pathetic, let's  bepythonic.")  # 生活很可怜，让我们更加pythonic。
print("Hello, {}. You are {} yeaars old.".format("Alice", 30))
print("{0}加上{1}等于{2}".format(10, 20, 10 + 20))
print("The number is {:.2f}".format(3.14159))  # 控制小数点后的位置
print("Left aligned: {:<10}".format("test"))  # 左对齐
print("Right aligned: (:>10)".format("test"))  # 右对齐
print("Center aligned:{:^10}".format("test"))  # 居中对齐
print("Padded: {:*^10}".format("test"))  # 填充和宽度
print("Number with commas: {:,}".format(123456789))  # 数字格式化，整数的千位分隔符
print("Percentage: {:.2%}".format(0.756))  # 百分比格式化，小数点后两位
import datetime  # 日期格式化

now = datetime.datetime.now()
print("Current date: {:%Y-%m-%d %H:%M:%S}".format(now))
print(r"python's book. \n")  # 特殊字符 r
