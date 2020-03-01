# function就是def，把代码封装到def的定义名function_name()，
# 执行时调用函数function_name()的名字

def function_name():
    print('hello function')

function_name()

a=10
b=10
print(a+b)
c=20
d=30
print(c+d)

def sum(num1,num2):
    print(num1+num2)

sum(4,10)
sum(12435,233556)

def fun2():
    return 'hello fun2'
# 不打印出字串，但是可以赋值
a=fun2()
print(a)

def sum2(a,b):
    return (a+b)
b=sum2(234,6778)
print(b)