"""
class MyClass:
    def __init__(self, name):
        self.name = name

my_class = MyClass("Bard")

print(my_class.name)

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

my_class.greet()
"""
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    def goodbye(self):
        print(f"Goodbye, {self.name}!")

my_class = MyClass("Bard")

my_class.greet()
my_class.goodbye()