def outer_function():
    var1 = 30 # local

    def inner_function():
        var2 = 90
        print(var2)

    def inner_function2():
        print(var1) # global vr can be accessed
        #print(var2) - var local to another function cant be accessed


    inner_function()
    inner_function2()

outer_function()
#inner_function() - inner function cant be accessed from outside of outer func