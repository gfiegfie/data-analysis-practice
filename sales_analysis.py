import pandas as pd

# 1. 读取 Excel 文件
df = pd.read_excel("销售数据.xlsx")
print("原始数据: ")
print(df)
print("\n" + "=" * 40 + "\n")

# 2. 计算总销售额
total_sales = df["销售额"].sum()
print(f"1. 总销售额: {total_sales} 元")

# 3. 计算平均每个商品的销售额
avg_sales = df["销售额"].mean()
print(f"2. 平均每个商品的销售额: {avg_sales:.2f} 元")

# 4. 找出销售额最高的商品
best_idx = df["销售额"].idxmax()
best_product = df.loc[best_idx, "商品名称"]
best_sales = df.loc[best_idx, "销售额"]
print(f"3. 卖得最好的商品: {best_product}, 销售额: {best_sales} 元")

# 5. 找出销售额最低的商品
worst_idx = df["销售额"].idxmax()
worst_product = df.loc[worst_idx, "商品名称"]
worst_sales = df.loc[worst_idx, "销售额"]
print(f"4. 买的最差的商品: {worst_product}, 销售额: {worst_sales} 元")

# 6. 筛选销售额超过 500 元的商品
high_sales = df[df["销售额"] > 500]
print("\n5. 销售额超过 500 元的商品: ")
print(high_sales[["商品名称", "销售额"]])
