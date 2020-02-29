import sys
# 获取参数的API
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QHBoxLayout,QPushButton
#本案例不使用面向对象的方式，(就是不使用类)，使用面向过程的方式
def onClick_Button():
    print('onclick')
# 创建一个应用
app=QApplication(sys.argv)
# 创建一个窗口
widget=QWidget()
# 创建一个按钮,放在widget窗口
btn=QPushButton(widget)
btn.setText('按钮')
# 绑定信号与槽（onClick_Button）
btn.clicked.connect(onClick_Button)

btn.move(24,52)

widget.resize(300,240)

widget.move(250,200)

widget.setWindowTitle('屏幕坐标系')
# 完成一个窗口
widget.show()
# 进入事件循环，要不整个循环会退出的
sys.exit(app.exec_())
# 定义一个单击事件，点击按钮后显示坐标值


