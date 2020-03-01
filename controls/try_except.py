# try expect
# 执行输入错误输入说明，反馈信息，这样程序就不会报红色

# print(10/0)
# 要避免使用者看到不明的错误，所以使用try～except的用法

try:
    print(10/0)
except:
    print('你的输入错误')

try:
    print(10/8)
    print(10/0)
    print(10+'0')
except ArithmeticError as e:
    print(e)
    # ArithmeticError是python自带的语法

try:
    print(10/8)
    print(10+'0')
except TypeError as e:
    print(e)
# TypeError是python自带的语法