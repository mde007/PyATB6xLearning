print("Hello World!")
# print(self, *args, sep=' ', end='\n', file=None):

# self - please ignore  (oops)
# *args - unlimited number of comma seperated arguments.
print("PramodDutta", 123, "Amit", "John")
print("PramodDutta", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145)
print("PramodDutta", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145, sep="-")
print("PramodDutta", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145, sep="*", end="\n")

# IndentationError: unexpected indent
print("PramodDutta", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145, sep="*", end="!!!", flush=True)
# Print() - Case sensitive
