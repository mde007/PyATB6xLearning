# Create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used, and I want you to also create the print function,
# which will print all the instance variable values.

class Person:
    a = 10
    b = 20
    c = 30
    d = 40
    e = 50

    def __init__(self):
        print("DC is called")
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
        print(self.e)

    def func1(self):
        print("Func1")

    def func2(self):
        print("Func2")

    def func3(self):
        print("Func3")

    def func4(self):
        print("Func4")

    def func5(self):
        print("Func5")


md = Person()
md.func1()
md.func2()
md.func3()
md.func4()
md.func5()