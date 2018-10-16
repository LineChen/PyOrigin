
class Boy(object):
    def test(self):
        pass


b = Boy()
print(b.test)
print(b.__dict__)

b.test = "string..."
print(b.test)
print(b.__dict__)


class Cal(object):
    def add(self):
        pass

    def _minus(self):
        pass

    def __multipy(self):
        pass


