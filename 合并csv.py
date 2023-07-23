import pandas as pd

# 定义两个csv文件的路径
csv_files = [
    '合并csv配套表格1.csv', 
    '合并csv配套表格2.csv'
]

# 初始化一个空列表，用于存储数据帧
df_list = []

# 打印找到的csv文件的总数
print(f"找到了{len(csv_files)}个csv文件。")

# 遍历csv文件列表
for i, csv in enumerate(csv_files, start=1):
    # 将每个csv文件读取为pandas数据帧，并追加到列表中
    df_list.append(pd.read_csv(csv))

    # 打印进度
    print(f"已读取{i}个，总共{len(csv_files)}个文件。")

# 将列表中的所有数据帧连接起来
combined_df = pd.concat(df_list)

# 定义要检查NaN值的列
cols_to_check = ['因子参数', '多头', '空头',]

# 在指定列中删除至少有一个元素丢失的行
combined_df = combined_df.dropna(subset=cols_to_check)

# 定义要转换为整数的列
cols_to_convert = ['因子参数', '多头', '空头',]

# 将列转换为整数
for col in cols_to_convert:
    combined_df[col] = combined_df[col].astype(int)

# 基于特定列删除重复行
combined_df = combined_df.drop_duplicates(subset=['因子名', '因子TF', '因子参数', '多头', '空头'])

# 按'desc'列的降序对DataFrame进行排序
combined_df = combined_df.sort_values('l', ascending=False)

# 打印消息，表示操作已完成
print("完成。")

# 将排序后的DataFrame保存到新的csv文件中
combined_df.to_csv('合并总.csv', index=False, encoding='utf-8-sig')

'''
代码功能说明：

此代码的主要功能是从两个csv文件中读取数据，然后对数据进行清洗、合并、去重和排序操作，最后保存为一个新的csv文件。以下是代码的详细步骤：

    读取CSV文件：代码首先定义了两个csv文件的路径，然后遍历这些文件路径，将每个文件读取为pandas数据帧，并存储在一个列表中。

    连接数据帧：所有单独的数据帧被连接起来，形成一个大的数据帧。

    删除缺失值：代码定义了需要检查缺失值（NaN）的列，然后从这些列中删除了包含缺失值的任何行。

    转换数据类型：某些列的数据类型被转换为整数。

    删除重复行：基于特定的列集合，代码删除了重复的行。

    排序数据：数据帧按照"l"列的值进行降序排序。

    保存数据：排序后的数据帧被保存为一个新的csv文件。
'''