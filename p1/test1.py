#encoding=utf-8
#测试json-类对象和json字符串互转
import json

class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Person(object):
    def __init__(self, name, age, dog):
        self.name = name
        self.age = age
        self.dog.name = dog.name
        self.dog.color = dog.color

def person_2_json(obj):
    return {
        "name" : obj.name,
        "age" : obj.age
    }

def json_2_person(d):
    return Person(d['name'], d['age'])

m = Person('line', 22)

m_json = json.dumps(m, default=person_2_json, indent=4)

print(m_json)

mm = json.loads(m_json, object_hook=json_2_person)

print(mm)
print('name:' , m.name , '\nage:' , m.age)