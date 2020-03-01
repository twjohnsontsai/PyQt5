# 继承，继承类的属性和功能

class Father:
    name='johnson'
    def eat(self):
        print(self.name,'can eat frult')

class Son(Father):
    pass
#Son主要是要演示继承的结果，所以pass就表示类成立， 不包含任何方法或是陈述的属性

jack=Son()
jack.eat()
# 因为name='johnson'是在def eat(self):（方法）之外，所以需要调用self.name
# Sun之所以可以使用Father的属性，是因为有了继承Sun(Father):，所以可以取用class Father:所有的属性
class Father:
    name='johnson'
    def eat(self):
        print(self.name,'can eat frult')

class Son(Father):
    def eat(self):
        print('son eat like',self.name)

jack=Son()
jack.eat()
# 这时候eat()调用的是son的    def eat(self):
#         print('son eat like',self.name)
#         叫重载（override)，就近的先行载入

class Father:
    name='johnson'
    def eat(self):
        print(self.name,'can eat frult')
class Mother:
    def walk(self):
        print('walk like her mother and',self.name)

class Son(Father,Mother):
    def eat(self):
        print('son eat like',self.name)

jack=Son()
jack.walk()
# 继承可以使用多类