# 导入os模块，它提供了与操作系统交互的方法和功能
import os
# 导入datetime模块，用于处理日期和时间
import datetime

# 定义要修改的文件夹的路径
path = '/opt/因子分类'

# 使用datetime获取当前时间并将其格式化为"_YYYY-MM-DD_HH-MM-SS"的形式
timestamp = datetime.datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")

# 使用os.listdir遍历指定文件夹中的所有文件和子文件夹
for filename in os.listdir(path):
    if filename.endswith('.csv'):  # 如果文件名以.csv结尾
        # 分割文件名和扩展名，并在文件名中插入时间戳
        new_filename = filename.rsplit('.', 1)[0] + timestamp + '.' + filename.rsplit('.', 1)[1]
        # 使用os.rename重命名文件
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))

'''
代码功能说明：

此代码的主要目的是自动重命名指定文件夹中的所有.csv文件，将当前的时间戳添加到每个文件名的末尾。

    模块导入：代码开始时，我们导入了os和datetime模块。os模块允许我们与操作系统交互，例如遍历文件夹和重命名文件。datetime模块允许我们处理日期和时间。

    指定路径：我们指定了要更改的文件夹的路径，这里是/opt/因子分类。

    获取并格式化当前时间：我们获取当前的日期和时间，并将其格式化为特定的形式，即"_YYYY-MM-DD_HH-MM-SS"。

    遍历并重命名：我们遍历指定文件夹中的所有文件。对于每个文件，如果其扩展名为.csv，我们将文件名和扩展名分开，并在它们之间插入我们之前创建的时间戳。然后，我们使用os.rename来重命名这个文件。
'''