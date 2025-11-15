def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
        print("End Deco1")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
        print("End Deco2")
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello!")


say_hello()