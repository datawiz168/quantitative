import pandas as pd

# 设定要读取的行数
n = 100

# 读取csv文件的前n行
df = pd.read_csv('多头数字占比配套.csv', nrows=n)

# 计算多头这一列各个数字的占比
counts = df['多头'].value_counts(normalize=True) * 100

# 将占比转换为保留两位小数的百分比形式
formatted_counts = counts.round(2).astype(str) + "%"

# 打印结果
print(formatted_counts)
