import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", encoding="utf-8")

print("数据前几行：")
print(df.head())

avg_age = df["年龄"].mean()
print("平均年龄：", avg_age)

city_avg = df.groupby("城市")["年龄"].mean()
print("各城市平均年龄：")
print(city_avg)

plt.bar(city_avg.index, city_avg.values)
plt.title("各城市平均年龄：")
plt.xlabel("城市")
plt.ylabel("平均年龄")
plt.show()
print("程序运行完毕！")
