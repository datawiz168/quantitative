import os
import time
start=time.time()
os.system("python ./自动遍历前准备.py")
os.system("python ./创建回放结果文件夹.py")
os.system("python ./更新因子.py")
os.system("python /opt/更新因子参数.py")
os.system("python ./一键更新检查.py")
time.sleep(3)
os.system("python ./策略回放.py")
end=time.time()
print('多个程序运行时间为: %s Seconds'%(end-start))
exit()
'''
这段代码主要是为了自动执行一系列的Python脚本，并在执行过程中插入一个3秒的暂停。
它还计算并输出了整个过程的总运行时间。这种自动化的方式可以帮助用户一次性执行多个脚本，
而不需要手动地一个接一个地运行它们
'''

