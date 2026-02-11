#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for number in original:
    if number > 5:
        new_set.add(number + 2)

print(original)
print(new_set)
