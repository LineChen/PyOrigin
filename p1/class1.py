class Person(object):
    name = 'Jack'
    sex = 'male'

class Student(object):
    def __init__(self, name, sex, age):
        self.name = name
        self._sex = sex
        self.__age = age

    def get_age(self):
        return self.__age

stu1 = Student('Jack', 'male', 20)

#打印student类的所有属性
print(dir(stu1))

#打印我们定义的属性
print(stu1.__dict__)

#一个下划线开头的属性可以直接访问
print(stu1._sex)

#两个下划线开头的属性无法直接访问
# print(stu1.__age) 无法访问


print(stu1.get_age())
print(stu1._Student__age)