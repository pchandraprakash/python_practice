"""
Exceptions are handled using try-except-finally blocks.
try block is where we enter our false code or a code which may/might cause problem during execution
except block is where we handle the exception
finally is a mandatory which will be executed irrespective of whether there is an exception or not.
"""
try:
    2 + 'S'
except Exception:
    print("There is an error in the code!")
finally:
    print(2+3)

try:
    f = open('sample', 'r')
    f.write("test this write")
except Exception:
    print("File does nor exist")
else:
    print("File reading is completed...")