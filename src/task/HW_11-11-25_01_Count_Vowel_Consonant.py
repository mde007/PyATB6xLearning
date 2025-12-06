# Write a program to Count vowels and consonants in a String

input_string = input("Enter the string: ")
vowels = "aeiou"
symbol = r"!@#$%^&*,./?;:{}[]()\|"

v_count = 0
c_count = 0
v_list = list()
c_list = list()

for char in input_string:
    if char.lower() in vowels:
        v_count = v_count+1
        if char not in v_list:
            v_list.append(char)
    elif char in symbol:
        continue
    elif char == " ":
        continue
    else:
        c_count = c_count+1
        if char not in c_list:
            c_list.append(char)


print(f"Vowels in the string: {v_list} and count of vowels: {v_count}")
print(f"Consonants in the string: {c_list} and count of consonants: {c_count}")
