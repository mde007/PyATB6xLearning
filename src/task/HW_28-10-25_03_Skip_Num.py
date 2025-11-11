# Skip numbers divisible by 3, from (0,100)

print("List of numbers between 0 and 100 and not divisible by 3:")

for i in range(101):
    if i % 3 == 0:
        continue
    else:
        print(i)
