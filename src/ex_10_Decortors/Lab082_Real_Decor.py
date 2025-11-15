# Flow of events is as below:
#1. time_deco before func stmts executed
#2. print_logs before func stmts executed
#3. function stmt executed
#4. print_logs after func stmts executed
#5. time_deco after func stmts executed

import time

def print_logs(func):
    def wrapper():
        print("Start of the logs")
        func()
        print("End of the log")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total Time Take by Func -> ", end_time - start_time)
        print("###########")
    return wrapper

@time_decorator
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)

@time_decorator
@print_logs
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(2)


test_ui_1()
test_ui_2()