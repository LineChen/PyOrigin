
class Boy(object):

    def __new__(cls, *args, **kwargs):
        print("invoke __new__ method :", args)
        return super(Boy, cls).__new__(cls)

    def __init__(self, name, age):
        print("invoke __init__ method ")
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Boy):
            return self.age == other.age
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Boy):
            return self.age + other.age
        else:
            return self.age


bb = Boy('Jack', 20)
cc = Boy('Rose', 20)

print(bb == cc)
print(bb + cc)
