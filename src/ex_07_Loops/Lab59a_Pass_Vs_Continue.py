for i in range(5):
    if i == 3:
        continue #skips current iteration and go to next iteration, skips print
    print("Number: ", i)

print("**********")

for i in range(5):
    if i == 3:
        pass #this if condition does nothing and prints next
    print("Number: ", i)