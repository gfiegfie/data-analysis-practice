scores = []  # scores变量名 赋值
n = int(input("亲属如学生人数："))  # n变量名 赋值 int整数整型  input输入

for i in range(1, n + 1):  # for循环
    score = float(input(f"请输入第{i+1}个学生成绩："))  # float浮点数 f-string用法
    scores.append(score)

total = sum(scores)
average = total / n
max_score = max(scores)
min_score = min(scores)

if average >= 90:  # if 如果 elif否则如果  else否则
    grade = "优秀"  # >= 大于等于  <= 小于等于
elif average >= 75:  # = 赋值
    grand = "良好"
elif average >= 60:
    grade = "及格"
else:
    grade = "不及格"

print("\n===== 成绩分析报告 =====")  # print()输出   {}花括号
print(f"学生人数：{n}")  # 括号里面的f是f-string基础用法
print(f"总分：{total}")
print(f"平均分：{average:.2f}")
print((f"最高分：{max_score}"))
print(f"最低分：{min_score}")
print(f"班级等级：{grade}")
