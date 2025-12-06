# Write a program to check Palindrome of String
# Let’s take the word "level":
# Forward: "level", Backward: "level"
# Both are identical → Palindrome ✅
# Now, "hello":
# Forward: "hello", Backward: "olleh"
# Not the same → Not a palindrome ❌

def is_palindrome(s):
    #s = s.lower()
    return s == s[::-1] #s[::-1] creates a reversed copy of the string s

check_str = input("Enter the string: ")
if not is_palindrome(check_str.lower()):
    print("Not a palindrome ❌")
else:
    print("Palindrome !!!")