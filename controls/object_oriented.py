# Object_oriented面向对象
# 格式：
# class        对象
# Student（）： class的对象

class Student():
    def eat(self):
        # 没有class就定位为function，有class就是method（属性），例如：学生可以吃，这时候吃就只属于Student（'class' ）
        # self指的就是class的 Student():
        print('student can eat')

    def study(self):
        print('study can study')


# 属于外部的eat（）和eat(self):无关

Student().eat()
#类 Student的eat()方法

inty = Student()
inty.study()
inty.eat()

fruit = 'apple'
print(fruit.upper())
# 把字串变成大写

#################################################
class Student():
    def eat(self, name, age):
        print(name, ' can eat', ' age is ', age)


Student().eat('johnson', '20')

################------Method-------##############
class Student():
    name = 'johnson'
    age = '18'

    def eat(self):
        print(self.name, ' can eat', ' age is ', self.age)
    # 把name和age移到def（method：有class就叫method）外,这时候的name和age就不属于self，也就是不属于student
    # 需要定位为self就归属于student
    # method里面要调用外面的变量，就需要为变量定义self（self.name）

    @staticmethod
    #静态的功能（方法）,只有写了@staticmethod才可以写不带self的def（方法）
    def walk():
        print('student can walk')

    def study(self):
        print('student can study in home')


Student().eat()
Student().walk()
Student().study()


student1=Student()
student1.eat()
student1.study()

student2=Student()
student2.walk()
student2.eat()

# class可以重复多次调用，这样可以节省代码量