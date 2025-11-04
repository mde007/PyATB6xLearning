"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""

code = float(input("API response code received: "))

if code==200:
    print("✅ Passed API Request!!!")
else:
    print("❌ Failed API Request!!!")
