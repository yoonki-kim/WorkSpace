import os
print(os.listdir())
print("")

f = open('test1.py', 'r')
a = f.read()
print(a)
f.close()
