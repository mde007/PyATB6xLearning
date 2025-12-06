# Write a program to check Palindrome of String
# Let’s take the word "level":
# Forward: "level", Backward: "level"
# Both are identical → Palindrome ✅
# Now, "hello":
# Forward: "hello", Backward: "olleh"
# Not the same → Not a palindrome ❌

input_string = "level"
# a,e, i,o,u.
# vowel ?

vowels = "aeiou"

vowels_count = 0
result = list()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count+1
        result.append(char)


print(vowels_count)
print(result)