name = "This is a Big line"
print(type(name))
name = name + str(1) #plain concatenation is not allowed within string and int, conversion is needed
print(name)
print(type(name))

first_name = "Pramod"
last_name = "Dutta"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))