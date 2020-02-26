import sys
from PyQt5.Qt import *
if __name__=='__main__':
    # 如果直接调用P3_开发第一个基于PyQt的桌面应用.py,条件才为True（真），并继续执行下面的程序，否则就是为False（否）
    # 创建QApplication类的实例,创建一个应用app=QApplication(sys.argv)，sys.argv会引入命令的参数
    app=QApplication(sys.argv)
    # 创建一个窗口
    w=QWidget()
    # 建立窗口的属性(尺寸）
    w.resize(300,150)
    # 移动窗口
    w.move(300,300)
    # 设置窗口的标题
    w.setWindowTitle('第一个基于P有Q图5的桌面应用')
    # 显示窗口
    w.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束（这是所有GUI程序通用的一个实现方法）
    sys.exit(app.exec_())