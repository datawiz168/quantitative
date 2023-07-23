# 导入os模块用于操作系统相关操作，导入time模块用于计时
import os
import time

# 获取当前时间作为起始时间
start = time.time()

# 获取当前脚本所在文件夹的父文件夹的绝对路径
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 根据root_path构建12个脚本的路径，这些脚本的名字是'选币数据整理i.py'，其中i从0到11
scripts = [
    os.path.join(root_path, 'ba', f'选币数据整理{i}.py') for i in range(12)
]

# 初始化一个列表来保存子进程的PID
pids = []
# 遍历所有脚本
for script in scripts:
    # 使用os.fork()创建一个子进程
    pid = os.fork()
    if pid > 0:
        # 如果在父进程中，os.fork()会返回子进程的PID
        pids.append(pid)
    else:
        # 如果在子进程中，os.fork()会返回0
        # 使用os.system在子进程中运行脚本
        os.system(f"python {script}")
        # 完成后，子进程退出
        os._exit(0)

# 在父进程中等待所有子进程完成
for pid in pids:
    os.waitpid(pid, 0)

# 获取结束时间
end = time.time()
# 打印整个程序的运行时间
print('程序运行时间为: %s Seconds'%(end-start))


'''
代码功能说明：

此代码的主要目的是并发地运行12个Python脚本。这些脚本名为 选币数据整理i.py，其中i从0到11。

    获取起始时间：使用time.time()获取程序开始的时间。

    构建脚本路径：确定要运行的12个Python脚本的路径。

    创建子进程并运行脚本：使用os.fork()为每个脚本创建一个子进程。在子进程中，使用os.system()运行脚本。每个子进程完成脚本的运行后会退出。

    等待子进程完成：在主进程（也就是父进程）中，使用os.waitpid()等待所有子进程完成。

    计算并打印运行时间：最后，代码计算整个程序的运行时间并打印结果。

通过使用os.fork()并发地运行多个脚本，该代码可以显著提高执行效率，特别是当每个脚本都需要大量的计算时。这种并发执行方式充分利用了多核处理器的能力，提高了资源的利用效率。
'''