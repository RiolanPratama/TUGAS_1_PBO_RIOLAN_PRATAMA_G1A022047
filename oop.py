class Orang:
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

Orang1 = Orang("Riolan", 19)
print(Orang1.get_name())
Orang1.set_name("David")
print(Orang1.get_name())
