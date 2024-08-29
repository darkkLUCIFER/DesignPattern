"""
    shallow copy vs. deep copy
    only for mutable objects (list, dictionary, set)
"""
# Shallow Copy: Assigning a new variable to an existing object,
# This does not create a new object, but rather a new reference to the same object
a = [1, 2, 3, 4, 5]
b = a

# Both `a` and `b` point to the same object in memory
print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4, 5]

# Print the memory addresses of `a` and `b`
print(id(a))  # 134056974666560
print(id(b))  # 134056974666560

# Modifying `b` will also modify `a` because they point to the same object
b[0] = 20

print(b)  # [20, 2, 3, 4, 5]
print(a)  # [20, 2, 3, 4, 5]


# Solution: Use list(), dict(), set() to create a new object
# This creates a new object, but it's still a shallow copy
w = list(a)
w[0] = 100

print(a)  # [20, 2, 3, 4, 5]
print(w)  # [100, 2, 3, 4, 5]


# Problem: Shallow copy doesn't work with nested objects
t = [1, 2, 3, [4, 5]]
n = list(t)

# Modifying a nested object in `n` will also modify `t`
n[3][0] = 12

print(t)  # [1, 2, 3, [12, 5]]
print(n)  # [1, 2, 3, [12, 5]]

# Solution: Use the copy module
import copy

# Shallow Copy: copy.copy()
# This creates a new object, but it's still a shallow copy
r = [12, 13, 14, [15, 16]]
y = copy.copy(r)
y[3][1] = 0

print(r)  # [12, 13, 14, [15, 0]]
print(y)  # [12, 13, 14, [15, 0]]

# Deep Copy: copy.deepcopy()
# This creates a completely new object, including nested objects
z = [21, 22, 23, [24, 25]]
h = copy.deepcopy(z)
h[3][0] = 0

print(z)  # [21, 22, 23, [24, 25]]
print(h)  # [21, 22, 23, [0, 25]]
