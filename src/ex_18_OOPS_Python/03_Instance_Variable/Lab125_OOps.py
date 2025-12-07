#global count = 0 - if we declare variable as global then it cant be assigned a value
count = 0

def increment():
    global count #make a variable global within a method
    count = count+1

increment()
increment()
increment()
print(count)