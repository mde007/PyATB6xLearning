"""
An API sometimes fails due to network delays. Write a program to retry the API call 3 times
until the response code becomes 200. If it still fails after 3 tries, print a failure message.
Hint: Use a while loop with a counter.

Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200
✅ Test Passed
"""
import random

attempt = 0 # Initialization
val = ["Response 200", "Response 404", "Response 503"]
while attempt < 3: # Condition
    code = random.choice(val)
    if code == "Response 200":
        print(f"{code}: The request was successful !!!")
        break
    else:
        attempt += 1 #Updation
        print(f"{code}: Retry!")

if attempt==3:
    print("❌ Failed API Request after 3 attempts !!!")

