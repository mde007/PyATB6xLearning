a = 10 # variable everywhere in the program, not global variable
class Person:
    b = 11 # Instance variable

    def print_info(self):
        c = 20 # Local variable
        print(c)
        print(self.b)
        print(a)


object_ref = Person()
#print(b) - cant access instance variable outside class
#print(c) - cant access local variable outside method