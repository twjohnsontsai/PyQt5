# QDesktopwidget
import sys
# 获取参数的API
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
# 从PyQt5.QtWidgets的包导入需要用的主窗口QMainWindow和应用程序QApplication（以任何形式创建程序都必须要用）
from PyQt5.QtGui import QIcon
# 创建图标
# from PyQt5.QtCore import QFile

class CenterForm(QMainWindow):
    # 然后开始编写类 FirstMainWin,然后从主窗口继承(QMainWindow)
    def __init__(self):
        # 编写类的代码前，要先初始化构造函数 __init__（self）,然后定义一个parent=把控件放到哪里
        super(CenterForm,self).__init__()
        # 如何做呢？调用父类 CenterForm传入.__init__(parent)
        self.setWindowTitle('让窗口居中')
        # 设置主窗口的标题
        self.resize(400,300)
        # 设置窗口的尺寸
    # 在CenterForm类中再添加一个方法、函数，他的作用就是让窗口居中
    def center(self):
        # 创建一个实例QDesktopWidget()然后计算获得屏幕的坐标系screenGeometry()
        screen=QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size=self.geometry()
        # 然后分别获取宽度（居中窗口左边缘的行坐标）、高度
        # （屏幕的宽度-窗口的宽度）/2
        # （屏幕的高度-窗口的高度）/2
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.hight()-size.height())/2
        # 然后在调用move的坐标就可以
        self.move(newLeft,newTop)

if __name__=='__main__':
    # 防止别的脚本调用，只有自己单独执行时，才会运行这个条件语句
    app=QApplication(sys.argv)
    # 创建app=QApplication(sys.argv)的对象，传入参数，这都是标准写法，通过这个来设置图标

    main=CenterForm()
    # 创建FirstMainWin()类
    main.show()
    # 调用show()来显示

    sys.exit(app.exec_())
    # 最后调用sys.exit(app.exec_())进入主循环

