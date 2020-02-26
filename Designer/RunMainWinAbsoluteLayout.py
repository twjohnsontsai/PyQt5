import sys
import MainWinAbsoluteLayout
# 在子目录下的档案，需要注明档案查询的设置
# 右键添加make directory as/Sources Root即可
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    # 只有直接运行这个脚本时才会继续往下执行，别的程序如果调用这个脚本文件不会执行这个条件语句
    app=QApplication(sys.argv)
    # 固定语句
    MainWindow=QMainWindow()
    # 创建主窗口
    ui=MainWinAbsoluteLayout.Ui_MainWindow()
    # 调用的是MainWinAbsoluteLayout.py的Ui_MainWindow()类
    # 主窗口的控件，由Ui_MainWindow()类接管了
    ui.setupUi(MainWindow)
    # 手动调用def setupUi方法来创建相应的控件，并且传入窗口对象的函数MainWindow
    # 向主窗口添加控件
    MainWindow.show()
    # 展示创建窗口
    sys.exit(app.exec_())
    # 执行主循环
# 独安装PyQtWebEngine，安装命令为：pip3 install PyQtWebEngine

