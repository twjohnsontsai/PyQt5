import johnson

# 调用了johnson模块，所以也会和下行的代码一起执行
print(('this is another moduel'))


def m2():
    print('this is youtube module')
m2()
# johnson.py如果没有限制调用，这时候执行m2就会把johnson.py的代码也执行，
# 如果johnson.py限定设置了if __name__=='__main__'，就不会执行了
# 当有调用johnson.py的m1()时，他才会出现
johnson.m1()
# github desk用途不大
# 如何找出github有用的执行程序