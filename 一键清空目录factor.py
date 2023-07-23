import os
import shutil
import time

# 获取当前文件的根目录
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',))
# 构建目标目录路径
target_dir = os.path.join(root_path, 'data', 'f', 's')

# 创建一个列表，用于存储目标目录中所有文件和子目录的绝对路径
file_list = []
for root, dirs, files in os.walk(target_dir):
    # 将所有文件的绝对路径添加到列表中
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)
    # 将所有子目录的绝对路径添加到列表中
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        file_list.append(dir_path)

# 检查列表中是否有任何文件或子目录
num_files = len(file_list)
if num_files == 0:
    print("目录下没有任何文件或子目录，无需删除！")
    exit()

# 将文件和子目录分为5个部分，每个部分的数量大致相等
num_parts = 5
# 如果文件数量少于5，调整部分的数量
if num_files < num_parts:
    num_parts = num_files

num_files_per_part = num_files // num_parts
# 如果文件数量除以部分数量有余数，调整计数
if num_files % num_parts != 0:
    num_parts += 1
    num_files_per_part = num_files // num_parts

# 创建一个列表的列表，其中每个子列表都包含每部分的文件
file_parts = [file_list[i:i+num_files_per_part] for i in range(0, num_files, num_files_per_part)]

# 逐个删除每个部分的文件
for i, file_part in enumerate(file_parts):
    print(f"开始删除第{i+1}份文件...")
    for file_path in file_part:
        try:
            # 使用系统的rm命令删除文件/目录
            os.system(f"rm -rf {file_path}")
        except Exception as e:
            # 如果出现错误，打印出来
            print(f"删除{file_path}失败。原因: {e}")
    # 在删除每部分后打印成功消息
    print(f"第{i+1}份文件删除成功！等待3秒继续...")
    # 在继续下一个部分之前等待3秒
    time.sleep(3)

# 在所有部分都被删除后打印成功消息
print("所有文件删除成功！")


'''
代码功能说明：

这段代码的主要功能是删除一个特定目录（及其子目录）下的所有文件和子目录。主要的操作步骤如下：

    目标目录定义：代码首先定义了要删除内容的目标目录。这个目录是基于当前脚本文件位置的相对路径。

    收集文件和目录：通过遍历目标目录及其所有子目录，代码收集了所有文件和子目录的绝对路径，并将它们存储在一个列表中。

    分组和计数：然后，这些文件和目录被分为5个部分，确保每个部分的数量大致相等。如果不能均匀分配，代码会进行适当的调整。

    分批删除：代码逐个删除每个部分的文件和目录。为了使用户能够看到删除过程的进度，每删除一个部分后，代码会等待3秒再继续下一个部分的删除。

    完成消息：当所有文件和目录都被删除后，代码会打印一个完成消息。

这种分批删除的方法有助于确保在删除大量文件和目录时，不会对文件系统造成太大压力。同时，通过在每个部分之间添加延迟，用户可以更容易地观察和控制删除过程。
'''
