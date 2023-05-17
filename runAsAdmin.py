# _*_ coding:utf-8 _*_ 
# @Time : 10:22 2023/5/17
# Author : Abner
# @File : runAsAdmin.py
# @Software : PyCharm

from pyscreeze import unicode
from sys import executable, exit
import ctypes


class RunAsAdmin:
    def __init__(self):
        self.__set_run_as_admin()

    def __set_run_as_admin(self):
        """
        设置程序以管理员身份运行。如果设置成功，打印成功信息；否则，打印失败信息。
        """
        print('检查管理员权限。')
        if ctypes.windll.shell32.IsUserAnAdmin():
            print('管理员权限已打开。')
            pass
        else:
            cnFile = __file__.decode('gb18030')  # 防止__file__路径中有中文
            ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", unicode(executable), cnFile, None, 1)

            result_message = f"设置管理员权限成功:{ret}" if ret > 32 else f"设置管理员权限失败:{ret}"
            print(result_message)
            exit(0)

# if __name__ == "__main__":
#     run_as_admin = RunAsAdmin()
