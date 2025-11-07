"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""
# Question 3 :
#
# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break c
import time
import random

wait_time = 0
page_loaded = True

while wait_time < 5:
    page_loaded = random.choice([False, True])
    if page_loaded:
        if wait_time == 0:
            print(f"✅ Page loaded successfully in {wait_time + 1} second.")
        else:
            print(f"✅ Page loaded successfully in {wait_time + 1} seconds.")
        break
    else:
        if wait_time == 0:
            print(f"⏳ Checking... ({wait_time + 1} second)")
        else:
            print(f"⏳ Checking... ({wait_time + 1} seconds)")
        time.sleep(1)  # wait for 1 second
        wait_time += 1

if not page_loaded:
    print("❌ Timeout! Page failed to load within 5 seconds.")