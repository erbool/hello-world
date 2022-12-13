def a_plus_b():
    a = int(input('a='))
    b = int(input('b='))
    print('a+b =', a+b)

a_plus_b()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, 'is walking...')

    def speak(self):
        print(self.name, ', is speaking age of', self.age)

adam = Person('Adam', 19)
maria = Person('Maria', 18)

print(adam.name, adam.age)
adam.speak()
adam.walk()

print(maria.name, maria.age)
maria.speak()
maria.walk()