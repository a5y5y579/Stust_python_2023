class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def _str_(self):
        return f"Name: {self.name}\n Age= {self.age}"
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()