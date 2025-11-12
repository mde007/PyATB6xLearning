#Function within function. Remember to call the inner function once inside main function

def f1():
    print("Welcome")

    #Step 1- Declare
    def f2():
        print("Hi")

    #Step 2 - Call
    f2()


f1()
# f2() - calling inside function outside of the main function not possible