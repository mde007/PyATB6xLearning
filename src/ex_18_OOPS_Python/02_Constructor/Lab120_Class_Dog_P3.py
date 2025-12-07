class Dog:
    # A
    name = None
    breed = None
    height = None
    weight = None
    def __init__(self):
        print("I will be called")

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass


# Object Ref
chow_ref = Dog() #prints "I will be called". Constructor called as soon as object created
print(chow_ref.name)
mow_ref = Dog() #prints "I will be called"
print(mow_ref.name)

# Dog().talk()