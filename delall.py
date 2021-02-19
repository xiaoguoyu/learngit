r"""
指令目录：
    delall 一个文件夹或者文件绝对路径
    如 delall C:\Users\abc\Desktop\test
      delall C:\Users\my\Desktop\qwerty.txt
    ---------------------------------------
"""
import os


class Commends:  # 建立Commends类，方便之后调用getattr
    def delall(self, path):  # 功能：删除path下所有文件和文件夹及path本身
        if os.path.isfile(path):  # 判断是否为文件
            try:
                os.remove("{0}".format(path))
                print("删除了{0}".format(path))
            except PermissionError:
                print("[WinError 5] 拒绝访问。:{0}".format(path))
            except FileNotFoundError:
                print("[WinError 3] 系统找不到指定的路径。: {0}".format(path))
            except OSError:
                print("[WinError 123] 文件名、目录名或卷标语法不正确。:{0}".format(path))
            except:
                print("不知道哪里出了点小问题，无法删除:{0}".format(path))
        else:
            all_file = []  # 防止抛出错误后找不到all_file列表，所以初始化
            try:
                all_file = os.listdir("{0}\\".format(path))  # 遍历path路径下的所有文件夹和文件（一层）
            except PermissionError:
                print("[WinError 5] 拒绝访问。:{0}".format(path))
            except FileNotFoundError:
                print("[WinError 3] 系统找不到指定的路径。: {0}".format(path))
            except OSError:
                print("[WinError 123] 文件名、目录名或卷标语法不正确。: {0}".format(path))
            except:
                print("不知道哪里出了点小问题，文件夹无法访问:{0}".format(path))
            for i in all_file:
                self.delall("{0}\\{1}".format(path, i))  # 既然是文件夹那就递归删除
            try:
                os.rmdir(path)
                print("删除了{0}".format(path))
            except PermissionError:
                print("[WinError 5] 拒绝访问。:{0}".format(path))
            except FileNotFoundError:
                print("[WinError 3] 系统找不到指定的路径。: {0}".format(path))
            except OSError:
                print("[WinError 123] 文件名、目录名或卷标语法不正确。:{0}".format(path))
            except:
                print("不知道哪里出了点小问题，无法删除:{0}".format(path))

    """
    def test(self, *attrs):
        print(attrs)
    """


def run(commend):
    cmdlist = commend.split(" ")
    # print(cmdlist)
    try:
        getattr(commends, cmdlist[0])(cmdlist[1])
    except:
        print("请确认您输入的指令与格式是否正确")


commends = Commends()
if __name__ == '__main__':
    while True:
        commend = input("commend>")
        run(commend)
