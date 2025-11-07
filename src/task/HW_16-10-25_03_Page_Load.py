"""
You want to check whether a web page loads within 3 seconds (performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds
"""
import random
import time

load_time = 0
page_load = True

while load_time < 3:
    page_load = random.choice([True, False])
    if page_load:
        if load_time == 0:
            print(f"Page successfully loaded within: {load_time + 1} second !!!")
        else:
            print(f"Page successfully loaded within: {load_time + 1} seconds !!!")
        break
    else:
        if load_time == 0:
            print(f"⏳ Page loading... ({load_time + 1} second)")
        else:
            print(f"⏳ Page loading... ({load_time + 1} seconds)")
        load_time += 1
        time.sleep(1.0)

if not page_load:
    print(f"⚠️ Page loading too slow !!!")
