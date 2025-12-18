#set

s={1,2,3,4,5,6,7,8,9}
print(type(s))
print(s)

#we cant acsses set by index

#methods
s.add(10000)
print(s)
s.remove(7)
print(s)
s.pop()
print(s)
s.clear()
print(s)

#operations
# | Method                   | Use             |
# | ------------------------ | --------------- |
# | `union()`                | Combine sets    |
# | `intersection()`         | Common elements |
# | `difference()`           | Difference      |
# | `symmetric_difference()` | Unique elements |
# | `issubset()`             | Check subset    |
# | `issuperset()`           | Check superset  |
