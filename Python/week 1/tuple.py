#tuple

a=(54,21,45,89,21,67,59,21,)
print(a)
print(type(a))

#accessing a tuple
print(a[2])
print(a[2:5])
print(a[-2])

#python tuple functions
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sorted(a))   #uses when only same datatype present
data=[0,0,0,0,False]
print(any(data))
b=[0,0,0,3,False]
print(any(b))
print(all(b))
print(all(a))

#methods of tuple
print(a.index(45))
print(a.count(21))

#existence of element using 'in'(membership operator)
print(56 in a)
print(21 not in a)

#concatenation
print(a+(19,34))

#iteration
for n in a:
    print(n,sep='')

#nesting(tuple of tuple)
num=(23,(2,7),11,36)
print(num)
print(num[1])
v=(num[1][0])
print(v)

#
info=1,23,67,89.45,'vaishu'
print(info)
print(type(info))
