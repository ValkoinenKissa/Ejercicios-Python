from platform import *

print(processor())

print(platform())
print(platform(1))
print(platform(0, 1))

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
