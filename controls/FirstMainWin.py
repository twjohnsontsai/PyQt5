import sys
# 获取参数的API
from PyQt5.QtWidgets import QMainWindow,QApplication
# 从PyQt5.QtWidgets的包导入需要用的主窗口QMainWindow和应用程序QApplication（以任何形式创建程序都必须要用）
from PyQt5.QtGui import QIcon
# 创建图标
# from PyQt5.QtCore import QFile

class FirstMainWin(QMainWindow):
    # 然后开始编写类 FirstMainWin,然后从主窗口继承(QMainWindow)
    def __init__(self):
        # 编写类的代码前，要先初始化构造函数 __init__（self）,然后定义一个parent=把控件放到哪里
        super(FirstMainWin,self).__init__()
        # 如何做呢？调用父类 FirstMainWin传入.__init__(parent)
        self.setWindowTitle('第一个主窗口应用')
        # 设置主窗口的标题
        self.resize(300,400)
        # 设置窗口的尺寸
        self.status=self.statusBar()
        # 默认窗口是添加状态栏的,通过这个方法获得状态栏
        self.status.showMessage('只存在5秒的信息',5000)
        # 在状态栏显示消息
#############注意输入代码时，注解要和换行同步，如果不是，写好代码后再补充上去###############


if __name__=='__main__':
    # 防止别的脚本调用，只有自己单独执行时，才会运行这个条件语句
    app=QApplication(sys.argv)
    # 创建app=QApplication(sys.argv)的对象，传入参数，这都是标准写法，通过这个来设置图标

    app.setWindowIcon(QIcon('./ico.ico '))
    # 需要导入ICO，ICO在Mac下比较好使，设置应用程序的图标
###########################图标是显示在程序坞里#######################################
    main=FirstMainWin()
    # 创建FirstMainWin()类
    main.show()
    # 调用show()来显示


    sys.exit(app.exec_())
    # 最后调用sys.exit(app.exec_())进入主循环

