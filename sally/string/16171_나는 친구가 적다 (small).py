# String
# Problem: 16171
# Memory: 29200KB
# Time: 68ms

original = input()
target = input()

for i in "0123456789":
    original = "".join(original.split(i))

if target in original:
    print(1)
else: print(0)