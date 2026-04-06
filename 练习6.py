name = "Eric"
print(f"Hello {name}, would you like to learn some Python tooay?")
print()
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
print()
name = "ada lovelace"
print(name.lower())  # 全小写
print(name.upper())  # 全大写
print(name.title())  # 首字母大写
print()
print(
    'Albert Einstein once said, "A person who never made a mistake never tried anything new.'
)
print()
famous_person = "Albert Einstein"
message = f'{famous_person} once said,  "A person who never made a mistake never tried anything new." '
print(message)
print()
name = "\t\n  Albert Einstein  \n\t"
print(f"原始：'{name}'")
print(f"使用 lstrip(): '{name.lstrip()}'")
print(f"使用 rstrip(): '{name.rstrip()}'")
print(f"使用 strip(): '{name.strip()}'")
print()
filename = "python_notes.text"
print(filename.removesuffix(".text"))
print()
"""
lstrip()：左去除 – 只删除字符串开头（左侧）的指定字符。

rstrip()：右去除 – 只删除字符串结尾（右侧）的指定字符。

strip()：两端去除 – 同时删除开头和结尾的指定字符。
"""
