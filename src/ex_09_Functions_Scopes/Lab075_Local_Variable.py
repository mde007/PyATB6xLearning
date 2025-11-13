pb_global_b = 12

def my_function():
    pb_a = 10
    print(pb_a)
    print(pb_global_b)

# print(pb_a) - local var cant be accessed outside
print(pb_global_b)
my_function()