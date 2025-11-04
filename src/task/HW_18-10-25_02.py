"""
An API sometimes fails due to network delays. Write a program to retry the API call 3 times until the response code becomes 200.
If it still fails after 3 tries, print a failure message.
Hint: Use a while loop with a counter.

Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200
✅ Test Passed
"""

code = float(input("API response code received: "))

if code==200:
    print("✅ Passed API Request!!!")
else:
    print("❌ Failed API Request!!!")
