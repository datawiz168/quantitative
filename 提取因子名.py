# 导入os模块，用于操作系统相关的操作
import os

# 定义存放因子的文件夹路径
factors_directory = '/opt/factors'
# 初始化一个空列表来存储找到的因子名
factors = []

# 使用os.listdir遍历指定文件夹中的所有文件
for filename in os.listdir(factors_directory):
    # 如果文件名以.py结尾并且不是'__init__.py'文件
    if filename.endswith('.py') and filename != '__init__.py':
        # 使用os.path.splitext去除文件的扩展名，从而得到因子的名称
        factor_name = os.path.splitext(filename)[0]
        # 将因子名添加到factors列表中
        factors.append(factor_name)

# 打印找到的所有因子名
print(factors)
# 打印找到的因子的总数
print(f"因子总数: {len(factors)}")


'''
代码功能说明：

此代码的主要目的是从指定的文件夹（/opt/factors）中列出所有的Python文件，并将这些文件的名称（除了扩展名）认为是"因子"的名称。这些"因子"通常是量化交易中使用的信号或策略。

    指定路径：代码开始时，我们定义了一个路径，该路径指向存放因子的文件夹。

    遍历文件夹：我们遍历指定文件夹中的所有文件。对于每个文件，我们检查它是否是一个Python文件（扩展名为.py）并确保它不是__init__.py文件，因为__init__.py通常用于Python包的初始化，并不包含实际的"因子"代码。

    获取因子名：对于每个满足条件的Python文件，我们使用os.path.splitext函数去除其扩展名，从而得到因子的名称。

    输出结果：最后，我们打印出找到的所有因子名和因子的总数。

通过这段代码，用户可以快速地从一个文件夹中获取所有的因子名，这对于量化策略的管理和概览非常有用。

'''