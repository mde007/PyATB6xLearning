class TestExample:
    def __init__(self):
        self.driver = "Chrome"
        self._config = "STAG"
        self.__api__key = "ABC12345"
    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"API Key: {self.__api__key}")

    def __private_method1(self):
        print("Private method1")

    def __private_method2(self):
        print("Private method2")

    def work(self):
        self.__private_method1()
        self.__private_method2()


obj = TestExample()
obj.show()
obj.work()

# Access levels:
print("Driver",obj.driver)          # ✅ Public — accessible
print("Config",obj._config)         # ⚠️ Protected — accessible but discouraged
# print(obj.__api__key)     # ❌ Private — AttributeError
