

from itertools import product

a = map(int, input.split())
b = map(int, input.split())
print(a)
print(b)

print(*product(a, b))