class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age

person1 = Person("Riolan", 19)
print(person1.get_name())
person1.set_name("David")
print(person1.get_name())
